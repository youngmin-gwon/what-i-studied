---
title: Jetpack Architecture Map은 세부 API 설명보다 기존 정본으로 연결하는 decision map이다
tags: [android, android/architecture, android/jetpack]
aliases: ["Jetpack Architecture Map"]
date modified: 2026-08-03 16:35:11 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Jetpack Architecture Map은 세부 API 설명보다 기존 정본으로 연결하는 decision map이다

Jetpack architecture 문서는 세부 API 설명을 반복하는 catalog 가 아니라 기존 정본으로 연결하는 decision map 이다.

### 정본 노트

- [Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/architecture-contracts/jetpack-architecture-is-recommended-responsibility-map-not-mandatory-stack.md)
- [UI, domain, data layer는 rendering, policy, source of truth를 분리한다](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/architecture-contracts/ui-domain-data-layers-separate-rendering-policy-and-source-of-truth.md)
- [아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/architecture-contracts/architecture-decisions-start-from-owner-lifetime-and-survival-requirements.md)
- [Jetpack Architecture 문서는 세부 구현을 반복하지 않는 map이어야 한다](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/architecture-contracts/jetpack-architecture-map-links-to-canonical-android-guides.md)

### 세부 주제별 정본

- [State Management](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md) - ViewModel, UI state, reducer, saved state.
- [Flow State Contracts](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md) - Flow, StateFlow, SharedFlow, stateIn.
- [Persistence Contracts](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md) - Room, DataStore, repository, durable source of truth.
- [Background Work Contracts](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md) - WorkManager, JobScheduler, AlarmManager, foreground service selection.
- [Navigation Contracts](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md) - Navigation state, routes, back stack.
- [Intent and Manifest Contracts](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md) - Intent, intent-filter, exported, PendingIntent.
- [Android Dependency Injection Map](01_inbox/mobile/android/02_app_framework/dependency-injection/android-dependency-injection-map.md) - Hilt, graph, scope, Android entry points.
- [Compose Runtime and State Model](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md) - recomposition, state observation, remember, effects.
- [Compose Layout, Animation, Accessibility](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md) - layout, modifier, animation, semantics.

공식 문서: [Guide to app architecture](https://developer.android.com/topic/architecture)
