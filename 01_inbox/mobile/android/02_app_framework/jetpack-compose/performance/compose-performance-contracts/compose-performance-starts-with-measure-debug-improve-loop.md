# Compose 성능 최적화는 measure, debug, improve 순환으로 진행한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Compose 성능 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)
관련 정본: [렌더링 성능은 프레임 지연의 원인을 분리한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

Compose 성능 문제도 추측으로 고치지 않는다.

먼저 어떤 사용자 여정이 느린지 정하고, 같은 입력과 같은 기기 조건에서 측정한다.

그 다음 trace, recomposition 정보, frame timing을 확인해 병목을 좁힌다.

마지막으로 작은 변경을 적용하고 같은 조건에서 다시 측정한다.

이 순환이 없으면 `remember`, `derivedStateOf`, lazy layout 교체 같은 처방이 실제 사용자 성능을 개선했는지 알 수 없다.

Compose는 필요한 부분만 다시 실행할 수 있지만, 모든 코드가 자동으로 빠르다는 뜻은 아니다.

상태 읽기 위치, 비싼 계산, 이미지 디코딩, layout 구조, 메인 스레드 작업은 여전히 프레임 예산을 소비한다.

따라서 Compose 성능 노트의 첫 질문은 “어떤 API를 쓸까”가 아니라 “어느 frame 또는 startup 구간이 느린가”여야 한다.

공식 참고: [Jetpack Compose 성능](https://developer.android.com/develop/ui/compose/performance)
