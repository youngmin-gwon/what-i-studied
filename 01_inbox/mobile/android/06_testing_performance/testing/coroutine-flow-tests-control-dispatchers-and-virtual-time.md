---
title: coroutine-flow-tests-control-dispatchers-and-virtual-time
tags: ["android", "android/testing-performance"]
aliases: []
date modified: 2026-08-03 18:15:02 +09:00
date created: 2026-07-31 23:24:22 +09:00
---

## Coroutine 과 Flow 테스트는 dispatcher 와 virtual time 을 통제해야 한다

Coroutine/Flow 테스트는 실제 background thread 와 실제 delay 에 의존하면 flaky 해진다. `runTest` 는 test scope 와 scheduler 를 제공하고, `TestDispatcher` 는 새 coroutine 실행 순서와 virtual time 을 통제하게 한다.

Code under test 가 dispatcher 를 직접 고정하면 테스트가 제어할 수 없다. dispatcher 나 scope 를 DI 로 주입하고, 테스트에서는 `StandardTestDispatcher`, `UnconfinedTestDispatcher`, `Dispatchers.Main` replacement 를 상황에 맞게 사용한다.

여러 `TestDispatcher` 를 만들더라도 같은 `TestCoroutineScheduler` 를 공유해야 시간 인식이 어긋나지 않는다. `advanceUntilIdle` 같은 virtual-time 제어는 pending coroutine 과 Flow emission assertion 을 결정적으로 만든다.

공식 문서: [Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test)

### 판단 기준

Testing/performance 노트는 빠른 피드백, release gate, 진단 trace, 반복 가능한 benchmark 를 분리해 선택하는 기준으로 읽는다.

### 경계

단일 측정값보다 재현 조건, device state, test layer, failure cost 를 함께 고정한다.
