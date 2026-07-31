---
title: produceState converts external state to Compose State
tags: [android, jetpack-compose, compose/state]
aliases: [produceState]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

# produceState converts external state to Compose State

`produceState`는 외부 비동기 source나 구독 기반 source를 Compose `State<T>`로 변환하는 adapter다. Composition에 들어오면 producer coroutine을 시작하고, key가 바뀌거나 call site가 사라지면 producer를 취소한다.

`value`에 같은 값을 다시 넣으면 downstream recomposition을 불필요하게 만들지 않도록 conflation된다. non-suspending callback source를 구독한다면 `awaitDispose`로 해제 경로를 함께 둔다.

Repository나 ViewModel을 대체하는 state holder가 아니다. 외부 source의 소유권과 business rule은 바깥 계층에 두고, `produceState`는 UI 수명에 맞춰 Compose State로 다리를 놓을 때만 사용한다.

관련 노트: [snapshotFlow는 Compose State를 cold Flow로 바꾼다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/snapshot-flow-converts-compose-state-to-cold-flow.md), [Compose 상태 API는 필요한 수명에 맞춰 선택한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-api-selection-by-lifetime.md)

출처: [Side-effects in Compose - produceState](https://developer.android.com/develop/ui/compose/side-effects#producestate)
