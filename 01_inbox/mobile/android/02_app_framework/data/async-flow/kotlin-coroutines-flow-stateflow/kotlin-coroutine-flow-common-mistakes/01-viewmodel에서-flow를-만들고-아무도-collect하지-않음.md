# ViewModel에서 Flow를 만들고 아무도 collect하지 않음

```kotlin
// collect 또는 stateIn이 없으면 실행되지 않음
repository.observeBenefits()
    .map { benefits -> BenefitUiState.Ready(benefits) }
```

Flow는 대부분 Cold입니다. `collect`, `stateIn`, `shareIn` 같은 최종 동작이 있어야 실제로 흐릅니다.
