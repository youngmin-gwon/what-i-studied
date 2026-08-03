---
title: compose-layout-measures-children-under-parent-constraints
tags: [android, compose/ui, jetpack-compose]
aliases: [Compose layout, Constraints]
date modified: 2026-08-03 18:10:27 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Compose layout measures children under parent constraints

Compose layout 은 부모가 자식에게 `Constraints` 를 전달하고, 자식이 그 제약 안에서 크기를 보고하며, 부모가 최종 크기와 자식 위치를 정하는 과정이다. 핵심 값은 최소/최대 width 와 height 다.

Layout phase 는 Composition phase 와 다르다. Composition 은 무엇을 만들지 결정하고, layout 은 만들어진 node 를 측정하고 배치한다.

제약은 bounded, unbounded, exact, 조합 형태로 들어올 수 있다. 커스텀 layout 이나 modifier 를 만들 때는 이 제약을 지키면서 parent/child size contract 를 깨지 않게 해야 한다.

관련 노트: [Compose frame pipeline은 composition, layout, drawing으로 나뉜다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-frame-pipeline-is-split-into-composition-layout-and-drawing.md), [Modifier 순서는 layout, draw, input wrapper의 적용 순서를 바꾼다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/modifier-order-changes-layout-draw-and-input-wrappers.md)

출처: [Compose layouts basics](https://developer.android.com/develop/ui/compose/layouts/basics), [Compose phases](https://developer.android.com/develop/ui/compose/phases)
