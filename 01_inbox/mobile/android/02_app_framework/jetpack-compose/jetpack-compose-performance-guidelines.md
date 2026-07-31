# Jetpack Compose 코드 수준 성능 최적화 가이드

이 문서는 Android Dev Summit ("More performance tips for Jetpack Compose") 세션 내용을 바탕으로, Jetpack Compose UI 작성 시 불필요한 리컴포지션(Recomposition)을 차단하고 렌더링 성능을 극대화하기 위한 **코드 수준의 최적화 규칙**을 정리합니다.

---

## 0. 성능 최적화의 대전제: Loop Cycle (Measure -> Debug -> Improve)

성능 최적화는 짐작이나 추측에 기반하여 코드를 조작하는 것이 아니라, **측정(Measure) -> 원인 분석/디버깅(Debug) -> 개선(Improve)**의 선순환 앙상블 순환 프로세스를 지켜야 합니다.

```
       ┌────────────────────────┐
       │     1. Measure (측정)   │
       │ (Macrobenchmark, Profiler)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │     2. Debug (디버깅)   │
       │ (Layout Inspector, Tracing)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │    3. Improve (개선)    │
       │ (State Read 지연, Stability)
       └───────────┬────────────┘
                   │
                   └───────► (다시 1. Measure로 돌아가 검증)
```

1. **Measure (측정)**
   * **측정 없는 최적화는 금물입니다.** 최적화를 적용하기 전에 Macrobenchmark, Android Studio Profiler, 또는 `reportFullyDrawn` 등을 사용해 정확한 Baseline(기준점) 지표를 수집해야 합니다.
2. **Debug (원인 분석)**
   * 지표가 저하되거나 프레임 드랍(Jank)이 발생하는 정확한 원인(불필요한 Recomposition, 메인 쓰레드 블로킹, Unstable 파라미터 등)을 Layout Inspector나 Perfetto 툴 등으로 추적 및 확인합니다.
3. **Improve (개선)**
   * 본 가이드 문서에서 소개하는 최적화 패턴(상태 읽기 지연, `derivedStateOf`, Stability Config 등)을 적용합니다.
4. **Re-Measure (재검증)**
   * 개선 후 반드시 다시 측정(Measure)하여 실제 지표가 얼마나 향상되었는지 수치로 검증하는 사이클을 반복합니다.

---

## 1. 상태 읽기 지연 (Defer State Reads)

Compose 최적화의 첫 번째 원칙은 **"상태 읽기(State Read)를 가능한 가장 늦은 렌더링 단계로 지연하는 것"**입니다.

### 1-1. 컴포즈의 3단계 파이프라인 복습
컴포즈는 상태가 변경되면 **1) Composition(구성) -> 2) Layout(배치) -> 3) Drawing(그리기)** 단계를 거칩니다.
* 일반적인 상태 읽기는 1단계(Composition)에서 발생하므로, 상태가 단 1픽셀만 변해도 관련 컴포저블 전체가 리컴포지션됩니다.
* 만약 상태 읽기를 2단계(Layout)나 3단계(Draw)로 지연시킬 수 있다면, 1단계 리컴포지션을 완전히 생략하고 픽셀 좌표 변경 또는 그리기만 빠르게 재수행할 수 있습니다.

### 1-2. 개선 예시 (람다 기반 Modifier 사용)
사용자가 화면을 스크롤할 때 스크롤 오프셋 상태값에 따라 컴포저블의 오프셋 위치를 이동시키는 시나리오입니다.

#### ❌ 나쁜 예 (매 프레임마다 Composition 발생)
```kotlin
val scrollState = rememberScrollState()

Box(
    Modifier.offset(
        // scrollState.value가 Composition 단계에서 바로 읽히기 때문에,
        // 스크롤이 움직일 때마다 Box 전체가 무수히 리컴포지션됩니다.
        x = 0.dp,
        y = scrollState.value.dp 
    )
)
```

#### 🐳 좋은 예 (State Read를 Layout/Draw 단계로 지연)
```kotlin
val scrollState = rememberScrollState()

Box(
    Modifier.offset {
        // 람다 {} 내부로 상태 읽기를 감싸면, Composition 단계에서는 람다 참조만 전달되고
        // 실제 스크롤 값은 2단계인 Layout(Measurement/Placement) 단계에서 비로소 읽힙니다.
        // 결과적으로 리컴포지션이 0회 발생합니다.
        IntOffset(x = 0, y = scrollState.value)
    }
)
```

