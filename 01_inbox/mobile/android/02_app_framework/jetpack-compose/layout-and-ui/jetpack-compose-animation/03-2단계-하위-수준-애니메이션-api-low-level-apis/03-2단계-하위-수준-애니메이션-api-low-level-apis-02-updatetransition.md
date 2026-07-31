# updateTransition

하나의 상태 변화(예: 탭 활성화, 접힘/펼침 상태 등)에 따라 **여러 애니메이션 값을 동기화**하여 일관된 전환 연출을 할 수 있도록 돕는 상태 기반 API입니다.

```kotlin
enum class BoxState { Collapsed, Expanded }

var boxState by remember { mutableStateOf(BoxState.Collapsed) }
val transition = updateTransition(targetState = boxState, label = "BoxTransition")

// 1. 크기 애니메이션 설정
val size by transition.animateDp(label = "Size") { state ->
    when (state) {
        BoxState.Collapsed -> 100.dp
        BoxState.Expanded -> 200.dp
    }
}

// 2. 색상 애니메이션 설정 (크기와 동기화됨)
val color by transition.animateColor(label = "Color") { state ->
    when (state) {
        BoxState.Collapsed -> Color.Blue
        BoxState.Expanded -> Color.Red
    }
}

Box(
    modifier = Modifier
        .size(size)
        .background(color)
        .clickable {
            boxState = if (boxState == BoxState.Collapsed) BoxState.Expanded else BoxState.Collapsed
        }
)
```
