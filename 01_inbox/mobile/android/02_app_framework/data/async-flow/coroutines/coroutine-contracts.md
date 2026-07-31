---
title: "Coroutine Contracts"
tags: [android, android/data, android/async, android/coroutines]
aliases: ["Coroutine Contracts"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Coroutine Contracts

Coroutine 정본은 Android 비동기 작업을 thread 생성 문제가 아니라 lifetime, cancellation, dispatcher, failure propagation의 계약으로 나눈다.

## 정본 노트

- [Coroutine은 thread가 아니라 취소 가능한 경량 작업이다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/coroutine-is-lightweight-cancellable-work-not-thread.md)
- [suspend 함수는 thread가 아니라 coroutine을 멈춘다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/suspend-function-suspends-coroutine-without-blocking-thread.md)
- [Structured concurrency는 부모 scope가 자식 작업의 수명을 소유하게 한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/structured-concurrency-parent-owns-child-lifetime.md)
- [Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/dispatcher-selects-execution-context-not-work-lifetime.md)
- [Coroutine 예외 전파는 builder와 supervision boundary가 결정한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/exception-propagation-needs-supervision-boundary.md)
- [병렬 Coroutine은 부모 scope와 실패 정책을 먼저 정해야 한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/parallel-coroutines-need-explicit-parent-and-failure-policy.md)

## 중복 방지 규칙

- 데이터 stream 모델은 [Flow Contracts](01_inbox/mobile/android/02_app_framework/data/async-flow/flow/flow-contracts.md)로 둔다.
- 화면 상태 조합은 [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)로 둔다.
- 화면 수명 소유자는 [Android ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md)과 lifecycle-aware collection 정본으로 연결한다.
