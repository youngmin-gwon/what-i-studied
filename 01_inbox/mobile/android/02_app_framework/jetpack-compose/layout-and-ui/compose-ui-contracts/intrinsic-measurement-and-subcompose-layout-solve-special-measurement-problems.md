---
title: intrinsic-measurement-and-subcompose-layout-solve-special-measurement-problems
tags: [android, compose/ui, jetpack-compose]
aliases: [Intrinsic measurement, SubcomposeLayout]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Intrinsic measurement and SubcomposeLayout solve special measurement problems

### 1. 개념 정의 (What)
고급 레이아웃 제어 기법인 **고유 크기 측정(Intrinsic Measurement)**과 **서브컴포지션 레이아웃(`SubcomposeLayout`)**은 단일 패스 측정 규칙을 우회하지 않으면서 특수한 레이아웃 측정 상호작용 문제를 해결하기 위한 **고급 렌더링 파이프라인 솔루션**이다.

---

### 2. Intrinsic & SubcomposeLayout의 필요성 (Why)
일반 Compose 단일 패스 레이아웃 모델에서는 두 자식 컴포넌트의 크기가 서로에게 종속되는 상황을 해결할 수 없다:
- **동적 가로 넓이 정렬 (Intrinsic)**: 두 개의 버튼 높이를 자식 중 더 긴 텍스트를 가진 버튼의 높이로 동적으로 맞추고 싶을 때, 자식을 직접 측정하기 전에 사전 크기 조회가 필요함.
- **측정 결과 기반 하위 Composition 결정 (`SubcomposeLayout`)**: `LazyColumn`처럼 주어진 화면 슬롯 크기(`Constraints`)를 측정한 결과에 따라 몇 개의 하위 Composable 아이템을 새로 컴포즈할지 결정해야 하는 경우.

이 두 도구는 단일 패스 레이아웃의 제약을 안전하게 준수하도록 돕는다.

---

### 3. 내부 동작 및 차이점 메커니즘 (How)

```
[1. Intrinsic Measurement (사전 고유 크기 조회)]
  부모가 직접 measure()를 호출하기 전, 자식의 minIntrinsicHeight / maxIntrinsicWidth 조회
  ---> 실제 자식 노드를 다중 측정하지 않고 예측된 계산값만 반환!

[2. SubcomposeLayout (지연 컴포지션)]
  Layout Phase 시작 
  ---> 부모 Constraints 측정 완료 
  ---> subcompose(slotId, content) 구동 
  ---> 즉석에서 Composition 생성 후 측정 및 배치!
```

1. **Intrinsic Measurement**: 자식 노드에게 "만약 너의 높이가 X라면 너의 너비는 몇인가?"를 질의하는 쿼리 패스로, 실제 노드를 2번 렌더링하지 않으므로 $O(2^N)$ 폭발을 일으키지 않는다.
2. **SubcomposeLayout 성능 주의사항**: `SubcomposeLayout`은 Composition과 Layout Phase를 결합하므로 일반 `Layout`보다 비싸다. 매 프레임마다 불필요하게 `subcompose`를 구동하면 성능이 저하된다 (`LazyColumn`, `BoxWithConstraints` 등에 한정 적용 권장).

---

### 4. Intrinsic Size와 SubcomposeLayout 활용 예시

```kotlin
// ✅ 1. Intrinsic Size 활용: 두 버튼의 높이를 가장 높은 텍스트에 동적으로 맞춤
@Composable
fun IntrinsicTwoButtons(
    modifier: Modifier = Modifier,
    leftText: String,
    rightText: String
) {
    // Modifier.height(IntrinsicSize.Min)으로 자식의 최소 고유 높이로 바운딩
    Row(modifier = modifier.height(IntrinsicSize.Min)) {
        Button(onClick = {}, modifier = Modifier.weight(1f).fillMaxHeight()) {
            Text(leftText)
        }
        Divider(color = Color.Black, modifier = Modifier.width(1.dp).fillMaxHeight())
        Button(onClick = {}, modifier = Modifier.weight(1f).fillMaxHeight()) {
            Text(rightText)
        }
    }
}

// ✅ 2. SubcomposeLayout 활용: 상단 헤더 크기를 측정한 뒤 하단 뷰 크기를 결정
@Composable
fun DynamicHeaderLayout(
    header: @Composable () -> Unit,
    body: @Composable (headerHeight: Dp) -> Unit,
    modifier: Modifier = Modifier
) {
    SubcomposeLayout(modifier = modifier) { constraints ->
        // 1. Header 슬롯 서브컴포즈 및 측정
        val headerPlaceables = subcompose("Header", header).map {
            it.measure(constraints)
        }
        val headerHeight = headerPlaceables.maxOfOrNull { it.height } ?: 0

        // 2. 측정된 headerHeight 크기를 인수로 넘겨 Body 슬롯 서브컴포즈
        val bodyPlaceables = subcompose("Body") {
            body(headerHeight.toDp())
        }.map {
            it.measure(constraints.copy(maxHeight = constraints.maxHeight - headerHeight))
        }

        layout(constraints.maxWidth, constraints.maxHeight) {
            headerPlaceables.forEach { it.placeRelative(0, 0) }
            bodyPlaceables.forEach { it.placeRelative(0, headerHeight) }
        }
    }
}
```

---

상위 문서: [Compose Layout, Animation, Accessibility 지침서](../compose-layout-animation-accessibility.md)

관련 노트: [Custom Layout measures and places children explicitly](./custom-layout-measures-and-places-children-explicitly.md), [Compose layout measures children under parent constraints](./compose-layout-measures-children-under-parent-constraints.md)

출처: [Custom layouts in Compose](https://developer.android.com/develop/ui/compose/layouts/custom)

검증일: 2026-08-05. Compose 공식 가이드의 Intrinsics 및 SubcomposeLayout 사양을 대조하여 IntrinsicSize.Min/Max 질의 알고리즘과 SubcomposeLayout 지연 컴포지션 서술을 정밀 보강했다.
