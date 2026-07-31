---
title: SELinux policy는 Binder service와 file boundary를 함께 제어한다
tags: [android, android/kernel, android/security, android/ipc]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

# SELinux policy는 Binder service와 file boundary를 함께 제어한다

Android SELinux는 file access만 제어하지 않는다. Binder call, service manager lookup, socket, device node, property access 같은 Android-specific boundary도 policy 대상이 된다.

Binder 경계에서는 service를 찾는 권한과 실제 Binder call 권한이 별도로 필요할 수 있다. 예를 들어 어떤 domain이 service manager에서 특정 service type을 `find`할 수 있는지와, target domain에 binder `call`을 할 수 있는지는 다른 policy decision이다.

이 때문에 “UID가 같으면 된다”거나 “permission을 받았으면 Binder 호출이 된다”는 설명은 부족하다. Android permission, AppOps, UID sandbox, SELinux domain/type policy가 서로 다른 층에서 함께 작동한다.

SELinux denial을 분석할 때는 `avc: denied`의 source context, target context, class, permission을 읽고, 해당 access가 정말 필요한 platform boundary인지 확인해야 한다. 단순히 permissive로 돌리거나 broad allow를 추가하면 보안 모델을 약화시킨다.

관련 노트: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md), [SELinux는 domain/type 정책으로 mandatory access control을 강제한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-enforces-mac-with-domain-type-policy.md)

근거: [SELinux concepts](https://source.android.com/docs/security/features/selinux/concepts), [Implement SELinux](https://source.android.com/docs/security/features/selinux/implement)
