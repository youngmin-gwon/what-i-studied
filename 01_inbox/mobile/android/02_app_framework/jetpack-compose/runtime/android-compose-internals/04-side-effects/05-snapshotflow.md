# snapshotFlow

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
