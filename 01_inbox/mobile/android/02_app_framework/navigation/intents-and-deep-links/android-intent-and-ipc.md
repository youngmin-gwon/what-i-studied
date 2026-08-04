---
title: android-intent-and-ipc
tags: [android, android/intents, android/navigation]
aliases: ["Android Intent and IPC"]
date modified: 2026-08-03 18:11:50 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Intent 와 IPC 는 컴포넌트 실행과 외부 진입을 연결한다

Intent 문서는 앱 컴포넌트 실행 요청과 외부 진입 경계를 정리한다. Binder IPC 자체는 system internals 정본으로 두고, 여기서는 Intent, Manifest, exported, package visibility, PendingIntent, Activity Result API 를 다룬다.

### 정본 지도

- [Intent 와 Manifest 계약](./intent-manifest-contracts/intent-manifest-contracts.md)
- [Intent는 컴포넌트 실행을 설명하는 메시지다](./intent-manifest-contracts/intent-describes-component-action-request.md)
- [AndroidManifest는 OS가 발견할 컴포넌트와 진입점을 선언한다](./intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md)
- [PendingIntent는 미래 Intent 실행 권한을 위임하는 token이다](./intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md)

관련 지도: [IPC and process contracts](../../../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
