---
title: camerax-and-camera2-have-different-control-boundaries
tags: [android, android/camera, android/media]
aliases: []
date modified: 2026-08-03 17:24:56 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## CameraX 와 Camera2 는 제어 경계가 다르다

Camera2 는 `CameraDevice`, `CaptureRequest`, `CameraCaptureSession`, `Surface` 를 직접 조합해 카메라 장치와 캡처 세션을 제어하는 framework API 다. 출력 대상, 요청 파라미터, 동시 스트림, capture timing 을 세밀하게 다뤄야 할 때 적합하다.

CameraX 는 Camera2 위에서 Preview, ImageCapture, ImageAnalysis, VideoCapture 같은 use case 와 lifecycle 바인딩을 제공하는 Jetpack 계층이다. 일반적인 미리보기, 사진, 분석, 녹화 앱은 CameraX 를 우선 검토하는 편이 유지보수에 유리하다.

둘의 차이는 "성능이 어느 쪽이 무조건 빠른가"가 아니다. CameraX 는 흔한 작업의 장치 호환성과 lifecycle 처리를 줄여 주고, Camera2 는 낮은 수준의 세션·요청 제어권을 제공한다.

선택 기준은 필요한 제어권이다. 표준 프리뷰/캡처/분석이면 CameraX, vendor-specific 기능이나 세밀한 stream 조합, capture request 제어가 필요하면 Camera2 를 검토한다.

관련 노트: [카메라 출력 Surface는 프리뷰, 분석, 녹화 파이프라인을 정의한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/camera-output-surfaces-define-preview-analysis-and-recording-pipelines.md)

근거: [CameraX overview](https://developer.android.com/media/camera/camerax), [Camera2 capture sessions and requests](https://developer.android.com/media/camera/camera2/capture-sessions-requests)
