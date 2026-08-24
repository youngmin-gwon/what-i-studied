---
title: custom-layout-placement
tags: [android, compose/ui, jetpack-compose]
aliases: [custom layout, MeasurePolicy]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Custom Layout measures and places children explicitly

### 1. 개념 정의 (What)
`Layout(content = { ... }, modifier = modifier, measurePolicy = { ... })`는 기본 제공 커스텀 컴포넌트(`Column`, `Row`, `Box`)만으로는 구현할 수 없는 특수한 UI 구조(예: 대각선 배치, 순차 래핑 FlowLayout, 원형 레이아웃)를 만들기 위해, **자식 노드들의 측정(Measurement)과 좌표 배치(Placement) 알고리즘을 개발자가 명시적으로 제어하는 커스텀 레이아웃 구축 API**다.

---

### 2. Custom Layout 구현의 필요성 (Why)
표준 `Column`과 `Row`만 중첩하여 복잡한 화면을 설계하려 할 때:
- **불필요한 노드 중첩**: 깊은 계층의 LayoutNode 트리가 형성되어 메모리 점유율과 렌더링 연산량이 증가함.
- **배치 한계**: 자식 간 커스텀 오프셋 계산(예: 텍스트의 베이스라인 오프셋 정렬)이 불가능함.

`Custom Layout`을 활용하면 단일 커스텀 노드 레벨에서 모든 자식을 한 번에 배치하므로 노드 트리를 획기적으로 평탄화(Flattening)할 수 있다.

---

### 3. MeasurePolicy 구현 메커니즘 (How)

```
[Layout 함수 실행]
         |
         v
[MeasureScope 블록 진입] (measurables: List<Measurable>, constraints: Constraints)
         |
         v
[1. 자식 노드 측정 (Measurement)]
  val placeable = measurable.measure(childConstraints)
         |
         v
[2. 부모 자신의 (width, height) 계산]
         |
         v
[3. layout(width, height) 호출 및 배치 (Placement)]
  layout(width, height) {
      placeable.placeRelative(x, y) // RTL 자동 지원 배치
  }
```

1. **Measurable to Placeable**: `Measurable`은 아직 측정되지 않은 자식 컴포넌트이며, `measure(constraints)`를 호출하는 순간 고정된 크기를 가진 `Placeable` 객체로 변환된다.
2. **`layout(w, h)` 및 `placeRelative`**: `MeasureScope.layout()` 블록 내부에서 `placeRelative(x, y)`를 사용해야 오른쪽에서 왼쪽으로 읽는 언어 설정(RTL, Right-To-Left) 환경에서도 자식 좌표가 자동으로 반전 계산되어 안전하게 표시된다.

---

### 4. 수직 수평 커스텀 대각선 레이아웃 구현 예시

```kotlin
@Composable
fun DiagonalLayout(
    modifier: Modifier = Modifier,
    spacing: Dp = 8.dp,
    content: @Composable () -> Unit
) {
    Layout(
        content = content,
        modifier = modifier
    ) { measurables, constraints ->
        val spacingPx = spacing.roundToPx()

        // 1. 모든 자식을 1회 측정
        val placeables = measurables.map { measurable ->
            measurable.measure(constraints)
        }

        // 2. 전체 부모 너비 및 높이 계산 (대각선 배치 누적)
        val totalWidth = placeables.sumOf { it.width } + (placeables.size - 1) * spacingPx
        val totalHeight = placeables.sumOf { it.height } + (placeables.size - 1) * spacingPx

        // 3. 자식 좌표 누적 배치
        layout(
            width = totalWidth.coerceIn(constraints.minWidth, constraints.maxWidth),
            height = totalHeight.coerceIn(constraints.minHeight, constraints.maxHeight)
        ) {
            var currentX = 0
            var currentY = 0

            placeables.forEach { placeable ->
                placeable.placeRelative(x = currentX, y = currentY)
                currentX += placeable.width + spacingPx
                currentY += placeable.height + spacingPx
            }
        }
    }
}
```

---

상위 문서: [Compose Layout, Animation, Accessibility 지침서](compose-layout-animation-accessibility.md)

관련 노트: [Compose layout measures children under parent constraints](compose-layout-constraints.md), [Intrinsic measurement and SubcomposeLayout solve special measurement problems](intrinsic-measurements-subcompose.md)

출처: [Custom layouts](https://developer.android.com/develop/ui/compose/layouts/custom)

검증일: 2026-08-05. Compose 공식 가이드의 Custom layout 섹션을 대조하여 MeasurePolicy 구현, Measurable->Placeable 변환 및 RTL 대응 placeRelative 알고리즘 서술을 정밀 보강했다.
