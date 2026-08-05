---
title: compose-layout-animation-accessibility
tags: [android, compose/ui, jetpack-compose]
aliases: [Compose accessibility, Compose layout, Compose UI]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Compose Layout, Animation, Accessibility 지침서

Jetpack Compose의 UI 시스템은 **레이아웃 측정 및 배치(Single-pass Layout), 값 및 상태 기반 애니메이션(Animation Pipeline), 픽셀 외적 의미를 전달하는 접근성 트리를 통한 세맨틱스(Semantics)**의 3대 핵심 기둥으로 구성된다.

정본 묶음: [Compose UI contracts](./compose-ui-contracts/compose-ui-contracts.md)

---

### 서브시스템 핵심 원칙 (What / Why / How)

1. **단일 패스 레이아웃 (Single-pass Layout)**
   - **What**: 부모 노드가 자식 노드에게 제약 조건(`Constraints`)을 하향 전달하고, 자식이 크기를 결정하여 복귀하면 부모가 위치를 배치하는 1회성 트리 측정 모델이다.
   - **Why**: 기존 View System의 고질적 성능 문제였던 $O(2^N)$ 복수 패스 재측정(Double Taxation / Multi-pass Measurement)을 구조적으로 방지한다.
   - **How**: 부모가 `Measurable.measure(constraints)`를 호출하여 단 1회 `Placeable`을 획득하도록 런타임이 측정 검증을 강제한다.

2. **선언적 애니메이션 시스템 (Declarative Motion)**
   - **What**: UI 상태의 변화에 맞춰 속성값이 시간에 따라 부드럽게 보간(Interpolation)되도록 묘사하는 물리/시간 기반 애니메이션 엔진이다.
   - **Why**: 명령형 `ObjectAnimator`의 이탈/동기화 버그를 제거하고 상태 변경과 애니메이션 반응을 일체화한다.
   - **How**: `animateAsState`, `updateTransition`, `Animatable` API를 기반으로 `AnimationSpec`(Spring, Tween)을 적용하여 Frame 틱마다 상태를 재계산한다.

3. **세맨틱스 접근성 트리 (Semantics Tree)**
   - **What**: LayoutNode 트리와 병렬로 존재하는 메타데이터 트로서, UI의 시각적 요소에 담긴 의미(Role, Label, Action)를 서술하는 구조체다.
   - **Why**: 시각 장애인을 위한 TalkBack 등의 접근성 서비스 및 자동화 UI 테스트 툴이 화면의 시각적 픽셀이 아닌 고유 의미를 이해할 수 있도록 지원한다.
   - **How**: `Modifier.semantics`를 통해 정보를 노드에 바인딩하고, `mergeDescendants` 또는 `clearAndSetSemantics`로 접근성 탐색 경계를 제어한다.

---

### 정본 계약 순서

- [Compose layout measures children under parent constraints](./compose-ui-contracts/compose-layout-measures-children-under-parent-constraints.md)
- [Modifier order changes layout draw and input wrappers](./compose-ui-contracts/modifier-order-changes-layout-draw-and-input-wrappers.md)
- [Size modifiers interpret requested size inside incoming constraints](./compose-ui-contracts/size-modifiers-interpret-requested-size-inside-incoming-constraints.md)
- [Custom Layout measures and places children explicitly](./compose-ui-contracts/custom-layout-measures-and-places-children-explicitly.md)
- [Intrinsic measurement and SubcomposeLayout solve special measurement problems](./compose-ui-contracts/intrinsic-measurement-and-subcompose-layout-solve-special-measurement-problems.md)
- [Compose animation API is selected by change unit and control level](./compose-ui-contracts/compose-animation-api-is-selected-by-change-unit-and-control-level.md)
- [AnimationSpec defines time physics and repeat policy](./compose-ui-contracts/animation-spec-defines-time-physics-and-repeat-policy.md)
- [Value animation APIs separate single target transition infinite and coroutine control](./compose-ui-contracts/value-animation-apis-separate-single-target-transition-infinite-and-coroutine-control.md)
- [Semantics Tree makes UI meaning visible to accessibility and tests](./compose-ui-contracts/semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md)
- [Semantics merging clearing and traversal control the unit of meaning](./compose-ui-contracts/semantics-merging-clearing-and-traversal-control-the-unit-of-meaning.md)
- [Accessibility quality requires service scanner and Semantics verification](./compose-ui-contracts/accessibility-quality-requires-service-scanner-and-semantics-verification.md)
- [Visual information and gestures need readable meaning and alternate actions](./compose-ui-contracts/visual-information-and-gestures-need-readable-meaning-and-alternate-actions.md)

---

관련 상위 문서: [Jetpack Compose 런타임과 상태 모델의 기본 개념](../runtime/compose-runtime-and-state-model.md)

검증일: 2026-08-05. Compose UI, Layout, Animation, Accessibility 공식 가이드를 대조하여 3대 핵심 기둥 서술 및 정본 문서 매핑을 정밀 보강했다.
