---
title: coroutine
tags: [android, android/async, android/coroutines, android/data]
aliases: ["Coroutine Contracts"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Coroutine 계약은 스레드 생성보다 수명과 취소 실패 전파를 다룬다

Kotlin Coroutine 정본은 Android 앱 내부의 비동기 작업을 단순한 OS Thread 생성/전환 기술이 아닌, **수명 관리(Lifetime Management)**, **협조적 취소(Cooperative Cancellation)**, **실행 맥락 분리(Execution Context Dispatching)**, **예외 전파 격리(Exception Supervision Boundary)**라는 4대 아키텍처 계약으로 정의한다.

### 정본 노트

- [Coroutine은 thread가 아니라 취소 가능한 경량 작업이다](./coroutine-is-lightweight-cancellable-work-not-thread.md) - OS 스레드 생성을 대체하는 유저스페이스 힙 객체와 협조적 취소 메커니즘.
- [suspend 함수는 thread가 아니라 coroutine을 멈춘다](./suspend-function-suspends-coroutine-without-blocking-thread.md) - CPS(Continuation-Passing Style) 변환 및 상태 머신(State Machine)에 의한 비차단 중단.
- [Structured concurrency는 부모 scope가 자식 작업의 수명을 소유하게 한다](./structured-concurrency-parent-owns-child-lifetime.md) - Job 트리 구조와 계층적 수명 관리 및 자원 누수 방지.
- [Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다](./dispatcher-selects-execution-context-not-work-lifetime.md) - ContinuationInterceptor를 통한 스레드 풀 분리와 Scope 소유권의 완전한 직교성.
- [Coroutine 예외 전파는 builder와 supervision boundary가 결정한다](./exception-propagation-needs-supervision-boundary.md) - childCancelled() 전달 메커니즘과 SupervisorJob을 통한 동형 형제 작업의 실패 격리.
- [병렬 Coroutine은 부모 scope와 실패 정책을 먼저 정해야 한다](./parallel-coroutines-need-explicit-parent-and-failure-policy.md) - coroutineScope와 supervisorScope를 활용한 고성능 동시성 조율.

### 아키텍처 분리 원칙

- **단일 비동기 작업 및 실행 트랜잭션**: 본 정본 클러스터에서 다룬다.
- **연속적 데이터 스트림 처리**: [Flow Contracts](../flow/flow.md) 정본으로 연결한다.
- **UI 화면 상태 유도 및 [viewmodel](../../../viewmodel.md) 연동**: [Flow와 [stateflow](../../../stateflow-and-sharedflow.md) 상태 계약](../flow-state/flow-state.md) 정본으로 연결한다.
- **안드로이드 구성요소 수명주기 결합**: [Android ViewModel](../../../architecture/state-management/viewmodel/viewmodel.md) 및 `lifecycleScope` 계약을 준수한다.
