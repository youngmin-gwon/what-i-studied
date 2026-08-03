---
title: Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다
tags: [android, android/data, android/async, android/coroutines]
aliases: ["Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다

`CoroutineDispatcher`는 coroutine이 어떤 thread 또는 thread pool에서 실행될지 고르는 execution context다. `Main`은 UI thread, `IO`는 blocking I/O, `Default`는 CPU work에 주로 맞춘다.

Scope는 작업이 누구의 수명에 묶이는지를 정한다. `withContext(Dispatchers.IO)`로 실행 위치를 바꿔도 그 작업은 여전히 호출한 부모 scope의 child이며, 부모가 취소되면 함께 취소된다.

따라서 dispatcher 선택은 성능과 thread-safety 문제이고, scope 선택은 취소와 lifetime 문제다. 두 개념을 섞으면 background work가 화면 수명에 묶여 사라지거나, 반대로 화면이 사라져도 작업이 계속 남는다.

공식 문서: [Coroutines basics](https://kotlinlang.org/docs/coroutines-basics.html), [Coroutine best practices](https://developer.android.com/kotlin/coroutines/coroutines-best-practices)
