---
title: apple-media-pipeline-deep
tags: [apple, apple/ui, apple/ui/media, audio, avfoundation, media, video]
aliases: ["AVFoundation 은 세션이 소유한 파이프라인이고 프레임은 복사하지 않고 참조로 흐른다", "AVFoundation", "미디어 파이프라인"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2025-12-16 16:09:09 +09:00
---

## AVFoundation 은 세션이 소유한 파이프라인이고 프레임은 복사하지 않고 참조로 흐른다

`AVFoundation` 은 개별 API 의 모음이 아니라 **`AVCaptureSession` / `AVAudioSession` / `AVPlayer` 가 각각 소유하는 파이프라인**이다. "왜 소리가 안 나지", "왜 화면이 검게 나오지"는 대부분 개별 호출이 아니라 세션의 구성 또는 상태 전이가 잘못된 결과다. 그리고 이 파이프라인 위를 흐르는 프레임은 **복사되지 않는다** — 4K 프레임 하나가 30MB 를 넘기 때문에, 하드웨어 버퍼의 참조(`CVPixelBuffer`)만 단계 사이를 이동한다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **Audio Session**: 내 앱에서 음악을 틀었는데, 사용자가 듣고 있던 팟캐스트가 끊겨야 할까요, 아니면 섞여야 할까요? (`AVAudioSession` Category)
- **Zero-copy**: 4K 영상의 프레임 하나는 30MB 가 넘습니다. 이걸 CPU 에서 복사하면 폰이 난로가 됩니다. 하드웨어 주소값만 넘기는 기술(`CVPixelBuffer`)을 이해해야 합니다.
- **Privacy (TCC)**: 카메라/마이크 권한을 언제, 어떻게 요청하느냐가 사용자 경험을 좌우합니다.

---

### 📷 Capture Pipeline

카메라에서 들어온 빛이 내 화면에 보이기까지의 과정입니다.

1. **AVCaptureDevice**: 물리적인 카메라(후면, 전면, 와이드)입니다.
2. **AVCaptureSession**: 파이프라인의 **중앙 제어 장치**입니다. 입력을 받아서 출력으로 내보냅니다.
3. **Inputs**: `AVCaptureDeviceInput` (카메라, 마이크).
4. **Outputs**:
   - `AVCapturePhotoOutput`: 고화질 사진 (셔터 랙 처리).
   - `AVCaptureVideoDataOutput`: 실시간 프레임(`CMSampleBuffer`). 필터링이나 머신러닝 분석에 씁니다.

```swift
// 세션 설정 (Heavy Operation, 백그라운드 스레드 권장)
session.beginConfiguration()
session.sessionPreset = .high
if session.canAddInput(input) { session.addInput(input) }
if session.canAddOutput(output) { session.addOutput(output) }
session.commitConfiguration()
session.startRunning() // Blocking Call, Main Thread에서 절대 호출 금지!
```

---

### 🎵 Audio Session Management

가장 많이 실수하는 부분입니다.

앱이 실행될 때 오디오 시스템(하드웨어)에게 "나 이런 소리 낼 거야"라고 신고해야 합니다.

- **Playback**: 음악 앱. 무음 모드 무시하고 소리 냄. 백그라운드 재생 가능.
- **Ambient**: 게임 효과음. 무음 모드면 소리 안 남. 다른 음악과 섞임.
- **PlayAndRecord**: 통화/녹음. 에코 캔슬레이션 활성화.

---

### 🎬 Playback (AVPlayer)

`AVPlayer` 는 단순해 보이지만 상태 머신(State Machine)입니다.

- **KVO (Key-Value Observing)**: `status` 프로퍼티를 감시해야 합니다.
  - `.unknown` -> `.readyToPlay`: 이제 재생 가능.
  - `.failed`: 네트워크 끊김이나 코덱 미지원.
- **HLS (HTTP Live Streaming)**: 네트워크 상태에 따라 1080p -> 720p -> 480p 로 자동으로 갈아탑니다(Adaptive Bitrate).

---

### 🔗 Zero-copy 데이터 흐름

동영상 처리의 핵심은 **"복사하지 않는 것"** 이다.

- **CVPixelBuffer**: 이미지 데이터를 담는 컨테이너. 실제 픽셀은 GPU 가 접근 가능한 메모리에 있고, 앱은 참조만 들고 다닌다.
- **Zero-copy Flow**: 카메라 → Metal(필터/렌더) → 인코더까지 데이터 복사 없이 메모리 주소만 넘긴다.
- **CPU 복사가 끼어드는 순간**: `CGImage` 변환, `UIImage` 생성, `CMSampleBuffer` 를 `Data` 로 직렬화. 여기서 발열과 프레임 드랍이 시작되므로 실시간 경로에서는 피한다.

---

### 더 보기

- [apple-rendering-and-media](apple-rendering-and-media.md) - Core Animation/Metal 렌더링 파이프라인
- [apple-privacy-and-tcc-details](../04_system_services/apple-privacy-and-tcc-details.md) - 카메라/마이크 권한 상세
