# Compose 안정성과 strong skipping은 skippability에 영향을 준다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Compose 성능 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)
관련 정본: [렌더링 성능은 프레임 지연의 원인을 분리한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

Compose가 composable 호출을 건너뛰려면 입력이 안정적으로 비교될 수 있어야 한다.

불안정 타입은 값이 바뀌지 않았어도 recomposition에서 더 넓게 다시 실행될 수 있다.

컬렉션 타입은 일반적으로 mutable 가능성을 보수적으로 해석하므로 불안정하게 판단될 수 있다.

불변 컬렉션, 안정적인 wrapper, 명시적인 stability 설정은 이 문제를 줄이는 선택지다.

Kotlin 2.0.20부터 Compose의 strong skipping mode는 기본 활성화되어, 불안정 인자를 받는 composable도 더 적극적으로 건너뛸 수 있다.

그래도 안정성 문제를 먼저 추측해 고치는 것은 위험하다.

Compose compiler report와 실제 성능 측정을 확인한 뒤 타입 안정성 개선을 적용한다.

공식 참고: [Compose 안정성 진단](https://developer.android.com/develop/ui/compose/performance/stability)

공식 참고: [Strong skipping](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping)
