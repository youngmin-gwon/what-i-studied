# 테스트 전략

상위 노트: [[viewmodel-ui-state-reducer]]

단순 화면은 ViewModel 테스트로 충분합니다.

```kotlin
@Test
fun signIn_withInvalidId_setsIdError() = runTest {
        val viewModel = SignInViewModel(fakeRepository)

        viewModel.signIn(id = "", password = "password")

        assertTrue(viewModel.uiState.value.isIdError)
    }
```

Reducer를 분리했다면 Reducer 테스트는 더 작고 빠르게 작성할 수 있습니다.

```kotlin
@Test
fun emailChanged_updatesEmailAndSubmitEnabled() {
    val reducer = SignUpStateReducer()

    val state = reducer.reduce(
        state = SignUpUiState(password = "password"),
        action = SignUpAction.EmailChanged("user@test.com"),
    )

    assertEquals("user@test.com", state.email)
    assertTrue(state.isSubmitEnabled)
}
```

Reducer 테스트는 Android framework, coroutine, Flow 없이 동작해야 합니다. 만약 reducer 테스트에 dispatcher, fake
repository, Android context가 필요해졌다면 책임이 섞인 것입니다.

---
