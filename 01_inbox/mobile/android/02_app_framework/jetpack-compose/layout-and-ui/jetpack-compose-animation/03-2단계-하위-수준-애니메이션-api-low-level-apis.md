# 2단계: 하위 수준 애니메이션 API (Low-level APIs)

특정 컴포저블의 단일 속성 값을 직접 부드럽게 보간하거나, 상태 머신을 기반으로 여러 요소의 복잡한 움직임을 정밀 제어할 때 사용합니다.

### 3-1. animate*AsState

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

### 3-2. updateTransition

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

### 3-3. rememberInfiniteTransition

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

### 3-4. Animatable

코루틴 범위를 통해 **애니메이션을 정밀하게 제어하거나 명령을 즉시 중단(SnapTo), 취소**해야 하는 가장 저수준의 애니메이션 상태 홀더입니다. 물리 기반 터치 스와이프
제스처 등에 적합합니다.

```kotlin
val colorAnim = remember { Animatable(Color.Gray) }

// 제스처 또는 특정 비동기 트리거 시 코루틴 내에서 실행
LaunchedEffect(isSuccess) {
    if (isSuccess) {
        // 부드럽게 Green으로 변환
        colorAnim.animateTo(Color.Green, animationSpec = spring())
    } else {
        // 즉시 Red로 값 스냅
        colorAnim.snapTo(Color.Red)
    }
}
```

---
