# ViewModel 의 목적

상위 노트: [android-viewmodel](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel.md)

##### 1. 설정 변경에서 데이터 유지

화면 회전, 언어 변경 등으로 Activity 가 재생성될 때 ViewModel 의 데이터는 유지된다.

```kotlin
// ❌ 나쁜 예: Activity에서 직접 데이터 관리
class MainActivity : AppCompatActivity() {
    private var users: List<User> = emptyList() // 화면 회전 시 사라짐!
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        loadUsers() // 회전할 때마다 다시 로드
    }
}

// ✅ 좋은 예: ViewModel 사용
class UserViewModel : ViewModel() {
    private val _users = MutableLiveData<List<User>>()
    val users: LiveData<List<User>> = _users
    // 설정 변경 시에도 데이터 유지됨
}

class MainActivity : AppCompatActivity() {
    private val viewModel: UserViewModel by viewModels()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 처음 생성 시에만 로드, 이후 회전 시에는 기존 ViewModel 재사용
        if (savedInstanceState == null) {
            viewModel.loadUsers()
        }
    }
}
```

##### 2. UI 와 비즈니스 로직 분리

Activity/Fragment 는 UI 표시에만 집중하고, 데이터 로직은 ViewModel 이 담당한다.

```kotlin
class UserViewModel(
    private val repository: UserRepository
) : ViewModel() {
    // 비즈니스 로직
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
    
    fun loadUsers() {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            try {
                val users = repository.getUsers()
                _uiState.value = UiState.Success(users)
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e.message)
            }
        }
    }
}

// Activity는 UI만 담당
class UserListActivity : AppCompatActivity() {
    private val viewModel: UserViewModel by viewModels()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        lifecycleScope.launch {
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
```

##### 3. 메모리 누수 방지

Activity 가 종료되면 ViewModel 도 자동으로 정리되어 메모리 누수를 방지한다.
