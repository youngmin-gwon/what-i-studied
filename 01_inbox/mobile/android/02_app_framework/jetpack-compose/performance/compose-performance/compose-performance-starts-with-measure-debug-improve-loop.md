---
title: compose-performance-starts-with-measure-debug-improve-loop
tags: [android, compose/performance, jetpack-compose]
aliases: []
date modified: 2026-08-06 14:48:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compose 성능 최적화는 측정·진단·개선 순환으로 진행한다

측정 메커니즘의 단위는 API가 아니라 사용자 여정과 metric이다. 같은 기기·release 빌드·입력에서 baseline을 만들고, trace로 원인을 좁힌 다음 한 가지 변경을 다시 측정한다.

```kotlin
@RunWith(AndroidJUnit4::class)
class FeedScrollBenchmark {
    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()

    @Test
    fun scroll() = benchmarkRule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(FrameTimingMetric()),
        compilationMode = CompilationMode.Partial(),
        iterations = 10,
        startupMode = StartupMode.WARM,
        setupBlock = {
            pressHome()
            startActivityAndWait()
        },
    ) {
        device.findObject(By.res("feed"))
            .fling(Direction.DOWN)
    }
}
```

Macrobenchmark는 앱과 다른 test process에서 실제 사용자 동작을 반복한다. debug build의 profiler 체감과 섞지 말고 benchmark가 대상으로 삼는 release/profileable variant, compilation mode, device 상태를 결과에 기록한다.

```text
1. Measure: 느린 feed scroll + FrameTimingMetric baseline
2. Debug: Perfetto에서 긴 frame의 composition/layout/draw 또는 main-thread 작업 식별
3. Improve: 상태 읽기 이동, 계산 이동, layout 단순화 중 하나만 적용
4. Re-measure: 같은 benchmark 분포와 trace를 baseline과 비교
```

Layout Inspector의 [recomposition](../../runtime/recomposition.md)/skip count는 원인 후보를 찾는 진단 자료이지 사용자 성능 metric 자체가 아니다. `remember`, `derivedStateOf`, lazy layout 교체도 frame timing이나 startup 결과가 개선되지 않으면 성공으로 기록하지 않는다. 평균 하나보다 반복 측정 분포와 느린 frame 지표를 함께 본다.

관련 노트: [Compose layout과 image 비용은 프레임 예산 안에서 관리한다](./compose-layout-and-image-cost-must-be-budgeted.md), [렌더링 성능은 프레임 지연의 원인을 분리한다](../../../../06_testing_performance/performance/performance/rendering-jank-is-frame-deadline-failure.md)

출처: [Compose 성능](https://developer.android.com/develop/ui/compose/performance), [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
