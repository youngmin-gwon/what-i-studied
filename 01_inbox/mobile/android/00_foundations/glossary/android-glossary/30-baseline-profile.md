---
title: 30-baseline-profile
tags: ["android", "android/glossary"]
aliases: ["Baseline Profiles"]
date modified: 2026-08-03 17:21:23 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Baseline Profile 은 앱 실행 및 주요 경로를 미리 JIT 컴파일하여 런타임 성능을 높인다

정의: Baseline Profile 은 앱의 critical user journey 에서 필요한 method/class 를 기록해 install-time 또는 ahead-of-time compilation hint 로 제공하는 성능 artifact 다.

혼동 방지: Baseline Profile 은 benchmark 자체가 아니다. profile 생성, profile 적용 검증, profiled/unprofiled 비교, startup/jank metric 측정을 분리해야 효과를 판단할 수 있다.

정본 링크:

- [Baseline profile generation](../../../06_testing_performance/performance/benchmark-baseline-contracts/baseline-profile-generation-records-critical-user-journeys.md)
- [Baseline profile verification](../../../06_testing_performance/performance/benchmark-baseline-contracts/baseline-profile-verification-compares-profiled-and-unprofiled-performance.md)
