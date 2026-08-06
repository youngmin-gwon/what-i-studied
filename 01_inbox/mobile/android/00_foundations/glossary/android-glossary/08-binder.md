---
title: 08-binder
tags: ["android", "android/glossary"]
aliases: ["[binder ipc](../../../01_system_internals/binder-ipc.md)"]
date modified: 2026-08-03 17:21:39 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Binder 는 안드로이드의 프로세스 간 통신(IPC)을 담당하는 핵심 메커니즘이다

정의: Binder 는 Android 에서 process boundary 를 넘는 object-capability style IPC 와 identity propagation 을 제공하는 kernel-mediated mechanism 이다.

혼동 방지: Binder 는 단순 message queue 가 아니다. call lifetime, transaction buffer, thread pool, caller identity, death notification 이 함께 서비스 경계를 정의한다.

정본 링크:

- [Binder IPC contract](../../../01_system_internals/ipc-and-process/ipc-process-contracts/binder-is-kernel-mediated-object-capability-ipc.md)
- [Binder transaction lifetime](../../../01_system_internals/ipc-and-process/ipc-process-contracts/binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md)
