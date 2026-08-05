---
title: android-intent-and-ipc
tags: [android, android/intents, android/navigation]
aliases: ["Android Intent and IPC"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android **Intent**(안드로이드 컴포넌트를 호출하기 위해 목적지와 전달 데이터를 명시하는 Binder IPC 메시지 객체) 와 **IPC(Inter-Process Communication)**(독립된 프로세스 간에 데이터와 명령을 주고받는 OS 차원의 통신 체계) 는 컴포넌트 실행과 외부 진입을 연결한다

배경 지식: [IPC 메커니즘](../../../../../operating-systems/ipc-mechanisms.md), [UNIX Domain Socket 계약](../../../../../operating-systems/ipc-contracts/unix-domain-socket-contracts.md)

Intent 문서는 앱 컴포넌트 실행 요청과 외부 진입 경계를 정리한다. Binder IPC 자체는 system internals 정본으로 두고, 여기서는 Intent, Manifest, exported, package visibility, PendingIntent, Activity Result API 를 다룬다.

### 정본 지도

- [Intent 와 Manifest 계약](intent-manifest-contracts/intent-manifest-contracts.md)
- [Intent는 컴포넌트 실행을 설명하는 메시지다](intent-manifest-contracts/intent-describes-component-action-request.md)
- [AndroidManifest는 OS가 발견할 컴포넌트와 진입점을 선언한다](intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md)
- [PendingIntent는 미래 Intent 실행 권한을 위임하는 token이다](intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md)

관련 지도: [IPC and process contracts](../../../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
