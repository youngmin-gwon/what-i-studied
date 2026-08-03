---
title: "Android XR은 평면 앱 포트가 아니라 공간 폼 팩터다"
tags: ["android", "android/platforms"]
---

# Android XR은 평면 앱 포트가 아니라 공간 폼 팩터다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

Android XR 대응은 기존 2D Android 앱을 큰 패널로 띄우는 것에서 시작할 수 있지만, 거기서 끝나면 공간 폼 팩터의 장점을 쓰지 못한다. XR 앱은 주변 공간, 시야, 거리, 입력 방식, 사용자의 신체적 편안함을 화면 설계의 일부로 다룬다.

## 구분

- 2D 호환 실행: 기존 Compose 또는 View UI를 XR 환경의 패널로 표시한다.
- 공간화: panel, orbiter, spatial layout, 3D model, spatial audio처럼 공간 속 위치와 깊이를 설계한다.
- 몰입 경험: 앱 환경, scene graph, perception, anchors 등 XR 전용 기능을 제품 경험에 통합한다.

## 시스템 UI 경계

Home Space는 여러 앱이 함께 있는 시스템 멀티태스킹 공간이고 Full Space는 앱이 몰입 기능을 사용할 수 있는 전면 공간이다. 앱은 현재 mode와 capability를 관찰하고 시스템이 제공하는 전환 경로를 존중한다. boundary, passthrough 고지, 권한 UI를 자체 장식처럼 숨기거나 대체하지 않는다.

## 관련 문서

- [Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/compose-for-xr-extends-compose-with-subspace-and-spatial-components.md)
- [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)

공식 문서: [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)

검증일: 2026-08-03. [Transition from Home Space to Full Space](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space), [Android XR app quality](https://developer.android.com/docs/quality-guidelines/android-xr)
