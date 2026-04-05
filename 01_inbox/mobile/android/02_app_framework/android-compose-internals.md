---
title: android-compose-internals
tags: [android, android/compose, android/jetpack, android/ui]
aliases: []
date modified: 2026-01-20 15:55:37 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Jetpack Compose Internals android android/compose android/ui

Jetpack Compose 의 내부 동작과 성능 최적화. 기본은 [android-jetpack-architecture](android-jetpack-architecture.md) 참고.

### Compose 기본 개념

Compose 는 선언적 UI 프레임워크다. 상태가 바뀌면 UI 가 자동으로 업데이트된다.

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Hello, $name!")
}

// 사용
setContent {
    Greeting("Android")
}
```

### 재구성 (Recomposition)

상태가 변경되면 Composable 함수가 다시 실행된다.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    
    Column {
        Text("Count: $count") // count 변경 시 이 부분만 재구성
        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}
```

#### 재구성 범위 최소화

```kotlin
// ❌ 나쁜 예: 전체 재구성
@Composable
fun BadExample() {
    var count by remember { mutableStateOf(0) }
    
    Column {
        ExpensiveComposable() // count 변경 시 불필요하게 재구성
        Text("Count: $count")
        Button(onClick = { count++ }) { Text("+") }
    }
}

// ✅ 좋은 예: 필요한 부분만 재구성
@Composable
fun GoodExample() {
    var count by remember { mutableStateOf(0) }
    
    Column {
        ExpensiveComposable() // 재구성 안 됨
        CountDisplay(count) // 이 부분만 재구성
        Button(onClick = { count++ }) { Text("+") }
    }
}

@Composable
fun CountDisplay(count: Int) {
    Text("Count: $count")
}
```

### 상태 관리

#### remember

Composition 동안 값을 기억한다.

```kotlin
@Composable
fun RememberExample() {
    // 재구성 시에도 유지됨
    val state = remember { mutableStateOf(0) }
    
    // 키 기반 remember
    val cachedValue = remember(key1 = userId) {
        expensiveComputation(userId)
    }
}
```

#### rememberSaveable

설정 변경과 프로세스 사망에서도 살아남는다.

```kotlin
@Composable
fun SaveableExample() {
    var text by rememberSaveable { mutableStateOf("") }
    
    TextField(
        value = text,
        onValueChange = { text = it }
    )
}

// 커스텀 Saver
data class City(val name: String, val country: String)

val CitySaver = Saver<City, List<String>>(
    save = { listOf(it.name, it.country) },
    restore = { City(it[0], it[1]) }
)

@Composable
fun CityPicker() {
    var city by rememberSaveable(stateSaver = CitySaver) {
        mutableStateOf(City("Seoul", "Korea"))
    }
}
```

#### State Hoisting

상태를 상위로 올려 재사용성을 높인다.

```kotlin
// ❌ Stateful (재사용 어려움)
@Composable
fun StatefulCounter() {
    var count by remember { mutableStateOf(0) }
    Button(onClick = { count++ }) {
        Text("Count: $count")
    }
}

// ✅ Stateless (재사용 쉬움)
@Composable
fun StatelessCounter(
    count: Int,
    onIncrement: () -> Unit
) {
    Button(onClick = onIncrement) {
        Text("Count: $count")
    }
}

// 사용
@Composable
fun CounterScreen() {
    var count by remember { mutableStateOf(0) }
    StatelessCounter(
        count = count,
        onIncrement = { count++ }
    )
}
```

### Side Effects

Composable 함수는 부수 효과가 없어야 하지만, 필요한 경우 특수 API 사용.

#### LaunchedEffect

Coroutine 실행.

```kotlin
@Composable
fun LoadDataExample(userId: String) {
    var user by remember { mutableStateOf<User?>(null) }
    
    LaunchedEffect(userId) {
        // userId 변경 시 이전 coroutine 취소하고 새로 시작
        user = repository.getUser(userId)
    }
    
    user?.let { Text(it.name) }
}
```

#### DisposableEffect

리소스 정리가 필요한 경우.

