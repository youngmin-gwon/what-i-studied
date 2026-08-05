---
title: media-audio-camera-contracts
tags: ["android", "android/system-services"]
aliases: ["미디어/오디오/카메라 시스템 서비스 접근 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## 미디어/오디오/카메라 시스템 서비스 접근 계약

이 지도는 오디오 포커스 조정, 카메라 접근 표면, 재생 상태 노출이라는 system-service 관점의 세 접근 지점을 다룬다. 코덱, 렌더링 파이프라인 자체는 다루지 않는다.

### 읽는 순서

1. [AudioManager는 포커스 요청으로 여러 앱의 동시 재생을 조정한다](./audiomanager-arbitrates-concurrent-playback-through-focus-requests.md)에서 여러 앱이 소리를 낼 때의 중재 모델을 본다.
2. [CameraManager 접근은 가용성 콜백과 캐릭터리스틱 조회로 시작한다](./cameramanager-access-starts-with-availability-and-characteristics.md)에서 카메라를 열기 전에 확인해야 할 것을 본다.
3. [MediaSession은 재생 상태를 시스템 UI와 외부 컨트롤러에 노출하는 계약이다](./mediasession-exposes-playback-state-to-system-and-external-controllers.md)에서 잠금화면/블루투스 컨트롤 연동 모델을 본다.

### 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| 다른 앱 소리와 겹치거나 갑자기 끊김 | audio focus 요청 타입과 focus 변화 콜백 처리 |
| 카메라를 열 수 없음(다른 앱이 사용 중 등) | availability 콜백과 카메라 disconnect 처리 |
| 잠금화면/블루투스에 재생 컨트롤이 안 뜸 | MediaSession 등록과 PlaybackState 갱신 여부 |

### 책임 경계

- 오디오 포커스 조정과 실제 오디오 디코딩/믹싱 파이프라인은 다른 계층이다. 이 지도는 조정 계약만 다룬다.
- 카메라의 프레임 처리, 인코딩, HAL 세부 구현은 `01_system_internals/graphics-and-media`가 담당한다.
- MediaSession은 UI 노출 계약이며 실제 미디어 재생 엔진(ExoPlayer/Media3 등)의 선택과는 독립적이다.

### 노트 목록

- [AudioManager는 포커스 요청으로 여러 앱의 동시 재생을 조정한다](./audiomanager-arbitrates-concurrent-playback-through-focus-requests.md)
- [CameraManager 접근은 가용성 콜백과 캐릭터리스틱 조회로 시작한다](./cameramanager-access-starts-with-availability-and-characteristics.md)
- [MediaSession은 재생 상태를 시스템 UI와 외부 컨트롤러에 노출하는 계약이다](./mediasession-exposes-playback-state-to-system-and-external-controllers.md)

검증일: 2026-08-03. [오디오 포커스 관리](https://developer.android.com/media/optimize/audio-focus)와 [Camera2 문서](https://developer.android.com/media/camera/camera2)를 기준으로 확인했다.
