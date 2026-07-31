---
title: "Parcelable"
tags: ["android", "android/glossary"]
aliases: ["Parcelable IPC payload"]
---

# Parcelable

정의: Parcelable은 Android가 Binder transaction이나 Intent extra에서 object graph를 process boundary에 맞게 flatten/unflatten하기 위한 serialization contract다.

혼동 방지: Parcelable은 business protocol 자체가 아니다. IPC boundary에서는 size limit, version compatibility, classloader, copy cost, trust boundary를 함께 설계해야 한다.

정본 링크:
- [AIDL boundary contract](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/aidl-defines-process-boundary-contract-not-business-protocol.md)
- [Binder transaction lifetime](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md)
