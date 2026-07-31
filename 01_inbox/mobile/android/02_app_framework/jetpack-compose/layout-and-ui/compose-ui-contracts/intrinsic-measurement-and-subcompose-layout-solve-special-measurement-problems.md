---
title: Intrinsic measurement and SubcomposeLayout solve special measurement problems
tags: [android, jetpack-compose, compose/ui]
aliases: [Intrinsic measurement, SubcomposeLayout]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# Intrinsic measurement and SubcomposeLayout solve special measurement problems

Intrinsic measurement는 실제 측정 전에 child가 특정 축에서 필요로 하는 자연 크기를 질의하는 API다. 이것은 일반적인 “child를 두 번 측정한다”와 같은 의미가 아니며, custom layout의 기본 intrinsic 추정이 맞지 않을 때 override한다.

`SubcomposeLayout`은 먼저 일부 content를 compose/measure한 결과를 바탕으로 뒤 content를 compose해야 하는 특수 문제를 해결한다. 일반 layout의 기본 도구가 아니라 composition과 measurement 순서를 의도적으로 엮는 API다.

`LazyColumn`이나 `BoxWithConstraints` 내부 구현을 앱 코드의 SubcomposeLayout 사용 계약처럼 단정하지 않는다. 정본에는 “측정 결과로 후속 content 구성을 결정해야 할 때 검토한다”는 수준을 유지한다.

관련 노트: [Custom Layout은 자식 측정과 배치를 직접 책임진다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/custom-layout-measures-and-places-children-explicitly.md), [Compose frame pipeline은 composition, layout, drawing으로 나뉜다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-frame-pipeline-is-split-into-composition-layout-and-drawing.md)

출처: [Intrinsic measurements](https://developer.android.com/develop/ui/compose/layouts/intrinsic-measurements), [SubcomposeLayout API](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/SubcomposeLayout)
