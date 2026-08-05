---
title: android-app-architecture
tags: [android, android/architecture]
aliases: ["Android App Architecture"]
date modified: 2026-08-05 11:21:16 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android 앱 아키텍처는 UI 패턴보다 수명과 OS 진입점을 나누는 문제다

Android 앱 아키텍처는 UI 패턴 이름보다 owner, lifetime, OS entry point 를 먼저 나누는 문제다.

### 정본 지도

- [Android App Components](./app-components/android-app-components.md) - Activity, Service, BroadcastReceiver, ContentProvider 를 OS entry point 로 정리한다.
- [Android Context Boundaries](./context-and-modularity/android-context-boundaries.md) - Context 종류와 lifetime, leak risk, Compose `LocalContext` 를 정리한다.
- [Jetpack Architecture Map](./jetpack-architecture/android-jetpack-architecture-map.md) - Jetpack architecture guidance 를 기존 정본 map 으로 연결한다.
- [Android State Management](./state-management/android-state-management.md) - ViewModel, UI state, reducer, saved state 의 정본.
- [Android Dependency Injection](../dependency-injection/android-dependency-injection-map.md) - object graph, binding, scope, Hilt/Metro, test override 의 정본.
- [Multiplatform Contracts](./multiplatform-contracts/multiplatform-contracts.md) - Kotlin Multiplatform 이 무엇을 공유하고 무엇을 플랫폼별로 남기는지, `expect`/`actual` 계약을 정리한다.

### 읽는 기준

앱이 외부에서 어떻게 호출되는지가 궁금하면 app components 로 간다. 어떤 Context 를 전달해야 하는지가 궁금하면 context boundary 로 간다. ViewModel, Flow, Room, WorkManager, Navigation, Hilt 의 세부 구현은 Jetpack map 에서 각 정본으로 이동한다.

### 관련 지도

- [Compose Runtime and State Model](../jetpack-compose/runtime/compose-runtime-and-state-model.md)
- [Compose Layout, Animation, Accessibility](../jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md)
- [Android Data Layer Map](../data/android-data-layer-map.md)
- [Background Work Contracts](../../04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)
- [Navigation Contracts](../navigation/navigation-contracts/navigation-contracts.md)

### UI System Map
- [UI System Map](../ui/system/android-ui-system.md)

### Context and Modularity

- [Coroutines & Flow Map](../data/async-flow/android-coroutines-flow.md)
- [Paging Contracts](../data/paging/paging-contracts/paging-contracts.md)

### Navigation Links
- [Adaptive Navigation](../navigation/adaptive-navigation/adaptive-layout-and-navigation.md)

### Navigation Links
- [Intent & IPC](../navigation/intents-and-deep-links/android-intent-and-ipc.md)

### Navigation Links
- [Android Deep Links](../navigation/intents-and-deep-links/android-deep-links.md)

### Navigation Links
- [Intent & Deep Link](../navigation/intents-and-deep-links/intent-and-deep-link.md)

### Navigation Links
- [Navigation 3 Guide](../navigation/navigation3/jetpack-navigation-3-guide.md)

### Subsystem Contract Maps
- [ui-system-contracts](../ui/system/ui-system-contracts/ui-system-contracts.md)
- [compose-ui-contracts](../jetpack-compose/layout-and-ui/compose-ui-contracts/compose-ui-contracts.md)
- [compose-runtime-contracts](../jetpack-compose/runtime/compose-runtime-contracts/compose-runtime-contracts.md)
- [compose-state-and-effect-contracts](../jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)
- [compose-design-system-contracts](../jetpack-compose/design-system-and-architecture/compose-design-system-contracts/compose-design-system-contracts.md)
- [compose-performance-contracts](../jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)
- [navigation3-contracts](../navigation/navigation3/navigation3-contracts/navigation3-contracts.md)
- [intent-manifest-contracts](../navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)
- [deep-link-contracts](../navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)
- [adaptive-navigation-contracts](../navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
- [context-contracts](./context-and-modularity/context-contracts/context-contracts.md)
- [architecture-contracts](./jetpack-architecture/architecture-contracts/architecture-contracts.md)
- [app-component-contracts](./app-components/app-component-contracts/app-component-contracts.md)
- [file-access-contracts](../data/storage/file-access-contracts/file-access-contracts.md)
- [persistence-contracts](../data/storage/persistence-contracts/persistence-contracts.md)
- [flow-state-contracts](../data/async-flow/flow-state-contracts/flow-state-contracts.md)
- [coroutine-contracts](../data/async-flow/coroutines/coroutine-contracts.md)
- [flow-contracts](../data/async-flow/flow/flow-contracts.md)
- [di-contracts](../dependency-injection/di-contracts/di-contracts.md)
- [dsl-syntax-does-not-change-ownership-lifetime-contracts](../dependency-injection/di-contracts/dsl-syntax-does-not-change-ownership-lifetime-contracts.md)
- [modular-di-follows-module-dependency-direction-and-feature-entry-contracts](../dependency-injection/di-contracts/modular-di-follows-module-dependency-direction-and-feature-entry-contracts.md)
