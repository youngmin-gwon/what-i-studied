---
title: VSync와 Choreographer는 frame deadline을 정의한다
tags: [android, android/graphics, android/performance]
aliases: [VSync, Choreographer]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

VSync는 display refresh와 맞물린 타이밍 신호이고, Choreographer는 앱의 입력, 애니메이션, drawing 작업을 다음 display frame에 맞춰 스케줄링하는 Android framework API다.

앱은 보통 Choreographer를 직접 다루지 않고 View, animation, Compose 같은 상위 API를 통해 간접적으로 사용한다. 직접 프레임 callback을 쓰는 경우는 custom rendering, game loop, GL/Vulkan 렌더링처럼 상위 UI toolkit을 우회하는 경우가 많다.

60Hz에서는 한 프레임 예산이 약 16.67ms이고, 90Hz는 약 11ms, 120Hz는 약 8ms로 줄어든다. 이 숫자는 앱 코드만의 시간이 아니라 다음 present까지 이어지는 전체 frame pipeline의 deadline으로 이해해야 한다.

deadline을 조금 넘긴 프레임은 “조금 늦게 표시”되는 것이 아니라 다음 display opportunity로 밀릴 수 있다. 사용자는 이것을 stutter나 jank로 느낀다.

관련 노트: [Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)

근거: [Choreographer API reference](https://developer.android.com/reference/android/view/Choreographer), [Slow rendering](https://developer.android.com/topic/performance/vitals/render)