> [!TIP]
> `Modifier.offset {}`, `Modifier.drawBehind {}`, `Modifier.graphicsLayer {}` 등 람다 인수를 받는 확장 Modifier들은 대부분 상태 읽기 지연을 지원하므로, 실시간 변화하는 상태를 화면에 반영할 때는 반드시 람다 형태의 함수형 API를 사용하십시오.

---

## 2. DerivedStateOf의 올바른 활용

`derivedStateOf`는 빈번하게 변경되는 상태(예: 스크롤 픽셀 단위 변화)를 바탕으로 **새로운 가공된 상태(예: 리스트의 첫 번째 아이템 표시 여부 등)를 유도할 때** 사용합니다.

### 2-1. 잘못된 사용 vs 올바른 사용
* **단순 상태 유도**: 단순 연산이나 두 값을 더하는 작업은 `derivedStateOf`를 쓰면 오버헤드만 커지며, `remember(key) { }`를 쓰는 것이 낫습니다.
* **상태 버퍼링/노이즈 제거**: 1px 단위의 고빈도 스크롤 이벤트 중에서 "특정 지점을 넘어섰는가?"와 같은 Boolean 전환점에만 컴포즈가 반응하도록 필터링할 때 `derivedStateOf`가 강력한 힘을 발휘합니다.

```kotlin
val listState = rememberLazyListState()

// ❌ 나쁜 예 (스크롤 할 때마다 true/false를 계속 판단하여 매번 리컴포지션 유발)
val isScrollToTop = listState.firstVisibleItemIndex == 0 

// 🐳 좋은 예 (스크롤 픽셀 값이 아무리 변해도 true -> false로 변경되는 경계점에서만 1회 리컴포지션 발생)
val isScrollToTop = remember {
    derivedStateOf { listState.firstVisibleItemIndex == 0 }
}
```

---

### 3-1. 불안정(Unstable) 타입과 기존 문제점
* **Collection 타입 사용**: `List`, `Map`, `Set` 등 Standard Collection 인터페이스는 내부 원소가 언제든지 변할 수 있는 가변 객체(예: `ArrayList`)일 가능성이 있어, 기존 Compose 컴파일러(Kotlin 1.x)는 이를 `Unstable`로 분류했습니다.
* 이로 인해 `List`를 받는 컴포저블은 매번 Skip되지 않고 불필요하게 리컴포지션이 발생하는 문제가 있었습니다.

### 3-2. Kotlin 2.x (Strong Skipping Mode) 도입 이후 변화
* **Kotlin 2.0+ & Compose Compiler 2.0+**: **Strong Skipping Mode**가 기본 활성화되었습니다.
* 파라미터가 Unstable 타입(일반 `List` 포함)이라도, 전달된 인스턴스의 **동등성(`equals()`) 비교**를 거쳐 이전과 값이 같다고 판단되면 컴포저블 실행을 안전하게 생략(Skip)합니다.
* 따라서 단순한 Recomposition Skip만을 목적으로 모든 `List`를 `ImmutableList`로 교체할 필요는 없습니다.

### 3-3. kotlinx-collections-immutable 도입 가이드라인
그럼에도 불고하고 `kotlinx-collections-immutable` (`PersistentList` 등)의 도입이 권장되는 상황은 다음과 같습니다:

1. **대용량 리스트의 `equals()` 비교 성능 최적화**
   * Strong Skipping이 동작할 때 리스트의 크기가 크면 `List.equals()` 비교 자체에 비용이 발생합니다.
   * `PersistentList`는 참조(Reference) 및 영구 구조(Persistent Data Structure) 기반 변경 추적이 가능하므로 `equals()` 비용을 최소화할 수 있습니다.
2. **도메인/State 모델의 엄격한 불변성 보장**
   * UI State(예: `UiState(items: PersistentList<Item>)`) 레벨에서 개발자의 실수로 인한 가변 객체 혼용을 언어/타입 차원에서 완전히 차단하고 싶을 때.
