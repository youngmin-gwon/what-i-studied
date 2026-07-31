# 화면 상태는 불변 모델로 만들고 변경은 명시적인 상태 전이로 제한한다

상위 문서: [Android UI State](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-state.md)


## 핵심 주장

화면에 공개하는 상태는 immutable data class 또는 sealed model로 만들고, 변경은 명시적인 action이나 함수가 요청한 전이로 제한한다.
UI가 상태 내부를 직접 수정할 수 없으면 상태의 source of truth와 변경 경로를 추적하기 쉽다.

```kotlin
data class LoginUiState(
    val email: String = "",
    val password: String = "",
    val isSubmitting: Boolean = false,
    val errorMessage: String? = null,
)
```

ViewModel 내부에서는 `MutableStateFlow`를 숨기고 읽기 전용 `StateFlow`만 공개한다.

```kotlin
private val _uiState = MutableStateFlow(LoginUiState())
val uiState: StateFlow<LoginUiState> = _uiState.asStateFlow()

fun onEmailChanged(email: String) {
    _uiState.update { it.copy(email = email, errorMessage = null) }
}
```

`copy`는 변경된 필드와 그 이유를 코드에 남긴다.
파생값은 전이 시 함께 계산하거나 별도 순수 함수로 계산해 일관성을 유지한다.

불변 모델은 모든 Compose state holder를 반드시 immutable data class로 바꾸라는 뜻은 아니다.
`TextFieldState`처럼 입력 pipeline을 위한 specialized holder는 별도 판단이 필요하지만, `NavController`나 `SnackbarHostState` 같은 실행기는 화면 상태에 넣지 않는다.

## 기대 효과

- 상태 변경 지점이 명확해진다.
- 이전 상태와 다음 상태를 테스트할 수 있다.
- 새 collector가 최신 snapshot을 안전하게 읽는다.
- UI와 외부 작업이 상태 변경 규칙을 우회하기 어려워진다.

## 전이의 명시성

입력 변경, 제출 시작, 제출 성공, 제출 실패를 각각 action이나 함수로 표현하면 변경 의도가 드러난다.
여러 곳에서 같은 mutable 객체를 수정하는 방식은 호출 순서에 따라 결과가 달라지기 쉽다.

불변 상태가 자동으로 좋은 모델을 보장하는 것은 아니다.
서로 모순되는 boolean을 많이 두거나, 실제 owner가 아닌 곳에서 상태를 복사하면 모델은 여전히 복잡해진다.
필요하면 sealed hierarchy와 value object로 유효한 상태 조합을 제한한다.

## 테스트 관점

상태 전이 테스트는 입력 상태를 고정하고 기대하는 새 snapshot을 비교한다.
UI 테스트보다 작은 단위로 검증할 수 있고, 상태를 바꾸는 우회 경로가 생겼는지도 쉽게 확인할 수 있다.
