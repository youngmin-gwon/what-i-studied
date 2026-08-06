---
title: heavy-work-does-not-belong-in-composition
tags: [android, compose/performance, jetpack-compose]
aliases: []
date modified: 2026-08-06 14:48:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## 무거운 작업은 composition 안에서 실행하지 않는다

Composable은 최초 composition뿐 아니라 state 변화로 반복 실행될 수 있고 보통 main thread에서 실행된다. 파일 I/O, network, 큰 정렬·파싱·bitmap decode를 본문에서 호출하면 재실행 횟수와 frame 지연이 결합된다. `remember`는 결과 수명을 보존할 뿐 작업을 background thread로 옮기지 않는다.

```kotlin
// 피해야 할 형태: remember 블록도 composition 중 main thread에서 실행된다.
@Composable
fun Report(rows: List<RowData>) {
    val summary = remember(rows) { expensiveSummarize(rows) }
    Text(summary)
}
```

실행 메커니즘을 분리해 CPU 작업은 UI 밖의 소유자와 적절한 dispatcher로 옮기고, UI에는 표시 상태만 전달한다.

```kotlin
class ReportViewModel(
    repository: ReportRepository,
) : ViewModel() {
    val summary = repository.rows
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
fun ReportScreen(viewModel: ReportViewModel) {
    val summary by viewModel.summary.collectAsStateWithLifecycle()
    Text(summary)
}
```

I/O 작업은 repository가 `Dispatchers.IO` 등 적합한 경계에서 수행한다. `LaunchedEffect`도 main dispatcher에서 시작하므로 그 안에서 무거운 동기 작업을 직접 실행하면 해결되지 않는다. 입력 변경 취소가 중요하면 `mapLatest` 같은 정책을 명시한다.

Perfetto trace에서 composition 구간과 main-thread runnable을 확인하고, 같은 입력의 FrameTimingMetric을 이동 전후 비교한다. startup에 필요한 작업이면 TTID뿐 아니라 콘텐츠가 실제 준비된 TTFD도 함께 측정한다. 화면을 떠난 뒤 작업 취소·공유 정책이 의도대로인지 coroutine test로 검증한다.

관련 노트: [Compose 성능 최적화는 측정·진단·개선 순환으로 진행한다](./compose-performance-starts-with-measure-debug-improve-loop.md), [렌더링 성능은 프레임 지연의 원인을 분리한다](../../../../06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

출처: [Compose 성능 모범 사례](https://developer.android.com/develop/ui/compose/performance/bestpractices), [Compose에서 lifecycle을 고려한 Flow 수집](https://developer.android.com/develop/ui/compose/state#other-supported-types-of-state)
