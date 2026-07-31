# `snapshotFlow`

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
