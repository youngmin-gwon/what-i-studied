---
title: compose-ui-contracts
tags: [android, compose/ui, jetpack-compose]
aliases: [Compose UI contracts]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Compose UI contracts

- [Compose layout은 부모 제약 안에서 자식을 측정하고 배치한다](./compose-layout-measures-children-under-parent-constraints.md)
- [Modifier 순서는 layout, draw, input wrapper의 적용 순서를 바꾼다](./modifier-order-changes-layout-draw-and-input-wrappers.md)
- [Size modifier는 incoming constraint 안에서 요청 크기를 해석한다](./size-modifiers-interpret-requested-size-inside-incoming-constraints.md)
- [Material 3 Expressive는 크기, Shape, 타이포그래피, 패딩 토큰과 Shape Morphing을 결합한다](./m3-expressive-bundles-size-shape-typography-padding-and-shape-morphing.md)
- [Custom Layout은 자식 측정과 배치를 직접 책임진다](./custom-layout-measures-and-places-children-explicitly.md)
- [Intrinsic measurement와 **SubcomposeLayout**(상위 레이아웃 계산 중 하위 요소 측정 결과를 바탕으로 하위 Composition을 동적으로 구성하는 레이아웃 API)은 특수한 측정 문제를 해결한다](./intrinsic-measurement-and-subcompose-layout-solve-special-measurement-problems.md)
- [Compose animation API는 변경 단위와 제어 수준으로 선택한다](./compose-animation-api-is-selected-by-change-unit-and-control-level.md)
- [값 애니메이션 API는 단일 target, transition, infinite, coroutine 제어로 나뉜다](./value-animation-apis-separate-single-target-transition-infinite-and-coroutine-control.md)
- [AnimationSpec은 시간, 물리, 반복 정책을 정의한다](./animation-spec-defines-time-physics-and-repeat-policy.md)
- [**Semantics**(접근성 서비스 및 UI 테스트 프레임워크가 읽을 수 있도록 UI 요소의 의미적 정보를 캡슐화한 정보 트리) Tree는 UI 의미를 접근성 서비스와 테스트에 드러낸다](./semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md)
- [시각 정보와 제스처에는 읽을 수 있는 의미와 대체 동작이 필요하다](./visual-information-and-gestures-need-readable-meaning-and-alternate-actions.md)
- [Semantics 병합, 정리, 탐색 순서는 의미 단위를 조정한다](./semantics-merging-clearing-and-traversal-control-the-unit-of-meaning.md)
- [접근성 품질은 서비스, 검사기, Semantics 테스트로 검증한다](./accessibility-quality-requires-service-scanner-and-semantics-verification.md)

### 다른 클러스터로 이동한 주제

- [Glance는 Compose UI가 아니라 RemoteViews 위젯 경계로 렌더링한다](../../../app-widgets/app-widget-contracts/glance-renders-app-widgets-through-remoteviews-not-compose-ui.md) - App Widget 전용 클러스터([App Widget 계약](../../../app-widgets/app-widget-contracts/app-widget-contracts.md))로 이전했다.
