---
title: android-graphics-media-runtime
tags: [android, android/graphics, android/media, android/system-internals]
aliases: [android-graphics-and-media, Graphics, Media Pipeline, SurfaceFlinger]
date modified: 2026-08-04 15:50:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## Android graphics/media runtime

Android의 그래픽과 미디어 런타임 체계는 단순 UI 툴킷 뷰 작성법을 넘어 **버퍼 소유권(Buffer Ownership)과 시간축 VSync 프레임 마감 시간(Frame Deadline)**을 통제하는 하드웨어 가속 실행 계약 위에 구축되어 있다. 앱은 Surface에 프레임을 생산하고, BufferQueue는 producer/consumer를 격리하며, SurfaceFlinger와 Hardware Composer(HWC)는 최적의 오버레이 방식으로 최종 디스플레이를 합성한다.

정본 묶음: [Graphics and media contracts](graphics-media-contracts/graphics-media-contracts.md)

### 계층 구분

Android 그래픽/미디어 노트는 다음 4개 하위 시스템 계층 중 어느 지점의 동작 계약을 설명하는지 명확히 구분한다.

```mermaid
graph TD
    AppLayer[1. App API Layer: Canvas, Compose, Camera2/CameraX, Media3, MediaCodec] --> FrameworkLayer
    FrameworkLayer[2. Framework Service Layer: Choreographer, RenderThread, AudioService, CameraService] --> NativeLayer
    NativeLayer[3. Native Service Layer: SurfaceFlinger, BufferQueue, AudioFlinger, mediaserver] --> HALLayer
    HALLayer[4. HAL / Kernel Layer: HWC HAL, Camera HAL3, Codec2 HAL, DRM TEE, ALSA/dmabuf]
```

- **App API**: `Canvas`/`Compose` 그리기, `Camera2`/`CameraX` 요청, `MediaCodec`/`Media3` 호출처럼 앱 프로세스가 직접 부르는 인터페이스.
- **Framework Service**: RenderThread 스케줄, `Choreographer`, `CameraService`, `AudioService`처럼 system_server 또는 앱 프로세스 내에서 파이프라인을 조율하는 계층.
- **Native Service**: `SurfaceFlinger`, `HWC` 서비스, `AudioFlinger`, `mediaserver`처럼 별도 Native C++ daemon 프로세스로 동작하며 Binder IPC로 통신하는 영역.
- **HAL/Kernel**: `HWC2 HAL`, `Camera HAL3`, `Codec2`, `Widevine DRM TEE`, `ALSA/dmabuf` 커널 드라이버 등 칩셋 벤더 하드웨어 자원에 직접 닿는 영역.

이 구분은 [Graphics and media contracts](graphics-media-contracts/graphics-media-contracts.md) index 문서에서 계약 단위로 세분화되어 기술된다.

### 관찰 신호 및 디버깅 접근법

시스템 정합성 이슈 및 성능 버벅임 발생 시 다음 덤프 명령어로 관찰 신호를 확보한다:
- `adb shell dumpsys SurfaceFlinger`: 레이어 Z-order 및 HWC hardware overlay 오프로드 상태
- `adb shell dumpsys gfxinfo <package>`: 프레임 렌더링 latency 및 Jank 비율
- `adb shell dumpsys media.camera`: 카메라 capture request 및 Output Surface 스트림 바인딩
- `adb shell dumpsys media.codec`: 인코더/디코더 하드웨어 세션 및 BufferQueue 대기 상태
- `adb shell dumpsys audio`: AudioFocus 스택 및 AudioTrack / MMAP 노드 현황
