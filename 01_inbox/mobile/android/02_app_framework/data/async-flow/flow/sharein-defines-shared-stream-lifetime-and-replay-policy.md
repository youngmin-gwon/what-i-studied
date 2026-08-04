---
title: sharein-defines-shared-stream-lifetime-and-replay-policy
tags: [android, android/async, android/data, android/flow]
aliases: ["shareIn은 shared stream의 수명과 replay 정책을 정의한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## shareIn 은 shared stream 의 수명과 replay 정책을 정의한다

`shareIn` 은 cold Flow 를 hot `SharedFlow` 로 바꾸고, upstream 을 어떤 scope 에서 언제 시작/중지할지와 늦게 구독한 collector 에게 몇 개의 값을 replay 할지 정한다.

핵심 파라미터는 `scope`, `SharingStarted`, `replay` 다. `scope` 는 sharing coroutine 의 lifetime 을 정하고, `SharingStarted` 는 subscriber 유무에 따른 시작 정책을 정하며, `replay` 는 새 subscriber 가 받을 이전 emission 수를 정한다.

현재값 하나가 항상 필요한 화면 상태라면 [stateIn contract](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/statein-requires-explicit-lifetime-and-sharing-policy.md) 가 더 직접적이다. 여러 collector 에게 event stream 이나 shared upstream 을 나눠야 한다면 `shareIn` 의 replay/lifetime 정책을 명시한다.

```kotlin
val sharedNotifications: SharedFlow<Notification> =
    notificationSource
        .shareIn(
            scope = applicationScope,
            started = SharingStarted.WhileSubscribed(5_000),
            replay = 1,
        )
```

`replay = 1` 이면 새로 구독한 collector 는 upstream 이 가장 최근에 emit 한 값 1개를 즉시 받은 뒤 이후 값을 이어서 받는다. `replay = 0` 으로 두면 구독 시점 이전에 나온 값은 받지 못하고, 구독 이후 새 emission 만 받는다. 이 replay buffer 크기를 upstream 이 emit 하는 빈도보다 작게 잡으면 느린 collector 는 일부 중간 값을 건너뛴 채 최신 값만 받게 된다.

공식 문서: [shareIn](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/share-in.html)
