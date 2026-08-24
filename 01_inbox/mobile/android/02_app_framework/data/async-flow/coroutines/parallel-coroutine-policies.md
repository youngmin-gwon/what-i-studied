---
title: parallel-coroutine-policies
tags: [android, android/data, android/async, android/coroutines]
aliases: ["병렬 Coroutine은 부모 scope와 실패 정책을 먼저 정해야 한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 병렬 Coroutine은 부모 scope와 실패 정책을 먼저 정해야 한다

### 개념 (What)
복수의 독립적인 비동기 작업을 동시에 실행할 때(`async` / `launch` 병렬 수행), **모든 작업이 성공해야만 결과를 합칠 것인가(All-or-Nothing)**, 아니면 **일부 작업이 실패하더라도 성공한 결과만 부분 취합할 것인가(Best-Effort Partial Success)**를 부모 Scope와 실패 조율 API로 명시하는 아키텍처 규칙이다.

### 왜 필요한가 (Why)
1. **리얼타임 취소 및 자원 낭비 방지**: 네트워크 요청 3개를 동시에 보냈을 때 1번 요청이 즉시 실패했다면, 남아있는 2, 3번 네트워크 요청을 계속 기다리거나 전송하는 것은 배터리, 데이터, CPU 자원의 낭비다. All-or-Nothing 상황에서는 단 하나의 실패 발생 시 나머지 병렬 작업을 즉시 동시 취소(Cancel)해야 한다.
2. **동시성 경쟁 상태(Race Condition) 및 Zombie Coroutine 방지**: 부모 Scope 구조 없이 개별적으로 `async`를 띄우면(예: `GlobalScope.async`), 일부 작업이 실패했음에도 다른 작업이 백그라운드에서 끝까지 실행되어 메모리 누수와 오염된 상태 업데이트를 일으킨다.

### 내부 메커니즘 (How)
1. **`coroutineScope` (All-or-Nothing)**:
   - `coroutineScope { ... }`는 새로운 Child Job을 생성하여 현재 CoroutineContext를 계승한다.
   - 내부에서 시작된 여러 `async` 작업 중 하나에서 예외가 발생하면, `coroutineScope`는 즉시 나머지 모든 `async` 자식들에게 `cancel()` 명령을 내리고, 호출자에게 해당 예외를 던진다.
   - `awaitAll()`을 사용하면 모든 자식의 결과를 수집하되 단 하나의 실패 시 즉시 빠른 실패(Fast-Fail)로 빠져나온다.
2. **`supervisorScope` + `runCatching` / `try-catch` (Best-Effort)**:
   - `supervisorScope { ... }`는 자식 간의 실패 전파를 차단한다.
   - 자식 `async` 내부의 실패가 형제를 취소시키지 않으므로, 각 `async`의 `await()` 호출부를 `runCatching { deferred.await() }` 또는 `try-catch`로 개별 보호하여 부분 성공 결과를 안전하게 취합할 수 있다.

```mermaid
graph TD
    subgraph "coroutineScope (Fast Fail All-or-Nothing)"
        A1["coroutineScope"] --> B1["async A (Success)"]
        A1 --> C1["async B (Fails!)"]
        C1 -->|"1. Fail & Cancel Parent"| A1
        A1 -->|"2. Cancel Sibling"| B1
    end

    subgraph "supervisorScope (Best Effort Partial Success)"
        A2["supervisorScope"] --> B2["async A (Success)"]
        A2 --> C2["async B (Fails!)"]
        C2 -.->"Isolated Failure"| C2
        B2 -->|"Returns Data"| A2
        C2 -->|"Returns Default / Fallback"| A2
    end

    style C1 fill:#ffebee,stroke:#c62828,color:#b71c1c
    style B1 fill:#ffebee,stroke:#c62828,color:#b71c1c
    style C2 fill:#ffebee,stroke:#c62828,color:#b71c1c
    style B2 fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
```

### 현대 표준 vs 레거시 비교

| 비교 항목 | 레거시 (RxJava Zip / ExecutorService) | 현대 표준 ([Kotlin Coroutines](kotlin-coroutines.md)) |
| :--- | :--- | :--- |
| **병렬 수집** | `Observable.zip()` 또는 `Future.get()` 차단 대기 | `coroutineScope` 내 `async` + `awaitAll()` 비차단 대기 |
| **부분 실패 처리** | `onErrorReturn()`을 각 Observables에 복잡하게 체이닝 | `supervisorScope` 내 `runCatching { deferred.await() }` |
| **자동 취소** | 한 작업 실패 시 다른 `Future`를 수동 `cancel(true)` 해야함 | `coroutineScope`가 자식 작업을 자동 원자적 취소 |

### Idiomatic Kotlin 코드 예시

```kotlin
data class HomeScreenData(val user: UserInfo, val products: List<Product>)
data class BestEffortHomeScreenData(val user: UserInfo?, val products: List<Product>)

class HomeRepository(
    private val userApi: UserApi,
    private val productApi: ProductApi
) {
    // 1. All-or-Nothing: 두 데이터 모두 필수인 경우 (하나라도 실패 시 전체 예외)
    suspend fun fetchHomeScreenStrict(): HomeScreenData = coroutineScope {
        val userDeferred = async { userApi.getUserInfo() }
        val productsDeferred = async { productApi.getTopProducts() }

        // userDeferred 실패 시 productsDeferred는 즉시 취소됨
        HomeScreenData(
            user = userDeferred.await(),
            products = productsDeferred.await()
        )
    }

    // 2. Best-Effort: 상품 목록 실패 시 빈 리스트로 대치하여 프로필은 보여주는 경우
    suspend fun fetchHomeScreenBestEffort(): BestEffortHomeScreenData = supervisorScope {
        val userDeferred = async { userApi.getUserInfo() }
        val productsDeferred = async { productApi.getTopProducts() }

        val user = runCatching { userDeferred.await() }.getOrNull()
        val products = runCatching { productsDeferred.await() }.getOrElse { emptyList() }

        BestEffortHomeScreenData(user = user, products = products)
    }
}
```

공식 문서: [Composing suspending functions](https://kotlinlang.org/docs/composing-suspending-functions.html)
