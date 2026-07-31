# ViewModel 통합

상위 노트: [android-compose-internals](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals.md)

```kotlin
@Composable
fun UserScreen(
    viewModel: UserViewModel = viewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    
    when (uiState) {
        is UiState.Loading -> LoadingIndicator()
        is UiState.Success -> UserContent(uiState.data)
        is UiState.Error -> ErrorMessage(uiState.message)
    }
}

// Hilt 사용
@Composable
fun UserScreen(
    viewModel: UserViewModel = hiltViewModel()
) {
    // ...
}
```
