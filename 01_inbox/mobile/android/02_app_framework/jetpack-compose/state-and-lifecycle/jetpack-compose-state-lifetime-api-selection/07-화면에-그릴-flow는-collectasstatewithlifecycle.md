# 화면에 그릴 Flow는 collectAsStateWithLifecycle

상위 노트: [jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)

Compose에서 `StateFlow<UiState>`를 화면에 그릴 상태로 읽을 때는 `collectAsStateWithLifecycle()`을 우선 사용합니다.

```kotlin
@Composable
fun ProfileRoute(
    viewModel: ProfileViewModel,
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    ProfileScreen(uiState = uiState)
}
```

이 API는 Flow를 lifecycle-aware하게 수집하고, 최신 값을 Compose `State`로 변환합니다. 화면이 보이지 않을 때 불필요한 수집을 줄이는 데 도움이
됩니다.

Compose에서 화면 상태를 읽기 위해 아래처럼 직접 수집하는 패턴은 대부분 피합니다.

```kotlin
LaunchedEffect(viewModel) {
    viewModel.uiState.collect { uiState ->
        // 화면 상태를 수동으로 반영
    }
}
```

화면에 그릴 상태라면 `collectAsStateWithLifecycle()`이 기본입니다. `LaunchedEffect`에서 collect하는 것은 snackbar,
navigation 같은 일회성 event를 처리할 때 더 적합합니다.

---
