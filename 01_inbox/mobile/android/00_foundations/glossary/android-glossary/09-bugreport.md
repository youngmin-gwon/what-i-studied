---
title: 09-bugreport
tags: ["android", "android/glossary"]
aliases: ["Android bugreport"]
date modified: 2026-08-03 17:21:38 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Bugreport 는 기기의 상태, 로그, 시스템 정보를 종합하여 버그를 분석하는 파일이다

정의: Bugreport 는 logcat, dumpsys, tombstone, traces, system properties 같은 device 상태 증거를 한 번에 수집하는 진단 bundle 이다.

혼동 방지: Bugreport 는 원인 분석의 출발점이지 benchmark 결과가 아니다. 시점, 재현 조건, device build, app version 을 같이 고정해야 의미 있는 증거가 된다.

정본 링크:

- [Debugging contracts](../../../06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
- [Dumpsys inspection contract](../../../01_system_internals/boot-and-runtime/system-server-contracts/dumpsys-is-system-service-state-inspection-interface.md)
