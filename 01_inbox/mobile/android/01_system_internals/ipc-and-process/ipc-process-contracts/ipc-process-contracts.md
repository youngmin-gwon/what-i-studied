---
title: ipc-process-contracts
tags: [android, android/ipc, android/system-internals]
aliases: ["IPC and process contracts", Android IPC contracts, Binder contracts]
date modified: 2026-08-06 14:58:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## IPC and process contracts

이 묶음은 Android IPC 와 process 를 "컴포넌트끼리 호출한다"가 아니라 process boundary, kernel mediated capability, service registration, thread pool, memory reclaim policy 의 계약으로 정리한다.

### 읽는 순서

1. Binder 가 무엇을 중재하는지(객체 참조, kernel 경계)를 먼저 본다.
2. transaction lifetime(call, copy, dispatch, reply)으로 비용이 어디서 생기는지 본다.
3. AIDL 이 만드는 것은 process boundary 계약이지 비즈니스 로직이 아님을 확인한다.
4. oneway 와 thread pool 로 동시성/backpressure 한계를 본다.
5. 문제가 생기면 IPC 디버깅 노트로 service 등록, call path, thread state 를 좁힌다.

### 문제 분류 기준

- "이 API 호출이 왜 이렇게 느린가" → [Binder transaction lifetime](binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md), [Binder thread pool](binder-thread-pool-is-service-concurrency-and-deadlock-boundary.md)
- "service 가 멈췄다/응답이 없다" → [Binder thread pool](binder-thread-pool-is-service-concurrency-and-deadlock-boundary.md), boot-and-runtime 의 [ANR은 responsiveness 계약 위반이다](../../boot-and-runtime/system-server-contracts/anr-responsiveness-contract.md)
- "이벤트를 보냈는데 유실/지연된다" → [oneway Binder](oneway-binder-removes-caller-waiting-not-server-backpressure.md)
- "서비스 호출이 permission/등록 단계에서 실패한다" → [IPC 디버깅](ipc-debugging-starts-from-service-registration-call-path-and-thread-state.md)
- "Binder와 socket/shared memory 중 무엇이 다른가" → **Binder는 Android framework의 typed RPC이고 POSIX IPC를 배제하지 않는다**
- "이 프로세스가 왜 죽었는가" → 이 묶음이 아니라 아래 Process/system service 링크로 이동한다.

### Binder 와 AIDL

- [Binder IPC](../../binder-ipc.md)
- [Binder transaction lifetime은 call, copy, dispatch, reply로 나뉜다](binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md)
- [AIDL은 process boundary 계약이지 비즈니스 프로토콜이 아니다](aidl-defines-process-boundary-contract-not-business-protocol.md)
- [oneway Binder는 caller 대기를 없애지만 server backpressure를 없애지 않는다](oneway-binder-removes-caller-waiting-not-server-backpressure.md)
- [Binder thread pool은 service concurrency와 deadlock 경계다](binder-thread-pool-is-service-concurrency-and-deadlock-boundary.md)
- [IPC 디버깅은 service 등록, call path, thread state에서 시작한다](ipc-debugging-starts-from-service-registration-call-path-and-thread-state.md)
- **Binder는 Android framework의 typed RPC이고 POSIX IPC를 배제하지 않는다** - Binder, Unix domain socket, shared memory와 FD 전달의 identity·copy·lifetime 차이를 비교한다.

### Process 와 system service 경계

- [Zygote fork의 메모리 이점은 copy-on-write가 유지될 때 생긴다](../../boot-and-runtime/zygote-runtime-contracts/zygote-copy-on-write.md)
- [system_server는 framework service를 한 process 안에서 시작한다](../../boot-and-runtime/system-server-contracts/system-server-startup.md)
- [system service는 Binder endpoint이자 platform policy enforcer다](../../boot-and-runtime/system-server-contracts/system-service-is-binder-endpoint-and-platform-policy-enforcer.md)
- [프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다](../../boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md)
- [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](../../kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)
- [Android app sandbox는 UID와 프로세스 경계로 앱을 격리한다](../../../05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)

### 인접 영역 진입점

Binder 는 IPC 메커니즘 하나이고, 그 위에 올라간 개별 system service 의 정책은 각자의 정본이 있다. 이 묶음에서는 "이것도 Binder service 다"만 확인하고, 서비스별 판단 기준은 아래로 이동한다.

- SurfaceFlinger, camera service, mediaserver 같은 native graphics/media service 의 buffer/session 계약은 [Graphics and media contracts](../../graphics-and-media/graphics-media-contracts/graphics-media-contracts.md) 가 정본이다. BufferQueue 는 버퍼 핸들을 프로세스 간에 넘기는 자료구조이고, 그 등록/제어 채널은 Binder 를 쓴다.
- ConnectivityService, netd 같은 network system service 의 정책 계약은 [연결성 계약](../../connectivity/connectivity-contracts/connectivity-contracts.md) 이 정본이다. 앱이 보는 `ConnectivityManager` 호출도 결국 Binder 를 통해 system_server 의 ConnectivityService 로 전달된다.
- system_server 가 여러 framework service 를 한 프로세스에서 어떻게 조율하는지는 [system_server와 ActivityManager 계약](../../boot-and-runtime/system-server-contracts/system-server-contracts.md) 이 정본이다.

### 중복 방지 규칙

- Intent, PendingIntent, Activity Result 는 app framework navigation 정본으로 둔다.
- system_server, ActivityManager, process importance 는 boot/runtime 의 system-server 정본으로 둔다.
- LMKD, PSI, zRAM 은 kernel 정본으로 두고, 이 묶음에서는 process 가 왜 kill 대상이 되는지만 연결한다.
- app sandbox 와 permission 은 security/privacy 정본으로 두고, Binder 문서에서는 통신 경계만 설명한다.
