---
title: Surface는 그래픽 버퍼 producer 측 계약이다
tags: [android, android/graphics, android/surface]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

`Surface`는 앱이 픽셀을 직접 소유한다는 뜻이 아니라, 그래픽 버퍼를 생산할 수 있는 endpoint를 받았다는 뜻이다. Canvas, OpenGL ES, Vulkan, MediaCodec, Camera2 같은 producer는 `Surface`를 대상으로 프레임을 제출할 수 있다.

`Surface` 뒤에는 보통 BufferQueue가 있고, 소비자는 SurfaceFlinger, MediaCodec, ImageReader, SurfaceTexture처럼 상황에 따라 달라진다. 같은 `Surface`라는 타입을 쓰더라도 화면 표시, 영상 인코딩, 이미지 분석의 의미는 소비자가 무엇인지에 따라 결정된다.

실무적으로 중요한 질문은 “이 Surface에 쓰면 누가 소비하는가”다. 화면 프리뷰라면 display pipeline으로 가고, encoder input surface라면 codec으로 가며, ImageReader surface라면 앱이 `Image`를 acquire해야 한다.

주의할 점은 `Surface`가 자동으로 CPU 접근 가능한 이미지나 zero-copy를 보장하지 않는다는 것이다. 접근 가능성, 포맷, 복사 비용, 동기화 방식은 producer/consumer 조합과 기기 구현에 좌우된다.

관련 노트: {link(CONTRACTS / "surface-based-media-pipeline-avoids-app-level-pixel-copy.md", "Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다")}, {link(CONTRACTS / "camera-output-surfaces-define-preview-analysis-and-recording-pipelines.md", "카메라 출력 Surface는 프리뷰, 분석, 녹화 파이프라인을 정의한다")}
