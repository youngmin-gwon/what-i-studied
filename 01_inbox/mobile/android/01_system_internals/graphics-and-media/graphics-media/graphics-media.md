---
title: graphics-media
tags: [android, android/graphics, android/media]
aliases: [Android graphics media contracts]
date modified: 2026-08-04 15:50:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## Graphics and media contracts

이 문서는 Android 그래픽 및 미디어 파이프라인을 API 사용법이 아닌 **실행 계약(Execution Contracts)** 관점에서 정리한 정본 인덱스다. 핵심 질문은 "누가 버퍼를 생산하고, 누가 소비하며, 어느 thread/service/HAL 경계에서 마감 시간(Deadline)을 놓치는가"이다.

상위 문서: [Android graphics/media runtime](../android-graphics-media-runtime.md)

### 읽는 순서

1. **렌더링 파이프라인 정본**: [Surface](surface-is-producer-side-for-graphic-buffers.md), [BufferQueue](bufferqueue-separates-producer-and-consumer-with-buffer-ownership.md), [SurfaceFlinger & HWC](surfaceflinger-composes-visible-layers-with-hwc.md), [파이프라인 전체 구조](android-rendering-pipeline-is-surface-to-bufferqueue-to-compositor.md)를 통해 버퍼 픽셀 전달 흐름을 이해한다.
2. **그리기와 프레임 스케줄링**: [Canvas/Compose는 합성기가 아니다](canvas-skia-and-compose-produce-drawing-commands-not-display-composition.md), [RenderThread 역할](renderthread-submits-render-work-without-making-ui-thread-free.md), [VSync와 Choreographer](vsync-and-choreographer-define-frame-deadline.md), [Jank 원인 분석](jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)으로 프레임 마감 시간을 파악한다.
3. **카메라 및 이미지 스트림**: [Camera HAL3 파이프라인](camera-hal-converts-capture-requests-into-result-buffers.md), [카메라 Output Surface](camera-output-surfaces-define-preview-analysis-and-recording-pipelines.md), [CameraX와 Camera2 경계](camerax-and-camera2-have-different-control-boundaries.md), [ImageReader 버퍼](imagereader-is-for-app-accessible-image-buffers.md)를 확인한다.
4. **미디어 비디오 코덱 & DRM**: [MediaCodec Surface 모드](mediacodec-surface-mode-connects-video-producers-and-consumers.md), [MediaCodec ByteBuffer 모드](mediacodec-bytebuffer-mode-makes-the-app-own-sample-flow.md), [Zero-Copy 파이프라인](surface-based-media-pipeline-avoids-app-level-pixel-copy.md), [DRM & Secure Codec](drm-protected-media-needs-secure-codec-and-output-path.md), [Media3 ExoPlayer](media3-exoplayer-is-playback-stack-not-low-level-codec-api.md)를 본다.
5. **오디오 파이프라인**: [AudioFocus 공유 정책](audiofocus-is-shared-output-policy-not-playback-permission.md), [AudioTrack, AAudio & Oboe](audiotrack-aaudio-and-oboe-choose-latency-and-portability-tradeoffs.md)로 오디오 출력 정책과 초저지연 경로를 이해한다.
6. **통합 디버깅**: [그래픽 미디어 디버깅](graphics-media-debugging-starts-from-timeline-and-component-state.md)을 바탕으로 Perfetto 및 dumpsys 관찰 신호를 결합한다.

### 문제 분류 기준

- **화면 버벅임 및 프레임 드롭(Jank)**: [Jank 원인 분석](jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md), [VSync와 Choreographer](vsync-and-choreographer-define-frame-deadline.md), [RenderThread 역할](renderthread-submits-render-work-without-making-ui-thread-free.md)
- **화면 합성 및 전력 효율 오버레이**: [Hardware Composer](hardware-composer-offloads-composition-under-device-constraints.md), [SurfaceFlinger & HWC](surfaceflinger-composes-visible-layers-with-hwc.md), [Canvas/Compose는 합성기가 아니다](canvas-skia-and-compose-produce-drawing-commands-not-display-composition.md)
- **카메라 촬영 및 ML 이미지 처리**: [카메라 Output Surface](camera-output-surfaces-define-preview-analysis-and-recording-pipelines.md), [ImageReader 버퍼](imagereader-is-for-app-accessible-image-buffers.md), [Camera HAL3 파이프라인](camera-hal-converts-capture-requests-into-result-buffers.md)
- **비디오 인코딩/디코딩 성능 및 DRM**: [MediaCodec Surface 모드](mediacodec-surface-mode-connects-video-producers-and-consumers.md), [DRM & Secure Codec](drm-protected-media-needs-secure-codec-and-output-path.md), [Zero-Copy 파이프라인](surface-based-media-pipeline-avoids-app-level-pixel-copy.md)
- **오디오 중첩 및 저지연 음동기화**: [AudioFocus 공유 정책](audiofocus-is-shared-output-policy-not-playback-permission.md), [AudioTrack, AAudio & Oboe](audiotrack-aaudio-and-oboe-choose-latency-and-portability-tradeoffs.md)
