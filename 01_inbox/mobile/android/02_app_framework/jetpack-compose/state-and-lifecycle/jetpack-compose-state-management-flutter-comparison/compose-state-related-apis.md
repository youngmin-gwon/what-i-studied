# `remember`는 아니지만 같이 알아야 하는 API

상위 노트: [[jetpack-compose-state-management-flutter-comparison]]

### `derivedStateOf`

`derivedStateOf`는 다른 상태에서 계산되는 파생 상태를 만들 때 사용합니다.

```kotlin
val listState = rememberLazyListState()
val showScrollToTop by remember {
    derivedStateOf {
        listState.firstVisibleItemIndex > 0
    }
}
```

스크롤처럼 자주 바뀌는 값에서 실제 UI 갱신은 특정 조건이 바뀔 때만 필요할 수 있습니다. 이때 `derivedStateOf`가 도움이 됩니다.

다만 단순 문자열 조합이나 가벼운 계산에 무조건 쓰는 것은 과합니다.

### `LaunchedEffect`

Composable이 Composition에 들어왔을 때 coroutine 작업을 시작합니다.

```kotlin
LaunchedEffect(userId) {
    viewModel.load(userId)
}
```

key가 바뀌면 기존 작업이 취소되고 다시 시작됩니다.

### `DisposableEffect`

등록과 해제가 쌍으로 필요한 작업에 씁니다.

```kotlin
DisposableEffect(lifecycleOwner) {
    val observer = LifecycleEventObserver { _, _ -> }
    lifecycleOwner.lifecycle.addObserver(observer)

    onDispose {
        lifecycleOwner.lifecycle.removeObserver(observer)
    }
}
```

### `produceState`

외부 async source를 Compose `State<T>`로 변환합니다.

```kotlin
val image by produceState<Image?>(initialValue = null, url) {
    value = imageRepository.load(url)
}
```

앱 아키텍처에서는 ViewModel/Repository로 빼는 편이 더 명확한 경우가 많습니다.

### `snapshotFlow`

Compose State 읽기를 Flow로 변환합니다.

```kotlin
LaunchedEffect(listState) {
    snapshotFlow { listState.firstVisibleItemIndex }
        .collect { index ->
            analytics.trackScroll(index)
        }
}
```

UI state 변화를 Flow operator와 연결해야 할 때 사용합니다.

---
