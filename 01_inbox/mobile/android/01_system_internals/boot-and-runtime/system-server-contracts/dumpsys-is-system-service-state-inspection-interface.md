---
title: "dumpsys는 system service의 현재 상태를 보는 inspection interface다"
tags: [android, android/system-internals, android/boot-runtime, android/system-server]
aliases: ["dumpsys는 system service의 현재 상태를 보는 inspection interface다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# dumpsys는 system service의 현재 상태를 보는 inspection interface다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

`dumpsys`는 Android framework service가 노출하는 현재 상태 덤프를 읽는 도구다. ActivityManager, WindowManager, PackageManager, PowerManager, JobScheduler 같은 service의 판단 결과를 볼 수 있으므로 로그만으로 원인을 알 수 없을 때 핵심 단서가 된다.

## 실무 규칙

- lifecycle 문제는 `dumpsys activity`, process 문제는 `dumpsys activity processes`와 `dumpsys meminfo`를 함께 본다.
- package scan과 permission 문제는 `dumpsys package`를 본다.
- background work는 `dumpsys jobscheduler`, `dumpsys alarm`, `dumpsys deviceidle`을 함께 본다.
- dump는 순간 상태이므로 재현 직후와 문제 발생 전후를 비교한다.

## 관련 문서

- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [디버깅 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)

공식 문서: [dumpsys](https://developer.android.com/tools/dumpsys)
