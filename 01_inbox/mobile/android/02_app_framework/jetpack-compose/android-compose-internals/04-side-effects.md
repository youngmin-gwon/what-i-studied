# Side Effects

상위 노트: [[android-compose-internals]]

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
