---
title: rescue-party-recovers-repeated-system-failures-in-stages
tags: [android, android/boot-runtime, android/system-internals, android/system-server]
aliases: ["Rescue Party는 반복되는 system failure를 단계적으로 복구한다"]
date modified: 2026-08-03 17:23:56 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Rescue Party 는 반복되는 system failure 를 단계적으로 복구한다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

Rescue Party 는 Android 8.0(API 26) 이상에 포함된 platform recovery 메커니즘이며, 반복적인 `system_server` crash 나 persistent system app crash 같은 상황에서 기기를 사용 가능한 상태로 되돌린다. 이 계약은 framework/native 계층 책임이며, 앱 코드가 호출하거나 설정할 수 있는 API 가 아니다. 목적은 앱 오류를 고치는 것이 아니라 시스템이 부팅 불능 상태에 빠지는 것을 막는 것이다.

### 판단 기준

- 공식 문서 기준 trigger 조건은 `system_server` 가 5 분 안에 5 회 넘게 재시작하거나, persistent system app 이 30 초 안에 5 회 넘게 crash 하는 경우다. 정확한 수치는 Android 버전별 구현에 따라 달라질 수 있으므로 현재 platform source 로 재확인한다.
- 각 단계는 최대 5 분 간격으로 점점 더 공격적인 조치(설정 초기화, package 관련 정리 등)로 escalate 하며, 최후 수단은 recovery mode 로 재부팅해 사용자에게 factory reset 을 요청하는 것이다.
- OEM customization 이나 platform service 변경은 Rescue Party trigger 와 복구 결과를 별도 테스트해야 한다.

### 관찰 가능 신호

- logcat 에서 `RescueParty` tag 와 `system_server` 재시작 로그를 함께 확인한다.
- 반복 crash 이력은 `dumpsys activity` 또는 `dropbox` 항목(`system_server_crash`, `system_app_crash`)에서 흔적을 볼 수 있다.

### 관련 문서

- [system_server는 framework service를 한 프로세스 안에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)
- [부팅 디버깅은 logcat 이전의 kernel, pstore, init 로그에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-debugging-starts-before-logcat-with-kernel-pstore-init-logs.md)

공식 문서: [Rescue Party](https://source.android.com/docs/core/tests/debug/rescue-party)
