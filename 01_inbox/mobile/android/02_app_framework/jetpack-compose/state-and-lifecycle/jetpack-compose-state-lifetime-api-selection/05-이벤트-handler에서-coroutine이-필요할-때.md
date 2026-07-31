# 이벤트 handler에서 coroutine이 필요할 때

상위 노트: [jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)

버튼 클릭, drawer 열기, scroll animation처럼 event handler 내부에서 coroutine을 시작해야 하면`rememberCoroutineScope()`
를 씁니다.

```kotlin
@Composable
fun ScrollToTopButton(
    listState: LazyListState,
) {
    val scope = rememberCoroutineScope()

    Button(
        onClick = {
            scope.launch {
                listState.animateScrollToItem(0)
            }
        }
    ) {
        Text("Top")
    }
}
```

이 scope는 composable이 composition에서 제거되면 취소됩니다.

적합한 작업:

- `SnackbarHostState.showSnackbar()`
- `DrawerState.open()`
- `LazyListState.animateScrollToItem()`
- bottom sheet show/hide

장기 비즈니스 작업이나 저장 작업은 ViewModel로 올리는 편이 좋습니다.

---
