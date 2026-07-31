# rememberInfiniteTransition

무한히 반복되는 애니메이션(예: 로딩 인디케이터의 회전, 심장 박동 효과, 그라데이션 쉬머 효과)을 만들 때 사용합니다.

```kotlin
val infiniteTransition = rememberInfiniteTransition(label = "InfinitePulse")

// 무한히 0.5f에서 1.0f 사이를 펄스 운동하는 애니메이션
val scale by infiniteTransition.animateFloat(
    initialValue = 0.5f,
    targetValue = 1.0f,
    animationSpec = infiniteRepeatable(
        animation = tween(1000),
        repeatMode = RepeatMode.Reverse
    ),
    label = "Scale"
)

Box(
    modifier = Modifier
        .size(100.dp)
        .graphicsLayer(scaleX = scale, scaleY = scale)
        .background(Color.Magenta)
)
```
