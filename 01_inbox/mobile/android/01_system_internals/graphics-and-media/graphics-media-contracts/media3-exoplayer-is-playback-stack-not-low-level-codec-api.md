---
title: Media3 ExoPlayer는 playback stack이지 저수준 codec API가 아니다
tags: [android, android/media, android/media3]
aliases: [ExoPlayer, Media3]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

# Media3 ExoPlayer는 playback stack이지 저수준 codec API가 아니다

Media3는 Android 미디어 앱을 위한 Jetpack 라이브러리 모음이고, ExoPlayer는 Media3의 기본 `Player` 구현이다. 앱은 `MediaItem`, player, session, UI, audio attributes, output surface 같은 상위 개념으로 재생을 구성한다.

ExoPlayer는 데이터를 읽고, buffering하고, track을 선택하고, decoder와 renderer를 연결하는 playback stack이다. 반면 MediaCodec은 codec buffer와 Surface 입출력을 직접 다루는 저수준 API다.

DASH/HLS 같은 adaptive streaming은 “네트워크가 빠르면 곧바로 고화질”이라는 단순 규칙이 아니다. bandwidth estimate, buffer health, track selection policy, renderer 상태, rebuffering 위험을 함께 고려한다.

새 코드와 문서에서는 standalone `com.google.android.exoplayer2`보다 `androidx.media3` API를 기준으로 적는다. 오래된 ExoPlayer 문서나 예제는 Media3 migration 여부를 확인해야 한다.

관련 노트: [AudioFocus는 재생 권한이 아니라 공유 출력 정책이다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/audiofocus-is-shared-output-policy-not-playback-permission.md), [DRM 보호 미디어는 secure codec과 보호된 출력 경로를 요구할 수 있다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/drm-protected-media-needs-secure-codec-and-output-path.md)

근거: [Create a basic media player app using Media3 ExoPlayer](https://developer.android.com/media/implement/playback-app), [Media3 migration guide](https://developer.android.com/media/media3/exoplayer/migration-guide)
