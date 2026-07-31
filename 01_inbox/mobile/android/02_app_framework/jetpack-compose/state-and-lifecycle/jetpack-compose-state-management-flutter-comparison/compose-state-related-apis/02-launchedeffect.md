# `LaunchedEffect`

Composable이 Composition에 들어왔을 때 coroutine 작업을 시작합니다.

```kotlin
LaunchedEffect(userId) {
    viewModel.load(userId)
}
```

key가 바뀌면 기존 작업이 취소되고 다시 시작됩니다.
