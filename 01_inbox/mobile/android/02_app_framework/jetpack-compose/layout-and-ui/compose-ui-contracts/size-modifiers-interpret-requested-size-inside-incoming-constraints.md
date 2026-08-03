---
title: size-modifiers-interpret-requested-size-inside-incoming-constraints
tags: [android, compose/ui, jetpack-compose]
aliases: [fillMaxSize, requiredSize, size modifier]
date modified: 2026-08-03 18:10:34 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Size modifiers interpret requested size inside incoming constraints

`size`, `width`, `height` 계열 modifier 는 요청 크기를 incoming constraints 안에서 해석한다. 앞쪽 modifier 가 exact constraint 를 만들면 뒤쪽 modifier 의 요청은 그 제약 안으로 맞춰질 수 있다.

`requiredSize` 계열은 incoming constraint 를 재정의하려는 강한 요청이다. 이때 parent 가 보고받는 크기와 실제 child 배치가 다르게 보일 수 있어 overflow, clipping, alignment 를 함께 봐야 한다.

`fillMax*` 는 허용된 최대 크기를 채우도록 최소 제약까지 끌어올릴 수 있고, `wrapContentSize` 는 child 가 더 작게 측정될 수 있도록 제약을 완화한 뒤 남는 공간에서 배치를 조정한다.

관련 노트: [Compose layout은 부모 제약 안에서 자식을 측정하고 배치한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/compose-layout-measures-children-under-parent-constraints.md), [Modifier 순서는 layout, draw, input wrapper의 적용 순서를 바꾼다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/modifier-order-changes-layout-draw-and-input-wrappers.md)

출처: [Constraints and modifier order](https://developer.android.com/develop/ui/compose/layouts/constraints-modifiers)
