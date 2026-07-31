# Repository 패턴과 함께 사용

```kotlin
// Repository
class UserRepository(
    private val api: ApiService,
    private val dao: UserDao
) {
    fun getUsers(): Flow<List<User>> = flow {
        emit(dao.getAll().first()) // 캐시 먼저
        val fresh = api.getUsers()  // 네트워크에서 최신 데이터
        dao.insertAll(fresh)
        emit(fresh)
    }
}

// ViewModel
class UserViewModel(
    private val repository: UserRepository
) : ViewModel() {
    val users: StateFlow<List<User>> = repository.getUsers()
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000),
            initialValue = emptyList()
        )
}
```
