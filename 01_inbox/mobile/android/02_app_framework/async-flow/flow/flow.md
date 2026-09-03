---
title: flow
tags: [android, android/async, android/concurrency, android/flow]
aliases: ["Flow Contracts"]
date modified: 2026-08-07 18:59:19 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Flow 계약은 반응형 비동기 스트림과 컨텍스트 보존을 다룬다

Kotlin `Flow` 정본은 연속적인 데이터 스트림(Data Stream)을 비동기적으로 처리하기 위한 표준 계약 체계다. RxJava 나 LiveData 가 지니던 스레드 컨텍스트 누수와 백프레셔(Backpressure) 복잡도를 해결하고, **Cold Stream 메커니즘**, **선언적 연산자 파이프라인**, **콜백 - 스트림 변환 자원 정리**, **Hot Stream 공유(shareIn)** 계약을 규정한다.

### 정본 노트

- [Cold Flow는 collect될 때 비로소 실행된다](cold-flow-execution.md) - 수집 시점마다 실행되는 온디맨드(On-demand) 데이터 공급 계약과 SafeCollector 컨텍스트 보존.
- [Flow 연산자는 선언적 취소와 조합을 유지하며 스트림을 변환한다](flow-stream-operators.md) - intermediate operator 체이닝과 flowOn 을 통한 안전한 스레드 분리.
- [callbackFlow는 리스너 등록과 해제 자원 정리를 위해 awaitClose를 필수 요구한다](callback-flow-cleanup.md) - Android 콜백 기반 API 를 Coroutine Flow 로 변환할 때의 메모리 누수 방지.
- [shareIn은 공유 스트림 수명과 replay 정책을 정의한다](flow-sharein-policy.md) - 단일 업스트림 실행을 복수 Downstream 수집자에게 브로드캐스트하는 Hot Stream 전환.

### 연결된 상태 계약

- 화면 상태 유도 및 [viewmodel](../../architecture/state-management/viewmodel.md) 연동: [Flow](../flow-state/flow-state.md) 와 [stateflow](../flow-state/stateflow-and-sharedflow.md) 상태 계약 노트 참조.
