# Coroutine이란?

Coroutine은 Kotlin이 제공하는 **가벼운 비동기 실행 단위**입니다.

스레드와 비슷하게 "어떤 일을 따로 실행한다"는 느낌은 있지만, 스레드 자체는 아닙니다.

| 구분     | Thread             | Coroutine                  |
|:-------|:-------------------|:---------------------------|
| 정체     | OS가 관리하는 무거운 실행 단위 | Kotlin 런타임이 관리하는 가벼운 작업 단위 |
| 비용     | 생성/전환 비용이 큼        | 매우 많이 만들어도 상대적으로 가벼움       |
| 중단     | 스레드가 실제로 막힘        | 중단 지점에서 쉬었다가 나중에 재개        |
| 코드 스타일 | 콜백/동기화 코드가 많아지기 쉬움 | 순차 코드처럼 읽히는 비동기 코드         |

쉽게 말하면 Coroutine은 **기다릴 때 자리를 비켜주는 작업 단위**입니다.

```kotlin
viewModelScope.launch {
    val user = userRepository.fetchUser()
    val benefits = benefitRepository.fetchBenefits(user.id)
    _uiState.value = BenefitUiState.Success(benefits)
}
```

위 코드는 위에서 아래로 읽힙니다. 하지만 `fetchUser()`나 `fetchBenefits()`가 오래 걸릴 때 메인 스레드를 붙잡고 멈추는 것이 아니라, Coroutine이
잠시 중단되었다가 결과가 오면 다시 이어서 실행됩니다.
