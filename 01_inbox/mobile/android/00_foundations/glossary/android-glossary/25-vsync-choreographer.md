---
title: 25-vsync-choreographer
tags: ["android", "android/glossary"]
aliases: ["Choreographer", "Vsync"]
date modified: 2026-08-03 17:21:02 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Vsync 와 Choreographer 는 디스플레이 주사율에 맞춰 UI 렌더링 프레임을 동기화한다

정의: Vsync 는 display refresh timing signal 이고, Choreographer 는 Android UI work 를 frame deadline 에 맞춰 scheduling 하는 framework component 다.

혼동 방지: Frame drop 은 draw 함수 하나만의 문제가 아니다. input, animation, layout, draw, RenderThread, GPU, SurfaceFlinger 까지 frame budget 을 공유한다.

정본 링크:

- [Vsync and Choreographer](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/vsync-and-choreographer-define-frame-deadline.md)
- [Jank frame deadline](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
