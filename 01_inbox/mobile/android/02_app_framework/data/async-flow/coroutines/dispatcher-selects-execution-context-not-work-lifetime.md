---
title: dispatcher-selects-execution-context-not-work-lifetime
tags: [android, android/async, android/coroutines, android/data]
aliases: ["Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Dispatcher 는 실행 위치를 고르고 Scope 는 작업 수명을 소유한다

`CoroutineDispatcher` 는 coroutine 이 어떤 thread 또는 thread pool 에서 실행될지 고르는 execution context 다. `Main` 은 UI thread, `IO` 는 blocking I/O, `Default` 는 CPU work 에 주로 맞춘다.

Scope 는 작업이 누구의 수명에 묶이는지를 정한다. `withContext(Dispatchers.IO)` 로 실행 위치를 바꿔도 그 작업은 여전히 호출한 부모 scope 의 child 이며, 부모가 취소되면 함께 취소된다.

따라서 dispatcher 선택은 성능과 thread-safety 문제이고, scope 선택은 취소와 lifetime 문제다. 두 개념을 섞으면 background work 가 화면 수명에 묶여 사라지거나, 반대로 화면이 사라져도 작업이 계속 남는다.

```kotlin
suspend fun loadBenefits(): List<Benefit> =
    withContext(Dispatchers.IO) {
        api.fetchBenefits() // IO thread pool에서 실행
    } // 반환 시 호출한 부모 scope의 dispatcher로 자동 복귀
```

메인 thread 에서 `Dispatchers.IO` 없이 blocking I/O 를 직접 실행하면 `android.os.NetworkOnMainThreadException` 이 발생하거나 `StrictMode` 가 `StrictMode$DiskReadViolation`/`NetworkViolation` 로그를 남긴다. 반대로 위 `withContext` 블록은 IO thread 에서 실행되더라도 여전히 `loadBenefits()` 를 호출한 coroutine 의 자식이므로, 그 부모가 취소되면 `withContext` 블록도 함께 취소된다. 즉 dispatcher 를 바꿔도 취소 트리는 유지된다.

공식 문서: [Coroutines basics](https://kotlinlang.org/docs/coroutines-basics.html), [Coroutine best practices](https://developer.android.com/kotlin/coroutines/coroutines-best-practices)
