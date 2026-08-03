---
title: audiofocus-is-shared-output-policy-not-playback-permission
tags: [android, android/audio, android/media]
aliases: []
date modified: 2026-08-03 17:24:51 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## AudioFocus 는 재생 권한이 아니라 공유 출력 정책이다

AudioFocus 는 여러 앱이 같은 오디오 출력 환경을 공유할 때 사용자 경험을 조정하기 위한 협력 규칙이다. 앱은 `AudioAttributes` 와 focus gain 종류로 재생 의도를 설명하고, focus 변화 callback 에 따라 일시정지, ducking, resume, stop 을 결정한다.

AudioFocus 를 얻었다고 물리 출력 장치를 독점하는 것은 아니다. 시스템은 여러 오디오 stream 을 mix 할 수 있고, focus 는 어떤 앱이 우선적으로 들려야 하는지와 다른 앱이 어떻게 양보해야 하는지를 표현한다.

Android 12 이상에서는 일부 focus 전환에서 시스템이 fade out 이나 mute 를 강제할 수 있다. 이전 버전에서는 앱이 callback 을 더 직접적으로 처리해야 하므로 버전별 정책 차이를 문서에 분리해 둬야 한다.

ExoPlayer 를 사용할 때는 player 의 audio attributes 설정으로 focus 처리를 위임할 수 있는 경우가 있다. 직접 구현할 때도 loss, transient loss, ducking, noisy route change 를 같은 정책으로 뭉개지 않는다.

관련 노트: [Media3 ExoPlayer는 playback stack이지 저수준 codec API가 아니다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/media3-exoplayer-is-playback-stack-not-low-level-codec-api.md)

근거: [Manage audio focus](https://developer.android.com/media/optimize/audio-focus)
