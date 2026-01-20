---
title: android-dependency-injection
tags: [android, android/dagger, android/di, android/hilt]
aliases: []
date modified: 2026-01-20 15:55:38 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Dependency Injection android android/di android/hilt

Hilt, Dagger, Koin 을 사용한 의존성 주입. 기본은 [android-jetpack-architecture](android-jetpack-architecture.md) 참고.

### 의존성 주입이란

객체가 필요로 하는 의존성을 외부에서 제공하는 패턴.

```kotlin
// ❌ 나쁜 예: 직접 생성 (강한 결합)
class UserRepository {
    private val api = RetrofitClient.create() // 테스트 어려움
}

// ✅ 좋은 예: 의존성 주입 (느슨한 결합)
class UserRepository(
    private val api: ApiService // 외부에서 주입
) {
    // 테스트 시 Mock 주입 가능
}
```

### Hilt (권장)

Dagger 기반의 Android 전용 DI 프레임워크.

#### 설정

```kotlin
// build.gradle.kts (프로젝트)
plugins {
    id("com.google.dagger.hilt.android") version "2.48" apply false
}

// build.gradle.kts (앱)
plugins {
    id("com.google.dagger.hilt.android")
    id("kotlin-kapt")
}

dependencies {
    implementation("com.google.dagger:hilt-android:2.48")
    kapt("com.google.dagger:hilt-compiler:2.48")
    
    // ViewModel
    implementation("androidx.hilt:hilt-navigation-compose:1.1.0")
    
    // WorkManager
    implementation("androidx.hilt:hilt-work:1.1.0")
    kapt("androidx.hilt:hilt-compiler:1.1.0")
}
```

#### Application 설정

```kotlin
@HiltAndroidApp
class MyApplication : Application()
```

#### Module 정의

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    
    @Provides
    @Singleton
    fun provideOkHttpClient(): OkHttpClient {
        return OkHttpClient.Builder()
            .addInterceptor(HttpLoggingInterceptor().apply {
                level = HttpLoggingInterceptor.Level.BODY
            })
            .connectTimeout(30, TimeUnit.SECONDS)
            .build()
    }
    
    @Provides
    @Singleton
    fun provideRetrofit(okHttpClient: OkHttpClient): Retrofit {
        return Retrofit.Builder()
            .baseUrl("https://api.example.com")
            .client(okHttpClient)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }
    
    @Provides
    @Singleton
    fun provideApiService(retrofit: Retrofit): ApiService {
        return retrofit.create(ApiService::class.java)
    }
}

@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {
    
    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext context: Context): AppDatabase {
        return Room.databaseBuilder(
            context,
            AppDatabase::class.java,
            "app_database"
        ).build()
    }
    
    @Provides
    fun provideUserDao(database: AppDatabase): UserDao {
        return database.userDao()
    }
}
```

#### Binds (인터페이스 바인딩)

```kotlin
interface UserRepository {
    suspend fun getUsers(): List<User>
}

class UserRepositoryImpl @Inject constructor(
    private val api: ApiService,
    private val userDao: UserDao
) : UserRepository {
    override suspend fun getUsers(): List<User> {
        return api.getUsers()
    }
}

@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    
    @Binds
    @Singleton
    abstract fun bindUserRepository(
        impl: UserRepositoryImpl
    ): UserRepository
}
```

#### Qualifiers (같은 타입 구분)

```kotlin
@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class IoDispatcher

@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class MainDispatcher

@Module
@InstallIn(SingletonComponent::class)
object DispatcherModule {
    
    @Provides
    @IoDispatcher
    fun provideIoDispatcher(): CoroutineDispatcher = Dispatchers.IO
    
    @Provides
    @MainDispatcher
    fun provideMainDispatcher(): CoroutineDispatcher = Dispatchers.Main
}

