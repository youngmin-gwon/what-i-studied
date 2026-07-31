# CompositionLocal

상위 노트: [[android-compose-internals]]

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
