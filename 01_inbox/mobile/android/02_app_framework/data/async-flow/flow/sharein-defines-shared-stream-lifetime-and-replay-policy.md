---
title: sharein-defines-shared-stream-lifetime-and-replay-policy
tags: [android, android/async, android/data, android/flow]
aliases: ["shareIn은 shared stream의 수명과 replay 정책을 정의한다"]
date modified: 2026-08-03 18:07:30 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## shareIn 은 shared stream 의 수명과 replay 정책을 정의한다

`shareIn` 은 cold Flow 를 hot `SharedFlow` 로 바꾸고, upstream 을 어떤 scope 에서 언제 시작/중지할지와 늦게 구독한 collector 에게 몇 개의 값을 replay 할지 정한다.

핵심 파라미터는 `scope`, `SharingStarted`, `replay` 다. `scope` 는 sharing coroutine 의 lifetime 을 정하고, `SharingStarted` 는 subscriber 유무에 따른 시작 정책을 정하며, `replay` 는 새 subscriber 가 받을 이전 emission 수를 정한다.

현재값 하나가 항상 필요한 화면 상태라면 [stateIn contract](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/statein-requires-explicit-lifetime-and-sharing-policy.md) 가 더 직접적이다. 여러 collector 에게 event stream 이나 shared upstream 을 나눠야 한다면 `shareIn` 의 replay/lifetime 정책을 명시한다.

공식 문서: [shareIn](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/share-in.html)
