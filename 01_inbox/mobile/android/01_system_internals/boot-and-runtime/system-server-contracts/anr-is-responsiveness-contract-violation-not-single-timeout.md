---
title: "ANR은 단일 timeout 숫자가 아니라 responsiveness 계약 위반이다"
tags: [android, android/system-internals, android/boot-runtime, android/system-server]
aliases: ["ANR은 단일 timeout 숫자가 아니라 responsiveness 계약 위반이다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# ANR은 단일 timeout 숫자가 아니라 responsiveness 계약 위반이다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

ANR은 앱이 정해진 시스템 상호작용에 제때 응답하지 못했다는 신호다. 입력, broadcast, service, content provider, foreground service start 등 경로마다 timeout과 판단 기준이 다를 수 있으므로 하나의 고정 숫자로 외우면 안 된다.

## 실무 규칙

- main thread에서 long-running I/O, lock wait, binder wait를 만들지 않는다.
- broadcast와 service work는 제한 시간 안에 넘기고 장기 작업은 적절한 background work로 넘긴다.
- ANR 분석은 traces, main thread stack, binder thread 상태, lock owner, system_server 로그를 함께 본다.
- timeout 값은 Android 버전과 foreground/background 조건에 따라 바뀔 수 있으므로 공식 문서와 현재 platform source를 확인한다.

## 관련 문서

- [성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)
- [디버깅 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)

공식 문서: [ANRs](https://developer.android.com/topic/performance/vitals/anr)
