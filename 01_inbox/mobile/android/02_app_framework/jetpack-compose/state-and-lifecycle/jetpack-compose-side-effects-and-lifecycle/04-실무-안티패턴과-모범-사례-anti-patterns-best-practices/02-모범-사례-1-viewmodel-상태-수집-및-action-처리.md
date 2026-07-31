# 모범 사례 1: ViewModel 상태 수집 및 Action 처리
화면 단위 비즈니스 로직은 `ViewModel` 내부에서 코루틴을 통해 처리하고 UI는 이를 구독만 합니다. UI 수준의 비동기 작업이 꼭 필요하다면 `LaunchedEffect`를 적용하세요.
```kotlin
@Composable
fun ProductRoute(
    viewModel: ProductViewModel,
    productId: String
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    
    // productId가 바뀔 때 로드하도록 ViewModel에 명령하거나, LaunchedEffect로 감쌉니다.
    LaunchedEffect(productId) {
        viewModel.loadProduct(productId)
    }
    
    ProductScreen(uiState)
}
```

---
