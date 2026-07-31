# SceneCore는 3D entity와 공간 환경을 다루는 계층이다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

SceneCore는 일반 화면 컴포저블을 배치하는 계층이 아니라 XR scene graph, entity, 3D model, spatial environment, spatial audio 같은 공간 객체를 다루는 계층이다.

## 언제 쓰는가

- 3D 모델을 UI 주변 또는 실제 공간 기준으로 배치해야 한다.
- panel보다 낮은 수준에서 entity 이동, 크기 조절, anchor, component를 제어해야 한다.
- spatial audio, environment, perception 기반 위치 지정이 제품 경험의 일부다.

## 경계

Compose for XR은 UI 선언과 공간 layout에 적합하다. SceneCore는 UI가 아닌 공간 객체와 scene graph 조작이 필요할 때 선택한다.

## 관련 문서

- [Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/compose-for-xr-extends-compose-with-subspace-and-spatial-components.md)
- [XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-quality-includes-performance-comfort-and-safety.md)

공식 문서: [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
