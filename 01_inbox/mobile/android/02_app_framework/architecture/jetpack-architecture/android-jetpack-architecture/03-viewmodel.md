# ViewModel

상위 노트: [android-jetpack-architecture](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture.md)

설정 변경에서 살아남는 UI 상태 홀더. 자세한 내용은 [android-viewmodel](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel.md) 참고.

```kotlin
class UserViewModel : ViewModel() {
    private val _users = MutableLiveData<List<User>>()
    val users: LiveData<List<User>> = _users
    
    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading
    
    fun loadUsers() {
        viewModelScope.launch {
            _isLoading.value = true
            try {
                val result = repository.getUsers()
                _users.value = result
            } catch (e: Exception) {
                // 에러 처리
            } finally {
                _isLoading.value = false
            }
        }
    }
    
    override fun onCleared() {
        super.onCleared()
        // 리소스 정리
    }
}

// Activity 에서 사용
class MainActivity : AppCompatActivity() {
    private val viewModel: UserViewModel by viewModels()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        viewModel.users.observe(this) { users ->
            // UI 업데이트
        }
        
        viewModel.loadUsers()
    }
}
```

##### SavedStateHandle (프로세스 사망 대응)

```kotlin
class DetailViewModel(
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {
    // 프로세스 사망 후에도 복원됨
    var userId: String
        get() = savedStateHandle.get<String>("user_id") ?: ""
        set(value) { savedStateHandle.set("user_id", value) }
    
    // LiveData 로도 사용 가능
    val userIdLiveData: LiveData<String> = savedStateHandle.getLiveData("user_id")
}

// Factory 없이 사용
class DetailActivity : AppCompatActivity() {
    private val viewModel: DetailViewModel by viewModels()
}
```
