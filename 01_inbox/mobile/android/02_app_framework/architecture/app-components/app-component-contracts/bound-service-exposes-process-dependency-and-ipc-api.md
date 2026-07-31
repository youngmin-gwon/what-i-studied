---
title: "Bound Service는 IBinder 계약으로 클라이언트와 연결된다"
tags: [android, android/architecture, android/app-components]
aliases: ["Bound Service는 IBinder 계약으로 클라이언트와 연결된다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Bound Service는 IBinder 계약으로 클라이언트와 연결된다

Bound Service는 클라이언트가 `bindService`로 연결해 `IBinder`를 통해 기능을 호출하는 컴포넌트다. 같은 프로세스 안에서는 local Binder로 충분할 수 있고, 다른 프로세스와 안정적인 인터페이스를 맺어야 할 때 AIDL을 검토한다.

순수 bound service의 수명은 연결된 클라이언트에 강하게 묶인다. 다만 service는 started이면서 bound일 수도 있으므로, bind 여부만으로 전체 수명을 단순화하면 안 된다.

AIDL은 대부분 앱의 기본 선택지가 아니다. IPC 실패, thread, permission, versioning, exported surface를 감당할 필요가 있을 때만 명시적으로 도입한다.

관련 노트: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md), [exported/permission 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/exported-and-permission-boundaries-decide-external-component-access.md), [컴포넌트 통신 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary.md).

공식 문서: [Bound services](https://developer.android.com/develop/background-work/services/bound-services)