3. **컴파일러 수준 명시적 안정을 위한 어노테이션 활용**
   * 일반 Data Class의 경우 `@Immutable` 또는 `@Stable` 어노테이션을 사용하여 컴파일러에 불변 객체임을 명시할 수 있습니다.

```kotlin
// 🐳 컴파일러가 Stable로 판단하도록 보증
@Immutable
data class User(
    val id: String,
    val name: String
)
```

### 3-4. 외부 라이브러리 및 클래스를 위한 Stability Configuration File 활용
수정 권한이 없는 외부 라이브러리/SDK 클래스(예: Java Time API, Ktor 객체, Google Maps SDK 등)가 UI State에 포함될 경우, Compose 컴파일러는 이를 `Unstable`로 오인할 수 있습니다.

이를 해결하기 위해 프로젝트 루트에 `compose_compiler_config.conf` 파일 지정을 통해 명시적으로 Stable 지정을 수행합니다:

1. **`compose_compiler_config.conf` 설정**:
   ```text
   // Java Standard & Network / Time APIs
   java.time.Instant
   java.time.LocalDate
   java.time.LocalDateTime
   java.time.ZonedDateTime

   // Ktor & Network Models
   io.ktor.http.Url
   ```

2. **Compose를 사용하는 각 모듈의 `build.gradle.kts` 설정**:
   ```kotlin
   composeCompiler {
       stabilityConfigurationFiles.add(rootProject.layout.projectDirectory.file("compose_compiler_config.conf"))
   }
   ```

---

## 4. `reportFullyDrawn` API를 이용한 시작 성능 최적화

수동 벤치마크나 Google Play Android Vitals 분석 시, 단순히 화면의 첫 번째 프레임이 렌더링된 속도(TTID, Time to Initial Display)보다 **실제 유저가 데이터를 로딩받아 인터랙션이 가능해진 시점(TTFD, Time to Fully Drawn)**이 더 중요합니다.

구글은 앱이 실제로 가치 있는 데이터를 완전히 화면에 띄운 순간을 OS 및 빌드 시스템에 정확히 리포트하도록 권장합니다.

### 4-1. Compose 전용 ReportDrawn API 활용법
Compose 환경에서는 편리하게 특정 조건이 참이 될 때 완전히 그려졌음을 수집하는 전용 API를 제공합니다.

* **`ReportDrawnWhen { predicate }`**: 람다 내부의 조건식이 참이 될 때까지 리포팅을 대기하며, 조건 충족 시 완전 드로잉을 시스템에 알립니다.
* **`ReportDrawnAfter { block }`**: 비동기 서스펜딩 함수가 완료되는 시점에 드로잉 완료를 보고합니다.

#### 🐳 예시 (네트워크 통신 완료 시점에 완전히 그려짐을 알림)
```kotlin
@Composable
fun MainScreen(viewModel: MainViewModel) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    // uiState가 Loading이 아니고 성공 또는 실패로 결과 데이터가 바인딩된 순간을
    // 시스템(Android OS 및 Macrobenchmark)에 'Fully Drawn' 상태로 보고합니다.
    ReportDrawnWhen { uiState is UiState.Success || uiState is UiState.Error }

    when (val state = uiState) {
        is UiState.Loading -> CircularProgressIndicator()
        is UiState.Success -> LazyColumn { /* 리스트 렌더링 */ }
        is UiState.Error -> Text("에러 발생")
    }
}
```

### 4-2. 기대 효과
* **정확한 매크로벤치마크 측정**: `StartupTimingMetric()` 측정 시 실제 서버 응답 및 가치 있는 화면 로딩 완료 시간까지 포함해 정확히 튜닝할 수 있습니다.
* **Baseline Profile 최적화 정교화**: 빌드 시스템 및 컴포저블 시작 규칙이 첫 껍데기 화면뿐만 아니라 **실제 비즈니스 데이터가 렌더링되는 시점의 모든 클래스/메서드까지 AOT 컴파일 대상에 고스란히 포함**시킵니다.

---

## 5. System Tracing & Perfetto 기반 원인 디버깅

성능 지표(TTID, TTFD)를 측정한 후 프레임 병목이나 병목 구간을 세부 분석하려면 **Tracing (추적) 툴링**을 활용해야 합니다.

