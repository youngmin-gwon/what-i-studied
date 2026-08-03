---
title: compose-for-xr-extends-compose-with-subspace-and-spatial-components
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:22 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## Compose for XR 은 기존 Compose 를 subspace 와 spatial component 로 확장한다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

Compose for XR 은 Compose mental model 을 버리는 새 UI 도구가 아니다. 기존 Compose 의 선언형 UI 를 유지하면서 `Subspace`, `SpatialPanel`, `SpatialRow`, `SpatialColumn`, `Orbiter` 같은 공간 배치 개념을 추가한다.

### 핵심 개념

- `Subspace` 는 3D 콘텐츠와 공간 UI 를 놓는 공간 계층이다.
- `SpatialPanel` 은 기존 2D UI 또는 콘텐츠를 공간 패널로 배치한다.
- `SubspaceModifier` 는 크기, 깊이, 위치, 이동, 크기 조절 같은 공간 속성을 붙인다.
- Spatialized component 를 쓸 수 없는 상태에는 제품이 명시적으로 2D 대응 UI 를 유지해야 한다.

### 실무 규칙

- 공간 UI 를 호출할 수 있는 위치와 일반 Compose UI 위치를 섞지 않는다.
- panel 크기와 거리 조정은 사용자의 가독성과 조작 가능성을 기준으로 정한다.
- back 처리와 focus 이동은 XR navigation 입력까지 포함해 검증한다.
- 기존 Compose 상태 모델은 유지하되, 공간 capability 와 session state 를 별도 입력으로 둔다.

### 실행 경계

공간화는 Full Space 에서만 지원된다. Home Space 에서는 앱이 다른 앱과 함께 2D 패널로 실행되므로, `LocalSession` 에서 요청한 space 전환 결과와 현재 capability 를 확인한 뒤 공간 UI 를 노출한다. Compose for XR API 가 존재한다는 사실만으로 현재 공간화가 가능하다고 판단하지 않는다.

### 관련 문서

- [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)
- [XR 앱은 공간 capability를 실행 중에 확인해야 한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-apps-must-check-spatial-capabilities-at-runtime.md)

공식 문서: [Develop spatial UI with Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose)

검증일: 2026-08-03. Compose API 안정성은 [XR Compose releases](https://developer.android.com/jetpack/androidx/releases/xr-compose), space mode 계약은 [Transition from Home Space to Full Space](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space) 에서 확인한다.
