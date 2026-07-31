# Hilt (Dependency Injection)

상위 노트: [[android-jetpack-architecture]]

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
