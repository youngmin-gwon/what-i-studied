# Reducer란 무엇인가

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

Reducer는 이전 상태와 action을 받아 새 상태를 계산하는 순수 함수입니다.

```text
oldState + action -> newState
```

Reducer는 상태를 소유하지 않습니다. Repository를 호출하지 않고, coroutine을 실행하지 않고, Android API도 사용하지 않습니다.

```kotlin
internal sealed interface SignUpAction {
    data class EmailChanged(val email: String) : SignUpAction
    data class PasswordChanged(val password: String) : SignUpAction
    data object SubmitStarted : SignUpAction
    data object SubmitFailed : SignUpAction
}

internal class SignUpStateReducer {
    fun reduce(
        state: SignUpUiState,
        action: SignUpAction,
    ): SignUpUiState {
        return when (action) {
            is SignUpAction.EmailChanged -> {
                val email = action.email
                state.copy(
                    email = email,
                    isSubmitEnabled = canSubmit(
                        email = email,
                        password = state.password,
                    ),
                )
            }

            is SignUpAction.PasswordChanged -> {
                val password = action.password
                state.copy(
                    password = password,
                    isSubmitEnabled = canSubmit(
                        email = state.email,
                        password = password,
                    ),
                )
            }

            SignUpAction.SubmitStarted -> {
                state.copy(isSubmitting = true)
            }

            SignUpAction.SubmitFailed -> {
                state.copy(isSubmitting = false)
            }
        }
    }

    private fun canSubmit(
        email: String,
        password: String,
    ): Boolean {
        return email.isNotBlank() && password.isNotBlank()
    }
}
```

ViewModel은 reducer를 호출해 상태를 반영합니다.

```kotlin
class SignUpViewModel(
    private val repository: AuthRepository,
    private val reducer: SignUpStateReducer = SignUpStateReducer(),
) : ViewModel() {
    private val _uiState = MutableStateFlow(SignUpUiState())
    val uiState: StateFlow<SignUpUiState> = _uiState.asStateFlow()

    fun onEmailChanged(email: String) {
        dispatch(SignUpAction.EmailChanged(email))
    }

    fun submit() {
        viewModelScope.launch {
            dispatch(SignUpAction.SubmitStarted)

            val result = repository.signUp(_uiState.value.email)

            if (result.isFailure) {
                dispatch(SignUpAction.SubmitFailed)
            }
        }
    }

    private fun dispatch(action: SignUpAction) {
        _uiState.update { state ->
            reducer.reduce(state, action)
        }
    }
}
```

---
