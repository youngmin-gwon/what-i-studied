---
title: Android 렌더링 파이프라인은 Surface 버퍼를 합성기로 넘기는 계약이다
tags: [android, android/graphics, android/system-internals]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

Android에서 화면에 보이는 대부분의 출력은 먼저 `Surface`에 그려진다. 앱, 비디오 디코더, 카메라 프리뷰, OpenGL/Vulkan 렌더러는 각각 버퍼를 생산하고, 그 버퍼는 `BufferQueue`를 통해 소비자에게 전달된다.

이 파이프라인의 핵심은 “누가 그렸는가”보다 “어떤 `Surface`가 어떤 소비자에게 버퍼를 넘기는가”다. 일반 앱 UI는 윈도우의 `Surface`에 렌더링되고, 화면에 보이는 여러 레이어는 SurfaceFlinger가 최종 디스플레이용으로 합성한다.

따라서 그래픽 성능을 볼 때는 View, Compose, Canvas만 보면 부족하다. 앱 스레드가 프레임을 준비했는지, RenderThread/GPU가 버퍼를 채웠는지, BufferQueue가 막혔는지, SurfaceFlinger/HWC가 제때 합성했는지를 같은 시간축에서 봐야 한다.

관련 노트: [Surface는 그래픽 버퍼 producer 측 계약이다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surface-is-producer-side-contract-for-graphic-buffers.md), [BufferQueue는 producer와 consumer를 버퍼 소유권으로 분리한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/bufferqueue-separates-producer-and-consumer-with-buffer-ownership.md), [SurfaceFlinger는 보이는 레이어를 HWC와 함께 합성한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surfaceflinger-composes-visible-layers-with-hwc.md)

근거: [AOSP Graphics](https://source.android.com/docs/core/graphics), [AOSP Graphics architecture](https://source.android.com/docs/core/graphics/architecture)