```kotlin
@Composable
fun LocationUpdates() {
    val context = LocalContext.current
    
    DisposableEffect(Unit) {
        val locationManager = context.getSystemService<LocationManager>()
        val listener = object : LocationListener {
            override fun onLocationChanged(location: Location) {
                // 처리
            }
        }
        
        locationManager?.requestLocationUpdates(
            LocationManager.GPS_PROVIDER,
            1000L,
            0f,
            listener
        )
        
        onDispose {
            // Composition 이 떠날 때 정리
            locationManager?.removeUpdates(listener)
        }
    }
}
```

#### SideEffect

Compose 상태를 non-Compose 코드에 전달.

```kotlin
@Composable
fun AnalyticsExample(screenName: String) {
    SideEffect {
        // 재구성마다 실행 (상태 변경 후)
        analytics.logScreenView(screenName)
    }
}
```

#### derivedStateOf

계산된 상태 최적화.

```kotlin
@Composable
fun TodoList(todos: List<Todo>) {
    val highPriorityTodos = remember(todos) {
        derivedStateOf {
            // todos 가 변경될 때만 재계산
            todos.filter { it.priority == Priority.HIGH }
        }
    }
    
    // highPriorityTodos.value 가 실제로 변경될 때만 재구성
    Text("High priority: ${highPriorityTodos.value.size}")
}
```

#### snapshotFlow

Compose State 를 Flow 로 변환.

```kotlin
@Composable
fun ScrollToTopButton(listState: LazyListState) {
    val showButton by remember {
        derivedStateOf {
            listState.firstVisibleItemIndex > 0
        }
    }
    
    // 또는 Flow 로
    LaunchedEffect(listState) {
        snapshotFlow { listState.firstVisibleItemIndex }
            .filter { it > 0 }
            .collect {
                // 처리
            }
    }
    
    if (showButton) {
        FloatingActionButton(onClick = { /* scroll to top */ }) {
            Icon(Icons.Default.ArrowUpward, null)
        }
    }
}
```

### 성능 최적화

#### Stability

Compose 는 타입의 안정성을 분석해 재구성을 건너뛴다.

**Stable 조건:**
1. 같은 인스턴스의 `equals()` 결과가 항상 같음
2. public 프로퍼티 변경 시 Composition 에 알림
3. 모든 public 프로퍼티가 stable

```kotlin
// ✅ Stable (data class with val)
data class User(val id: String, val name: String)

// ❌ Unstable (var)
data class MutableUser(var id: String, var name: String)

// ✅ Stable (명시적 표시)
@Stable
class CustomUser(var id: String) {
    // Compose 가 변경을 추적할 수 있도록 구현
}

// ✅ Immutable
@Immutable
data class ImmutableUser(val id: String, val name: String)
```

#### 람다 최적화

```kotlin
// ❌ 나쁜 예: 재구성마다 새 람다 생성
@Composable
fun BadLambda(items: List<String>) {
    LazyColumn {
        items(items) { item ->
            Button(onClick = { viewModel.onItemClick(item) }) {
                Text(item)
            }
        }
    }
}

// ✅ 좋은 예: 람다 재사용
@Composable
fun GoodLambda(items: List<String>, onItemClick: (String) -> Unit) {
    LazyColumn {
        items(items) { item ->
            ItemRow(item, onItemClick)
        }
    }
}

@Composable
fun ItemRow(item: String, onClick: (String) -> Unit) {
    Button(onClick = { onClick(item) }) {
        Text(item)
    }
}
```

#### key 사용

리스트 아이템의 정체성을 명확히 한다.

```kotlin
@Composable
fun UserList(users: List<User>) {
    LazyColumn {
        items(
            items = users,
            key = { user -> user.id } // 재정렬 시 애니메이션 올바르게 동작
        ) { user ->
            UserCard(user)
        }
    }
}
```

### LazyColumn/LazyRow 최적화

