---
title: boot-debugging-starts-before-logcat-with-kernel-pstore-init-logs
tags: [android, android/boot, android/boot-runtime, android/system-internals]
aliases: ["부팅 디버깅은 logcat 이전의 kernel, pstore, init 로그에서 시작한다"]
date modified: 2026-08-03 17:23:11 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 부팅 디버깅은 logcat 이전의 kernel, pstore, init 로그에서 시작한다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

부팅 실패는 Android framework 가 올라오기 전에 발생할 수 있다. 따라서 `logcat` 만 보면 bootloader, kernel panic, early mount, SELinux, init rc 오류를 놓치기 쉽다.

### 점검 순서

- reboot 이전 crash 는 `/sys/fs/pstore` 와 ramoops 를 먼저 확인한다.
- kernel 단계는 `dmesg`, bootconfig, cmdline, mount 실패 로그를 본다.
- `init` 단계는 `init` tag, `init.svc.*`, service restart, rc parser 오류를 본다.
- framework 이후 문제는 `system_server`, `ActivityManager`, `PackageManager`, System UI 로그로 넘어간다.
- boot performance 는 bootchart 와 Perfetto trace 를 사용하되, 먼저 어느 단계가 느린지 구간을 나눈다.

### 관련 문서

- [init 디버깅은 로그, property, service 상태를 함께 본다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-debugging-uses-logs-properties-and-service-state.md)
- [디버깅 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
