# ViewModel이라는 이름이 헷갈리는 이유

상위 노트: [[viewmodel-ui-state-reducer]]

아래 문장은 이해를 돕기 위한 일부러 강한 표현입니다.

```text
Android ViewModel은 "View가 쓰는 immutable model"이 아니다.
Android ViewModel은 "수명주기를 아는 UI state container"다.
```

`ViewModel`이라는 이름만 보면 `UserUiModel`, `SignInUiState` 같은 immutable data class가 떠오를 수 있습니다. 하지만
Android의 `ViewModel` 클래스는 그런 객체가 아닙니다.

Android `ViewModel`은 보통 아래처럼 생겼습니다.

```kotlin
class LoginViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(LoginUiState())
    val uiState: StateFlow<LoginUiState> = _uiState.asStateFlow()

    fun onLoginClick() {
        viewModelScope.launch {
            // repository 호출
            // state 갱신
        }
    }
}
```

즉, Android ViewModel은 immutable model이 아니라 mutable state holder입니다. 더 정확히는 mutable state를 내부에 숨기고,
외부에는 읽기 전용 observable state를 공개하는 화면 단위 상태 컨테이너입니다.

역사적으로 MVVM의 ViewModel은 WPF/Silverlight 계열에서 `Property`와 `Command`를 노출하고 View가 binding하는 대상에 가까웠습니다.

```text
View
 <-> Binding
ViewModel
 - Property
 - Command
```

Android의 `ViewModel` 클래스는 MVVM 패턴 전체를 강제하기 위해 만들어진 타입이라기보다, configuration change 후에도 화면 관련 상태와 작업을
유지하기 위한 Jetpack 구성요소입니다. Compose, StateFlow, Coroutine이 붙으면서 오늘날에는 다음 역할을 함께 맡는 경우가 많아졌습니다.

- UI state holder
- user action handler
- `viewModelScope` owner
- Repository/UseCase 호출 조율자
- 화면 상태의 source of truth

따라서 이 문서에서 `ViewModel`이라고 할 때는 "View의 immutable model"이 아니라 **Android 플랫폼이 제공하는 lifecycle-aware
screen state holder**를 의미합니다.

---
