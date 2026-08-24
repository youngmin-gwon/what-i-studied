---
title: structured-concurrency
tags: [android, android/async, android/coroutines, android/data]
aliases: ["Structured concurrency는 부모 scope가 자식 작업의 수명을 소유하게 한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Structured concurrency는 부모 scope가 자식 작업의 수명을 소유하게 한다

### 개념 (What)
`structured concurrency`(구조화된 동시성)는 비동기 작업들을 파편화된 독립 스레드가 아니라, **엄격한 부모-자식 트리 구조(Parent-Child Tree Hierarchy)**로 조직화하여 수명과 취소, 실패를 관리하는 파라다임이다. "부모 Scope는 모든 자식 작업이 완전히 끝날 때까지 완료되지 않으며, 부모가 취소되면 모든 자식도 함께 취소된다"는 대원칙을 가진다.

### 왜 필요한가 (Why)
1. **비동기 작업 누수(Coroutine Leak) 박멸**: 과거 `Thread`나 `GlobalScope.launch`는 실행된 비동기 작업이 Activity나 ViewModel의 수명을 초과하여 백그라운드에서 계속 실행되는 누수 현상을 유발했다. Structured Concurrency는 컴포넌트 파괴 시 Scope만 cancel 하면 하위의 모든 작업이 100% 자동 정지되도록 보장한다.
2. **예측 가능한 리소스 수거**: 네트워크 연결, 파일 IO, 락(Lock) 해제 등의 정리 작업이 부모 작업 종료 이전에 확실히 완료됨을 구조적으로 보장한다.

### 내부 메커니즘 (How)
1. **Job 트리 형성**:
   - `CoroutineScope.launch`나 `async`로 새 Coroutine을 생성하면, 새 Coroutine의 `Job`은 부모 Context의 `Job`을 찾아 `parent.attachChild(childJob)`를 실행하여 `ChildHandle`로 연결된다.
2. **상태 머신 단계별 수명 관리**:
   - 부모 `Job`은 자식 Coroutine들이 실행 중일 때 `Active` 상태를 유지한다.
   - 부모의 본래 코드 실행이 끝나면 부모는 바로 `Completed`가 되는 것이 아니라 **`Completing` (자식 완료 대기)** 상태에 진입한다.
   - 모든 자식 Coroutine이 `Completed` 또는 `Cancelled` 상태에 도달하면 비로소 부모 `Job`이 `Completed` 상태로 전이된다.
3. **취소 전파**:
   - 부모 `Job.cancel()` 호출 시 부모는 `Cancelling` 상태로 바뀌며, 자식 핸들 리스트를 순회하여 모든 자식 `Job.cancel()`을 즉시 유저스페이스 억제 신호로 전달한다.

```mermaid
graph TD
    A["CoroutineScope (e.g. viewModelScope)"] --> B["Parent Job (State: Active -> Completing -> Completed)"]
    B -->|"attachChild()"| C["Child Job 1 (Network Fetch)"]
    B -->|"attachChild()"| D["Child Job 2 (DB Query)"]
    
    E"[viewmodel.onCleared()"] -->|"1. cancel()"| B
    B -->|"2. Recursive cancel()"| C
    B -->|"2. Recursive cancel()"| D

    style A fill:#fff3e0,stroke:#f57c00,color:#e65100
    style B fill:#e1f5fe,stroke:#0288d1,color:#01579b
    style C fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
    style D fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
```

### 현대 표준 vs 레거시 비교

| 비교 항목 | 레거시 (GlobalScope / CompositeDisposable) | 현대 표준 (Structured Concurrency) |
| :--- | :--- | :--- |
| **수명 소유자** | 없음 (글로벌 런타임에 흩어짐) | `viewModelScope`, `lifecycleScope` 등 명시적 Scope |
| **취소 누락** | `onDestroy()`에서 `disposable.clear()` 누락 시 메모리 누수 | Scope 소유자의 Lifecycle 해제 시 트리 전체 자동 취소 |
| **작업 완결성** | 부모 함수가 끝나도 자식 스레드가 뒤에서 돌아감 | 부모는 모든 자식이 종료될 때까지 완료 대기 (`Completing`) |

### Idiomatic Kotlin 코드 예시

```kotlin
class PaymentViewModel(
    private val paymentRepository: PaymentRepository
) : ViewModel() {

    init {
        // viewModelScope가 부모 Scope가 됨
        viewModelScope.launch {
            // 부모 Coroutine 시작
            val logJob = launch { trackAnalytics() } // 자식 1
            val paymentJob = launch { processTransaction() } // 자식 2
            
            // 두 자식이 모두 끝날 때까지 부모 coroutine은 Completing 상태로 대기함
        }
    }

    private suspend fun trackAnalytics() {
        delay(1_000)
    }

    private suspend fun processTransaction() {
        paymentRepository.executePayment()
    }
    
    // 사용자가 화면을 이탈하여 ViewModel이 파괴되면
    // viewModelScope 내부의 cancellation이 트리를 따라 logJob, paymentJob을 모두 자동 정지함
}
```

공식 문서: [Coroutines basics - Structured concurrency](https://kotlinlang.org/docs/coroutines-basics.html#structured-concurrency)
