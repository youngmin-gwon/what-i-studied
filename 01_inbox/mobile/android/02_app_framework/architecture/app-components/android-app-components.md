---
title: "Android App Components"
tags: [android, android/architecture, android/app-components]
aliases: ["Android App Components"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Android App Components

앱 컴포넌트는 앱 내부 layer가 아니라 Android OS가 앱을 발견하고 호출하는 실행 경계다.

## 정본 노트

- [안드로이드 앱 컴포넌트는 OS가 호출하는 실행 경계다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/android-app-components-are-system-entry-points-not-in-process-objects.md)
- [Activity는 사용자에게 보이는 entry point이자 프로세스 우선순위 신호다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/activity-is-user-visible-entry-point-and-process-priority-signal.md)
- [Activity 콜백은 화면 인스턴스의 visibility와 interaction 경계를 알린다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/activity-lifecycle-callbacks-describe-visibility-and-interaction-boundaries.md)
- [설정 변경은 Activity를 재생성할 수 있으므로 상태를 화면 인스턴스에서 분리해야 한다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/configuration-change-recreates-activity-but-not-all-screen-state.md)
- [프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md)
- [Task와 back stack은 OS가 관리하는 Activity 작업 기록이지 앱 내부 navigation state가 아니다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/task-and-back-stack-are-os-activity-navigation-not-app-navigation-state.md)
- [Service는 UI 없는 컴포넌트이지 일반 background task runner가 아니다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/service-is-background-or-remote-work-entry-point-not-general-task-runner.md)
- [Foreground Service는 사용자에게 보이는 진행 중 작업 계약이다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/foreground-service-is-user-visible-ongoing-work-contract.md)
- [Bound Service는 IBinder 계약으로 클라이언트와 연결된다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/bound-service-exposes-process-dependency-and-ipc-api.md)
- [BroadcastReceiver는 짧은 이벤트 entry point이지 background worker가 아니다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/broadcastreceiver-is-short-lived-event-entry-point-not-background-worker.md)
- [Context-registered Receiver의 수명은 등록한 Context를 따른다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/context-registered-receiver-lifetime-follows-registering-context.md)
- [ContentProvider는 URI와 권한을 가진 데이터 공유 API다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/contentprovider-publishes-uri-addressed-data-with-permission-boundary.md)
- [FileProvider는 파일 경로 대신 제한된 content URI 접근권을 준다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/fileprovider-grants-narrow-uri-access-instead-of-file-path-sharing.md)
- [AndroidManifest는 OS가 발견할 컴포넌트와 권한 경계를 선언한다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/manifest-declares-components-permissions-features-and-exported-boundaries.md)
- [android:exported와 권한은 외부 컴포넌트 접근 경계를 결정한다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/exported-and-permission-boundaries-decide-external-component-access.md)
- [컴포넌트 통신은 Intent, Binder, URI, PendingIntent 경계로 나눈다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary.md)

## 주변 정본

- [Intent and Manifest Contracts](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)
- [Background Work Contracts](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)
- [Android 권한 계약](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md)
- [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
- [Persistence Contracts](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
