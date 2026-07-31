---
title: Graphics and media contracts
tags: [android, android/graphics, android/media]
aliases: [Android graphics media contracts]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

# Graphics and media contracts

이 묶음은 Android graphics/media를 API 사용법이 아니라 실행 계약으로 정리한다. 핵심 질문은 “누가 버퍼를 생산하고, 누가 소비하며, 어느 thread/service/HAL 경계에서 deadline을 놓치는가”다.

## 그래픽 파이프라인

- [Android 렌더링 파이프라인은 Surface 버퍼를 합성기로 넘기는 계약이다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/android-rendering-pipeline-is-surface-to-bufferqueue-to-compositor.md)
- [Surface는 그래픽 버퍼 producer 측 계약이다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surface-is-producer-side-contract-for-graphic-buffers.md)
- [Canvas, Skia, Compose는 합성기가 아니라 그리기 명령의 생산자다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/canvas-skia-and-compose-produce-drawing-commands-not-display-composition.md)
- [RenderThread는 렌더 작업을 나누지만 UI 스레드 비용을 없애지 않는다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/renderthread-submits-render-work-without-making-ui-thread-free.md)
- [BufferQueue는 producer와 consumer를 버퍼 소유권으로 분리한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/bufferqueue-separates-producer-and-consumer-with-buffer-ownership.md)
- [SurfaceFlinger는 보이는 레이어를 HWC와 함께 합성한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surfaceflinger-composes-visible-layers-with-hwc.md)
- [Hardware Composer는 기기 제약 안에서 합성을 offload한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/hardware-composer-offloads-composition-under-device-constraints.md)
- [VSync와 Choreographer는 frame deadline을 정의한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/vsync-and-choreographer-define-frame-deadline.md)
- [Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)

## 카메라와 미디어

- [CameraX와 Camera2는 제어 경계가 다르다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/camerax-and-camera2-have-different-control-boundaries.md)
- [Camera HAL은 capture request를 result와 output buffer로 변환한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/camera-hal-converts-capture-requests-into-result-buffers.md)
- [카메라 출력 Surface는 프리뷰, 분석, 녹화 파이프라인을 정의한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/camera-output-surfaces-define-preview-analysis-and-recording-pipelines.md)
- [ImageReader는 앱이 접근할 수 있는 이미지 버퍼를 제공한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/imagereader-is-for-app-accessible-image-buffers.md)
- [MediaCodec ByteBuffer 모드는 앱이 sample 흐름을 소유한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/mediacodec-bytebuffer-mode-makes-the-app-own-sample-flow.md)
- [MediaCodec Surface 모드는 영상 producer와 consumer를 연결한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/mediacodec-surface-mode-connects-video-producers-and-consumers.md)
- [Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surface-based-media-pipeline-avoids-app-level-pixel-copy.md)
- [Media3 ExoPlayer는 playback stack이지 저수준 codec API가 아니다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/media3-exoplayer-is-playback-stack-not-low-level-codec-api.md)
- [AudioTrack, AAudio, Oboe는 지연 시간과 이식성의 trade-off를 고른다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/audiotrack-aaudio-and-oboe-choose-latency-and-portability-tradeoffs.md)
- [AudioFocus는 재생 권한이 아니라 공유 출력 정책이다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/audiofocus-is-shared-output-policy-not-playback-permission.md)
- [DRM 보호 미디어는 secure codec과 보호된 출력 경로를 요구할 수 있다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/drm-protected-media-needs-secure-codec-and-output-path.md)
- [그래픽과 미디어 디버깅은 timeline과 component state에서 시작한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/graphics-media-debugging-starts-from-timeline-and-component-state.md)

## 중복 방지 규칙

- Compose 문서는 recomposition, layout, draw 비용을 설명하고, SurfaceFlinger/HWC 합성 정책은 이 묶음으로 연결한다.
- Camera 문서는 use case와 session/output Surface 선택을 설명하고, HAL 내부 구현은 보장된 앱 API처럼 적지 않는다.
- Media3/ExoPlayer 문서는 playback orchestration을 설명하고, codec buffer 소유권은 MediaCodec 노트로 분리한다.
- 성능 문서는 고정 latency 숫자보다 측정 구간, refresh rate, trace 근거를 먼저 둔다.
