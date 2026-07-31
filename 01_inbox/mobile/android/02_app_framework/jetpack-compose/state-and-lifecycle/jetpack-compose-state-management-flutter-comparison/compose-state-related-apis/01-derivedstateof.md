# `derivedStateOf`

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
