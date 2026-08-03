---
title: init-debugging-uses-logs-properties-and-service-state
tags: [android, android/boot-runtime, android/init, android/system-internals]
aliases: ["init 디버깅은 로그, property, service 상태를 함께 본다"]
date modified: 2026-08-03 17:23:37 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## init 디버깅은 로그, property, service 상태를 함께 본다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

init 문제는 service 하나가 안 뜬 것처럼 보여도 rc parser, SELinux denial, mount 실패, property trigger 순서, service restart policy 가 원인일 수 있다. 따라서 로그와 property 상태를 동시에 봐야 한다.

### 점검 순서

- early boot 문제는 `dmesg` 와 kernel log 에서 `init:` 메시지를 찾는다.
- service 상태는 `getprop init.svc.<name>` 과 `getprop | grep init.svc` 로 본다.
- 수동 제어는 `ctl.start`, `ctl.stop`, `ctl.restart` property 를 통해 수행한다.
- `zygote` restart 는 앱 프로세스 전체에 영향을 주므로 개발 기기에서만 신중히 실행한다.
- parser 오류는 vendor rc path 와 line number 가 로그에 남는지 확인한다.

### 관련 문서

- [부팅 디버깅은 logcat 이전의 kernel, pstore, init 로그에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-debugging-starts-before-logcat-with-kernel-pstore-init-logs.md)
- [디버깅 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
