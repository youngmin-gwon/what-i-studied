# 성능 최적화의 대전제: Loop Cycle (Measure -> Debug -> Improve)

상위 노트: [[jetpack-compose-performance-guidelines]]

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
