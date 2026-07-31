# LaunchedEffect

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
