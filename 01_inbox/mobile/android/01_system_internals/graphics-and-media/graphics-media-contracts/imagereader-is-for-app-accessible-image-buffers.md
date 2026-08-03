---
title: imagereader-is-for-app-accessible-image-buffers
tags: [android, android/camera, android/media]
aliases: []
date modified: 2026-08-03 17:25:09 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## ImageReader 는 앱이 접근할 수 있는 이미지 버퍼를 제공한다

ImageReader 는 다른 media API 가 렌더링한 데이터를 앱이 `Image` 객체로 직접 읽을 수 있게 하는 Surface consumer 다. Camera2, MediaCodec 같은 producer 는 ImageReader 가 제공하는 Surface 를 출력 대상으로 사용할 수 있다.

`acquireLatestImage()` 는 실시간 분석에서 오래된 이미지를 버리고 최신 이미지에 따라잡기 좋고, `acquireNextImage()` 는 순서대로 처리해야 하는 batch/background 작업에 더 맞다. 어떤 방식을 쓰든 acquire 한 이미지는 `close()` 해서 큐를 비워야 한다.

ImageReader 의 `maxImages` 는 동시에 앱이 잡고 있을 수 있는 이미지 수의 상한이다. 이 상한을 넘기면 새 이미지를 얻지 못하거나 producer 가 stall/drop 상태가 될 수 있다.

ImageReader 를 쓰는 이유는 CPU 또는 앱 로직이 픽셀에 접근해야 하기 때문이다. 화면 표시나 인코딩처럼 앱이 픽셀을 직접 읽을 필요가 없다면 SurfaceView 나 codec Surface 경로가 더 적절할 수 있다.

관련 노트: [카메라 출력 Surface는 프리뷰, 분석, 녹화 파이프라인을 정의한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/camera-output-surfaces-define-preview-analysis-and-recording-pipelines.md)

근거: [ImageReader API reference](https://developer.android.com/reference/android/media/ImageReader)