### 5-1. 최신 툴링 환경 (Kotlin 2.x / AGP 8.3+)
과거(Kotlin 1.x / Compose 1.4 이전)에는 `androidx.tracing:tracing-perfetto`나 `runtime-tracing` 라이브러리를 manual로 Gradle에 추가하고 `perfettoSdkTracing.enable=true` 설정을 켜야 했습니다.

현재 **Kotlin 2.x & AndroidX Benchmark** 환경에서는 `benchmark-macro-junit4` 및 `baselineprofile` 플러그인에 Tracing 툴링이 **기본 내장/자동 주입**되어 별도 Gradle 작업 없이 Perfetto Trace 수집이 즉시 가능합니다.

### 5-2. 커스텀 Tracing 코딩 규칙 (`trace("") { }`)
Compose Compiler가 기본 생성하는 `@Composable` 추적 외에, **개발자의 복잡한 계산이나 비동기 로직 구간을 Perfetto 타임라인 상에서 정밀 추적**하려면 `androidx.tracing.trace` 블록으로 감싸주어야 합니다.

#### 🐳 작성 예시
```kotlin
import androidx.tracing.trace

@Composable
fun DashboardFeedList(items: List<FeedItem>) {
    // Perfetto 뷰어 타임라인 상에 'DashboardDataProcessing' 구간을 명시하여 시간 측정
    val processedItems = remember(items) {
        trace("DashboardDataProcessing") {
            items.filter { it.isValid }.sortedByDescending { it.timestamp }
        }
    }

    LazyColumn {
        items(processedItems) { item ->
            FeedItemRow(item)
        }
    }
}
```

### 5-3. 메모리(RAM) 및 Heap Dump 디버깅 (Memory Profiler & Play Console Vitals)
성능 디버깅 시 CPU 프레임 외에도 **메모리(RAM) 사용량과 힙(Heap) 할당**을 상시 트래킹해야 합니다.

1. **Android Studio Memory Profiler 분석**:
   * **Heap Dump (힙 덤프)**: 리컴포지션이나 화면 전환 시 Destroy된 Activity, Context, ViewModel 객체가 메모리에서 누수(Leaked)되지 않고 릴리즈되는지 추적합니다.
   * **Allocation Tracking (할당 추적)**: `@Composable` 함수 내부에서 단시간에 과도한 임시 객체(`String` 결합, Collection 생성, 비트맵 생성 등)가 할당되어 **GC Pauses(가비지 컬렉터로 인한 프레임 멈춤)**를 유발하는지 감지합니다.
2. **Google Play Console - Memory Vitals (RAM Tier 분석)**:
   * 실제 유저 디바이스 환경의 **Low Memory Kills (LMK, 메모리 부족으로 OS가 앱을 강제 종료하는 현상)** 비율을 모니터링합니다.
   * 기기별 RAM 등급(예: 2GB, 4GB, 8GB RAM Tier)에 따라 앱의 Peak RAM 사용량을 트래킹하여 최저 사양 기기에서도 OOM 없이 동작하도록 모니터링합니다.
3. **Compose 메모리 최적화 실무 지침**:
   * 재사용 가능한 `Regex`, `DateFormat`, `Paint` 등의 무거운 객체는 `@Composable` 함수 내부에서 매번 생성하지 말고 `remember`로 캐싱하거나 클래스 상수로 뺍니다.
   * 대용량 Bitmap 디코딩 시 `AsyncImage` 및 `BitmapFactory.Options`를 사용해 렌더링 뷰 크기에 맞춰 Downsampling 디코딩합니다.

### 5-4. Low Memory Killer (LMK) 프로세스 강제 종료 대비 및 `rememberSaveable` 보존 전략
차세대 Android OS는 메모리 압박 시 백그라운드 프로세스를 우선순위에 따라 즉각 강제 종료(Process Death)합니다.

* **프로세스 재구동 시 UX 보존 (`rememberSaveable`)**:
  * 단순 `remember`로 관리되는 상태는 LMK에 의해 앱 프로세스가 죽었다가 사용자가 돌아왔을 때 모두 파괴(초기화)됩니다.
  * 유저의 입력 폼, 스크롤 위치, 탭 선택 상태 등 핵심 UI 상태는 **`rememberSaveable`**이나 `SavedStateHandle`을 사용하여 LMK 복구 후에도 데이터가 보존되도록 구현해야 합니다.

