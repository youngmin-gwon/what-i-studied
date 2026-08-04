---
title: 15-looper-handler
tags: ["android", "android/glossary"]
aliases: ["Handler", "Looper", "MessageQueue"]
date modified: 2026-08-03 17:21:35 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Looper 와 Handler 는 스레드의 메시지 큐를 관리하고 이벤트를 순차적으로 처리한다

정의: Looper 는 thread 의 MessageQueue 를 돌리고, Handler 는 그 queue 에 work 를 post 하거나 message 를 dispatch 하는 Android thread scheduling primitive 다.

혼동 방지: Looper/Handler 는 coroutine 자체가 아니다. UI thread responsiveness, delayed work, callback dispatch 를 이해하는 하위 primitive 이며, 긴 작업을 main thread 에 남겨도 되는 허가가 아니다.

정본 링크:

- [Main thread responsiveness](../../../06_testing_performance/performance/performance-contracts/main-thread-work-controls-responsiveness.md)
- [Coroutine is not thread](../../../02_app_framework/data/async-flow/coroutines/coroutine-is-lightweight-cancellable-work-not-thread.md)
