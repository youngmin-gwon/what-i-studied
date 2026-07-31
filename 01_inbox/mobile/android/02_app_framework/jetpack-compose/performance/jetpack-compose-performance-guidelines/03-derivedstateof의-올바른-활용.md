# DerivedStateOf의 올바른 활용

상위 노트: [[jetpack-compose-performance-guidelines]]

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
