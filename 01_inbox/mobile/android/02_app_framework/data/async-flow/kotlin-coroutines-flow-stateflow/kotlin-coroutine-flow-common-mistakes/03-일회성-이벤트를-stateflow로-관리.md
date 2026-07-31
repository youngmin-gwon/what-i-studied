# 일회성 이벤트를 StateFlow로 관리

```kotlin
// 화면 회전 후 Snackbar가 다시 뜰 수 있음
data class UiState(
    val snackbarMessage: String? = null,
)
```

이 방식은 상태 복원이나 재구독 시 이벤트가 다시 처리될 수 있습니다. Snackbar, Toast, Navigation은 `SharedFlow`나 `Channel`로 분리하는
편이 안전합니다.
