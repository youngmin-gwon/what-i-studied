---
title: compose-layout-measures-children-under-parent-constraints
tags: [android, compose/ui, jetpack-compose]
aliases: [Single-pass Layout, Constraints]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Compose layout measures children under parent constraints

### 1. 개념 정의 (What)
Compose의 레이아웃 알고리즘은 **단일 패스(Single-pass) 측정 모델**을 따른다. 부모 노드는 자식 노드에게 최소/최대 너비와 높이를 지정하는 **제약 조건(`Constraints`)**을 하향(Top-down)으로 전달하며, 자식 노드는 전달받은 제약 안에서 스스로의 크기(`Placeable`)를 측정해 상향(Bottom-up)으로 반환한 후 부모가 이를 픽셀 좌표에 배치(Placement)한다.

---

### 2. 단일 패스 제약 시스템의 필요성 (Why)
기존 Android View System(XML 레이아웃)에서는 `RelativeLayout`이나 `LinearLayout(weight=1)` 사용 시 자식 뷰를 두 번 이상 측정하는 **이중 세금(Double Taxation / Multi-pass Measurement)** 현상이 빈번했다.

이로 인해 레이아웃 트리가 깊어질수록 측정 연산 비용이 지수 함수적($O(2^N)$)으로 폭증하여 심각한 UI Jank와 프레임 드롭이 발생했다. Compose는 **"모든 UI 노드는 단 1회만 측정될 수 있다"**는 철저한 단일 패스 제약을 런타임 수준에서 강제하여 $O(N)$의 선형적 렌더링 성능을 보장한다.

---

### 3. 내부 측정 및 배치 메커니즘 (How)

```
[1. Parent 노드가 Constraints 하향 전달]
        Constraints (minW, maxW, minH, maxH)
                         |
                         v
[2. Child 노드가 스스로의 크기 결정]
        Measurable.measure(constraints) 실행
                         |
                         v
[3. Child 가 Placeable (width, height) 상향 반환]
                         |
                         v
[4. Parent 가 layout(w, h) 블록 내에서 배치]
        placeable.placeRelative(x, y)
```

1. **Constraints 구조체**: `Constraints(minWidth, maxWidth, minHeight, maxHeight)` 4개 정수 필드로 구성되며 메모리 낭비를 줄이기 위해 64비트 정수로 패킹되어 전달된다.
2. **단일 측정 예외 방지**: 동일한 `Measurable` 객체에 대해 한 번의 Layout 패스에서 `measure()`를 두 번 이상 호출하면 Compose Runtime이 `IllegalStateException` 예외를 발생시킨다.

---

### 4. Layout 측정 구조의 기초 코드 예시

```kotlin
@Composable
fun CustomBox(
    modifier: Modifier = Modifier,
    content: @Composable () -> Unit
) {
    Layout(
        content = content,
        modifier = modifier
    ) { measurables, constraints ->
        // 1. 단 1회만 자식 측정 (Constraints 하향 전달)
        val placeables = measurables.map { measurable ->
            measurable.measure(constraints)
        }

        // 2. 부모 크기 계산 (자식 중 최대 크기 선택)
        val maxWidth = placeables.maxOfOrNull { it.width } ?: constraints.minWidth
        val maxHeight = placeables.maxOfOrNull { it.height } ?: constraints.minHeight

        // 3. 배치 실행 (Placement)
        layout(maxWidth, maxHeight) {
            placeables.forEach { placeable ->
                placeable.placeRelative(x = 0, y = 0)
            }
        }
    }
}
```

---

상위 문서: [Compose Layout, Animation, Accessibility 지침서](../compose-layout-animation-accessibility.md)

관련 노트: [Modifier order changes layout draw and input wrappers](./modifier-order-changes-layout-draw-and-input-wrappers.md), [Size modifiers interpret requested size inside incoming constraints](./size-modifiers-interpret-requested-size-inside-incoming-constraints.md)

출처: [Compose layout basics](https://developer.android.com/develop/ui/compose/layouts/basics)

검증일: 2026-08-05. Compose 공식 가이드의 Single-pass Layout 알고리즘 사양을 대조하여 Constraints 하향 전달, Double Taxation 방지 및 1회 측정 강제 메커니즘 서술을 정밀 보강했다.
