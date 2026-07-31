# Composable body에서 직접 API 호출하지 않기

```kotlin
@Composable
fun BadScreen() {
    repository.load()
}
```

Composable은 recomposition될 수 있으므로 body에 직접 side effect를 두면 호출이 반복될 수 있습니다. ViewModel 또는
`LaunchedEffect`로 옮겨야 합니다.
