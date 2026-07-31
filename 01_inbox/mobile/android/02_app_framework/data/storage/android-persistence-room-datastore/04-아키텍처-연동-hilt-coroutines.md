# 🏛️ 아키텍처 연동 (Hilt + Coroutines)

데이터 레이어는 언제나 캡슐화되어야 하며, UI 레이어는 `Flow` 를 통해 데이터를 관찰해야 한다.

```kotlin
class UserRepository @Inject constructor(
    private val userDao: UserDao,
    private val userPrefs: DataStore<UserPreferences>
) {
    val users: Flow<List<User>> = userDao.getAllUsers()
    val preferences: Flow<UserPreferences> = userPrefs.data
}
```
