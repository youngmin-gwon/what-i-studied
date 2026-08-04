---
title: flow-contracts
tags: [android, android/async, android/data, android/flow]
aliases: ["Flow Contracts"]
date modified: 2026-08-03 18:07:28 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Flow 계약은 값을 방출하는 시점보다 수집과 실행 수명을 정의한다

Flow 정본은 비동기 stream 을 cold execution, operator cancellation, callback bridge, sharing policy 로 나눈다. 핵심은 "값을 몇 번 emit 하는가"보다 누가 collect 하고 어느 수명에서 upstream 이 실행되는가다.

### 정본 노트

- [Cold Flow는 collect될 때 실행된다](./cold-flow-runs-when-collected.md)
- [Flow operator는 stream 변환과 취소 규칙을 드러낸다](./flow-operators-transform-stream-with-declared-cancellation-and-combination.md)
- [callbackFlow는 awaitClose로 등록과 해제를 대칭으로 보장해야 한다](./callbackflow-requires-awaitclose-for-registration-cleanup.md)
- [shareIn은 shared stream의 수명과 replay 정책을 정의한다](./sharein-defines-shared-stream-lifetime-and-replay-policy.md)
- [Flow와 StateFlow 상태 계약](../flow-state-contracts/flow-state-contracts.md)

### 중복 방지 규칙

- one-off event 와 current state 구분은 Flow/StateFlow 상태 계약으로 둔다.
- UI collection 은 lifecycle-aware collection 정본으로 둔다.
- Room/DataStore 가 Flow 를 노출하는 이유는 persistence 정본으로 둔다.
