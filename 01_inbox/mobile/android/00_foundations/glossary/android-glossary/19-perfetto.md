---
title: "Perfetto"
tags: ["android", "android/glossary"]
aliases: ["System trace", "Perfetto trace"]
---

# Perfetto

정의: Perfetto는 Android system trace를 수집해 UI thread, RenderThread, SurfaceFlinger, scheduler, binder, I/O 같은 timeline을 함께 분석하는 tracing platform이다.

혼동 방지: Perfetto trace는 benchmark 점수가 아니다. 어떤 frame이나 operation이 왜 늦었는지 진단하는 증거이며, 반복 측정과 통제된 benchmark는 별도 계약으로 봐야 한다.

정본 링크:
- [Profiler and Perfetto diagnosis](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/profiler-perfetto-dumpsys-are-diagnosis-tools-not-benchmarks.md)
- [Jank frame deadline contract](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
