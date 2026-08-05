---
title: compose-layout-animation-accessibility
tags: [android, compose/ui, jetpack-compose]
aliases: [Compose accessibility, Compose layout, Compose UI]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Compose layout animation accessibility

Compose UI 정본은 Runtime mental model 과 분리해 layout, modifier, custom measurement, animation, semantics, app widget surface 를 다룬다. 이 지도는 기존 `layout-and-ui` 문서를 UI 계약 단위로 다시 묶는다.

정본 묶음: [Compose UI contracts](./compose-ui-contracts/compose-ui-contracts.md)

### Layout

- [Compose layout은 부모 제약 안에서 자식을 측정하고 배치한다](./compose-ui-contracts/compose-layout-measures-children-under-parent-constraints.md)
- [Modifier 순서는 layout, draw, input wrapper의 적용 순서를 바꾼다](./compose-ui-contracts/modifier-order-changes-layout-draw-and-input-wrappers.md)
- [Size modifier는 incoming constraint 안에서 요청 크기를 해석한다](./compose-ui-contracts/size-modifiers-interpret-requested-size-inside-incoming-constraints.md)
- [Custom Layout은 자식 측정과 배치를 직접 책임진다](./compose-ui-contracts/custom-layout-measures-and-places-children-explicitly.md)
- [Intrinsic measurement와 **SubcomposeLayout**(상위 레이아웃 계산 중 하위 요소 측정 결과를 바탕으로 하위 Composition을 동적으로 구성하는 레이아웃 API)은 특수한 측정 문제를 해결한다](./compose-ui-contracts/intrinsic-measurement-and-subcompose-layout-solve-special-measurement-problems.md)

### Animation

- [Compose animation API는 변경 단위와 제어 수준으로 선택한다](./compose-ui-contracts/compose-animation-api-is-selected-by-change-unit-and-control-level.md)
- [값 애니메이션 API는 단일 target, transition, infinite, coroutine 제어로 나뉜다](./compose-ui-contracts/value-animation-apis-separate-single-target-transition-infinite-and-coroutine-control.md)
- [AnimationSpec은 시간, 물리, 반복 정책을 정의한다](./compose-ui-contracts/animation-spec-defines-time-physics-and-repeat-policy.md)

### Accessibility

- [**Semantics**(접근성 서비스 및 UI 테스트 프레임워크가 읽을 수 있도록 UI 요소의 의미적 정보를 캡슐화한 정보 트리) Tree는 UI 의미를 접근성 서비스와 테스트에 드러낸다](./compose-ui-contracts/semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md)
- [시각 정보와 제스처에는 읽을 수 있는 의미와 대체 동작이 필요하다](./compose-ui-contracts/visual-information-and-gestures-need-readable-meaning-and-alternate-actions.md)
- [Semantics 병합, 정리, 탐색 순서는 의미 단위를 조정한다](./compose-ui-contracts/semantics-merging-clearing-and-traversal-control-the-unit-of-meaning.md)
- [접근성 품질은 서비스, 검사기, Semantics 테스트로 검증한다](./compose-ui-contracts/accessibility-quality-requires-service-scanner-and-semantics-verification.md)

### Widget Surface

App widget 전용 계약(lifecycle, RemoteViews 제약, 설정 Activity, 갱신 주기)은 별도 클러스터로 이전했다.

- [App Widget 계약](../../app-widgets/app-widget-contracts/app-widget-contracts.md) - [Glance는 Compose UI가 아니라 RemoteViews 위젯 경계로 렌더링한다](../../app-widgets/app-widget-contracts/glance-renders-app-widgets-through-remoteviews-not-compose-ui.md) 포함.

관련 Runtime 지도: [Compose runtime and state model](../runtime/compose-runtime-and-state-model.md)

관련 Design System 지도: [Compose design system](../design-system-and-architecture/compose-design-system.md)

관련 성능 지도: [Compose 성능 계약](../performance/compose-performance-contracts/compose-performance-contracts.md)
