# 자주 하는 실수

상위 노트: [[kotlin-coroutines-flow-stateflow]]

### 8-1. ViewModel에서 Flow를 만들고 아무도 collect하지 않음

```kotlin
// collect 또는 stateIn이 없으면 실행되지 않음
repository.observeBenefits()
    .map { benefits -> BenefitUiState.Ready(benefits) }
```

Flow는 대부분 Cold입니다. `collect`, `stateIn`, `shareIn` 같은 최종 동작이 있어야 실제로 흐릅니다.

### 8-2. UI 상태를 SharedFlow로 관리

```kotlin
// 화면 상태에는 부적합
private val _uiState = MutableSharedFlow<HomeUiState>()
```

화면 상태는 최신값이 항상 있어야 합니다. `StateFlow`를 쓰는 것이 맞습니다.

### 8-3. 일회성 이벤트를 StateFlow로 관리

```kotlin
// 화면 회전 후 Snackbar가 다시 뜰 수 있음
data class UiState(
    val snackbarMessage: String? = null,
)
```

이 방식은 상태 복원이나 재구독 시 이벤트가 다시 처리될 수 있습니다. Snackbar, Toast, Navigation은 `SharedFlow`나 `Channel`로 분리하는
편이 안전합니다.

### 8-4. Coroutine 취소를 고려하지 않음

Coroutine은 취소될 수 있습니다. 특히 화면이 사라지거나 새 검색어가 들어오면 이전 작업이 취소되는 것이 정상입니다.

긴 루프를 직접 돌린다면 취소 가능 지점을 고려해야 합니다.

```kotlin
while (isActive) {
    syncOnce()
    delay(60_000)
}
```

### 8-5. 무거운 작업을 Main Dispatcher에서 실행

```kotlin
// 대량 JSON 파싱이나 파일 작업을 Main에서 직접 실행하지 않기
viewModelScope.launch {
    val text = file.readText()
    _uiState.value = UiState(text)
}
```

```kotlin
// I/O 작업은 IO Dispatcher로 이동
viewModelScope.launch {
    val text = withContext(Dispatchers.IO) {
        file.readText()
    }
    _uiState.value = UiState(text)
}
```

---
