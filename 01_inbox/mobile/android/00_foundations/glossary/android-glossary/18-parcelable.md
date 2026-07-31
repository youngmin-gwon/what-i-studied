---
title: 18-parcelable
tags: ["android", "android/glossary"]
aliases: ["Parcelable IPC payload"]
date modified: 2026-08-01 01:07:26 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Parcelable

정의: Parcelable 은 Android 가 Binder transaction 이나 Intent extra 에서 object graph 를 process boundary 에 맞게 flatten/unflatten 하기 위한 serialization contract 다.

혼동 방지: Parcelable 은 business protocol 자체가 아니다. IPC boundary 에서는 size limit, version compatibility, classloader, copy cost, trust boundary 를 함께 설계해야 한다.

정본 링크:

- [AIDL boundary contract](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/aidl-defines-process-boundary-contract-not-business-protocol.md)
- [Binder transaction lifetime](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md)
