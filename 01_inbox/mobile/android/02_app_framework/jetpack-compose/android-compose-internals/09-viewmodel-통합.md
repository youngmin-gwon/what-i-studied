# ViewModel 통합

상위 노트: [[android-compose-internals]]

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
