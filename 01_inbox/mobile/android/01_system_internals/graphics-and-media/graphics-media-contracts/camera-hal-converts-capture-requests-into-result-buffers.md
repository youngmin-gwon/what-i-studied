---
title: Camera HAL은 capture request를 result와 output buffer로 변환한다
tags: [android, android/media, android/camera, android/hal]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

# Camera HAL은 capture request를 result와 output buffer로 변환한다

Android 카메라 파이프라인은 앱의 capture request를 카메라 subsystem이 처리하고, 결과 metadata와 하나 이상의 output buffer를 돌려주는 구조로 이해할 수 있다. 앱은 보통 CameraX나 Camera2를 통해 이 계약에 접근한다.

Camera HAL은 camera framework와 vendor camera driver/hardware 사이의 경계다. 센서, ISP, 3A, 후처리, stream configuration 같은 세부 동작은 기기 구현에 크게 의존한다.

앱 수준에서 확실히 다룰 수 있는 것은 `CameraCharacteristics`, capture session, request parameter, output `Surface`, result metadata, timestamp 같은 framework 계약이다. HAL 내부 메모리 경로나 DMABuf 사용 여부를 앱 API의 일반 보장처럼 적으면 안 된다.

따라서 카메라 성능이나 품질 문제를 설명할 때는 공개 API 계약과 vendor 구현 추정을 분리해야 한다. 문서에는 “HAL이 무엇을 보장한다”보다 “framework가 어떤 형태로 request/result/output surface를 모델링한다”를 먼저 적는다.

관련 노트: [Android HAL and kernel](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md), [Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surface-based-media-pipeline-avoids-app-level-pixel-copy.md)

근거: [AOSP Camera HAL](https://source.android.com/docs/core/camera/camera3)
