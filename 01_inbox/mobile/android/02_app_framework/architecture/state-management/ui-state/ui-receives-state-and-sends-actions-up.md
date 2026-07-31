# UI는 상태를 아래로 받고 사용자 행동을 위로 전달한다

상위 문서: [Android UI State](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-state.md)


## 핵심 주장

Compose 화면의 기본 데이터 흐름은 `state down, action up`이다.
화면은 ViewModel의 상태를 받아 그리고, 사용자의 행동은 callback이나 `UiAction`으로 올린다.
화면이 상태를 직접 변경하거나 ViewModel이 Composable을 직접 조작하지 않으면 흐름의 방향이 분명해진다.

## 흐름

```text
ViewModel -> StateFlow<UiState> -> UI render
UI event -> callback/UiAction -> ViewModel
```

```kotlin
data class SignInUiState(
    val id: String = "",
    val isSubmitting: Boolean = false,
)

@Composable
fun SignInRoute(viewModel: SignInViewModel) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()

    SignInScreen(
        uiState = state,
        onIdChanged = viewModel::onIdChanged,
        onSubmitClick = viewModel::onSubmitClick,
    )
}
```

`SignInScreen`은 입력을 받아 callback을 호출할 뿐 상태 소유자에게 직접 접근하지 않는다.
ViewModel은 callback을 처리하고 상태를 변경하거나 Repository 작업을 조율한다.

## 경계

- UI는 `MutableStateFlow`를 노출하지 않는다.
- ViewModel은 `NavController`, `SnackbarHostState` 같은 UI 실행기를 보관하지 않는다.
- Composable body에서 네트워크, 저장, 데이터베이스 작업을 직접 시작하지 않는다.
- 단순 화면에서는 명시적인 함수 callback이 sealed `UiAction`보다 읽기 쉽다.

## 판단 기준

상태를 다시 그려야 하는가를 먼저 결정하고, 행동은 그 상태 변화를 요청하는 입력으로 모델링한다.
이렇게 하면 화면 재구성이나 새 collector가 생겨도 UI가 같은 상태를 다시 렌더링할 수 있다.
