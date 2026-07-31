# Flow

상위 노트: [[android-coroutines-flow]]

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

##### Flow 연산자

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
