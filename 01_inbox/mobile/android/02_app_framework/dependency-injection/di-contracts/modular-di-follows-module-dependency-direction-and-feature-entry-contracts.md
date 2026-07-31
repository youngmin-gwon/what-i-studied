# 멀티 모듈 DI는 module dependency 방향과 feature entry 계약을 따른다

DI graph가 모듈 의존성 방향을 거꾸로 만들면 build graph와 runtime graph가 충돌한다. base/app module은 feature가 요구하는 contract를 알 수 있어야 하고, feature는 자신이 소유한 implementation과 entry를 명확히 노출해야 한다.

Navigation, dynamic feature, feature API module, implementation module이 섞일수록 graph를 하나로 크게 만드는 것보다 boundary별 dependency contract를 분리하는 편이 낫다.

관련 노트: [Navigation contracts](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md), [Dynamic feature module](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md).
