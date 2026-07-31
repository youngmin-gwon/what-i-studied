# SavedStateHandle

상위 노트: [android-viewmodel](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel.md)

프로세스 사망 후에도 데이터를 복원할 수 있게 해주는 기능이다. [android-process-and-memory](01_inbox/mobile/android/01_system_internals/ipc-and-process/android-process-and-memory.md) 참고.

```kotlin
class DetailViewModel(
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {
    
    // 1. 간단한 값 저장/복원
    var userId: String?
        get() = savedStateHandle.get<String>("user_id")
        set(value) = savedStateHandle.set("user_id", value)
    
    // 2. LiveData로 사용
    val userIdLiveData: LiveData<String> = savedStateHandle.getLiveData("user_id")
    
    // 3. StateFlow로 사용
    val userIdFlow: StateFlow<String?> = savedStateHandle.getStateFlow("user_id", null)
    
    // 4. 복잡한 객체도 저장 가능 (Parcelable/Serializable)
    var user: User?
        get() = savedStateHandle.get<User>("user")
        set(value) = savedStateHandle.set("user", value)
    
    fun loadUser(id: String) {
        userId = id // 자동으로 SavedStateHandle에 저장
        viewModelScope.launch {
            val result = repository.getUser(id)
            user = result // 프로세스 사망 후에도 복원됨
        }
    }
}

// Activity/Fragment에서 사용 (별도 설정 불필요)
class DetailActivity : AppCompatActivity() {
    private val viewModel: DetailViewModel by viewModels()
    // SavedStateHandle이 자동으로 주입됨
}
```

**SavedStateHandle vs onSaveInstanceState:**

| SavedStateHandle | onSaveInstanceState |
|-----------------|---------------------|
| ViewModel 내부에서 사용 | Activity/Fragment 에서 사용 |
| 자동으로 저장/복원 | 수동으로 Bundle 처리 |
| 타입 안전 | Bundle 로 타입 캐스팅 필요 |
| 권장 방식 | 레거시 방식 |
