# Koin (경량 DI)

상위 노트: [[android-dependency-injection]]

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
