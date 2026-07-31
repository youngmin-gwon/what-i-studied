# Compose layout과 image 비용은 프레임 예산 안에서 관리한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Compose 성능 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)
관련 노트: [렌더링 성능은 프레임 지연의 원인을 분리한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

Compose UI도 layout, measure, draw, image loading 비용을 가진다.

`BoxWithConstraints`처럼 유용한 layout 도구도 남용하면 하위 tree의 재측정 비용을 키울 수 있다.

비동기 이미지는 표시 크기와 디코딩 크기를 맞추고, placeholder와 error 상태를 안정적으로 제공해야 한다.

큰 이미지, 반복되는 clipping, shadow, alpha 합성은 GPU 비용을 늘릴 수 있다.

Lazy list에서는 key와 contentType을 적절히 제공해 item 재사용과 상태 보존을 돕는다.

layout 변경은 접근성과 화면 구조를 깨지 않는 범위에서 수행한다.

공식 참고: [Compose lazy layout 성능](https://developer.android.com/develop/ui/compose/lists#performance)
