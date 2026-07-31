---
title: "Looper와 Handler"
tags: ["android", "android/glossary"]
aliases: ["Looper", "Handler", "MessageQueue"]
---

# Looper와 Handler

정의: Looper는 thread의 MessageQueue를 돌리고, Handler는 그 queue에 work를 post하거나 message를 dispatch하는 Android thread scheduling primitive다.

혼동 방지: Looper/Handler는 coroutine 자체가 아니다. UI thread responsiveness, delayed work, callback dispatch를 이해하는 하위 primitive이며, 긴 작업을 main thread에 남겨도 되는 허가가 아니다.

정본 링크:
- [Main thread responsiveness](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/main-thread-work-controls-responsiveness.md)
- [Coroutine is not thread](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/coroutine-is-lightweight-cancellable-work-not-thread.md)