> [!TIP]
> **Tracing 및 메모리 가이드라인 Summary**:
> 1. 화면의 메인 로딩 기준 시점은 `ReportDrawnWhen`으로 **Measure(측정)**합니다.
> 2. 프레임 드랍(Jank) 발생 시 Perfetto Trace를 생성하여 **Debug(원인 분석)**합니다.
> 3. 무거운 가공/비즈니스 연산에는 `trace("SectionName") { }`를 감싸 **정확한 병목 구간을 식별**합니다.
> 4. 메모리 누수 및 GC 멈춤 현상은 **Memory Profiler(Heap Dump)**와 **Play Console Memory Vitals**로 추적합니다.
> 5. LMK(Low Memory Killer) 프로세스 종료 대비를 위해 유저 UI 상태는 **`rememberSaveable`**로 보존합니다.



---

## 6. BoxWithConstraints 사용 시 주의사항 및 대체 방안

`BoxWithConstraints`는 하위 컴포저블의 레이아웃 제약조건(`maxWidth`, `maxHeight` 등)을 사전에 확인하여 분기 UI를 그릴 때 매우 유용한 컴포저블입니다.

### 6-1. 성능상 오버헤드와 남용 금지 이유
* **Subcomposition(하위 구성) 오버헤드**: `BoxWithConstraints`는 레이아웃 측정(Measurement) 단계에서 제약조건을 파악한 뒤, 람다 내부의 컴포저블을 비동기로 다시 컴포지션(Subcomposition)합니다.
* 이 과정은 일반 `Box`나 `Column`보다 **훨씬 큰 리컴포지션 오버헤드와 CPU 파이프라인 지연**을 유발하므로 리스트 아이템 내부나 스크롤이 잦은 UI에서 남용하면 심각한 프레임 드랍(Jank)의 원인이 됩니다.

### 6-2. 올바른 사용 조건 vs 대체 방안
* ❌ **지양해야 할 케이스**: 단순 `Modifier` 크기 계산, 스크롤 영역 내부 아이템 렌더링.
* 🐳 **권장 케이스**: 화면 폭에 따라 전혀 다른 형태의 UI 구조(예: 싱글 뷰 vs 스플릿 뷰)로 분기해야 하는 최상위 윈도우/스크린 레이아웃.
* 💡 **대체 방안**:
  1. `Modifier.layout` 확장 함수 사용: 단기 측정 및 크기 조정만 필요한 경우 1단계 Subcomposition을 건너뛰고 2단계 Layout에서만 작업 수행.
  2. `WindowSizeClass` 활용: 화면 폭에 따른 분기는 `BoxWithConstraints` 대신 WindowSizeClass(Compact/Medium/Expanded)를 사용해 최상단에서 전역으로 분기.

---

## 7. `remember` 내 무거운 연산(Heavy Computation) 격리

`remember`는 화면이 리컴포지션될 때 이전 계산 결과를 보존하여 CPU 낭비를 막아주는 핵심 API입니다.

### 7-1. 오직 "비용이 큰 연산"에만 적용하는 이유
`remember` 역시 공짜가 아닙니다. 내부적으로 Slot Table 인덱스를 확인하고 메모리 캐시를 조회/갱신하는 오버헤드가 발생합니다.
* **단순 연산**: `a + b`, 단순 문자열 이어서 붙이기 등은 `remember` 오버헤드가 더 큽니다.
* **무거운 연산(Heavy Computation)**: Sorting(정렬), Filtering(필터링), Regex 검증, 데이터 변환 연산 등은 리컴포지션마다 재실행되면 CPU 타임을 심각하게 갉아먹으므로 반드시 `remember(key)`로 감싸야 합니다.

```kotlin
// ❌ 단순 연산에 remember 지양 (오버헤드가 더 큼)
val fullName = remember(firstName, lastName) { "$firstName $lastName" }

// 🐳 복잡한 연산 및 필터링에는 필수 적용
val sortedActiveUsers = remember(users) {
    trace("SortActiveUsers") {
        users.filter { it.isActive }
             .sortedByDescending { it.lastLoginTimestamp }
    }
}
```

---

