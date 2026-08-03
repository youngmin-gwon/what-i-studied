---
title: "그래픽과 미디어 디버깅은 timeline과 component state에서 시작한다"
tags: [android, android/debugging, android/graphics, android/media]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

# 그래픽과 미디어 디버깅은 timeline과 component state에서 시작한다

그래픽과 미디어 문제는 단일 로그보다 시간축과 component state를 같이 봐야 한다. 앱 thread, RenderThread, binder, sched, SurfaceFlinger, codec, audio mixer가 서로 다른 지점에서 대기할 수 있기 때문이다.

렌더링 문제는 Android Studio jank detection, Perfetto FrameTimeline, `adb shell dumpsys gfxinfo <package>`, `adb shell dumpsys SurfaceFlinger`로 시작한다. 목표는 “어느 frame이 deadline을 놓쳤는가”와 “그 frame에서 가장 긴 구간이 어디인가”를 찾는 것이다.

미디어 문제는 `adb shell dumpsys media.codec`, `adb shell dumpsys media.audio_flinger`, player event log, dropped frame, rebuffering, audio underrun, codec format change를 같이 본다. `dumpsys` 필드와 Perfetto data source 이름은 Android 버전과 vendor에 따라 달라질 수 있다.

문제 원인을 “GPU 문제”, “코덱 문제”, “zero-copy 문제”로 바로 단정하지 않는다. 먼저 재현 조건, device, refresh rate, codec, resolution, route, thermal state, foreground/background 상태를 고정하고 trace를 수집한다.

관련 노트: [Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md), [AudioTrack, AAudio, Oboe는 지연 시간과 이식성의 trade-off를 고른다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/audiotrack-aaudio-and-oboe-choose-latency-and-portability-tradeoffs.md)
