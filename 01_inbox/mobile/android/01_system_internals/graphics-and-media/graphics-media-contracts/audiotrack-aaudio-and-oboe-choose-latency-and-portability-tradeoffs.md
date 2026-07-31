---
title: AudioTrack, AAudio, Oboe는 지연 시간과 이식성의 trade-off를 고른다
tags: [android, android/media, android/audio]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

AudioTrack은 앱이 PCM 데이터를 Android 오디오 출력 경로에 쓰는 Java/Kotlin API다. 일반 미디어 재생, 효과음, 커스텀 PCM 출력에서 사용할 수 있지만, `getMinBufferSize()`가 전체 지연 시간이나 최적 버퍼를 보장하지는 않는다.

AAudio는 API 26에서 도입된 NDK 오디오 API로, 낮은 지연이 중요한 native audio 앱을 위한 stream 기반 API다. 성능 모드와 sharing mode를 요청할 수 있지만 실제 경로는 기기, route, sample rate, mixer, exclusive mode 허용 여부가 결정한다.

Oboe는 C++ wrapper로 AAudio가 가능한 기기에서는 AAudio를 사용하고, 구형 기기에서는 다른 경로로 fallback할 수 있게 돕는다. 게임이나 실시간 오디오처럼 저지연 요구가 강한 경우 Oboe를 먼저 검토할 수 있다.

고정된 숫자로 “AAudio는 10ms, AudioTrack은 45ms”처럼 문서화하면 위험하다. 지연 시간은 output latency, round-trip latency, callback buffer, device route, thermal/scheduler 상태를 분리해 측정해야 한다.

관련 노트: [AudioFocus는 재생 권한이 아니라 공유 출력 정책이다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/audiofocus-is-shared-output-policy-not-playback-permission.md), [그래픽과 미디어 디버깅은 timeline과 component state에서 시작한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/graphics-media-debugging-starts-from-timeline-and-component-state.md)

근거: [AAudio](https://developer.android.com/ndk/guides/audio/aaudio/aaudio), [Low latency audio with Oboe](https://developer.android.com/games/sdk/oboe/low-latency-audio)
