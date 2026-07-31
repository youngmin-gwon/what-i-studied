---
title: "Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다"
tags: ["android", "android/platforms"]
---

# Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

Compose for XR은 Compose mental model을 버리는 새 UI 도구가 아니다. 기존 Compose의 선언형 UI를 유지하면서 `Subspace`, `SpatialPanel`, `SpatialRow`, `SpatialColumn`, `Orbiter` 같은 공간 배치 개념을 추가한다.

## 핵심 개념

- `Subspace`는 3D 콘텐츠와 공간 UI를 놓는 공간 계층이다.
- `SpatialPanel`은 기존 2D UI 또는 콘텐츠를 공간 패널로 배치한다.
- `SubspaceModifier`는 크기, 깊이, 위치, 이동, 크기 조절 같은 공간 속성을 붙인다.
- Spatialized component는 공간 기능이 비활성화되면 2D 대응 요소로 fallback될 수 있다.

## 실무 규칙

- 공간 UI를 호출할 수 있는 위치와 일반 Compose UI 위치를 섞지 않는다.
- panel 크기와 거리 조정은 사용자의 가독성과 조작 가능성을 기준으로 정한다.
- back 처리와 focus 이동은 XR navigation 입력까지 포함해 검증한다.
- 기존 Compose 상태 모델은 유지하되, 공간 capability와 session state를 별도 입력으로 둔다.

## 관련 문서

- [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)
- [XR 앱은 공간 capability를 실행 중에 확인해야 한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-apps-must-check-spatial-capabilities-at-runtime.md)

공식 문서: [Develop spatial UI with Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose)
