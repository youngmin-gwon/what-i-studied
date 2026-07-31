# 검색 패턴: query StateFlow + flatMapLatest

```kotlin
class SearchViewModel(
    private val repository: ProductRepository,
) : ViewModel() {
    private val query = MutableStateFlow("")

    val uiState: StateFlow<SearchUiState> =
        query
            .debounce(300)
            .distinctUntilChanged()
            .flatMapLatest { keyword ->
                if (keyword.isBlank()) {
                    flowOf(emptyList())
                } else {
                    repository.searchProducts(keyword)
                }
            }
            .map { products ->
                SearchUiState.Ready(products)
            }
            .stateIn(
                scope = viewModelScope,
                started = SharingStarted.WhileSubscribed(5_000),
                initialValue = SearchUiState.Ready(emptyList()),
            )

    fun onQueryChange(value: String) {
        query.value = value
    }
}
```

`flatMapLatest`가 핵심입니다. 새 검색어가 들어오면 이전 검색 Flow를 취소하고 최신 검색만 유지합니다.
