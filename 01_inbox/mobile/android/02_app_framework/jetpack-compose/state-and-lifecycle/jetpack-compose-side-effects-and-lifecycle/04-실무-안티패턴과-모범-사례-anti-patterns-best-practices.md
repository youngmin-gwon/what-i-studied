# 실무 안티패턴과 모범 사례 (Anti-Patterns & Best Practices)

상위 노트: [[jetpack-compose-side-effects-and-lifecycle]]

### ❌ 안티패턴 1: Composable 영역에서 직접 API 호출
```kotlin
@Composable
fun ProductScreen(productId: String, repository: ProductRepository) {
    // Recomposition이 발생할 때마다 네트워크 요청이 중복 실행됩니다!
    val product = repository.loadProduct(productId) 
    
    ProductDetail(product)
}
```

###  모범 사례 1: ViewModel 상태 수집 및 Action 처리
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

### ❌ 안티패턴 2: 비-코루틴 콜백에서 LaunchedEffect 실행 시도
```kotlin
@Composable
fun BadButton() {
    Button(
        onClick = {
            // Composable 함수 내부가 아닌 onClick 람다 내부이므로 LaunchedEffect를 직접 호출할 수 없어 컴파일 오류 발생!
            LaunchedEffect(Unit) { 
                doSomething()
            }
        }
    ) { Text("Click") }
}
```

###  모범 사례 2: `rememberCoroutineScope` 사용
```kotlin
@Composable
fun GoodButton() {
    val scope = rememberCoroutineScope()
    
    Button(
        onClick = {
            // 이벤트 핸들러 내부에서는 스코프를 활용해 코루틴을 실행합니다.
            scope.launch {
                doSomething()
            }
        }
    ) { Text("Click") }
}
```

---

### ❌ 안티패턴 3: State 업데이트 지연을 방지하고자 Effect를 무분별하게 재생성
```kotlin
@Composable
fun BadTimer(onTick: () -> Unit) {
    // onTick이 바뀔 때마다 LaunchedEffect가 취소되고 처음부터 다시 시작하여 타이머가 정상 동작하지 못합니다!
    LaunchedEffect(onTick) {
        while(true) {
            delay(1000L)
            onTick()
        }
    }
}
```

###  모범 사례 3: `rememberUpdatedState`로 해결
```kotlin
@Composable
fun GoodTimer(onTick: () -> Unit) {
    val currentOnTick by rememberUpdatedState(onTick)
    
    // LaunchedEffect는 Unit으로 최초 1회만 실행하고 변경되지 않지만,
    // currentOnTick은 항상 최신의 onTick을 안전하게 참조합니다.
    LaunchedEffect(Unit) {
        while(true) {
            delay(1000L)
            currentOnTick()
        }
    }
}

---
