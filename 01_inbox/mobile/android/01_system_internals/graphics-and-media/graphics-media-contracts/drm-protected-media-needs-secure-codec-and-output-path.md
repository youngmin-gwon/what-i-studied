---
title: DRM 보호 미디어는 secure codec과 보호된 출력 경로를 요구할 수 있다
tags: [android, android/media, android/drm]
aliases: [DRM, Widevine, MediaDrm]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

DRM 보호 미디어 재생은 단순히 파일을 복호화하는 일이 아니다. 앱 또는 Media3는 DRM scheme, license server, session, key request, key status, codec, output protection을 함께 만족해야 한다.

`MediaDrm`은 DRM scheme의 provisioning, session, key request, offline license 같은 저수준 기능을 제공한다. ExoPlayer/Media3는 이 과정을 playback stack 안에서 추상화할 수 있지만, 라이선스 URL과 인증 방식은 콘텐츠 서비스의 계약이다.

Widevine security level이나 `MediaDrm` security level은 기기와 세션에 따라 달라진다. L1/L3를 절대적인 “하드웨어 전체 처리/소프트웨어 전체 처리”로 단순화하기보다 runtime capability와 실제 license policy 결과를 확인해야 한다.

보호 콘텐츠는 secure decoder나 보호된 output path를 요구할 수 있다. AOSP 그래픽 문서의 protected buffer 설명처럼, 보호 버퍼는 일반 GPU 접근이나 capture 경로에서 제한될 수 있다.

관련 노트: {link(contracts_hub / "surfaceflinger-composes-visible-layers-with-hwc.md", "SurfaceFlinger는 보이는 레이어를 HWC와 함께 합성한다")}, {link(contracts_hub / "media3-exoplayer-is-playback-stack-not-low-level-codec-api.md", "Media3 ExoPlayer는 playback stack이지 저수준 codec API가 아니다")}

근거: [MediaDrm API reference](https://developer.android.com/reference/android/media/MediaDrm), [AOSP BufferQueue and Gralloc protected buffers](https://source.android.com/docs/core/graphics/arch-bq-gralloc)
