---
title: 카메라 출력 Surface는 프리뷰, 분석, 녹화 파이프라인을 정의한다
tags: [android, android/media, android/camera]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

Camera2 세션을 만들 때 앱은 하나 이상의 output `Surface`를 미리 구성한다. 각 Surface는 프리뷰, 이미지 분석, 사진 캡처, 영상 녹화 같은 병렬 파이프라인의 destination이 된다.

`SurfaceView`나 `PreviewView`는 사용자가 보는 viewfinder에 적합하고, `ImageReader`는 앱이 `Image`를 acquire해서 YUV/JPEG/RAW 데이터를 읽어야 할 때 사용한다. `MediaCodec`이나 `MediaRecorder`의 Surface는 영상 인코딩으로 직접 이어지는 출력 대상이 될 수 있다.

중요한 제약은 모든 Surface 조합이 가능한 것은 아니라는 점이다. 크기, 포맷, stream use case, 동시 출력 수, dynamic range 조합은 기기 capability와 capture session 설정에 따라 성공, 실패, 성능 저하로 갈릴 수 있다.

`ImageReader`에서는 acquire한 `Image`를 반드시 닫아야 한다. 이미지를 오래 들고 있으면 reader의 max image 큐가 고갈되어 producer가 막히거나 오래된 프레임을 처리하게 된다.

관련 노트: {link(CONTRACTS / "surface-is-producer-side-contract-for-graphic-buffers.md", "Surface는 그래픽 버퍼 producer 측 계약이다")}, {link(CONTRACTS / "imagereader-is-for-app-accessible-image-buffers.md", "ImageReader는 앱이 접근할 수 있는 이미지 버퍼를 제공한다")}

근거: [Camera2 capture sessions and requests](https://developer.android.com/media/camera/camera2/capture-sessions-requests), [Camera2 package summary](https://developer.android.com/reference/android/hardware/camera2/package-summary)
