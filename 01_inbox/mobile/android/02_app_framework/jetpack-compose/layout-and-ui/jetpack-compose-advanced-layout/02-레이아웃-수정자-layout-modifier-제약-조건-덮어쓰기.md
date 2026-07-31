# 레이아웃 수정자 (Layout Modifier) & 제약 조건 덮어쓰기

전체 커스텀 레이아웃을 만드는 것이 과도할 때(Overkill), 단 하나의 컴포저블 속성이나 여백만을 부모 제약 조건과 다르게 직접 조작하기 위해 `Modifier.layout`을 사용합니다.

### 2-1. Modifier.layout 사용법
개별 컴포저블의 측정 및 배치 로직에 직접 개입할 수 있습니다.

```kotlin
fun Modifier.customPosition() = this.layout { measurable, constraints ->
    // 1. 전달받은 제약조건으로 자식을 측정
    val placeable = measurable.measure(constraints)
    
    // 2. 부모의 크기 및 자식의 배치 위치 지정
    layout(placeable.width, placeable.height) {
        // 원하는 X, Y 위치에 배치
        placeable.placeRelative(0, 0)
    }
}
```

### 2-2. Modifier.width vs Modifier.requiredWidth (제약 조건 강제)
부모 레이아웃이 자식에게 엄격한 제약(Constraints)을 보낼 때, Modifier가 작동하는 방식의 차이를 이해해야 합니다.

* **Modifier.width**:
  * 부모가 제공하는 제약 조건 범위 내에서 작동합니다.
  * 만약 부모가 최대 너비를 `100.dp`로 제한(`Constraints.maxWidth`)하고 자식이 `Modifier.width(150.dp)`를 요구하더라도, **부모의 제약 조건이 우선(Override)** 하여 최종 너비는 `100.dp`로 강제 제한됩니다.
* **Modifier.requiredWidth**:
  * 부모가 부여한 제약 조건을 무시하고 지정한 크기를 강제로 보장합니다.
  * 부모의 최대 너비가 `100.dp`라 하더라도 `requiredWidth(150.dp)`를 적용하면 자식은 `150.dp` 크기로 그려지며, 이로 인해 부모 영역을 벗어나는 오버플로우나 클리핑(Clipping)이 발생할 수 있습니다.

---
