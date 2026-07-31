# UI 에서 Flow 수집

상위 노트: [[android-coroutines-flow]]

##### View 시스템

```kotlin
class UserActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // ✅ 권장: repeatOnLifecycle
        lifecycleScope.launch {
            repeatOnLifecycle(Lifecycle.State.STARTED) {
                // STARTED 에서 수집 시작, STOPPED 에서 자동 취소
                viewModel.uiState.collect { state ->
                    when (state) {
                        is UiState.Loading -> showLoading()
                        is UiState.Success -> showUsers(state.users)
                        is UiState.Error -> showError(state.message)
                    }
                }
            }
        }
    }
}
```

##### Compose

```kotlin
@Composable
fun UserScreen(viewModel: UserViewModel = hiltViewModel()) {
    // ✅ 생명주기 인식 수집 (Compose 표준)
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    
    when (uiState) {
        is UiState.Loading -> CircularProgressIndicator()
        is UiState.Success -> UserList((uiState as UiState.Success).users)
        is UiState.Error -> ErrorMessage((uiState as UiState.Error).message)
    }
}
```
