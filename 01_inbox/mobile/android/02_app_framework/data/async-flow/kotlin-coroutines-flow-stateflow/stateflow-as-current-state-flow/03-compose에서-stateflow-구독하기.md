# Compose에서 StateFlow 구독하기

Compose에서는 `collectAsStateWithLifecycle()`을 사용해 StateFlow를 구독합니다.

```kotlin
@Composable
fun ProfileRoute(
    viewModel: ProfileViewModel = viewModel(),
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    ProfileScreen(
        uiState = uiState,
        onRetryClick = viewModel::load,
    )
}
```

`collectAsStateWithLifecycle()`은 화면 생명주기를 고려해, 화면이 보이는 동안에만 안전하게 Flow를 수집합니다.

> [!IMPORTANT]
> Compose에서 Flow를 직접 `collect`하려고 `LaunchedEffect`를 남발하지 마세요. 화면에 그릴 상태라면 대부분
`collectAsStateWithLifecycle()`이 맞습니다.
