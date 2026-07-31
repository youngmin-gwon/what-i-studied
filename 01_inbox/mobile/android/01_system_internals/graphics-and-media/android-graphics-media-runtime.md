---
title: Android graphics/media runtime
tags: [android, android/graphics, android/media, android/system-internals]
aliases: [android-graphics-and-media, Graphics, Media Pipeline, SurfaceFlinger]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

Android의 graphics/media runtime은 UI toolkit 사용법보다 버퍼와 시간축을 먼저 봐야 이해된다. 앱은 Surface에 프레임을 생산하고, BufferQueue는 producer/consumer를 분리하며, SurfaceFlinger와 HWC는 보이는 레이어를 display frame으로 합성한다.

미디어도 같은 구조 위에 있다. 카메라 프레임, codec 입출력, video playback, DRM protected output은 모두 어떤 Surface와 buffer ownership을 쓰는지에 따라 성능과 제약이 달라진다.

정본 묶음: [Graphics and media contracts](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/graphics-media-contracts.md)

## 핵심 지도

- [렌더링 파이프라인](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/android-rendering-pipeline-is-surface-to-bufferqueue-to-compositor.md)
- [VSync와 Choreographer](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/vsync-and-choreographer-define-frame-deadline.md)
- [Jank와 frame deadline](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
- [CameraX와 Camera2](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/camerax-and-camera2-have-different-control-boundaries.md)
- [MediaCodec Surface 모드](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/mediacodec-surface-mode-connects-video-producers-and-consumers.md)
- [Media3 ExoPlayer](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/media3-exoplayer-is-playback-stack-not-low-level-codec-api.md)
- [AudioTrack, AAudio, Oboe](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/audiotrack-aaudio-and-oboe-choose-latency-and-portability-tradeoffs.md)
- [DRM protected media](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/drm-protected-media-needs-secure-codec-and-output-path.md)
- [그래픽/미디어 디버깅](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/graphics-media-debugging-starts-from-timeline-and-component-state.md)

## 정리 기준

기존 `android-graphics-and-media` 하위 노트는 API 예제와 시스템 내부 설명이 섞여 있었다. 이 노트는 그 내용을 Surface, BufferQueue, SurfaceFlinger, Camera, MediaCodec, Audio, DRM의 의미 단위로 다시 묶은 허브다.
