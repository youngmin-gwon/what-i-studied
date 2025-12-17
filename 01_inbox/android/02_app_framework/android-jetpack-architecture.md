---
title: android-jetpack-architecture
tags: [android, android/jetpack, android/architecture, android/viewmodel, android/room]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android Jetpack Architecture Components android android/jetpack android/architecture

Jetpack 라이브러리로 견고한 앱 아키텍처를 만드는 방법. 기본은 [[android-foundations]] 참고.

### 아키텍처 개요

**권장 아키텍처 (MVVM):**
```
UI Layer (Activity/Fragment/Compose)
    ↓
ViewModel (UI 상태 관리)
    ↓
Repository (데이터 소스 추상화)
    ↓
Data Sources (Room, Retrofit, DataStore)
```

### ViewModel

설정 변경에서 살아남는 UI 상태 홀더. 자세한 내용은 [[android-viewmodel]] 참고.

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

#### SavedStateHandle (프로세스 사망 대응)

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

### LiveData

생명주기를 인식하는 Observable 데이터 홀더.

```kotlin
// MutableLiveData 생성
private val _counter = MutableLiveData<Int>(0)
val counter: LiveData<Int> = _counter

// 값 업데이트
_counter.value = 1 // 메인 스레드
_counter.postValue(1) // 백그라운드 스레드

// 관찰
counter.observe(viewLifecycleOwner) { value ->
    textView.text = value.toString()
}

// Transformations
val doubledCounter: LiveData<Int> = Transformations.map(counter) { it * 2 }

val userLiveData: LiveData<User> = Transformations.switchMap(userIdLiveData) { id ->
    repository.getUserById(id)
}

// MediatorLiveData (여러 소스 결합)
val combined = MediatorLiveData<String>().apply {
    addSource(liveData1) { value = combineValues() }
    addSource(liveData2) { value = combineValues() }
}
```

### StateFlow (Kotlin Coroutines)

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

### Room Database

이미 [[android-storage-systems]] 에서 다뤘으나 추가 기능 소개.

#### 관계 (Relation)

```kotlin
// 일대다 관계
@Entity
data class User(
    @PrimaryKey val userId: Int,
    val name: String
)

@Entity
data class Post(
    @PrimaryKey val postId: Int,
    val userId: Int,
    val title: String
)

data class UserWithPosts(
    @Embedded val user: User,
    @Relation(
        parentColumn = "userId",
        entityColumn = "userId"
    )
    val posts: List<Post>
)

@Dao
interface UserDao {
    @Transaction
    @Query("SELECT * FROM User")
    fun getUsersWithPosts(): Flow<List<UserWithPosts>>
}
```

#### Migration

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(database: SupportSQLiteDatabase) {
        database.execSQL("ALTER TABLE User ADD COLUMN email TEXT")
    }
}

val db = Room.databaseBuilder(context, AppDatabase::class.java, "app_db")
    .addMigrations(MIGRATION_1_2)
    .build()
```

#### FTS (Full-Text Search)

```kotlin
@Entity
@Fts4
data class Article(
    @PrimaryKey @ColumnInfo(name = "rowid") val id: Int,
    val title: String,
    val content: String
)

@Dao
interface ArticleDao {
    @Query("SELECT * FROM Article WHERE Article MATCH :query")
    fun search(query: String): Flow<List<Article>>
}
```

### WorkManager

지연 가능한 백그라운드 작업 스케줄링.

```kotlin
// Worker 정의
class UploadWorker(
    context: Context,
    params: WorkerParameters
) : CoroutineWorker(context, params) {
    
    override suspend fun doWork(): Result {
        val imageUri = inputData.getString("image_uri") ?: return Result.failure()
        
        return try {
            uploadImage(imageUri)
            Result.success()
        } catch (e: Exception) {
            if (runAttemptCount < 3) {
                Result.retry()
            } else {
                Result.failure()
            }
        }
    }
    
    private suspend fun uploadImage(uri: String) {
        // 업로드 로직
        setProgress(workDataOf("progress" to 50))
    }
}

// 작업 예약
val uploadRequest = OneTimeWorkRequestBuilder<UploadWorker>()
    .setInputData(workDataOf("image_uri" to uri.toString()))
    .setConstraints(
        Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .setRequiresBatteryNotLow(true)
            .build()
    )
    .setBackoffCriteria(
        BackoffPolicy.EXPONENTIAL,
        10, TimeUnit.SECONDS
    )
    .build()

WorkManager.getInstance(context).enqueue(uploadRequest)

