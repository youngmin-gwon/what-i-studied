---
title: 앱 컴포넌트 계약은 OS가 보는 진입점 경계를 설명한다
tags: [android, android/app-components, android/architecture]
aliases: ["App Component Contracts"]
date modified: 2026-08-03 16:34:27 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 앱 컴포넌트 계약은 OS가 보는 진입점 경계를 설명한다

Activity, Service, BroadcastReceiver, ContentProvider 를 각각의 OS-visible contract 로 읽기 위한 정본 모음이다.

### Entry Point

- [앱 컴포넌트는 OS entry point다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/android-app-components-are-system-entry-points-not-in-process-objects.md)
- [Manifest는 컴포넌트와 권한 경계를 선언한다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/manifest-declares-components-permissions-features-and-exported-boundaries.md)
- [exported와 권한은 외부 접근 경계를 결정한다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/exported-and-permission-boundaries-decide-external-component-access.md)
- [컴포넌트 통신은 경계별 API로 나뉜다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary.md)

### Components

- [Activity](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/activity-is-user-visible-entry-point-and-process-priority-signal.md)
- [Service](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/service-is-background-or-remote-work-entry-point-not-general-task-runner.md)
- [BroadcastReceiver](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/broadcastreceiver-is-short-lived-event-entry-point-not-background-worker.md)
- [ContentProvider](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/contentprovider-publishes-uri-addressed-data-with-permission-boundary.md)
