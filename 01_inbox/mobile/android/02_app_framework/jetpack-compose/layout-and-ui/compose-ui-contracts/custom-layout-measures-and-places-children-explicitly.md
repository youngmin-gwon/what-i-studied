---
title: custom-layout-measures-and-places-children-explicitly
tags: [android, compose/ui, jetpack-compose]
aliases: [custom layout, MeasurePolicy]
date modified: 2026-08-03 18:10:29 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Custom Layout measures and places children explicitly

`Layout` 과 `MeasurePolicy` 는 child `Measurable` 을 주어진 constraints 로 측정하고, 얻은 `Placeable` 을 `layout(width, height)` 블록에서 배치하는 API 다. `Modifier.layout` 은 별도 layout composable 을 만들지 않고 한 node 의 측정과 배치만 바꿀 때 쓴다.

Compose UI 는 일반적으로 child 를 실제로 한 번만 측정하게 한다. 같은 child 를 여러 constraints 로 반복 측정하는 방식은 허용되지 않으며, 필요한 사전 크기 정보는 intrinsic API 같은 별도 경로로 다룬다.

커스텀 layout 은 parent size 결정, child placement, RTL 을 고려한 `placeRelative`, alignment line, constraints 준수까지 직접 책임진다.

관련 노트: [Intrinsic measurement와 SubcomposeLayout은 특수한 측정 문제를 해결한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/intrinsic-measurement-and-subcompose-layout-solve-special-measurement-problems.md), [Compose layout과 image 비용은 프레임 예산 안에서 관리한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-layout-and-image-cost-must-be-budgeted.md)

출처: [Custom layouts](https://developer.android.com/develop/ui/compose/layouts/custom)
