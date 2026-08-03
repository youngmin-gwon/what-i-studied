---
title: "RenderThread는 렌더 작업을 나누지만 UI 스레드 비용을 없애지 않는다"
tags: [android, android/graphics, android/performance]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

# RenderThread는 렌더 작업을 나누지만 UI 스레드 비용을 없애지 않는다

RenderThread는 Android 하드웨어 가속 렌더링에서 UI 스레드와 분리되어 렌더링 작업 일부를 수행하는 스레드다. UI 스레드는 입력 처리, 애니메이션 상태 갱신, measure/layout, display list 기록 같은 작업을 계속 담당한다.

RenderThread가 있다는 말은 “그리기는 모두 백그라운드에서 처리된다”는 뜻이 아니다. UI 스레드가 늦게 display list를 만들거나 레이아웃을 오래 잡으면 RenderThread가 충분히 빨라도 프레임 deadline을 놓친다.

반대로 UI 스레드가 빠르게 끝나도 GPU 제출, buffer swap, SurfaceFlinger 합성, HWC 결정에서 막히면 사용자는 jank를 본다. 따라서 렌더링 분석은 UI thread와 RenderThread를 분리해서 보되, 둘 중 하나만 원인이라고 단정하지 않는다.

실무에서는 Perfetto나 Android Studio Profiler에서 `Choreographer#doFrame`, View/Compose 작업, RenderThread, GPU completion, SurfaceFlinger 구간을 함께 본다.

관련 노트: [VSync와 Choreographer는 frame deadline을 정의한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/vsync-and-choreographer-define-frame-deadline.md), [그래픽과 미디어 디버깅은 timeline과 component state에서 시작한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/graphics-media-debugging-starts-from-timeline-and-component-state.md)
