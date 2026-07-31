# System Tracing & Perfetto 기반 원인 디버깅

상위 노트: [jetpack-compose-performance-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines.md)

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
