---
title: ipc-debugging-starts-from-service-registration-call-path-and-thread-state
tags: [android, android/debugging, android/ipc]
aliases: [Binder debugging, IPC debugging]
date modified: 2026-08-03 17:25:29 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## IPC 디버깅은 service 등록, call path, thread state 에서 시작한다

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

IPC 문제는 "호출이 실패했다"만 보면 원인이 넓다. service 가 등록됐는지, caller 가 handle 을 얻었는지, permission 이 통과했는지, Binder thread 가 막혔는지, callee process 가 살아 있는지를 순서대로 좁혀야 한다.

앱 레벨에서는 logcat stack trace 보다 boundary 상태가 더 중요할 때가 많다. platform/service 레벨에서는 `dumpsys`, service list, binder stats, tombstone, SELinux denial 을 함께 봐야 한다.

### 실무 규칙

- 먼저 service discovery 와 permission denial 을 확인한다.
- 다음으로 caller thread block 과 callee Binder thread stack 을 분리한다.
- native boundary 가 있으면 tombstone, `lshal`, VINTF, SELinux denial 을 함께 본다.
- performance issue 는 transaction 횟수, payload 크기, callee 처리 시간을 나눠 측정한다.

관련 노트: [dumpsys는 system service 상태 검사 인터페이스다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/dumpsys-is-system-service-state-inspection-interface.md), [Native service debugging은 init, Binder, VINTF, SELinux, tombstone을 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-service-debugging-separates-init-binder-vintf-selinux-and-tombstones.md)