```kotlin
@Composable
fun OptimizedList(items: List<Item>) {
    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        items(
            items = items,
            key = { it.id },
            contentType = { it.type } // 같은 타입끼리 재사용
        ) { item ->
            when (item.type) {
                ItemType.TEXT -> TextItem(item)
                ItemType.IMAGE -> ImageItem(item)
            }
        }
    }
}

// Sticky Header
@Composable
fun GroupedList(groups: Map<String, List<Item>>) {
    LazyColumn {
        groups.forEach { (header, items) ->
            stickyHeader {
                Text(
                    text = header,
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(Color.Gray)
                        .padding(16.dp)
                )
            }
            
            items(items) { item ->
                ItemCard(item)
            }
        }
    }
}
```

### Modifier 최적화

```kotlin
// ❌ 나쁜 예: 재구성마다 새 Modifier 생성
@Composable
fun BadModifier(isSelected: Boolean) {
    Box(
        modifier = Modifier
            .size(100.dp)
            .background(if (isSelected) Color.Blue else Color.Gray)
    )
}

// ✅ 좋은 예: Modifier 재사용
@Composable
fun GoodModifier(isSelected: Boolean) {
    val backgroundColor = if (isSelected) Color.Blue else Color.Gray
    
    Box(
        modifier = Modifier
            .size(100.dp)
            .background(backgroundColor)
    )
}

// ✅ 더 좋은 예: remember 사용
@Composable
fun BetterModifier(isSelected: Boolean) {
    val modifier = remember(isSelected) {
        Modifier
            .size(100.dp)
            .background(if (isSelected) Color.Blue else Color.Gray)
    }
    
    Box(modifier = modifier)
}
```

### CompositionLocal

트리 전체에 값을 전파.

```kotlin
// 정의
val LocalUserId = compositionLocalOf<String> { error("No user ID provided") }

// 제공
@Composable
fun App() {
    CompositionLocalProvider(LocalUserId provides "user123") {
        UserScreen()
    }
}

// 사용
@Composable
fun UserScreen() {
    val userId = LocalUserId.current
    Text("User: $userId")
}

// 기본 제공되는 것들
LocalContext.current // Context
LocalConfiguration.current // Configuration
LocalDensity.current // Density
LocalLifecycleOwner.current // LifecycleOwner
```

### ViewModel 통합

```kotlin
@Composable
fun UserScreen(
    viewModel: UserViewModel = viewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    
    when (uiState) {
        is UiState.Loading -> LoadingIndicator()
        is UiState.Success -> UserContent(uiState.data)
        is UiState.Error -> ErrorMessage(uiState.message)
    }
}

// Hilt 사용
@Composable
fun UserScreen(
    viewModel: UserViewModel = hiltViewModel()
) {
    // ...
}
```

### Navigation Compose

### Navigation Compose (Type-Safe Routing)

> [!WARNING] **Devil's Advocate : String Route는 이제 그만**
> 과거 Compose Navigation은 `"detail/{id}"` 와 같은 String URL 기반 라우팅을 사용하여 오타에 취약하고 인수 전달이 불편했습니다.
> **Navigation 2.8+ 버전부터는 `kotlinx.serialization` 기반의 Type-Safe 라우팅으로 완전히 대체**되었습니다. String 기반 라우팅 코드를 발견하면 리팩토링 대상입니다.

```kotlin
// 1. Route 타겟을 Serializable 데이터 구조로 정의
@Serializable object Home
@Serializable data class Detail(val userId: String)

@Composable
fun AppNavigation() {
    val navController = rememberNavController()
    
    NavHost(navController = navController, startDestination = Home) {
        composable<Home> {
            HomeScreen(
                onNavigateToDetail = { id ->
                    navController.navigate(Detail(userId = id))
                }
            )
        }
        
        composable<Detail> { backStackEntry ->
            // 2. Type-safe하게 인자 추출
            val detail = backStackEntry.toRoute<Detail>()
            DetailScreen(userId = detail.userId)
        }
    }
}
```

### 테스팅

