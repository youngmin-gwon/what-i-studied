---
title: parallel-coroutines-need-explicit-parent-and-failure-policy
tags: [android, android/data, android/async, android/coroutines]
aliases: ["병렬 Coroutine은 부모 scope와 실패 정책을 먼저 정해야 한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 병렬 Coroutine 은 부모 scope 와 실패 정책을 먼저 정해야 한다

여러 coroutine을 동시에 실행할 때 핵심은 `async`를 몇 개 쓰는지가 아니라 결과, 취소, 실패가 어떤 규칙으로 합쳐지는지다. 같은 사용자 액션에서 시작된 병렬 작업은 보통 하나의 부모 scope 안에 있어야 한다.

`coroutineScope` 안에서 여러 `async`를 실행하면 자식 중 하나가 실패할 때 형제 작업도 취소된다. 화면을 구성하는 필수 데이터들이 모두 성공해야 하는 경우에는 이 기본 전파가 자연스럽다.

```kotlin
suspend fun loadHome(): HomeData = coroutineScope {
    val userDeferred = async { userRepository.fetchUser() }
    val benefitsDeferred = async { benefitRepository.fetchBenefits() }
    // benefitsDeferred가 실패하면 userDeferred도 취소되고 예외가 호출자에게 전파된다
    HomeData(userDeferred.await(), benefitsDeferred.await())
}
```

반대로 일부 실패를 허용하려면 `supervisorScope`나 개별 `runCatching` 같은 명시적인 경계가 필요하다. 실패가 형제 작업까지 전파되어야 하는지, 아니면 실패한 결과만 대체해야 하는지를 코드 구조로 드러내야 한다.

```kotlin
suspend fun loadHomeBestEffort(): HomeData = supervisorScope {
    val userDeferred = async { userRepository.fetchUser() }
    val benefitsDeferred = async { benefitRepository.fetchBenefits() }
    val user = runCatching { userDeferred.await() }.getOrDefault(User.Guest)
    // benefitsDeferred 실패는 user 결과에 영향을 주지 않는다
    val benefits = runCatching { benefitsDeferred.await() }.getOrDefault(emptyList())
    HomeData(user, benefits)
}
```

`coroutineScope` 버전은 하나라도 실패하면 `loadHome()` 호출자가 예외를 그대로 받는다. `supervisorScope` 버전은 각 `await()` 호출을 개별적으로 감싸지 않으면 여전히 첫 실패에서 예외가 던져지므로, sibling 격리가 필요한 코드는 `supervisorScope` 선언만으로 끝나지 않고 각 결과를 `runCatching` 이나 `try/catch` 로 개별 처리해야 한다.

Android에서는 병렬 작업을 ViewModel 안에 둔다고 자동으로 안전해지지 않는다. ViewModel은 수명 소유자를 제공할 뿐이고, 내부 병렬 작업의 실패 정책은 별도로 설계해야 한다.

관련 노트: [Coroutine 예외 전파는 builder와 supervision boundary가 결정한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/exception-propagation-needs-supervision-boundary.md)
