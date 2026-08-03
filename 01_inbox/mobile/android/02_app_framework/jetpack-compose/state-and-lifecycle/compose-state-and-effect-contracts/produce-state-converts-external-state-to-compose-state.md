---
title: produceState는 외부 상태를 Compose 상태로 변환한다
tags: [android, compose/state, jetpack-compose]
aliases: [produceState]
date modified: 2026-08-03 16:37:39 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

# produceState는 외부 상태를 Compose 상태로 변환한다

`produceState` 는 외부 비동기 source 나 구독 기반 source 를 Compose `State<T>` 로 변환하는 adapter 다. Composition 에 들어오면 producer coroutine 을 시작하고, key 가 바뀌거나 call site 가 사라지면 producer 를 취소한다.

`value` 에 같은 값을 다시 넣으면 downstream recomposition 을 불필요하게 만들지 않도록 conflation 된다. non-suspending callback source 를 구독한다면 `awaitDispose` 로 해제 경로를 함께 둔다.

Repository 나 ViewModel 을 대체하는 state holder 가 아니다. 외부 source 의 소유권과 business rule 은 바깥 계층에 두고, `produceState` 는 UI 수명에 맞춰 Compose State 로 다리를 놓을 때만 사용한다.

관련 노트: [snapshotFlow는 Compose State를 cold Flow로 바꾼다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/snapshot-flow-converts-compose-state-to-cold-flow.md), [Compose 상태 API는 필요한 수명에 맞춰 선택한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-api-selection-by-lifetime.md)

출처: [Side-effects in Compose - produceState](https://developer.android.com/develop/ui/compose/side-effects#producestate)
