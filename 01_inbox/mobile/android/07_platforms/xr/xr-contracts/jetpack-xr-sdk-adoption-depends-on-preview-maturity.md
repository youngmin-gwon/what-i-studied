# Jetpack XR SDK는 preview 성숙도를 전제로 채택해야 한다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

Jetpack XR SDK는 Android XR 개발을 위한 공식 Jetpack 계층이지만, 현재는 Developer Preview 성격의 라이브러리를 포함한다. 따라서 제품 적용 여부는 API 안정성, 기기 지원, 알려진 이슈, 배포 채널을 확인한 뒤 결정해야 한다.

## 실무 규칙

- Compose for XR, SceneCore, ARCore for Jetpack XR, XR Runtime의 release notes를 각각 확인한다.
- alpha API 이름과 동작은 바뀔 수 있으므로 앱 핵심 구조에 직접 퍼뜨리지 않는다.
- XR 전용 코드는 일반 Android UI와 경계를 두고 feature flag 또는 별도 module로 격리한다.
- 공식 sample과 codelab 기준으로 현재 가능한 surface를 먼저 검증한다.
- 기기명이나 출시 상태는 문서화 시점 기준 정보로 적고 주기적으로 갱신한다.

## 관련 문서

- [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
- [Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/compose-for-xr-extends-compose-with-subspace-and-spatial-components.md)

공식 문서: [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk), [Jetpack Compose for XR release notes](https://developer.android.com/jetpack/androidx/releases/xr-compose)

기준일: 2026-07-31. Jetpack Compose for XR 최신 alpha는 2026-07-15의 `1.0.0-alpha16`으로 확인했다.
