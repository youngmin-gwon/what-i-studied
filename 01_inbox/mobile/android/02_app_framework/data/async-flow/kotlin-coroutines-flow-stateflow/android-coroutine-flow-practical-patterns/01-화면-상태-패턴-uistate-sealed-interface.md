# 화면 상태 패턴: UiState sealed interface

로딩/성공/에러 상태가 분명한 화면에서는 `sealed interface`를 자주 씁니다.

```kotlin
sealed interface BenefitUiState {
    data object Loading : BenefitUiState
    data class Ready(val benefits: List<Benefit>) : BenefitUiState
    data class Error(val message: String) : BenefitUiState
}
```

```kotlin
val uiState: StateFlow<BenefitUiState> =
    repository.observeBenefits()
        .map { benefits ->
            val state: BenefitUiState = BenefitUiState.Ready(benefits)
            state
        }
        .onStart {
            emit(BenefitUiState.Loading)
        }
        .catch {
            emit(BenefitUiState.Error("혜택 목록을 불러오지 못했습니다."))
        }
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000),
            initialValue = BenefitUiState.Loading,
        )
```
