# [[mobile-security]] > [[android-coroutines-flow]]

## Coroutines & Flow: Asynchronous Mastery

Kotlin **Coroutines**와 **Flow**를 활용한 안드로이드의 비동기 프로그래밍 모델을 심층 분석합니다. 

단순히 스레드를 바꾸는 도구를 넘어, 어떻게 하면 복잡한 비즈니스 로직을 동기 코드처럼 간결하게 유지하면서도 선언적으로 데이터 스트림을 관리할 수 있을지 이해하는 것이 목표입니다.

---

### 💡 Context: Kotlin Coroutines vs Swift Concurrency

비동기 처리의 현대적인 패러다임은 플랫폼마다 유사하지만 명확한 차이가 있습니다. Kotlin의 `suspend`는 Swift의 `async`와 대응되며, `Flow`는 `AsyncSequence`와 많은 개념을 공유합니다.

> [!NOTE] **상호 참조**
> Swift의 비동기 모델은 [[apple-swift-concurrency]]를 참고하세요.

---

### 구조적 동시성 (Structured Concurrency)

코루틴은 반드시 **CoroutineScope** 안에서 시작되어야 하며, 스코프가 취소되면 하위 코루틴도 모두 취소된다.

```kotlin
// ✅ 구조적: viewModelScope 가 ViewModel.onCleared() 시 자동 취소
class UserViewModel : ViewModel() {
    fun loadData() {
        viewModelScope.launch {
            val user = fetchUser()     // 자동 취소 대상
            val posts = fetchPosts()   // 자동 취소 대상
            _uiState.value = UiState.Success(user, posts)
        }
    }
}

// ❌ 비구조적: GlobalScope 는 취소되지 않음 → 메모리 누수
GlobalScope.launch {
    // ViewModel 이 사라져도 계속 실행됨!
}
```

#### Android 제공 Scope

| Scope | 생명주기 | 용도 |
|-------|----------|------|
| `viewModelScope` | ViewModel `onCleared()` 시 취소 | UI 상태 관리 |
| `lifecycleScope` | Activity/Fragment `DESTROYED` 시 취소 | UI 작업 |
| `repeatOnLifecycle` | STARTED↔STOPPED 반복 | Flow 수집 |
| `rememberCoroutineScope()` | Composition 이탈 시 취소 | Compose 이벤트 |

### Dispatchers

```kotlin
viewModelScope.launch {
    // 기본: Dispatchers.Main (UI 스레드)
    _isLoading.value = true
    
    val result = withContext(Dispatchers.IO) {
        // IO 스레드 풀: 네트워크, DB, 파일 I/O
        repository.fetchFromNetwork()
    }
    
    val processed = withContext(Dispatchers.Default) {
        // CPU 집약적 작업: 정렬, 파싱, 암호화
        processLargeData(result)
    }
    
    // 다시 Main 으로 자동 복귀
    _uiState.value = UiState.Success(processed)
}
```

| Dispatcher | 스레드 수 | 용도 |
|------------|-----------|------|
| `Main` | 1 (UI 스레드) | UI 업데이트, StateFlow 방출 |
| `IO` | 64+ (탄력적) | 네트워크, DB, 파일 |
| `Default` | CPU 코어 수 | 정렬, JSON 파싱, 암호화 |
| `Unconfined` | 호출 스레드 → 재개 스레드 | 테스트 용도 (실 사용 지양) |

### 예외 처리

```kotlin
// 1. try-catch (가장 일반적)
viewModelScope.launch {
    try {
        val user = repository.getUser(id)
        _uiState.value = UiState.Success(user)
    } catch (e: HttpException) {
        _uiState.value = UiState.Error("서버 오류: ${e.code()}")
    } catch (e: IOException) {
        _uiState.value = UiState.Error("네트워크 연결을 확인하세요")
    }
}

// 2. CoroutineExceptionHandler (최상위 핸들러)
val handler = CoroutineExceptionHandler { _, throwable ->
    Log.e("Coroutine", "Uncaught exception", throwable)
    _uiState.value = UiState.Error(throwable.message)
}

viewModelScope.launch(handler) {
    riskyOperation()
}

// 3. SupervisorJob (자식 실패가 부모/형제에 전파되지 않음)
viewModelScope.launch {
    supervisorScope {
        launch { fetchUser() }     // 실패해도
        launch { fetchPosts() }    // 이것은 계속 실행
    }
}
```

> [!WARNING] **`launch` vs `async` 예외 전파 차이**
> - `launch`: 예외가 **즉시 부모로 전파** → try-catch 가 launch 블록 **내부** 에 있어야 함
> - `async`: 예외가 `await()` 호출 시 **던져짐** → await 지점에서 catch 가능

### 병렬 실행

```kotlin
viewModelScope.launch {
    // ✅ 병렬 실행 (async + awaitAll)
    val userDeferred = async { repository.getUser(id) }
    val postsDeferred = async { repository.getPosts(id) }
    
    val user = userDeferred.await()
    val posts = postsDeferred.await()
    // 또는: val (user, posts) = awaitAll(userDeferred, postsDeferred)
    
    _uiState.value = UiState.Success(user, posts)
}

// ❌ 순차 실행 (느림)
viewModelScope.launch {
    val user = repository.getUser(id)   // 1초
    val posts = repository.getPosts(id) // 1초
    // 총 2초
}
```

### Flow

Cold Stream: 수집(collect)할 때만 데이터를 생산한다.

