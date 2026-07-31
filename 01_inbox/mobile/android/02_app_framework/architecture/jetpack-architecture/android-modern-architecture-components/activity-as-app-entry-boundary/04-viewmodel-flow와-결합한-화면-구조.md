# ViewModel + Flow와 결합한 화면 구조

현대 Activity/Compose 구조에서 화면 상태는 Activity가 아니라 `ViewModel`이 들고, UI는 `Flow`를 생명주기에 맞게 구독합니다.

```kotlin
data class ProductUiState(
    val isLoading: Boolean = false,
    val products: List<Product> = emptyList(),
    val errorMessage: String? = null,
)

class ProductViewModel(
    private val repository: ProductRepository,
) : ViewModel() {
    val uiState: StateFlow<ProductUiState> =
        repository.observeProducts()
            .map { products -> ProductUiState(products = products) }
            .stateIn(
                scope = viewModelScope,
                started = SharingStarted.WhileSubscribed(5_000),
                initialValue = ProductUiState(isLoading = true),
            )
}
```

```kotlin
@Composable
fun ProductRoute(
    viewModel: ProductViewModel = viewModel(),
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    ProductScreen(
        uiState = uiState,
        onProductClick = { productId ->
            // Navigation 호출
        },
    )
}
```

> [!NOTE]
> Activity는 OS와 Compose 세계를 연결하는 입구입니다. 화면 상태와 비즈니스 로직을 Activity에 오래 붙잡아 두면, 생명주기 변화와 테스트가 모두
> 어려워집니다.

---
