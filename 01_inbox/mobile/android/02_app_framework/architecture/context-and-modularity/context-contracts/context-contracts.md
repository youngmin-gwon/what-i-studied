---
title: "Context Contracts"
tags: [android, android/architecture, android/context]
aliases: ["Context Contracts"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Context Contracts

Context를 type 이름보다 owner/lifetime/capability로 고르는 정본 모음이다.

## Notes

- [Context는 Android 환경 capability이지 일반 DI container가 아니다](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-is-android-environment-capability-not-dependency-container.md)
- [Application Context는 프로세스 수명 작업에 맞고 themed UI에는 맞지 않는다](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/application-context-fits-process-lifetime-work-not-themed-ui.md)
- [Activity Context는 window와 theme를 가지지만 수명이 짧다](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/activity-context-carries-window-theme-and-short-lifetime.md)
- [컴포넌트 Context의 수명은 Service, Receiver, Provider 경계를 따른다](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/component-context-lifetime-follows-service-receiver-provider-boundary.md)
- [LocalContext는 Composition에서 읽는 Android Context이지 Flutter BuildContext가 아니다](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/localcontext-is-composition-scoped-android-context-not-flutter-buildcontext.md)
- [ViewModel과 Repository는 UI Context를 보관하지 않는다](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/viewmodel-and-repository-should-not-retain-ui-context.md)
- [Context leak은 참조가 컴포넌트 수명보다 오래 살 때 발생한다](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-leaks-happen-when-reference-outlives-component-lifetime.md)
