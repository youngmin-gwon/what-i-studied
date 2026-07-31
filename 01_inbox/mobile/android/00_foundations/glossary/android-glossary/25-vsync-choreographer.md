---
title: "Vsync와 Choreographer"
tags: ["android", "android/glossary"]
aliases: ["Vsync", "Choreographer"]
---

# Vsync와 Choreographer

정의: Vsync는 display refresh timing signal이고, Choreographer는 Android UI work를 frame deadline에 맞춰 scheduling하는 framework component다.

혼동 방지: Frame drop은 draw 함수 하나만의 문제가 아니다. input, animation, layout, draw, RenderThread, GPU, SurfaceFlinger까지 frame budget을 공유한다.

정본 링크:
- [Vsync and Choreographer](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/vsync-and-choreographer-define-frame-deadline.md)
- [Jank frame deadline](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
