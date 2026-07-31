# 무거운 작업을 Main Dispatcher에서 실행

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
