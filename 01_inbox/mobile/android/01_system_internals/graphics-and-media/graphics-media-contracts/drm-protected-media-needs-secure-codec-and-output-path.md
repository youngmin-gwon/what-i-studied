---
title: drm-protected-media-needs-secure-codec-and-output-path
tags: [android, android/drm, android/media]
aliases: [DRM, MediaDrm, Widevine]
date modified: 2026-08-03 17:25:03 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## DRM 보호 미디어는 secure codec 과 보호된 출력 경로를 요구할 수 있다

DRM 보호 미디어 재생은 단순히 파일을 복호화하는 일이 아니다. 앱 또는 Media3 는 DRM scheme, license server, session, key request, key status, codec, output protection 을 함께 만족해야 한다.

`MediaDrm` 은 DRM scheme 의 provisioning, session, key request, offline license 같은 저수준 기능을 제공한다. ExoPlayer/Media3 는 이 과정을 playback stack 안에서 추상화할 수 있지만, 라이선스 URL 과 인증 방식은 콘텐츠 서비스의 계약이다.

Widevine security level 이나 `MediaDrm` security level 은 기기와 세션에 따라 달라진다. L1/L3 를 절대적인 "하드웨어 전체 처리/소프트웨어 전체 처리"로 단순화하기보다 runtime capability 와 실제 license policy 결과를 확인해야 한다.

보호 콘텐츠는 secure decoder 나 보호된 output path 를 요구할 수 있다. AOSP 그래픽 문서의 protected buffer 설명처럼, 보호 버퍼는 일반 GPU 접근이나 capture 경로에서 제한될 수 있다.

관련 노트: [SurfaceFlinger는 보이는 레이어를 HWC와 함께 합성한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surfaceflinger-composes-visible-layers-with-hwc.md), [Media3 ExoPlayer는 playback stack이지 저수준 codec API가 아니다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/media3-exoplayer-is-playback-stack-not-low-level-codec-api.md)

근거: [MediaDrm API reference](https://developer.android.com/reference/android/media/MediaDrm), [AOSP BufferQueue and Gralloc protected buffers](https://source.android.com/docs/core/graphics/arch-bq-gralloc)
