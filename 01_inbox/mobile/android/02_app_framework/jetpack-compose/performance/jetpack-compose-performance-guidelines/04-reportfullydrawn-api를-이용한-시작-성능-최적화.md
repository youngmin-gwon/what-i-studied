# `reportFullyDrawn` API를 이용한 시작 성능 최적화

상위 노트: [[jetpack-compose-performance-guidelines]]

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
