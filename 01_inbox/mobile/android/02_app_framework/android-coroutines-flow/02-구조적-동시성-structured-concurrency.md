# 구조적 동시성 (Structured Concurrency)

상위 노트: [[android-coroutines-flow]]

코루틴은 반드시 **CoroutineScope** 안에서 시작되어야 하며, 스코프가 취소되면 하위 코루틴도 모두 취소된다.

```kotlin
// ✅ 구조적: viewModelScope 가 ViewModel.onCleared() 시 자동 취소
class UserViewModel : ViewModel() {
    fun loadData() {
        viewModelScope.launch {
            val user = fetchUser()     // 자동 취소 대상
            val posts = fetchPosts()   // 자동 취소 대상
            _uiState.value = UiState.Success(user, posts)
        }
    }
}

// ❌ 비구조적: GlobalScope 는 취소되지 않음 → 메모리 누수
GlobalScope.launch {
    // ViewModel 이 사라져도 계속 실행됨!
}
```

##### Android 제공 Scope

| Scope | 생명주기 | 용도 |
|-------|----------|------|
| `viewModelScope` | ViewModel `onCleared()` 시 취소 | UI 상태 관리 |
| `lifecycleScope` | Activity/Fragment `DESTROYED` 시 취소 | UI 작업 |
| `repeatOnLifecycle` | STARTED↔STOPPED 반복 | Flow 수집 |
| `rememberCoroutineScope()` | Composition 이탈 시 취소 | Compose 이벤트 |
