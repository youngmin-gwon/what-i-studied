---
title: "부팅 완료는 단일 property가 아니라 관측 가능한 milestone 묶음이다"
tags: [android, android/system-internals, android/boot-runtime, android/boot]
aliases: ["부팅 완료는 단일 property가 아니라 관측 가능한 milestone 묶음이다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 부팅 완료는 단일 property가 아니라 관측 가능한 milestone 묶음이다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

부팅 완료를 `sys.boot_completed=1` 하나로 정의하면 분석이 거칠어진다. kernel ready, `init` service start, Zygote start, `system_server` boot phases, PackageManager scan, System UI, Launcher 표시, 사용자 unlock은 서로 다른 milestone이다.

## 실무 규칙

- boot performance 목표는 어느 milestone까지의 시간인지 먼저 고정한다.
- framework boot complete와 사용자가 첫 조작을 할 수 있는 시점은 다를 수 있다.
- Direct Boot 환경에서는 credential encrypted storage가 열리기 전에도 일부 service와 app component가 동작할 수 있다.
- boot receiver, app startup, System UI 문제를 같은 boot complete 로그 하나로 묶지 않는다.

## 관련 문서

- [부팅 디버깅은 logcat 이전의 kernel, pstore, init 로그에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-debugging-starts-before-logcat-with-kernel-pstore-init-logs.md)
- [FBE의 CE와 DE 저장소는 잠금 해제 전후 접근 가능성이 다르다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/fbe-ce-and-de-separate-storage-availability.md)
