# UI 상태를 SharedFlow로 관리

```kotlin
// 화면 상태에는 부적합
private val _uiState = MutableSharedFlow<HomeUiState>()
```

화면 상태는 최신값이 항상 있어야 합니다. `StateFlow`를 쓰는 것이 맞습니다.
