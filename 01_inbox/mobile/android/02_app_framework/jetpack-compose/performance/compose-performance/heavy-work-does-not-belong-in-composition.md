---
title: heavy-work-does-not-belong-in-composition
tags: [android, compose/performance, jetpack-compose]
aliases: [무거운 작업은 composition 안에서 실행하지 않는다]
date modified: 2026-08-06 16:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## 무거운 작업은 composition 안에서 실행하지 않는다

---

### 초보자를 위한 핵심 개념 요약

Jetpack Compose에서 `@Composable` 함수 본문(Composition 단계)은 화면을 그리기 위해 **메인 스레드(Main UI Thread)**에서 빈번하게 실행됩니다. 

만약 `@Composable` 본문 내부에서 파일 읽기/쓰기, 네트워크 통신, 대용량 리스트 정렬, 비트맵 디코딩, JSON 파싱 등 무거운 작업을 직접 수행하면, 화면을 1초에 60회 혹은 120회 그려내야 하는 프레임 마감 시간(16ms / 8ms)을 놓치게 되어 **화면 멈춤 및 튕김 현상(Jank/Frame Drop)**이 발생합니다.

---

### 흔히 하는 오해와 주의점

1. **`remember`는 스레드를 바꾸지 않는다!**
   * `remember { expensiveSummarize(rows) }` 처럼 작성하면 연산 결과를 재사용할 뿐, 계산 자체는 **Composition 도중 메인 스레드에서** 실행됩니다. 따라서 무거운 연산이 시작될 때 메인 스레드가 멈춥니다.
2. **`LaunchedEffect`도 기본적으로 메인 스레드에서 시작한다!**
   * `LaunchedEffect` 내부 작업은 `Dispatchers.Main.immediate`에서 실행됩니다. 따라서 내부에서 `withContext(Dispatchers.Default)` 같은 디스패처 전환 없이 긴 동기 연산을 수행하면 여전히 UI 스레드를 블로킹합니다.

---

### 잘못된 구현 vs 올바른 구현 비교

#### ❌ 피해야 할 구현 (Composition 중 메인 스레드 연산)

```kotlin
// 안 좋은 예: remember 블록 내부 계산도 Composition 중 UI 메인 스레드에서 실행됨
@Composable
fun ReportScreen(rows: List<RowData>) {
    // rows가 변경될 때마다 메인 스레드가 멈춘 채 연산을 수행함!
    val summary = remember(rows) { expensiveSummarize(rows) }
    Text(text = summary)
}
```

#### ⭕ 올바른 구현 (ViewModel과 백그라운드 Dispatcher 활용)

무거운 작업은 UI 영역 밖인 [ViewModel](../../../architecture/state-management/viewmodel/viewmodel.md)과 데이터 레이어로 격리하고, 적절한 코루틴 디스패처(`Dispatchers.Default` 또는 `Dispatchers.IO`)를 사용합니다.

```kotlin
class ReportViewModel(
    repository: ReportRepository,
) : ViewModel() {
    // Dispatchers.Default (CPU 연산 전용 스레드 풀)로 작업을 백그라운드 이관
    val summary: StateFlow<String> = repository.rows
        .mapLatest { rows ->
            withContext(Dispatchers.Default) { expensiveSummarize(rows) }
        }
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5_000),
            initialValue = "",
        )
}

@Composable
fun ReportScreen(
    viewModel: ReportViewModel,
) {
    // UI는 백그라운드에서 계산 완료된 상태값만 안전하게 구독하여 표시
    val summary by viewModel.summary.collectAsStateWithLifecycle()
    Text(text = summary)
}
```

---

### 성능 측정 및 진단 가이드

1. **Perfetto & Android Studio Profiler**: Trace에서 `Recompose` 구간이 메인 스레드(Main-thread runnable)를 장시간 점유하는지 감지합니다.
2. **Frame metrics 측정**: 무거운 작업을 백그라운드로 옮기기 전후의 `FrameTimingMetric` 및 화면 진입 시 첫 프레임(TTID)과 실제 콘텐츠 완료 시점(TTFD)을 비교 측정합니다.
3. **Coroutine Unit Test**: 화면을 벗어날 때 백그라운드 작업 취소 및 공유 흐름(`WhileSubscribed`)이 의도한 대로 동작하는지 단위 테스트로 검증합니다.

---

### 연관 노트

- [Composable 본문은 빠르고 멱등성을 가지며 부작용이 없어야 한다](../../runtime/compose-runtime/composable-body-purity.md)
- [Compose 성능 최적화는 측정·진단·개선 순환으로 진행한다](./compose-performance-starts-with-measure-debug-improve-loop.md)
- [렌더링 성능은 프레임 지연의 원인을 분리한다](../../../../06_testing_performance/performance/performance/rendering-jank-is-frame-deadline-failure.md)

---

### 출처 및 공식 문서

- [Compose 성능 모범 사례](https://developer.android.com/develop/ui/compose/performance/bestpractices)
- [Compose에서 lifecycle을 고려한 Flow 수집](https://developer.android.com/develop/ui/compose/state#other-supported-types-of-state)
