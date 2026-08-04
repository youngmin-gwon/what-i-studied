---
title: audiomanager-arbitrates-concurrent-playback-through-focus-requests
tags: ["android", "android/system-services"]
aliases: ["AudioManager는 포커스 요청으로 여러 앱의 동시 재생을 조정한다"]
date modified: 2026-08-04 15:30:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## AudioManager는 포커스 요청으로 여러 앱의 동시 재생을 조정한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [미디어/오디오/카메라 시스템 서비스 접근 계약](./media-audio-camera-contracts.md)

### 핵심 정의

여러 앱이 동시에 소리를 재생하려 할 때, Android는 오디오 하드웨어를 직접 잠그는 대신 "오디오 포커스"라는 협력적 신호 체계로 조정한다. 앱은 재생 전 `AudioManager`(또는 `AudioFocusRequest`)로 포커스를 요청하고, 시스템은 다른 포커스 보유자에게 콜백으로 통지한 뒤 요청자에게 포커스를 부여할지 결정한다.

### 메커니즘

포커스 요청 타입은 상황에 따라 다르다. `AUDIOFOCUS_GAIN`은 배타적 재생(음악 앱), `AUDIOFOCUS_GAIN_TRANSIENT`는 짧은 알림음처럼 일시적 재생, `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`는 내비게이션 안내처럼 다른 앱 소리를 줄이기만 하면 되는 경우에 사용한다. 시스템은 포커스를 새 요청자에게 넘기면서 이전 보유자의 `OnAudioFocusChangeListener`에 `AUDIOFOCUS_LOSS`(영구 상실) 또는 `AUDIOFOCUS_LOSS_TRANSIENT`(일시 상실)를 통지한다.

이 체계는 강제가 아니라 협력적 규약이다. 앱이 포커스를 잃고도 콜백을 무시하고 계속 재생하면 시스템이 강제로 소리를 끄지는 않지만, 다른 앱과 소리가 겹치는 나쁜 사용자 경험이 발생한다.

### 판단 기준

- 배경음악처럼 다른 소리와 공존해도 되는 경우가 아니라면 포커스 상실 콜백에서 반드시 일시정지하거나 음량을 낮춘다.
- 짧은 효과음(알림, 버튼 클릭)은 `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`를 사용해 배경 재생 앱이 완전히 멈추지 않고 볼륨만 낮추도록 한다.
- 미디어 재생 앱은 `MediaSession`과 포커스 요청을 함께 관리하는 것이 좋다. `MediaSession`이 재생 상태를 시스템에 노출하는 표준 경로이기 때문이다.

### 경계

- 이 노트는 여러 앱 간 재생 조정 계약을 다룬다. 재생 상태를 잠금화면/외부 기기에 노출하는 것은 [MediaSession은 재생 상태를 시스템 UI와 외부 컨트롤러에 노출하는 계약이다](./mediasession-exposes-playback-state-to-system-and-external-controllers.md)가 다룬다.
- 실제 오디오 디코딩, 믹싱, 저지연 경로 구현은 `01_system_internals/graphics-and-media`가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys audio`에서 현재 포커스 스택(어떤 패키지가 포커스를 보유 중인지)과 최근 포커스 변화 이력을 확인할 수 있다.

### 공식 문서

- https://developer.android.com/media/optimize/audio-focus
- https://developer.android.com/reference/android/media/AudioFocusRequest
