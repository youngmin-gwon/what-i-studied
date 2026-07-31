---
title: Platform debugging은 build, boot, service, VINTF, sepolicy, CTS를 분리한다
tags: [android, android/aosp, android/debugging]
aliases: [Platform debugging]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Platform debugging은 build, boot, service, VINTF, sepolicy, CTS를 분리한다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Platform customization 문제는 앱 crash처럼 한 로그에서 끝나지 않는다. build graph, image contents, boot stage, init service state, Binder service registration, HAL/VINTF, sepolicy denial, compatibility test failure를 층별로 분리해야 한다.

좋은 디버깅은 먼저 실패 지점을 boot 이전, init, framework service, app/API, certification 단계 중 하나로 좁힌다. 그다음 해당 단계의 관찰 도구를 사용한다.

## 실무 규칙

- 부팅 전 문제는 bootloader, kernel log, pstore, init log부터 본다.
- service 문제는 `init.svc.*`, `service list`, `dumpsys`, Binder thread state를 확인한다.
- HAL 문제는 VINTF manifest, service registration, SELinux denial, tombstone을 함께 본다.
- CTS/VTS/GTS 실패는 테스트 이름보다 contract layer를 먼저 분류한다.

관련 노트: [IPC 디버깅은 service 등록, call path, thread state에서 시작한다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-debugging-starts-from-service-registration-call-path-and-thread-state.md), [Debugging contracts](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