// 사용
class UserRepository @Inject constructor(
    @IoDispatcher private val ioDispatcher: CoroutineDispatcher
) {
    suspend fun loadUsers() = withContext(ioDispatcher) {
        // IO 작업
    }
}
```

#### Component Scopes

| Component | Scope | 생명주기 |
|-----------|-------|---------|
| SingletonComponent | @Singleton | Application |
| ActivityRetainedComponent | @ActivityRetainedScoped | Activity (설정 변경 유지) |
| ViewModelComponent | @ViewModelScoped | ViewModel |
| ActivityComponent | @ActivityScoped | Activity |
| FragmentComponent | @FragmentScoped | Fragment |
| ViewComponent | @ViewScoped | View |
| ServiceComponent | @ServiceScoped | Service |

```kotlin
@Module
@InstallIn(ViewModelComponent::class)
object ViewModelModule {
    
    @Provides
    @ViewModelScoped
    fun provideAnalytics(): Analytics {
        return Analytics() // ViewModel 생명주기
    }
}
```

#### Activity/Fragment 주입

```kotlin
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    
    @Inject
    lateinit var analytics: Analytics
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        analytics.logEvent("MainActivity_Created")
    }
}

@AndroidEntryPoint
class UserFragment : Fragment() {
    
    @Inject
    lateinit var userRepository: UserRepository
    
    private val viewModel: UserViewModel by viewModels()
}
```

#### ViewModel 주입

```kotlin
@HiltViewModel
class UserViewModel @Inject constructor(
    private val repository: UserRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {
    
    val users = repository.getUsers()
        .stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
}

// Activity/Fragment 에서 사용
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    private val viewModel: UserViewModel by viewModels()
}
```

#### WorkManager 주입

```kotlin
@HiltWorker
class UploadWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    private val repository: UploadRepository
) : CoroutineWorker(context, params) {
    
    override suspend fun doWork(): Result {
        return try {
            repository.upload()
            Result.success()
        } catch (e: Exception) {
            Result.failure()
        }
    }
}

// Application 에 HiltWorkerFactory 설정
@HiltAndroidApp
class MyApplication : Application(), Configuration.Provider {
    
    @Inject
    lateinit var workerFactory: HiltWorkerFactory
    
    override fun getWorkManagerConfiguration() =
        Configuration.Builder()
            .setWorkerFactory(workerFactory)
            .build()
}
```

#### Entry Point (Hilt 가 관리하지 않는 클래스)

```kotlin
@EntryPoint
@InstallIn(SingletonComponent::class)
interface AnalyticsEntryPoint {
    fun analytics(): Analytics
}

class CustomContentProvider : ContentProvider() {
    
    private val analytics: Analytics by lazy {
        val appContext = context?.applicationContext ?: throw IllegalStateException()
        val hiltEntryPoint = EntryPointAccessors.fromApplication(
            appContext,
            AnalyticsEntryPoint::class.java
        )
        hiltEntryPoint.analytics()
    }
    
    override fun onCreate(): Boolean {
        analytics.logEvent("ContentProvider_Created")
        return true
    }
}
```

### Dagger (수동 설정)

Hilt 보다 유연하지만 복잡함.

```kotlin
// Component
@Singleton
@Component(modules = [AppModule::class, NetworkModule::class])
interface AppComponent {
    fun inject(activity: MainActivity)
    
    @Component.Factory
    interface Factory {
        fun create(@BindsInstance application: Application): AppComponent
    }
}

// Module
@Module
class AppModule {
    
    @Provides
    @Singleton
    fun provideContext(application: Application): Context {
        return application.applicationContext
    }
}

// Application
class MyApplication : Application() {
    val appComponent: AppComponent by lazy {
        DaggerAppComponent.factory().create(this)
    }
}

// Activity
class MainActivity : AppCompatActivity() {
    
    @Inject
    lateinit var analytics: Analytics
    
    override fun onCreate(savedInstanceState: Bundle?) {
        (application as MyApplication).appComponent.inject(this)
        super.onCreate(savedInstanceState)
    }
}

