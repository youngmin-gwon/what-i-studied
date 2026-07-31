# ViewModel 안의 `copy()`가 많아질 때

상위 노트: [[viewmodel-ui-state-reducer]]

작은 화면은 ViewModel 안에서 직접 상태를 갱신하는 것이 가장 단순합니다.

```kotlin
fun onEmailChanged(email: String) {
    _uiState.update { state ->
        state.copy(
            email = email,
            isSubmitEnabled = email.isNotBlank() && state.password.isNotBlank(),
        )
    }
}
```

이 정도는 별도 abstraction이 필요 없습니다.

하지만 아래 조건이 겹치면 ViewModel이 빠르게 커집니다.

- 입력 필드가 많다.
- `onXxxChanged()`가 10개 이상 늘어난다.
- `copy()`와 검증 로직이 여러 함수에 반복된다.
- 어떤 action이 어떤 상태 전이를 만드는지 ViewModel 전체를 읽어야 알 수 있다.
- coroutine, repository 호출, 상태 계산, 일회성 이벤트 발행이 한 함수에 섞인다.

이때 상태 계산만 별도 순수 Kotlin 객체로 분리할 수 있습니다. 이 객체를 Reducer라고 부릅니다.

---
