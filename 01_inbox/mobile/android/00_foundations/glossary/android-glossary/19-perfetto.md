---
title: 19-perfetto
tags: ["android", "android/glossary"]
aliases: ["Perfetto trace", "System trace"]
date modified: 2026-08-03 17:21:33 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Perfetto 는 전체 시스템의 성능 및 추적 데이터를 수집하는 통합 프로파일링 도구다

정의: Perfetto 는 Android system trace 를 수집해 UI thread, RenderThread, SurfaceFlinger, scheduler, binder, I/O 같은 timeline 을 함께 분석하는 tracing platform 이다.

혼동 방지: Perfetto trace 는 benchmark 점수가 아니다. 어떤 frame 이나 operation 이 왜 늦었는지 진단하는 증거이며, 반복 측정과 통제된 benchmark 는 별도 계약으로 봐야 한다.

정본 링크:

- [Profiler and Perfetto diagnosis](../../../06_testing_performance/performance/performance-contracts/profiler-perfetto-dumpsys-are-diagnosis-tools-not-benchmarks.md)
- [Jank frame deadline contract](../../../01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
