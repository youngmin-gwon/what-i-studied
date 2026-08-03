---
title: android-app-architecture
tags: [android, android/architecture]
aliases: ["Android App Architecture"]
date modified: 2026-08-03 17:28:08 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android 앱 아키텍처는 UI 패턴보다 수명과 OS 진입점을 나누는 문제다

Android 앱 아키텍처는 UI 패턴 이름보다 owner, lifetime, OS entry point 를 먼저 나누는 문제다.

### 정본 지도

- [Android App Components](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components.md) - Activity, Service, BroadcastReceiver, ContentProvider 를 OS entry point 로 정리한다.
- [Android Context Boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md) - Context 종류와 lifetime, leak risk, Compose `LocalContext` 를 정리한다.
- [Jetpack Architecture Map](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture-map.md) - Jetpack architecture guidance 를 기존 정본 map 으로 연결한다.
- [Android State Management](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md) - ViewModel, UI state, reducer, saved state 의 정본.
- [Android Dependency Injection](01_inbox/mobile/android/02_app_framework/dependency-injection/android-dependency-injection-map.md) - object graph, binding, scope, Hilt/Metro, test override 의 정본.

### 읽는 기준

앱이 외부에서 어떻게 호출되는지가 궁금하면 app components 로 간다. 어떤 Context 를 전달해야 하는지가 궁금하면 context boundary 로 간다. ViewModel, Flow, Room, WorkManager, Navigation, Hilt 의 세부 구현은 Jetpack map 에서 각 정본으로 이동한다.

### 관련 지도

- [Compose Runtime and State Model](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md)
- [Compose Layout, Animation, Accessibility](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md)
- [Android Data Layer Map](01_inbox/mobile/android/02_app_framework/data/android-data-layer-map.md)
- [Background Work Contracts](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)
- [Navigation Contracts](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md)
