---
title: binder-is-kernel-mediated-object-capability-ipc
tags: [android, android/binder, android/ipc]
aliases: [Binder IPC]
date modified: 2026-08-03 17:25:24 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Binder 는 객체 참조를 커널이 중재하는 capability IPC 다

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

Binder 의 핵심은 byte stream 이 아니라 remote object reference 다. client 는 handle 을 통해 service 의 method 를 호출하고, kernel Binder driver 는 process 간 buffer 전달, object reference, death notification, caller identity 를 중재한다.

그래서 Binder 를 단순 직렬화나 socket 대체물로 보면 중요한 경계를 놓친다. 권한 검사는 API 표면의 permission 만이 아니라 service 등록, caller UID/PID, SELinux binder policy, exported component 경계와 함께 해석해야 한다.

### 실무 규칙

- Binder API 는 "누가 이 handle 을 얻을 수 있는가"를 먼저 설계한다.
- system service 호출은 library call 처럼 보여도 process boundary 와 permission boundary 를 지난다.
- 큰 payload, file descriptor, long-running work 는 transaction 비용과 lifetime 을 분리한다.
- native/HAL Binder 는 앱 AIDL 과 같은 단어를 쓰더라도 안정성, 버전, SELinux 경계가 다르다.

관련 노트: [SELinux policy는 Binder service와 file boundary를 함께 제어한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-policy-controls-binder-service-and-file-boundaries.md)
