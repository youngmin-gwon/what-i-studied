---
title: snapshotFlow converts Compose State to a cold Flow
tags: [android, jetpack-compose, compose/state]
aliases: [snapshotFlow]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

# snapshotFlow converts Compose State to a cold Flow

`snapshotFlow`는 block 안에서 읽은 Compose `State`를 관찰해 cold `Flow`로 바꾸는 adapter다. Flow가 collect될 때 block이 실행되고, 읽은 state가 바뀌어 새 결과가 이전 결과와 다르면 값을 emit한다.

이 API는 `derivedStateOf`와 방향이 다르다. `derivedStateOf`는 Compose 안에서 `State` 결과를 만들고, `snapshotFlow`는 Compose State read를 Flow pipeline으로 내보내 analytics, debounce, filter 같은 Flow operator와 연결한다.

`snapshotFlow` block 안에서는 Compose state read만 안정적으로 수행하고 side effect는 Flow collector 쪽에서 처리한다. mapped 결과의 의미가 달라졌을 때만 downstream으로 보내고 싶다면 Flow operator를 추가한다.

관련 노트: [produceState는 외부 상태를 Compose State로 바꾼다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/produce-state-converts-external-state-to-compose-state.md), [derivedStateOf는 고빈도 입력에서 저빈도 결과를 만들 때 쓴다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/derivedstateof-is-for-high-frequency-derived-values.md)

출처: [Side-effects in Compose - snapshotFlow](https://developer.android.com/develop/ui/compose/side-effects#snapshotflow)
