# `derivedStateOf` (파생 상태 최적화)
* **목적**: 자주 변경되는 상태(State)들로부터 특정 조건의 파생 상태를 만들 때, 불필요한 재구성(Recomposition) 횟수를 제한합니다.
* **동작**: 내부 상태가 아무리 많이 변하더라도 계산된 결과 값 자체가 변경될 때만 수신처에 재구성을 유발합니다.
* **주요 사용처**: 스크롤 위치 계산, 리스트 필터링, 조건부 UI 노출 판정.

```kotlin
@Composable
fun ScrollTargetList(lazyListState: LazyListState) {
    // 스크롤 인덱스는 스크롤할 때마다 계속 변경되지만, 
    // derivedStateOf를 쓰면 '5개 이상 스크롤되었는지 여부'가 바뀔 때만 Recomposition이 실행됩니다.
    val showButton by remember {
        derivedStateOf {
            lazyListState.firstVisibleItemIndex > 5
        }
    }

    if (showButton) {
        FloatingActionButton(onClick = { /* ... */ })
    }
}
```

---
