---
title: android-coroutines-flow
tags: [android, android/async, android/data]
aliases: ["Android [Coroutines](coroutines/kotlin-coroutines.md) and Flow"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Coroutine 과 Flow 는 비동기 작업의 수명과 stream sharing 을 분리한다

Android 비동기 프로그래밍 패러다임은 **[Kotlin Coroutines](coroutines/kotlin-coroutines.md)**와 **Flow**를 핵심 아키텍처 표준으로 삼는다. 이전의 `Thread`, `Handler`, `AsyncTask`, `RxJava`, `LiveData` 조합이 지니던 리소스 누수, 스레드 차단(Blocking), 복잡한 상태 관리 문제를 해결하고, **(1) 작업 수명 관리([structured concurrency](../../../../../computer-science/structured-concurrency.md))**, **(2) 실행 환경 분리(Dispatchers)**, **(3) 반응형 데이터 스트림(Cold Flow / Hot Stream)**을 완전하게 분리하여 제공한다.

### 정본 지도

- [Coroutine Contracts](coroutines/coroutine.md) - Coroutine Scope, suspend 함수 메커니즘, Dispatcher 선택, 예외 전파 및 병렬 작업 계약.
- [Flow Contracts](flow/flow.md) - Cold Flow 실행 메커니즘, 연산자 파이프라인, callbackFlow 소멸 처리, shareIn 공유 정책.
- [Flow와 [stateflow](flow-state/stateflow-and-sharedflow.md) 상태 계약](./flow-state/flow-state.md) - Repository stream 데이터 공급, ViewModel의 StateFlow 조합, UI Lifecycle-aware 수집 계약.
- [Coroutine/Flow 테스트 계약](../../../06_testing_performance/testing/coroutine-flow-testing.md) - TestDispatcher 와 Virtual Time 제어를 통한 결정론적 비동기 검증.

```mermaid
graph TD
    A["Data Layer (Repository/DataSource)"] -->|"Cold Flow (Data Stream)"| B["Domain / UseCase"]
    B -->|"Cold Flow / Suspend Result"| C"UI Layer ([viewmodel)"]
    C -->|"stateIn() / combine()"| D["StateFlow (UiState)"]
    D -->|"collectAsStateWithLifecycle()"| E["UI Layer (Compose / View)"]

    style A fill:#e1f5fe,stroke:#0288d1,color:#01579b
    style D fill:#fff3e0,stroke:#f57c00,color:#e65100
    style E fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
```

### 아키텍처 판단 및 읽는 기준

1. **작업의 수명과 취소 경계**: 작업이 언제 시작되어 언제 취소되어야 하는가? $\rightarrow$ [Structured Concurrency 계약](coroutines/structured-concurrency.md)과 `viewModelScope` / `lifecycleScope` 소유권을 확인한다.
2. **스레드 및 실행 위치**: CPU 연산인가, I/O 차단인가, UI 렌더링인가? $\rightarrow$ [Dispatcher 선택 계약](coroutines/coroutine-dispatchers.md)을 통해 실행 위치를 고른다.
3. **실패 격리 범위**: 자식 작업 하나가 실패했을 때 전체 작업을 취소할 것인가? $\rightarrow$ [Supervision Boundary 계약](coroutines/coroutine-exception-propagation.md)을 적용한다.
4. **스트림 발행 동작**: 수집자가 있을 때만 실행하는가, 아니면 항상 최신 상태를 유지하는가? $\rightarrow$ [Cold Flow](flow/cold-flow-execution.md) vs [StateFlow / SharedFlow](flow-state/stateflow-vs-flow.md)를 구분한다.
5. **UI 백그라운드 자원 낭비 방지**: 화면이 안 보일 때 수집을 중단하는가? $\rightarrow$ [Lifecycle-aware Collection](flow-state/lifecycle-aware-flow-collection.md) API를 사용한다.

관련 지도: [Android Data Layer Map](../android-data-layer-map.md), [Android State Management](../../architecture/state-management/android-state-management.md)
