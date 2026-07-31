---
title: Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다
tags: [android, android/graphics, android/performance]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

Jank는 사용자가 보는 프레임 흐름이 끊기는 현상이다. 원인은 UI thread의 긴 작업, layout/draw 비용, RenderThread 지연, GPU 작업, BufferQueue backpressure, SurfaceFlinger/HWC composition, thermal throttling처럼 여러 구간에 있을 수 있다.

따라서 “jank = recomposition 문제”나 “jank = GPU 문제”로 바로 좁히면 위험하다. 먼저 Perfetto, Android Studio profiler, `dumpsys gfxinfo`로 어떤 frame이 deadline을 놓쳤는지 보고, 그 frame의 시간축에서 가장 긴 구간을 찾는다.

프레임 예산은 refresh rate에 따라 달라진다. 60fps 목표에서는 약 16ms, 90fps에서는 약 11ms, 120fps에서는 약 8ms가 기준이 된다. 다만 이 숫자는 진단 시작점이지 모든 파이프라인 단계의 독립 예산이 아니다.

앱 수준 개선은 불필요한 measure/layout/draw 감소, main thread work 제거, Compose recomposition 범위 축소, bitmap/영상 처리의 Surface 경로 사용, Recycler/List 측정 최적화처럼 원인 구간에 맞춰야 한다.

관련 노트: [Rendering jank is frame deadline failure](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md), [그래픽과 미디어 디버깅은 timeline과 component state에서 시작한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/graphics-media-debugging-starts-from-timeline-and-component-state.md)

근거: [Android Studio jank detection](https://developer.android.com/studio/profile/jank-detection), [Slow rendering](https://developer.android.com/topic/performance/vitals/render)
