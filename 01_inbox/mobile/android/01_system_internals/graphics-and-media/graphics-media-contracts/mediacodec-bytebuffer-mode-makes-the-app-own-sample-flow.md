---
title: mediacodec-bytebuffer-mode-makes-the-app-own-sample-flow
tags: [android, android/codec, android/media]
aliases: []
date modified: 2026-08-03 17:25:12 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## MediaCodec ByteBuffer 모드는 앱이 sample 흐름을 소유한다

MediaCodec 의 ByteBuffer 모드는 앱이 codec 입력 buffer 를 얻어 샘플을 채우고, 출력 buffer 에서 결과를 읽는 방식이다. 동기식 API 에서는 dequeue/queue 호출을 사용하고, 비동기식 API 에서는 callback 으로 사용 가능한 buffer 를 받는다.

이 모드에서는 presentation timestamp, codec-specific data, format change, end-of-stream, encrypted sample 여부를 앱이 명확히 관리해야 한다. 사용한 출력 buffer 는 반드시 codec 에 release 해야 다음 작업이 진행된다.

ByteBuffer 모드는 muxing, packet parsing, custom transform, CPU 접근이 필요한 처리에는 적합하다. 하지만 고해상도 raw video frame 을 앱 메모리로 가져와 복사하거나 색 변환하면 CPU 와 메모리 대역폭 비용이 커질 수 있다.

따라서 영상 프레임을 화면이나 encoder 로 바로 넘길 수 있다면 Surface 입출력을 먼저 검토하고, 앱이 실제 bytes 를 소유해야 하는 경우에 ByteBuffer 모드를 선택한다.

관련 노트: [MediaCodec Surface 모드는 영상 producer와 consumer를 연결한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/mediacodec-surface-mode-connects-video-producers-and-consumers.md)

근거: [MediaCodec API reference](https://developer.android.com/reference/android/media/MediaCodec)
