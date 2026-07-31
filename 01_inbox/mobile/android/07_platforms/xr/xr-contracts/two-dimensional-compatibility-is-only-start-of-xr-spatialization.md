# 2D 호환 실행은 XR 공간화의 시작점일 뿐이다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

기존 Android 앱을 XR 환경의 2D 패널로 띄우는 것은 좋은 시작점이다. 하지만 XR의 제품 가치는 패널을 많이 띄우는 데서 끝나지 않고, 사용자의 시야, 거리, 주변 공간, 입력 맥락에 맞게 기능을 공간화할 때 생긴다.

## 판단 기준

- 정보 입력과 설정처럼 평면 UI가 더 빠른 작업은 2D 패널로 유지한다.
- 위치, 크기, 깊이, 실제 공간과의 관계가 의미를 만드는 기능만 공간화한다.
- 3D object나 immersive environment는 제품 과업을 단축하거나 이해를 높일 때 도입한다.
- business state와 화면 state는 2D/공간 표현 사이에서 공유하되, spatial session state는 별도 입력으로 둔다.

## 관련 문서

- [Android XR은 평면 앱 포트가 아니라 공간 폼 팩터다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/android-xr-is-spatial-form-factor-not-flat-port.md)
- [Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/compose-for-xr-extends-compose-with-subspace-and-spatial-components.md)
- [SceneCore는 3D entity와 공간 환경을 다루는 계층이다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/scenecore-manages-3d-entities-and-spatial-environments.md)

공식 문서: [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
