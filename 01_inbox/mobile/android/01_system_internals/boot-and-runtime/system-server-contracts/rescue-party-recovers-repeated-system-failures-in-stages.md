---
title: "Rescue Party는 반복되는 system failure를 단계적으로 복구한다"
tags: [android, android/system-internals, android/boot-runtime, android/system-server]
aliases: ["Rescue Party는 반복되는 system failure를 단계적으로 복구한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Rescue Party는 반복되는 system failure를 단계적으로 복구한다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

Rescue Party는 반복적인 system_server crash, boot loop, 심각한 system service failure 같은 상황에서 기기를 사용 가능한 상태로 되돌리기 위한 platform recovery 메커니즘이다. 목적은 앱 오류를 고치는 것이 아니라 시스템이 부팅 불능 상태에 빠지는 것을 막는 것이다.

## 판단 기준

- 반복 실패를 관찰한 뒤 점진적으로 더 강한 복구 조치를 시도한다.
- settings reset, package manager 관련 정리, factory reset prompt 같은 단계는 Android 버전별 구현에 따라 달라질 수 있다.
- OEM customization이나 platform service 변경은 Rescue Party trigger와 복구 결과를 별도 테스트해야 한다.

## 관련 문서

- [system_server는 framework service를 한 프로세스 안에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)
- [부팅 디버깅은 logcat 이전의 kernel, pstore, init 로그에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-debugging-starts-before-logcat-with-kernel-pstore-init-logs.md)
