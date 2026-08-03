---
title: ui-domain-data-layers-separate-rendering-policy-and-source-of-truth
tags: [android, android/architecture, android/jetpack]
aliases: ["UI, domain, data layer는 rendering, policy, source of truth를 분리한다"]
date modified: 2026-08-03 17:27:37 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## UI, domain, data layer 는 rendering, policy, source of truth 를 분리한다

UI layer 는 상태를 그리고 사용자 action 을 올린다. ViewModel/state holder 는 화면 state 와 외부 작업을 조율한다. Domain layer 는 여러 화면이나 repository 에 걸친 business rule 이 실제 복잡도를 줄일 때만 둔다. Data layer 는 repository 와 data source 를 통해 source of truth 와 동기화 정책을 가진다.

이 구분은 package 이름보다 ownership 이 중요하다. 화면이 사라져도 살아야 하는 데이터는 UI layer 가 소유하지 않고, user-visible immediate work 와 deferrable durable work 는 background-work 정책으로 분리한다.

앱 컴포넌트는 이 layer 를 시작하거나 연결하는 entry point 다. Activity 가 곧 ViewModel 은 아니고, Service 가 곧 repository 는 아니며, Receiver 가 곧 worker 도 아니다.

관련 노트: [앱 컴포넌트 허브](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components.md), [ViewModel 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [background work 정본](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md).

공식 문서: [Guide to app architecture](https://developer.android.com/topic/architecture)