## 8. 비동기 이미지 로딩 (Asynchronous Image Loading)

화면에 네트워크 URL이나 고해상도 이미지가 포함되어 있을 때 메인 쓰레드에서 비트맵을 직접 디코딩하면 **화면이 수십 ms 동안 멈추는 프레임 멈춤(Jank)**이 발생합니다.

### 8-1. `AsyncImage` vs `rememberAsyncImagePainter` vs `painterResource`
* **`painterResource(R.drawable.xxx)`**: **앱 내 정적 로컬 리소스(vector, small png)**를 불러올 때 사용합니다. 네트워크 URL이나 무거운 외부 비트맵 디코딩에는 사용할 수 없습니다.
* **`AsyncImage` (Coil 고도화 API - 권장 🐳)**:
  * 내부적으로 `SubcomposeAsyncImage`나 `Image` 컴포저블을 래핑하여 백그라운드 I/O 디코딩, 캐싱, Placeholder 렌더링을 최적화합니다.
  * 별도의 `remember` 선언 없이 컴포저블 파이프라인 안에서 가장 깔끔하고 성능 효율적으로 비동기 이미지를 로딩합니다.
* **`rememberAsyncImagePainter` (Low-level Painter API)**:
  * `Image(painter = rememberAsyncImagePainter(...))` 형태로 custom `Painter` 호환성이 꼭 필요한 특수한 경우(예: 확장 Modifier와의 직접 결합)에만 제한적으로 사용합니다.

### 8-2. `placeholder` 및 `error` 처리 시 `rememberAsyncImagePainter` 활용
* **로컬 드로어블 Placeholder**: `placeholder = painterResource(R.drawable.placeholder)` 처럼 앱 패키지 내 정적 리소스를 쓸 때는 `painterResource`를 바로 전달합니다.
* **비동기/네트워크 Placeholder 및 Error Image**:
  * 만약 Placeholder나 Error 이미지 자체도 로컬 정적 리소스가 아닌 **비동기로 로드해야 하는 URL이나 외부 이미지인 경우**, `placeholder = rememberAsyncImagePainter(model = placeholderUrl)` 형태로 `rememberAsyncImagePainter`를 지정해야 합니다.

```kotlin
// 🐳 1) 일반적인 로컬 드로어블을 Placeholder로 사용하는 경우
AsyncImage(
    model = imageUrl,
    contentDescription = "프로필 이미지",
    modifier = Modifier
        .size(60.dp)
        .clip(CircleShape),
    placeholder = painterResource(R.drawable.placeholder_avatar)
)

// 🐳 2) Placeholder 자체도 비동기/네트워크 이미지를 사용하는 경우 (rememberAsyncImagePainter 사용)
AsyncImage(
    model = imageUrl,
    contentDescription = "프로필 이미지",
    modifier = Modifier
        .size(60.dp)
        .clip(CircleShape),
    placeholder = rememberAsyncImagePainter(model = placeholderUrl),
    error = rememberAsyncImagePainter(model = fallbackUrl)
)
```

---

## 9. 무거운 프레임 (Heavy Frames) 분해 및 스케줄링

한 프레임(16ms 또는 8.3ms) 내에 너무 많은 컴포저블을 한 번에 그리려고 하면 16ms 윈도우를 초과하여 프레임이 떨어집니다.

### 9-1. 무거운 프레임을 여러 프레임으로 분해하는 방법

1. **LazyList의 `contentType` 지정**:
   * LazyColumn/LazyRow 사용 시 `contentType`을 지정하면 불필요한 ViewHolder 및 Composition 재생성을 방지하고 리사이클링 효율을 극대화합니다.
2. **Composable 지연 렌더링 (Deferred Rendering)**:
   * 덜 중요한 컴포저블(예: 하단 다이얼로그, 세부 정보 섹션)은 `LaunchedEffect`나 `withContext(Dispatchers.Default)` 이후 상태를 넘겨 다음 프레임으로 렌더링을 분산시킵니다.
3. **`Modifier.drawWithCache` 활용**:
   * Draw 단계에서 매번 Canvas 객체나 Brush, Path를 새로 생성하지 않고 이전 렌더링 오브젝트를 재사용하여 프레임 당 드로잉 타임을 단축합니다.


