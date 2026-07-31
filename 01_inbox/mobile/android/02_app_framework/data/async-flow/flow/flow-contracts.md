---
title: "Flow Contracts"
tags: [android, android/data, android/async, android/flow]
aliases: ["Flow Contracts"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Flow Contracts

Flow 정본은 비동기 stream을 cold execution, operator cancellation, callback bridge, sharing policy로 나눈다. 핵심은 “값을 몇 번 emit하는가”보다 누가 collect하고 어느 수명에서 upstream이 실행되는가다.

## 정본 노트

- [Cold Flow는 collect될 때 실행된다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow/cold-flow-runs-when-collected.md)
- [Flow operator는 stream 변환과 취소 규칙을 드러낸다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow/flow-operators-transform-stream-with-declared-cancellation-and-combination.md)
- [callbackFlow는 awaitClose로 등록과 해제를 대칭으로 보장해야 한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow/callbackflow-requires-awaitclose-for-registration-cleanup.md)
- [shareIn은 shared stream의 수명과 replay 정책을 정의한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow/sharein-defines-shared-stream-lifetime-and-replay-policy.md)
- [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)

## 중복 방지 규칙

- one-off event와 current state 구분은 Flow/StateFlow 상태 계약으로 둔다.
- UI collection은 lifecycle-aware collection 정본으로 둔다.
- Room/DataStore가 Flow를 노출하는 이유는 persistence 정본으로 둔다.
