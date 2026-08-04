---
title: suspend-function-suspends-coroutine-without-blocking-thread
tags: [android, android/async, android/coroutines, android/data]
aliases: ["suspend 함수는 thread가 아니라 coroutine을 멈춘다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## suspend 함수는 thread 가 아니라 coroutine 을 멈춘다

`suspend` 함수는 호출한 thread 를 점유한 채 기다리는 함수가 아니다. 실행을 중단할 수 있는 지점을 표시하고, 기다리는 동안 현재 coroutine 을 suspend 상태로 돌린 뒤 나중에 이어서 실행할 수 있게 한다.

이 차이 때문에 Android UI 코드에서 `suspend` 함수는 callback 보다 읽기 쉬운 순차 코드로 보이지만, 내부 계약은 여전히 비동기다. 호출자는 어떤 scope 에서 이 함수를 실행하는지, 취소가 들어오면 중단 지점이 협조적으로 빠져나올 수 있는지 확인해야 한다.

`suspend` 는 thread 전환을 자동으로 의미하지 않는다. 무거운 작업은 `withContext(Dispatchers.IO)` 나 적절한 dispatcher 선택과 함께 설계해야 한다. 실행 위치는 [Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/dispatcher-selects-execution-context-not-work-lifetime.md) 의 관심사다.

따라서 repository 의 suspend API 는 "이 함수가 완료될 때까지 호출 coroutine 을 논리적으로 기다리게 한다"는 계약을 가진다. UI thread 를 막지 않는다는 점과 작업이 취소 가능해야 한다는 점이 핵심이다.

```kotlin
suspend fun fetchUser(id: String): User {
    delay(2_000) // thread를 점유하지 않고 coroutine만 2초간 suspend한다
    return api.getUser(id)
}
```

메인 thread 에서 `viewModelScope.launch { fetchUser(id) }` 를 호출해도 `delay(2_000)` 동안 UI 는 계속 응답한다. 만약 여기서 `Thread.sleep(2_000)` 을 대신 썼다면 같은 thread 를 점유하는 다른 작업이 함께 멈추고, 메인 thread 라면 ANR(`Application Not Responding`) 로 이어질 수 있다. 취소 협조가 없는 suspend 함수, 예를 들어 `while (true) { /* delay 없이 반복 */ }` 처럼 suspension point 가 없는 루프는 부모 coroutine 이 취소되어도 스스로 멈추지 않는다.

공식 문서: [Kotlin Coroutines basics](https://kotlinlang.org/docs/coroutines-basics.html)
