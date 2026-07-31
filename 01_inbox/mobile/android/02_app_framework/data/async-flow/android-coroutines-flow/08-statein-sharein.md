# stateIn / shareIn

상위 노트: [android-coroutines-flow](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow.md)

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
| `WhileSubscribed(5000)` | 구독자 없으면 5 초 후 중단 | **권장** (회전 시 재시작 방지) |
