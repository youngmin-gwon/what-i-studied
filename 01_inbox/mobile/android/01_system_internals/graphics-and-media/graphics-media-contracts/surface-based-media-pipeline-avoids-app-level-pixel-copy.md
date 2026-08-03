---
title: surface-based-media-pipeline-avoids-app-level-pixel-copy
tags: [android, android/graphics, android/media]
aliases: []
date modified: 2026-08-03 17:25:14 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다

카메라, codec, display 를 Surface 로 연결하면 앱이 프레임을 CPU 배열로 꺼냈다가 다시 넣는 단계를 줄일 수 있다. 이 때문에 실무에서는 Surface 경로를 "zero-copy 에 가깝다"거나 "앱 수준 픽셀 복사를 피한다"고 설명한다.

정확히는 시스템 전체에 복사가 전혀 없다는 보장이 아니다. BufferQueue 는 producer 와 consumer 의 버퍼 소유권을 조정하고, Gralloc/HAL/codec/display 구현은 포맷과 usage flag 에 맞는 메모리를 선택한다.

예를 들어 Camera2 preview Surface, MediaCodec input Surface, decoder output Surface, SurfaceView 는 모두 앱이 픽셀을 직접 만지지 않는 경로를 만들 수 있다. 반대로 ImageReader 나 Bitmap 처리로 CPU 접근을 요구하면 복사와 동기화 비용이 커질 수 있다.

문서에서는 `zero-copy` 라는 표현을 쓸 때 "앱 코드가 명시적인 CPU 픽셀 복사를 하지 않는 경로"로 좁혀 적는 것이 안전하다. 실제 복사 여부는 trace 와 기기별 구현으로 확인한다.

관련 노트: [BufferQueue는 producer와 consumer를 버퍼 소유권으로 분리한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/bufferqueue-separates-producer-and-consumer-with-buffer-ownership.md), [DRM 보호 미디어는 secure codec과 보호된 출력 경로를 요구할 수 있다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/drm-protected-media-needs-secure-codec-and-output-path.md)