```kotlin
class CounterTest {
    @get:Rule
    val composeTestRule = createComposeRule()
    
    @Test
    fun counterIncrementsOnButtonClick() {
        composeTestRule.setContent {
            Counter()
        }
        
        // 초기 상태 확인
        composeTestRule.onNodeWithText("Count: 0").assertExists()
        
        // 버튼 클릭
        composeTestRule.onNodeWithText("Increment").performClick()
        
        // 업데이트된 상태 확인
        composeTestRule.onNodeWithText("Count: 1").assertExists()
    }
    
    @Test
    fun textFieldUpdatesOnInput() {
        composeTestRule.setContent {
            var text by remember { mutableStateOf("") }
            TextField(value = text, onValueChange = { text = it })
        }
        
        composeTestRule.onNode(hasSetTextAction())
            .performTextInput("Hello")
        
        composeTestRule.onNodeWithText("Hello").assertExists()
    }
}
```

### 디버깅

```kotlin
// Layout Inspector 사용
// Android Studio → Tools → Layout Inspector

// Recomposition 횟수 확인
@Composable
fun DebugComposable() {
    val count = remember { mutableStateOf(0) }
    
    SideEffect {
        count.value++
        Log.d("Compose", "Recomposed ${count.value} times")
    }
    
    Text("Hello")
}

// Composition Tracing
// adb shell setprop debug.compose.trace on
```

### Kotlin 2.0+ Compose 컴파일러 분리

> [!WARNING] **Kotlin 2.0 마이그레이션 필수 변경**
> Kotlin 2.0부터 Compose 컴파일러 플러그인이 Kotlin 에 **내장**되었다. 별도의 `compose-compiler` 의존성과 `kotlinCompilerExtensionVersion` 설정이 **삭제**되어야 한다.

```kotlin
// ❌ Kotlin 1.x (이전 방식)
android {
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.4"  // 삭제 대상
    }
}

// ✅ Kotlin 2.0+ (현대 방식)
plugins {
    alias(libs.plugins.kotlin.compose)  // Compose 컴파일러 플러그인
}
// composeOptions 블록 자체가 불필요
```

**마이그레이션 체크리스트:**
1. `build.gradle.kts` 에서 `composeOptions { kotlinCompilerExtensionVersion }` 제거
2. `plugins` 블록에 `kotlin-compose` 플러그인 추가
3. `libs.versions.toml` 에서 Compose Compiler 버전 참조 제거

### Strong Skipping Mode (Compose 1.6+)

Compose 컴파일러가 더 공격적으로 재구성을 건너뛸 수 있도록 한다. **Kotlin 2.0+ 에서는 기본 활성화.**

**기존**: Unstable 파라미터를 가진 Composable 은 항상 재구성
**Strong Skipping**: Unstable 파라미터도 `equals()` 비교를 통해 **같으면 건너뜀**

```kotlin
// 기존: List<User> 는 Unstable → UserList 는 항상 재구성됨
// Strong Skipping: List<User> 도 equals() 비교 → 같은 리스트면 건너뜀
@Composable
fun UserList(users: List<User>) {
    LazyColumn {
        items(users) { user -> UserCard(user) }
    }
}
```

**실무 영향:**
- `@Stable`, `@Immutable` 어노테이션의 필요성이 줄어듦
- `kotlinx.collections.immutable` (`ImmutableList` 등) 없이도 성능 확보 가능
- 그래도 `data class` + `val` 조합은 여전히 권장 (의도 명확화)

> [!NOTE] **iOS 비교: SwiftUI 의 렌더링 최적화**
> SwiftUI 는 `@Observable` 매크로(iOS 17+)를 통해 **프로퍼티 수준 추적**을 자동화한다. Compose 의 Strong Skipping Mode 와 유사하게, 실제로 변경된 프로퍼티를 사용하는 뷰만 다시 그린다.
> 차이점: SwiftUI 는 프레임워크가 자동으로 감지하는 반면, Compose 는 `equals()` 기반 비교에 의존한다.
> 자세한 내용은 [apple-observation-framework](../../apple/01_language_concurrency/apple-observation-framework.md) 참고.

### 더 보기

[android-jetpack-architecture](android-jetpack-architecture.md), [android-app-components-deep-dive](android-app-components-deep-dive.md), [android-coroutines-flow](android-coroutines-flow.md), [android-performance-and-debug](../06_testing_performance/android-performance-and-debug.md), [android-testing-and-quality](../06_testing_performance/android-testing-and-quality.md)

