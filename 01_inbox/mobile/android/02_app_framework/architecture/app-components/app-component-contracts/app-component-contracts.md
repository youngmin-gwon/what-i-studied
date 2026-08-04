---
title: app-component-contracts
tags: [android, android/app-components, android/architecture]
aliases: ["App Component Contracts"]
date modified: 2026-08-03 17:26:56 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 앱 컴포넌트 계약은 OS 가 보는 진입점 경계를 설명한다

Activity, Service, BroadcastReceiver, ContentProvider 를 각각의 OS-visible contract 로 읽기 위한 정본 모음이다.

### Entry Point

- [앱 컴포넌트는 OS entry point다](./android-app-components-are-system-entry-points-not-in-process-objects.md)
- [Manifest는 컴포넌트와 권한 경계를 선언한다](./manifest-declares-components-permissions-features-and-exported-boundaries.md)
- [exported와 권한은 외부 접근 경계를 결정한다](./exported-and-permission-boundaries-decide-external-component-access.md)
- [컴포넌트 통신은 경계별 API로 나뉜다](./component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary.md)

### Components

- [Activity](./activity-is-user-visible-entry-point-and-process-priority-signal.md)
- [Service](./service-is-background-or-remote-work-entry-point-not-general-task-runner.md)
- [BroadcastReceiver](./broadcastreceiver-is-short-lived-event-entry-point-not-background-worker.md)
- [ContentProvider](./contentprovider-publishes-uri-addressed-data-with-permission-boundary.md)


### Detailed Contracts
- [process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md](process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md)
- [task-and-back-stack-are-os-activity-navigation-not-app-navigation-state.md](task-and-back-stack-are-os-activity-navigation-not-app-navigation-state.md)
- [fileprovider-grants-narrow-uri-access-instead-of-file-path-sharing.md](fileprovider-grants-narrow-uri-access-instead-of-file-path-sharing.md)
- [context-registered-receiver-lifetime-follows-registering-context.md](context-registered-receiver-lifetime-follows-registering-context.md)
- [foreground-service-is-user-visible-ongoing-work-contract.md](foreground-service-is-user-visible-ongoing-work-contract.md)
- [configuration-change-recreates-activity-but-not-all-screen-state.md](configuration-change-recreates-activity-but-not-all-screen-state.md)
- [activity-lifecycle-callbacks-describe-visibility-and-interaction-boundaries.md](activity-lifecycle-callbacks-describe-visibility-and-interaction-boundaries.md)
- [bound-service-exposes-process-dependency-and-ipc-api.md](bound-service-exposes-process-dependency-and-ipc-api.md)
