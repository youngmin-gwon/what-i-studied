---
title: "system_server는 framework service를 한 프로세스 안에서 시작한다"
tags: [android, android/system-internals, android/boot-runtime, android/system-server]
aliases: ["system_server는 framework service를 한 프로세스 안에서 시작한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# system_server는 framework service를 한 프로세스 안에서 시작한다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

`system_server`는 Zygote가 시작하는 특별한 Java process이며 ActivityManager, PackageManager, WindowManager, PowerManager 같은 framework service를 한 프로세스 안에서 순차적으로 초기화한다.

## 판단 기준

- `system_server`가 올라오기 전에는 앱 컴포넌트 lifecycle을 관리할 framework service가 없다.
- framework service 간 초기화 순서는 boot phase와 의존성에 묶인다.
- `system_server` crash는 일반 앱 crash가 아니라 시스템 재시작 또는 부팅 실패로 이어질 수 있다.
- native daemon과 framework service의 경계는 Binder, HAL, system property, 파일 권한으로 연결된다.

## 관련 문서

- [Zygote는 framework 공통 상태를 preload한 뒤 앱 프로세스를 fork한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md)
- [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

공식 문서: [Architecture overview](https://source.android.com/docs/core/architecture)
