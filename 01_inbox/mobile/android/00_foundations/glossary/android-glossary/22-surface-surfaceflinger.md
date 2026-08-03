---
title: "Surface와 SurfaceFlinger는 앱의 그래픽 버퍼를 합성하여 디스플레이에 출력한다"
tags: ["android", "android/glossary"]
aliases: ["Surface", "SurfaceFlinger"]
date modified: 2026-08-01 01:07:36 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# Surface와 SurfaceFlinger는 앱의 그래픽 버퍼를 합성하여 디스플레이에 출력한다

정의: Surface 는 graphic buffer producer side contract 이고, SurfaceFlinger 는 visible layer 를 Hardware Composer 와 함께 최종 화면으로 합성하는 system compositor 다.

혼동 방지: 앱의 View/Compose drawing 과 display composition 은 같은 단계가 아니다. 앱은 buffer 를 생산하고, SurfaceFlinger/HWC 는 여러 layer 를 device display timing 에 맞춰 합성한다.

정본 링크:

- [Surface producer contract](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surface-is-producer-side-contract-for-graphic-buffers.md)
- [SurfaceFlinger composition](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surfaceflinger-composes-visible-layers-with-hwc.md)
