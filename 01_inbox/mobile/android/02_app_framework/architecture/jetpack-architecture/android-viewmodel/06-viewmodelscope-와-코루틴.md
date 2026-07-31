# ViewModelScope 와 코루틴

상위 노트: [android-viewmodel](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel.md)

`viewModelScope` 는 ViewModel 의 생명주기에 맞춰 자동으로 취소되는 코루틴 스코프다.

```kotlin
class UserViewModel : ViewModel() {
    
    fun loadUsers() {
        // ✅ viewModelScope 사용 (권장)
        viewModelScope.launch {
            // ViewModel.onCleared() 시 자동 취소
            val users = repository.getUsers()
        }
    }
    
    // ❌ GlobalScope 사용 금지
    fun loadUsersWrong() {
        GlobalScope.launch {
            // 절대 취소되지 않아 메모리 누수 발생!
        }
    }
    
    // 여러 코루틴 동시 실행
    fun loadAllData() {
        viewModelScope.launch {
            val users = async { repository.getUsers() }
            val posts = async { repository.getPosts() }
            
            // 병렬 실행 후 결과 조합
            val allData = awaitAll(users, posts)
        }
    }
    
    // 에러 처리
    fun loadUsersWithErrorHandling() {
        viewModelScope.launch {
            try {
                val users = repository.getUsers()
                _users.value = users
            } catch (e: Exception) {
                _error.value = e.message
            }
        }
    }
}
```