// Subcomponent (Activity Scope)
@ActivityScope
@Subcomponent(modules = [ActivityModule::class])
interface ActivityComponent {
    fun inject(activity: MainActivity)
    
    @Subcomponent.Factory
    interface Factory {
        fun create(): ActivityComponent
    }
}

@Module(subcomponents = [ActivityComponent::class])
object SubcomponentModule
```

### Koin (경량 DI)

리플렉션 기반, 간단하지만 컴파일 타임 검증 없음.

```kotlin
// build.gradle.kts
dependencies {
    implementation("io.insert-koin:koin-android:3.5.0")
    implementation("io.insert-koin:koin-androidx-compose:3.5.0")
}

// Module 정의
val networkModule = module {
    single {
        OkHttpClient.Builder()
            .addInterceptor(HttpLoggingInterceptor())
            .build()
    }
    
    single {
        Retrofit.Builder()
            .baseUrl("https://api.example.com")
            .client(get())
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }
    
    single { get<Retrofit>().create(ApiService::class.java) }
}

val repositoryModule = module {
    single<UserRepository> { UserRepositoryImpl(get(), get()) }
}

val viewModelModule = module {
    viewModel { UserViewModel(get()) }
}

// Application
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        startKoin {
            androidLogger()
            androidContext(this@MyApplication)
            modules(networkModule, repositoryModule, viewModelModule)
        }
    }
}

// Activity
class MainActivity : AppCompatActivity() {
    private val analytics: Analytics by inject()
    private val viewModel: UserViewModel by viewModel()
}

// Compose
@Composable
fun UserScreen() {
    val viewModel: UserViewModel = koinViewModel()
}
```

### 테스트

#### Hilt 테스트

```kotlin
// build.gradle.kts
dependencies {
    androidTestImplementation("com.google.dagger:hilt-android-testing:2.48")
    kaptAndroidTest("com.google.dagger:hilt-compiler:2.48")
}

// 테스트
@HiltAndroidTest
class UserRepositoryTest {
    
    @get:Rule
    var hiltRule = HiltAndroidRule(this)
    
    @Inject
    lateinit var repository: UserRepository
    
    @Before
    fun init() {
        hiltRule.inject()
    }
    
    @Test
    fun testGetUsers() = runTest {
        val users = repository.getUsers()
        assertThat(users).isNotEmpty()
    }
}

// 모듈 교체
@Module
@TestInstallIn(
    components = [SingletonComponent::class],
    replaces = [NetworkModule::class]
)
object FakeNetworkModule {
    
    @Provides
    @Singleton
    fun provideFakeApiService(): ApiService {
        return FakeApiService()
    }
}
```

#### Koin 테스트

```kotlin
class UserRepositoryTest : KoinTest {
    
    @get:Rule
    val koinTestRule = KoinTestRule.create {
        modules(testModule)
    }
    
    private val repository: UserRepository by inject()
    
    @Test
    fun testGetUsers() = runTest {
        val users = repository.getUsers()
        assertThat(users).isNotEmpty()
    }
}

val testModule = module {
    single<ApiService> { FakeApiService() }
    single<UserRepository> { UserRepositoryImpl(get()) }
}
```

### 비교

| 특징 | Hilt | Dagger | Koin |
|------|------|--------|------|
| 학습 곡선 | 중간 | 높음 | 낮음 |
| 컴파일 타임 검증 | ✅ | ✅ | ❌ |
| 성능 | 빠름 | 빠름 | 약간 느림 |
| Android 통합 | 최고 | 수동 | 좋음 |
| 보일러플레이트 | 적음 | 많음 | 매우 적음 |
| 권장 사용 | 대부분의 앱 | 복잡한 앱 | 간단한 앱 |

### 더 보기

[android-jetpack-architecture](android-jetpack-architecture.md), [android-testing-and-quality](../06_testing_performance/android-testing-and-quality.md), [android-gradle-build-system](android-gradle-build-system.md)
