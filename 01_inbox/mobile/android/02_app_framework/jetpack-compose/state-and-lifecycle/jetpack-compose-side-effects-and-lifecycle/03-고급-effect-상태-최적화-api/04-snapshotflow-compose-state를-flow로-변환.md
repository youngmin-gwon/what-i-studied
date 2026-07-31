# `snapshotFlow` (Compose State를 Flow로 변환)
* **목적**: Compose State의 변화를 감지하여 Reactive Stream(Flow)으로 변환한 뒤, Flow 연산자(filter, debounce 등)를 적용할 수 있게 해줍니다.

```kotlin
@Composable
fun SearchAnalytics(lazyListState: LazyListState) {
    LaunchedEffect(lazyListState) {
        snapshotFlow { lazyListState.firstVisibleItemIndex }
            .distinctUntilChanged()
            .filter { it > 0 }
            .collect { index ->
                analytics.trackUserReachedIndex(index)
            }
    }
}
```

---
