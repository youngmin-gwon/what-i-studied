# animate*AsState

가장 널리 쓰이는 하위 레벨 API로, 상태 변경 시 특정 단일 값(`Float`, `Color`, `Dp`, `Offset`, `IntSize` 등)을 부드럽게 변환시켜 줍니다.

```kotlin
var isRed by remember { mutableStateOf(false) }

// 상태 변경 시 자동으로 색상이 애니메이션화됨
val backgroundColor by animateColorAsState(
    targetValue = if (isRed) Color.Red else Color.Green,
    animationSpec = tween(durationMillis = 1000)
)

Box(
    modifier = Modifier
        .size(100.dp)
        .background(backgroundColor)
        .clickable { isRed = !isRed }
)
```
