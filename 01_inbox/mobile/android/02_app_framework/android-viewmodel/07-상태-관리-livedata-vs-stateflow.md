# 상태 관리: LiveData vs StateFlow

상위 노트: [[android-viewmodel]]

##### LiveData (Legacy)

>[!CAUTION] **Devil's Advocate : LiveData 의 한계와 레거시화**
>과거 `LiveData` 는 안드로이드 생명주기를 알아서 처리해준다는 이유로 각광받았으나, **코루틴(Flow) 생태계가 안착하면서 완전히 도태된 구시대 기술**이 되었습니다.
>비동기 연산의 한계, 메인 스레드 락 등 단점이 명확하여 구글 공식 문서에서조차 신규 개발 시 `StateFlow` 사용을 권장하고 있습니다. View 시스템이더라도 `repeatOnLifecycle` 을 사용하는 것이 표준입니다.

```kotlin
class UserViewModel : ViewModel() {
    private val _users = MutableLiveData<List<User>>()
    val users: LiveData<List<User>> = _users
    
    // Transformations
    val userCount: LiveData<Int> = Transformations.map(users) { it.size }
    
    val firstUser: LiveData<User?> = Transformations.switchMap(users) { list ->
        liveData { emit(list.firstOrNull()) }
    }
    
    // MediatorLiveData (여러 소스 결합)
    val combinedData = MediatorLiveData<String>().apply {
        addSource(users) { value = combineData() }
        addSource(posts) { value = combineData() }
    }
}
```

**장점:**

- 생명주기 자동 인식 (Activity 가 백그라운드면 업데이트 안 함)
- 메인 스레드에서만 관찰 가능
- 간단한 API

**단점:**

- 초기값 설정 불가
- 코루틴과의 통합이 약함

##### StateFlow (Compose 권장)

```kotlin
class UserViewModel : ViewModel() {
    private val _users = MutableStateFlow<List<User>>(emptyList())
    val users: StateFlow<List<User>> = _users.asStateFlow()
    
    // 초기값 필수
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
    
    // Flow 연산자 사용
    val userCount: StateFlow<Int> = users
        .map { it.size }
        .stateIn(viewModelScope, SharingStarted.Lazily, 0)
    
    // combine으로 여러 Flow 결합
    val combinedState: StateFlow<CombinedState> = combine(
        users,
        posts,
        isLoading
    ) { users, posts, loading ->
        CombinedState(users, posts, loading)
    }.stateIn(viewModelScope, SharingStarted.Lazily, CombinedState())
}

// Activity에서 수집
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.users.collect { users ->
            // STARTED 상태일 때만 수집
        }
    }
}

// Compose에서 수집
@Composable
fun UserScreen(viewModel: UserViewModel = viewModel()) {
    val users by viewModel.users.collectAsStateWithLifecycle()
    // 생명주기 인식하며 자동 수집/취소
}
```

**장점:**

- 초기값 설정 가능
- 코루틴 Flow API 활용 가능
- Compose 와 완벽 통합
- cold stream 을 hot stream 으로 변환

**단점:**

- 생명주기 자동 인식 안 함 (직접 처리 필요)
