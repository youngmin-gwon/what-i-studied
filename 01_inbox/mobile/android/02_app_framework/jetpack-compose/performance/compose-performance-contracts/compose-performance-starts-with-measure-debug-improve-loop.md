---
title: compose-performance-starts-with-measure-debug-improve-loop
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compose 성능 최적화는 measure, debug, improve 순환으로 진행한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](../../../../06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
배경 지식: [프로세스 생명주기 및 상태](../../../../../../operating-systems/process-states-lifecycle.md)

관련 지도: [Compose 성능 계약](./compose-performance-contracts.md)

관련 노트: [렌더링 성능은 프레임 지연의 원인을 분리한다](../../../../06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

Compose 성능 문제도 추측으로 고치지 않는다.

먼저 어떤 사용자 여정이 느린지 정하고, 같은 입력과 같은 기기 조건에서 측정한다.

그 다음 trace, recomposition 정보, frame timing 을 확인해 병목을 좁힌다.

trace 는 Android Studio Profiler 의 System Trace(Perfetto 기반)나 Macrobenchmark 라이브러리로 실제 기기에서 수집하고, Layout Inspector 의 recomposition count 표시로 어떤 composable 이 자주 다시 그려지는지 확인한다.

마지막으로 작은 변경을 적용하고 같은 조건에서 다시 측정한다.

이 순환이 없으면 `remember`, `**derivedStateOf**(고빈도 입력 상태 변경 중 최종 결과값이 뒤집힐 때만 Recomposition 스코프를 무효화하는 파생 상태 생성 API)`, lazy layout 교체 같은 처방이 실제 사용자 성능을 개선했는지 알 수 없다.

Compose 는 필요한 부분만 다시 실행할 수 있지만, 모든 코드가 자동으로 빠르다는 뜻은 아니다.

상태 읽기 위치, 비싼 계산, 이미지 디코딩, layout 구조, 메인 스레드 작업은 여전히 프레임 예산을 소비한다.

따라서 Compose 성능 노트의 첫 질문은 "어떤 API 를 쓸까"가 아니라 "어느 frame 또는 startup 구간이 느린가"여야 한다.

공식 참고: [Jetpack Compose 성능](https://developer.android.com/develop/ui/compose/performance)
