# Jetpack Compose 에서 사용

```kotlin
// 1. StateFlow 사용 (Compose 권장)
class UserViewModel : ViewModel() {
    private val _users = MutableStateFlow<List<User>>(emptyList())
    val users: StateFlow<List<User>> = _users.asStateFlow()
    
    private val _isLoading = MutableStateFlow(false)
    val isLoading: StateFlow<Boolean> = _isLoading.asStateFlow()
    
    fun loadUsers() {
        viewModelScope.launch {
            _isLoading.value = true
            try {
                _users.value = fetchUsersFromApi()
            } finally {
                _isLoading.value = false
            }
        }
    }
}

// 2. Composable에서 사용
@Composable
fun UserScreen(
    viewModel: UserViewModel = viewModel()
) {
    // StateFlow를 Compose State로 변환
    val users by viewModel.users.collectAsStateWithLifecycle()
    val isLoading by viewModel.isLoading.collectAsStateWithLifecycle()
    
    Column {
        if (isLoading) {
            CircularProgressIndicator()
        }
        
        LazyColumn {
            items(users) { user ->
                UserItem(user = user)
            }
        }
        
        Button(onClick = { viewModel.loadUsers() }) {
            Text("Load Users")
        }
    }
}

// 3. Navigation Compose에서 공유
@Composable
fun NavGraph() {
    val navController = rememberNavController()
    
    NavHost(navController, startDestination = "list") {
        composable("list") { backStackEntry ->
            // Navigation 스코프의 ViewModel
            val viewModel = viewModel<UserViewModel>(
                viewModelStoreOwner = backStackEntry
            )
            UserListScreen(viewModel)
        }
        
        composable("detail/{userId}") { backStackEntry ->
            // 같은 ViewModel 공유
            val viewModel = viewModel<UserViewModel>(
                viewModelStoreOwner = navController.getBackStackEntry("list")
            )
            UserDetailScreen(viewModel)
        }
    }
}
```