```kotlin
// Repository 에서 Flow 반환
class UserRepository(private val dao: UserDao) {
    fun getUsers(): Flow<List<User>> = dao.getAllUsers()  // Room 이 자동 Flow 지원
    
    fun searchUsers(query: String): Flow<List<User>> = flow {
        val cached = dao.search(query)
        emit(cached)                    // 로컬 캐시 먼저
        
        val fresh = api.search(query)   // 네트워크
        dao.insertAll(fresh)
        emit(fresh)                     // 최신 데이터
    }.flowOn(Dispatchers.IO)            // 생산은 IO 에서
}
```

#### Flow 연산자

```kotlin
repository.getUsers()
    .map { users -> users.filter { it.isActive } }      // 변환
    .distinctUntilChanged()                                // 변경 시에만
    .debounce(300)                                         // 300ms 디바운스
    .catch { e -> emit(emptyList()) }                      // 에러 처리
    .onEach { users -> analytics.log("users: ${users.size}") }
    .flowOn(Dispatchers.IO)                                // 위 연산자는 IO 에서
    .collect { users ->                                    // 수집은 Main 에서
        updateUI(users)
    }
```

### StateFlow vs SharedFlow

| 특성 | StateFlow | SharedFlow |
|------|-----------|------------|
| 초기값 | **필수** | 불필요 |
| 최신 값 보관 | `.value` 로 즉시 접근 | `replay` 설정 시 |
| 동일 값 방출 | **무시** (distinctUntilChanged) | 허용 |
| 구독자 없을 때 | 값 유지 | 설정에 따라 |
| **용도** | **UI 상태** (Loading, Success, Error) | **이벤트** (토스트, 네비게이션) |

```kotlin
class UserViewModel : ViewModel() {
    // ✅ UI 상태: StateFlow
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
    
    // ✅ 일회성 이벤트: SharedFlow 또는 Channel
    private val _events = MutableSharedFlow<UiEvent>()
    val events: SharedFlow<UiEvent> = _events.asSharedFlow()
    
    // Channel 방식 (이벤트가 반드시 소비되어야 할 때)
    private val _navEvents = Channel<NavEvent>()
    val navEvents = _navEvents.receiveAsFlow()
    
    fun navigateToDetail(id: String) {
        viewModelScope.launch {
            _navEvents.send(NavEvent.GoToDetail(id))
        }
    }
}
```

### stateIn / shareIn

Cold Flow 를 Hot Flow 로 변환한다.

```kotlin
class UserViewModel(repository: UserRepository) : ViewModel() {
    val users: StateFlow<List<User>> = repository.getUsers()
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5_000), // 5초간 구독자 없으면 중단
            initialValue = emptyList()
        )
    
    val searchResults: StateFlow<List<User>> = searchQuery
        .debounce(300)
        .flatMapLatest { query -> repository.searchUsers(query) }
        .stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
}
```

**SharingStarted 전략:**

| 전략 | 동작 | 용도 |
|------|------|------|
| `Eagerly` | 즉시 시작, 스코프 종료까지 | 항상 최신 데이터 필요 |
| `Lazily` | 첫 구독자 등장 시 시작 | 지연 로딩 |
| `WhileSubscribed(5000)` | 구독자 없으면 5초 후 중단 | **권장** (회전 시 재시작 방지) |

### UI 에서 Flow 수집

#### View 시스템

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

#### Compose

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

### callbackFlow

콜백 기반 API 를 Flow 로 변환한다.

```kotlin
fun locationUpdates(): Flow<Location> = callbackFlow {
    val locationManager = context.getSystemService<LocationManager>()
    val listener = object : LocationListener {
        override fun onLocationChanged(location: Location) {
            trySend(location)  // 콜백 → Flow
        }
    }
    
    locationManager?.requestLocationUpdates(
        LocationManager.GPS_PROVIDER, 1000L, 0f, listener
    )
    
    awaitClose {
        // Flow 가 취소될 때 정리
        locationManager?.removeUpdates(listener)
    }
}

// 사용
viewModelScope.launch {
    locationUpdates()
        .conflate()  // 처리 못 한 이전 값은 버림
        .collect { location ->
            _currentLocation.value = location
        }
}
```

### 테스팅

```kotlin
class UserViewModelTest {
    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()  // TestDispatcher
    
    @Test
    fun `loadUsers emits success state`() = runTest {
        // Given
        val fakeRepository = FakeUserRepository()
        val viewModel = UserViewModel(fakeRepository)
        
        // When
        viewModel.loadUsers()
        
        // Then
        val state = viewModel.uiState.value
        assertThat(state).isInstanceOf(UiState.Success::class.java)
    }
    
    @Test
    fun `flow emits correct sequence`() = runTest {
        val flow = flowOf(1, 2, 3)
        val results = flow.toList()
        assertThat(results).isEqualTo(listOf(1, 2, 3))
    }
}

// TestDispatcher Rule
class MainDispatcherRule(
    val dispatcher: TestDispatcher = UnconfinedTestDispatcher()
) : TestWatcher() {
    override fun starting(description: Description) {
        Dispatchers.setMain(dispatcher)
    }
    override fun finished(description: Description) {
        Dispatchers.resetMain()
    }
}
```

### 🔗 연관 문서 및 심화 학습
- [[android-viewmodel]] - UI 상태 관리와 생명주기 인식
- [[android-jetpack-architecture]] - 권장 아키텍처 가이드라인
- [[android-compose-internals]] - 선언형 UI에서의 상태 변경 및 재구성
- [[android-testing-and-quality]] - 코루틴 및 Flow 단위 테스트 기법