// 진행 상황 관찰
WorkManager.getInstance(context)
    .getWorkInfoByIdLiveData(uploadRequest.id)
    .observe(this) { workInfo ->
        if (workInfo.state == WorkInfo.State.RUNNING) {
            val progress = workInfo.progress.getInt("progress", 0)
            progressBar.progress = progress
        }
    }
```

#### 주기적 작업

```kotlin
val periodicWork = PeriodicWorkRequestBuilder<SyncWorker>(
    15, TimeUnit.MINUTES // 최소 15분
).build()

WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "sync",
    ExistingPeriodicWorkPolicy.KEEP,
    periodicWork
)
```

#### 작업 체인

```kotlin
val cleanup = OneTimeWorkRequestBuilder<CleanupWorker>().build()
val download = OneTimeWorkRequestBuilder<DownloadWorker>().build()
val process = OneTimeWorkRequestBuilder<ProcessWorker>().build()

WorkManager.getInstance(context)
    .beginWith(cleanup)
    .then(download)
    .then(process)
    .enqueue()
```

### Navigation Component

화면 간 이동을 선언적으로 관리.

```xml
<!-- res/navigation/nav_graph.xml -->
<navigation
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    app:startDestination="@id/homeFragment">
    
    <fragment
        android:id="@+id/homeFragment"
        android:name="com.example.HomeFragment">
        <action
            android:id="@+id/action_home_to_detail"
            app:destination="@id/detailFragment"
            app:enterAnim="@anim/slide_in_right"
            app:exitAnim="@anim/slide_out_left" />
    </fragment>
    
    <fragment
        android:id="@+id/detailFragment"
        android:name="com.example.DetailFragment">
        <argument
            android:name="userId"
            app:argType="string" />
    </fragment>
</navigation>
```

```kotlin
// Activity 에 NavHost 설정
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val navController = findNavController(R.id.nav_host_fragment)
        setupActionBarWithNavController(navController)
    }
    
    override fun onSupportNavigateUp(): Boolean {
        return findNavController(R.id.nav_host_fragment).navigateUp()
    }
}

// Fragment 에서 이동
class HomeFragment : Fragment() {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        button.setOnClickListener {
            val action = HomeFragmentDirections.actionHomeToDetail("user123")
            findNavController().navigate(action)
        }
    }
}

// Safe Args 로 인자 받기
class DetailFragment : Fragment() {
    private val args: DetailFragmentArgs by navArgs()
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val userId = args.userId
        // 사용
    }
}
```

### Paging 3

대량 데이터를 효율적으로 로드.

```kotlin
// PagingSource
class UserPagingSource(
    private val api: ApiService
) : PagingSource<Int, User>() {
    
    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, User> {
        return try {
            val page = params.key ?: 1
            val response = api.getUsers(page, params.loadSize)
            
            LoadResult.Page(
                data = response.users,
                prevKey = if (page == 1) null else page - 1,
                nextKey = if (response.users.isEmpty()) null else page + 1
            )
        } catch (e: Exception) {
            LoadResult.Error(e)
        }
    }
    
    override fun getRefreshKey(state: PagingState<Int, User>): Int? {
        return state.anchorPosition?.let { anchorPosition ->
            state.closestPageToPosition(anchorPosition)?.prevKey?.plus(1)
                ?: state.closestPageToPosition(anchorPosition)?.nextKey?.minus(1)
        }
    }
}

// Repository
class UserRepository(private val api: ApiService) {
    fun getUsersPaged(): Flow<PagingData<User>> {
        return Pager(
            config = PagingConfig(
                pageSize = 20,
                enablePlaceholders = false,
                prefetchDistance = 5
            ),
            pagingSourceFactory = { UserPagingSource(api) }
        ).flow
    }
}

// ViewModel
class UserViewModel(private val repository: UserRepository) : ViewModel() {
    val users: Flow<PagingData<User>> = repository.getUsersPaged()
        .cachedIn(viewModelScope)
}

// Adapter
class UserAdapter : PagingDataAdapter<User, UserViewHolder>(USER_COMPARATOR) {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserViewHolder {
        // ViewHolder 생성
    }
    
    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        val user = getItem(position)
        holder.bind(user)
    }
    
    companion object {
        private val USER_COMPARATOR = object : DiffUtil.ItemCallback<User>() {
            override fun areItemsTheSame(oldItem: User, newItem: User) =
                oldItem.id == newItem.id
            
            override fun areContentsTheSame(oldItem: User, newItem: User) =
                oldItem == newItem
        }
    }
}

// Fragment 에서 사용
class UserListFragment : Fragment() {
    private val viewModel: UserViewModel by viewModels()
    private val adapter = UserAdapter()
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        recyclerView.adapter = adapter
        
