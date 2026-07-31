---
title: Binder는 객체 참조를 커널이 중재하는 capability IPC다
tags: [android, android/ipc, android/binder]
aliases: [Binder IPC]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Binder는 객체 참조를 커널이 중재하는 capability IPC다

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

Binder의 핵심은 byte stream이 아니라 remote object reference다. client는 handle을 통해 service의 method를 호출하고, kernel Binder driver는 process 간 buffer 전달, object reference, death notification, caller identity를 중재한다.

그래서 Binder를 단순 직렬화나 socket 대체물로 보면 중요한 경계를 놓친다. 권한 검사는 API 표면의 permission만이 아니라 service 등록, caller UID/PID, SELinux binder policy, exported component 경계와 함께 해석해야 한다.

## 실무 규칙

- Binder API는 “누가 이 handle을 얻을 수 있는가”를 먼저 설계한다.
- system service 호출은 library call처럼 보여도 process boundary와 permission boundary를 지난다.
- 큰 payload, file descriptor, long-running work는 transaction 비용과 lifetime을 분리한다.
- native/HAL Binder는 앱 AIDL과 같은 단어를 쓰더라도 안정성, 버전, SELinux 경계가 다르다.

관련 노트: [SELinux policy는 Binder service와 file boundary를 함께 제어한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-policy-controls-binder-service-and-file-boundaries.md)
