---
title: "Android UI System Contracts"
tags: ["android", "android/app-framework"]
---

# Android UI System Contracts

Android UI 문서는 View System, Compose, list rendering, modern system UI 요구사항을 서로 다른 계약으로 나눠 읽는다.

## 정본 노트

- [Android UI는 imperative View에서 declarative Compose로 중심이 이동했다](01_inbox/mobile/android/02_app_framework/ui/system/ui-system-contracts/android-ui-is-moving-from-imperative-views-to-declarative-compose.md)
- [View System은 object tree를 변경하고 Compose는 state에서 UI를 재계산한다](01_inbox/mobile/android/02_app_framework/ui/system/ui-system-contracts/view-system-mutates-object-tree-while-compose-recomputes-ui-from-state.md)
- [RecyclerView와 LazyColumn은 같은 목록 문제를 푸는 다른 렌더링 계약이다](01_inbox/mobile/android/02_app_framework/ui/system/ui-system-contracts/recyclerview-and-lazycolumn-are-list-rendering-patterns-not-identical-apis.md)
- [Modern Android UI는 edge-to-edge, insets, back, adaptive layout을 함께 다룬다](01_inbox/mobile/android/02_app_framework/ui/system/ui-system-contracts/modern-android-ui-requires-edge-to-edge-insets-back-and-adaptive-layout.md)

관련 지도: [Compose Runtime과 상태 모델](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Compose Layout, Animation, Accessibility](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md)
