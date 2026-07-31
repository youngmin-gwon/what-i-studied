---
title: "Surface와 SurfaceFlinger"
tags: ["android", "android/glossary"]
aliases: ["Surface", "SurfaceFlinger"]
---

# Surface와 SurfaceFlinger

정의: Surface는 graphic buffer producer side contract이고, SurfaceFlinger는 visible layer를 Hardware Composer와 함께 최종 화면으로 합성하는 system compositor다.

혼동 방지: 앱의 View/Compose drawing과 display composition은 같은 단계가 아니다. 앱은 buffer를 생산하고, SurfaceFlinger/HWC는 여러 layer를 device display timing에 맞춰 합성한다.

정본 링크:
- [Surface producer contract](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surface-is-producer-side-contract-for-graphic-buffers.md)
- [SurfaceFlinger composition](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surfaceflinger-composes-visible-layers-with-hwc.md)
