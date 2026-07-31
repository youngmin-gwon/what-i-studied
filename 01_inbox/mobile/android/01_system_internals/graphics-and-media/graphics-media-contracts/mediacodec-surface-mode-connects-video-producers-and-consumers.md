---
title: MediaCodec Surface 모드는 영상 producer와 consumer를 연결한다
tags: [android, android/media, android/codec]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

MediaCodec은 encoder input 또는 decoder output에 `Surface`를 사용할 수 있다. Encoder는 `createInputSurface()`로 입력 Surface를 만들 수 있고, decoder는 configure 단계에서 출력 Surface를 받아 decoded frame을 화면이나 다른 consumer로 보낼 수 있다.

Surface 모드는 앱이 매 프레임을 ByteBuffer로 꺼내 복사하는 단계를 줄일 수 있다. 카메라에서 encoder로, decoder에서 display로 이어지는 video pipeline에서 특히 중요하다.

하지만 Surface 모드가 “시스템 전체에서 항상 zero-copy”라는 뜻은 아니다. 내부 포맷 변환, 색 공간 변환, GPU 합성, codec/HAL 경계, protected buffer 정책에 따라 복사나 추가 작업이 생길 수 있다.

정확한 판단은 API 모드만 보고 하지 않는다. `MediaCodecInfo`, output format, frame rendered callback, Perfetto trace, device-specific 동작을 함께 확인한다.

관련 노트: {link(CONTRACTS / "surface-based-media-pipeline-avoids-app-level-pixel-copy.md", "Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다")}, {link(CONTRACTS / "mediacodec-bytebuffer-mode-makes-the-app-own-sample-flow.md", "MediaCodec ByteBuffer 모드는 앱이 sample 흐름을 소유한다")}

근거: [MediaCodec API reference](https://developer.android.com/reference/android/media/MediaCodec)
