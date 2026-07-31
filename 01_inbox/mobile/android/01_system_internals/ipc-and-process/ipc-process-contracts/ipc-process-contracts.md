---
title: IPC and process contracts
tags: [android, android/ipc, android/system-internals]
aliases: [Android IPC contracts, Binder contracts]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# IPC and process contracts

이 묶음은 Android IPC와 process를 “컴포넌트끼리 호출한다”가 아니라 process boundary, kernel mediated capability, service registration, thread pool, memory reclaim policy의 계약으로 정리한다.

## Binder와 AIDL

- [Binder는 객체 참조를 커널이 중재하는 capability IPC다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/binder-is-kernel-mediated-object-capability-ipc.md)
- [Binder transaction lifetime은 call, copy, dispatch, reply로 나뉜다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md)
- [AIDL은 process boundary 계약이지 비즈니스 프로토콜이 아니다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/aidl-defines-process-boundary-contract-not-business-protocol.md)
- [oneway Binder는 caller 대기를 없애지만 server backpressure를 없애지 않는다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/oneway-binder-removes-caller-waiting-not-server-backpressure.md)
- [Binder thread pool은 service concurrency와 deadlock 경계다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/binder-thread-pool-is-service-concurrency-and-deadlock-boundary.md)
- [IPC 디버깅은 service 등록, call path, thread state에서 시작한다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-debugging-starts-from-service-registration-call-path-and-thread-state.md)

## Process와 system service 경계

- [Zygote fork의 메모리 이점은 copy-on-write가 유지될 때 생긴다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-fork-saves-memory-while-copy-on-write-pages-stay-clean.md)
- [system_server는 framework service를 한 process 안에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)
- [system service는 Binder endpoint이자 platform policy enforcer다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-service-is-binder-endpoint-and-platform-policy-enforcer.md)
- [프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md)
- [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)
- [Android app sandbox는 UID와 프로세스 경계로 앱을 격리한다](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)

## 중복 방지 규칙

- Intent, PendingIntent, Activity Result는 app framework navigation 정본으로 둔다.
- system_server, ActivityManager, process importance는 boot/runtime의 system-server 정본으로 둔다.
- LMKD, PSI, zRAM은 kernel 정본으로 두고, 이 묶음에서는 process가 왜 kill 대상이 되는지만 연결한다.
- app sandbox와 permission은 security/privacy 정본으로 두고, Binder 문서에서는 통신 경계만 설명한다.
