---
title: ui-system
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:12:11 +09:00
date created: 2026-07-31 23:38:40 +09:00
---

## Android UI System Contracts

Android UI 문서는 View System, Compose, list rendering, modern system UI 요구사항을 서로 다른 계약으로 나눠 읽는다.

### 정본 노트

- [Android UI는 imperative View에서 declarative Compose로 중심이 이동했다](./android-ui-is-moving-from-imperative-views-to-declarative-compose.md)
- [View System은 object tree를 변경하고 Compose는 state에서 UI를 재계산한다](./view-system-mutates-object-tree-while-compose-recomputes-ui-from-state.md)
- [RecyclerView와 LazyColumn은 같은 목록 문제를 푸는 다른 렌더링 계약이다](./recyclerview-and-lazycolumn-are-list-rendering-patterns-not-identical-apis.md)
- [Modern Android UI는 edge-to-edge, insets, back, adaptive layout을 함께 다룬다](./modern-android-ui-requires-edge-to-edge-insets-back-and-adaptive-layout.md)

관련 지도: [Compose Runtime과 상태 모델](../../../jetpack-compose/runtime/compose-runtime-and-state-model.md), [Compose Layout, Animation, Accessibility](../../../jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md)
