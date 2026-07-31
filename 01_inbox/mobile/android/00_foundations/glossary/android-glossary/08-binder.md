---
title: "Binder"
tags: ["android", "android/glossary"]
aliases: ["Binder IPC"]
---

# Binder

정의: Binder는 Android에서 process boundary를 넘는 object-capability style IPC와 identity propagation을 제공하는 kernel-mediated mechanism이다.

혼동 방지: Binder는 단순 message queue가 아니다. call lifetime, transaction buffer, thread pool, caller identity, death notification이 함께 서비스 경계를 정의한다.

정본 링크:
- [Binder IPC contract](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/binder-is-kernel-mediated-object-capability-ipc.md)
- [Binder transaction lifetime](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md)
