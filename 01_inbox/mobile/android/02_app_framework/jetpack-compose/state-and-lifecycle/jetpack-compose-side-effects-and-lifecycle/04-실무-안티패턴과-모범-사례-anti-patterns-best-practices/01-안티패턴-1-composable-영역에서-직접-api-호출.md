# ❌ 안티패턴 1: Composable 영역에서 직접 API 호출
```kotlin
@Composable
fun ProductScreen(productId: String, repository: ProductRepository) {
    // Recomposition이 발생할 때마다 네트워크 요청이 중복 실행됩니다!
    val product = repository.loadProduct(productId) 
    
    ProductDetail(product)
}
```
