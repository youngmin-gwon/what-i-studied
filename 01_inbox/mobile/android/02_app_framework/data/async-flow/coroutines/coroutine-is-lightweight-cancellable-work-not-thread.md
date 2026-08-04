---
title: coroutine-is-lightweight-cancellable-work-not-thread
tags: [android, android/async, android/coroutines, android/data]
aliases: ["Coroutine은 thread가 아니라 취소 가능한 경량 작업이다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Coroutine 은 thread 가 아니라 취소 가능한 경량 작업이다

Coroutine 은 OS thread 자체가 아니라 중단, 재개, 취소를 표현하는 작업 단위다. 그래서 Android 코드에서 coroutine 을 설계할 때 핵심 질문은 "어느 thread 를 만들 것인가"가 아니라 "이 작업의 수명은 누가 소유하고 언제 취소되는가"다.

`launch` 나 `async` 로 시작한 작업은 반드시 어떤 `CoroutineScope` 에 속한다. 화면 수명에 묶이는 작업은 `viewModelScope` 나 lifecycle-aware scope 에 둔다. 앱 전체 작업처럼 화면보다 오래 살아야 하는 경우에도 별도 application scope 처럼 명시적인 소유자를 둔다.

Thread 선택은 `Dispatcher` 가 담당한다. 네트워크, 디스크, CPU 작업을 어디에서 실행할지는 [Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다](./dispatcher-selects-execution-context-not-work-lifetime.md) 에서 결정하고, 작업의 부모 - 자식 수명은 [Structured concurrency는 부모 scope가 자식 작업의 수명을 소유하게 한다](./structured-concurrency-parent-owns-child-lifetime.md) 로 유지한다.

실무 판단은 단순하다. coroutine 을 만들 때 반환값보다 먼저 수명 소유자와 취소 경로를 확인한다. 이 둘이 명확하지 않으면 작업은 가벼워 보여도 leak 이나 중복 실행의 원인이 된다.

```kotlin
class BenefitViewModel(
    private val repository: BenefitRepository,
) : ViewModel() {
    fun refresh() {
        viewModelScope.launch { // Job은 ViewModel.onCleared()에서 자동 취소된다
            repository.sync()
        }
    }
}
```

`viewModelScope` 는 수천 개의 OS thread 를 만들지 않고도 동시에 수만 개의 coroutine 을 유지할 수 있다. 화면이 종료되어 `onCleared()` 가 호출되면 이 scope 의 `Job` 이 취소되고, 그 안에서 실행 중이던 `sync()` 는 다음 suspension point 에서 `kotlinx.coroutines.JobCancellationException` 을 받으며 정리된다. `GlobalScope.launch` 로 같은 작업을 시작하면 이 취소 연결이 끊어져 화면이 사라진 뒤에도 작업이 계속 실행되고, StrictMode 나 LeakCanary 로 그 ViewModel 인스턴스가 해제되지 않는 leak 으로 관찰된다.

공식 문서: [Kotlin Coroutines basics](https://kotlinlang.org/docs/coroutines-basics.html), [CoroutineScope API](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/)
