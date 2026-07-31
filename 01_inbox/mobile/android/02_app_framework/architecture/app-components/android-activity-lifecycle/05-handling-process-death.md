# 🧟‍♂️ Handling Process Death

##### 1. SavedStateHandle (권장)

ViewModel 내부에서 `SavedStateHandle` 을 쓰면, 보일러플레이트 코드 없이 프로세스 킬에 대비할 수 있습니다.

```kotlin
class MyViewModel(private val state: SavedStateHandle) : ViewModel() {
    // 값이 바뀌면 자동으로 Bundle에 저장됨
    val searchQuery = state.getLiveData("query", "")

    fun setQuery(query: String) {
        state["query"] = query
    }
}
```

##### 2. onSaveInstanceState (Old School)

단순한 View 상태(스크롤 위치, EditText 내용)는 View 시스템이 알아서 저장해 주지만, 커스텀 변수는 직접 저장해야 합니다.

```kotlin
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putInt("score", currentScore) // 1MB 제한 주의!
}
```

---
