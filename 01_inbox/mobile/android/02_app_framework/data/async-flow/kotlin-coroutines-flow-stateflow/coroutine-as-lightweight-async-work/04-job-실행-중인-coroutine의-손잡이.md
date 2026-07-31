# Job: 실행 중인 Coroutine의 손잡이

`launch`를 호출하면 `Job`이 반환됩니다.

`Job`은 실행 중인 Coroutine을 추적하고 취소할 수 있는 손잡이입니다.

```kotlin
private var searchJob: Job? = null

fun search(keyword: String) {
    searchJob?.cancel()
    searchJob = viewModelScope.launch {
        val result = repository.search(keyword)
        _uiState.value = SearchUiState.Success(result)
    }
}
```

검색어가 바뀔 때 이전 검색을 취소하고 최신 검색만 유지하는 패턴입니다. 다만 Flow를 쓰면 이 패턴은 보통 `debounce` + `flatMapLatest`로 더 깔끔하게
표현할 수 있습니다.
