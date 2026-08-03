---
title: mediacodec-surface-mode-connects-video-producers-and-consumers
tags: [android, android/codec, android/media]
aliases: []
date modified: 2026-08-03 17:25:13 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## MediaCodec Surface 모드는 영상 producer 와 consumer 를 연결한다

MediaCodec 은 encoder input 또는 decoder output 에 `Surface` 를 사용할 수 있다. Encoder 는 `createInputSurface()` 로 입력 Surface 를 만들 수 있고, decoder 는 configure 단계에서 출력 Surface 를 받아 decoded frame 을 화면이나 다른 consumer 로 보낼 수 있다.

Surface 모드는 앱이 매 프레임을 ByteBuffer 로 꺼내 복사하는 단계를 줄일 수 있다. 카메라에서 encoder 로, decoder 에서 display 로 이어지는 video pipeline 에서 특히 중요하다.

하지만 Surface 모드가 "시스템 전체에서 항상 zero-copy"라는 뜻은 아니다. 내부 포맷 변환, 색 공간 변환, GPU 합성, codec/HAL 경계, protected buffer 정책에 따라 복사나 추가 작업이 생길 수 있다.

정확한 판단은 API 모드만 보고 하지 않는다. `MediaCodecInfo`, output format, frame rendered callback, Perfetto trace, device-specific 동작을 함께 확인한다.

관련 노트: [Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surface-based-media-pipeline-avoids-app-level-pixel-copy.md), [MediaCodec ByteBuffer 모드는 앱이 sample 흐름을 소유한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/mediacodec-bytebuffer-mode-makes-the-app-own-sample-flow.md)

근거: [MediaCodec API reference](https://developer.android.com/reference/android/media/MediaCodec)
