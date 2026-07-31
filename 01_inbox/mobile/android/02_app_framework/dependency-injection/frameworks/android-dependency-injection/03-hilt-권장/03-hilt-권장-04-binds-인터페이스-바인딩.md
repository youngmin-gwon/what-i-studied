# Binds (인터페이스 바인딩)

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
