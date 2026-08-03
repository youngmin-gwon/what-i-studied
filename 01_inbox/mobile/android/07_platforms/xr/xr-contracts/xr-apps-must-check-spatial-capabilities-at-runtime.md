---
title: "XR 앱은 공간 capability를 실행 중에 확인해야 한다"
tags: ["android", "android/platforms"]
---

# XR 앱은 공간 capability를 실행 중에 확인해야 한다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

XR 앱은 어떤 공간 기능이 항상 가능하다고 가정하면 안 된다. Home Space, Full Space, 기기 종류, 사용자 조작, 시스템 상태에 따라 spatial UI, 3D content, environment, passthrough, spatial audio 같은 capability가 달라질 수 있다.

## 실무 규칙

- 현재 환경에서 가능한 기능을 `Session.scene.spatialCapabilities`로 확인한 뒤 UI를 선택한다.
- 공간 기능이 없을 때 2D fallback이 자연스럽게 남아야 한다.
- capability 변화는 일회성 초기화 값이 아니라 UI state 입력으로 취급하고 `addSpatialCapabilitiesChangedListener`로 갱신을 관찰한다.
- 권한이 필요한 perception 또는 scene understanding 기능은 권한 요청과 실패 UI를 함께 설계한다.

## 관련 문서

- [Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/compose-for-xr-extends-compose-with-subspace-and-spatial-components.md)
- [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)

공식 문서: [Check for spatial capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities), [Transition from Home Space to Full Space](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space)

검증일: 2026-08-03. capability는 기기뿐 아니라 Home Space/Full Space 전환과 시스템·사용자 조작으로도 달라질 수 있다.
