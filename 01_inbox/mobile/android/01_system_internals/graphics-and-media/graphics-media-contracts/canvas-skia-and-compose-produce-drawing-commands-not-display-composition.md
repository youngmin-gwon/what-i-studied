---
title: "Canvas, Skia, Compose는 합성기가 아니라 그리기 명령의 생산자다"
tags: [android, android/graphics, android/compose]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

# Canvas, Skia, Compose는 합성기가 아니라 그리기 명령의 생산자다

Canvas와 Skia는 앱이 한 레이어의 내용을 그리는 쪽에 가깝다. Custom View의 `onDraw(canvas)`나 Compose의 drawing 단계는 현재 윈도우나 레이어가 제출할 그래픽 내용을 만든다.

이 단계는 최종 화면 전체를 합성하는 단계와 다르다. 상태바, 내비게이션 바, 앱 윈도우, 동영상 Surface 같은 여러 레이어를 어떤 순서와 방식으로 합칠지는 SurfaceFlinger와 HWC 쪽의 책임이다.

Compose도 이 경계를 넘지 않는다. Compose Runtime은 composition, layout, draw를 통해 UI 내용을 계산하고 그리기 명령을 만들지만, 디스플레이 레이어 합성 정책 자체를 대체하지 않는다.

그래서 Compose 성능 문제와 SurfaceFlinger 합성 문제는 같은 “렌더링”이라는 이름 아래 있어도 관찰 지점이 다르다. Compose에서는 recomposition/layout/draw 비용을 보고, 시스템 그래픽에서는 buffer queue, frame deadline, composition path를 본다.

관련 노트: [Compose performance contracts](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md), [Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