        lifecycleScope.launch {
            viewModel.users.collectLatest { pagingData ->
                adapter.submitData(pagingData)
            }
        }
        
        // 로딩 상태 표시
        adapter.addLoadStateListener { loadState ->
            progressBar.isVisible = loadState.refresh is LoadState.Loading
            errorText.isVisible = loadState.refresh is LoadState.Error
        }
    }
}
```

### Hilt (Dependency Injection)

```kotlin
// Application
@HiltAndroidApp
class MyApplication : Application()

// Module
@Module
@InstallIn(SingletonComponent::class)
object AppModule {
    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext context: Context): AppDatabase {
        return Room.databaseBuilder(context, AppDatabase::class.java, "app_db")
            .build()
    }
    
    @Provides
    fun provideUserDao(database: AppDatabase): UserDao {
        return database.userDao()
    }
}

// Repository
class UserRepository @Inject constructor(
    private val userDao: UserDao,
    private val api: ApiService
) {
    fun getUsers(): Flow<List<User>> = userDao.getAll()
}

// ViewModel
@HiltViewModel
class UserViewModel @Inject constructor(
    private val repository: UserRepository
) : ViewModel() {
    val users = repository.getUsers()
        .stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
}

// Activity
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    private val viewModel: UserViewModel by viewModels()
}

// Fragment
@AndroidEntryPoint
class UserFragment : Fragment() {
    private val viewModel: UserViewModel by viewModels()
}
```

### Lifecycle

생명주기를 인식하는 컴포넌트.

```kotlin
class MyObserver : DefaultLifecycleObserver {
    override fun onCreate(owner: LifecycleOwner) {
        // Activity/Fragment onCreate 시
    }
    
    override fun onStart(owner: LifecycleOwner) {
        // onStart 시
    }
    
    override fun onResume(owner: LifecycleOwner) {
        // onResume 시
    }
    
    override fun onPause(owner: LifecycleOwner) {
        // onPause 시
    }
    
    override fun onStop(owner: LifecycleOwner) {
        // onStop 시
    }
    
    override fun onDestroy(owner: LifecycleOwner) {
        // onDestroy 시
    }
}

// 사용
class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        lifecycle.addObserver(MyObserver())
    }
}

// 커스텀 LifecycleOwner
class MyLocationManager(private val context: Context) : LifecycleObserver {
    @OnLifecycleEvent(Lifecycle.Event.ON_START)
    fun startLocationUpdates() {
        // 위치 업데이트 시작
    }
    
    @OnLifecycleEvent(Lifecycle.Event.ON_STOP)
    fun stopLocationUpdates() {
        // 위치 업데이트 중지
    }
}
```

### DataBinding

XML 에서 직접 데이터 바인딩.

```xml
<!-- layout.xml -->
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <data>
        <variable
            name="viewModel"
            type="com.example.UserViewModel" />
    </data>
    
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{viewModel.userName}" />
        
        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="@{() -> viewModel.loadUser()}"
            android:text="Load" />
    </LinearLayout>
</layout>
```

```kotlin
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private val viewModel: UserViewModel by viewModels()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        binding.viewModel = viewModel
        binding.lifecycleOwner = this
    }
}
```

### 아키텍처 패턴

#### Repository Pattern

```kotlin
class UserRepository(
    private val localDataSource: UserDao,
    private val remoteDataSource: ApiService
) {
    fun getUsers(): Flow<List<User>> = flow {
        // 로컬 데이터 먼저 방출
        emit(localDataSource.getAll().first())
        
        // 네트워크에서 최신 데이터 가져오기
        try {
            val remoteUsers = remoteDataSource.getUsers()
            localDataSource.insertAll(remoteUsers)
            emit(remoteUsers)
        } catch (e: Exception) {
            // 네트워크 실패 시 로컬 데이터 유지
        }
    }
}
```

#### Use Case Pattern

```kotlin
class GetUserUseCase(private val repository: UserRepository) {
    operator fun invoke(userId: String): Flow<User> {
        return repository.getUserById(userId)
    }
}

class UserViewModel(
    private val getUserUseCase: GetUserUseCase
) : ViewModel() {
    fun loadUser(userId: String) {
        viewModelScope.launch {
            getUserUseCase(userId).collect { user ->
                // 처리
            }
        }
    }
}
```

### 더 보기

[[android-viewmodel]], [[android-compose-internals]], [[android-app-components-deep-dive]], [[android-storage-systems]], [[android-dependency-injection]], [[android-testing-and-quality]]
