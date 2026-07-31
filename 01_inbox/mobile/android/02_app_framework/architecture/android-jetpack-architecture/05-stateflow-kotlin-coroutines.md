# StateFlow (Kotlin Coroutines)

상위 노트: [[android-jetpack-architecture]]

LiveData 의 현대적 대안.

```kotlin
class UserViewModel : ViewModel() {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
    
    private val _users = MutableStateFlow<List<User>>(emptyList())
    val users: StateFlow<List<User>> = _users.asStateFlow()
    
    fun loadUsers() {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            try {
                val result = repository.getUsers()
                _users.value = result
                _uiState.value = UiState.Success
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e.message)
            }
        }
    }
}

// Activity/Fragment 에서 수집
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.users.collect { users ->
            // UI 업데이트
        }
    }
}

// Compose 에서 수집
@Composable
fun UserScreen(viewModel: UserViewModel = viewModel()) {
    val users by viewModel.users.collectAsStateWithLifecycle()
    
    LazyColumn {
        items(users) { user ->
            Text(user.name)
        }
    }
}
```
