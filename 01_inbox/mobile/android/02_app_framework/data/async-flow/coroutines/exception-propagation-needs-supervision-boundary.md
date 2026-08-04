---
title: exception-propagation-needs-supervision-boundary
tags: [android, android/async, android/coroutines, android/data]
aliases: ["Coroutine 예외 전파는 builder와 supervision boundary가 결정한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Coroutine 예외 전파는 builder 와 supervision boundary 가 결정한다

Coroutine 실패 동작은 `launch` 와 `async` 중 무엇으로 시작했는지, 그리고 어떤 부모 boundary 아래에 있는지에 따라 달라진다. `launch` 의 처리되지 않은 예외는 부모로 전파되고, `async` 의 예외는 `await()` 에서 관찰된다.

일반 parent-child 관계에서는 자식 실패가 부모 취소로 이어질 수 있다. 독립 작업 일부가 실패해도 sibling 을 계속 살려야 한다면 `supervisorScope` 나 `SupervisorJob` 처럼 명시적 supervision boundary 를 둔다.

`CoroutineExceptionHandler` 는 이미 전파되어 처리되지 않은 예외를 관찰하는 마지막 지점이지, 임의의 child 실패를 모두 복구하는 catch-all 이 아니다. `runCatching` 이나 넓은 `catch` 를 쓸 때는 `CancellationException` 을 삼켜 structured cancellation 을 깨지 않도록 다시 던져야 한다.

```kotlin
viewModelScope.launch {
    try {
        repository.sync()
    } catch (e: CancellationException) {
        throw e // 취소는 다시 던져 structured cancellation을 유지한다
    } catch (e: IOException) {
        _uiState.value = UiState.Error
    }
}
```

`launch` 로 시작한 위 블록에서 처리되지 않은 예외는 `viewModelScope` 를 취소시키고 나머지 sibling coroutine 도 함께 취소된다. 반면 같은 로직을 `async { repository.sync() }` 로 시작하면 예외는 즉시 전파되지 않고 `deferred.await()` 를 호출하는 시점에 다시 던져진다. `catch (e: CancellationException)` 절을 빠뜨리고 모든 예외를 삼키면, 실제로는 사용자가 화면을 나가 취소된 작업인데도 `UiState.Error` 로 잘못 표시되는 버그가 생긴다.
