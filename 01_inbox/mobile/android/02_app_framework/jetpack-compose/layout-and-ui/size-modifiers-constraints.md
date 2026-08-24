---
title: size-modifiers-constraints
tags: [android, compose/ui, jetpack-compose]
aliases: [fillMaxSize, requiredSize, size modifier]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Size modifiers interpret requested size inside incoming constraints

### 1. 개념 정의 (What)
크기 조절 `Modifier`들(`size`, `fillMaxSize`, `wrapContentSize`, `requiredSize`, `widthIn`)은 고정된 픽셀 값을 직접 대입하는 것이 아니라, **상위 노드로부터 수신된 제약 조건(`Incoming Constraints`)을 해석하고 변형(Modify Constraints)하여 하위 노드로 전파하는 제약 인터프리터(Constraint Interpreter) 메커니즘**이다.

---

### 2. 제약 조건 변형 해석의 필요성 (Why)
부모 레이아웃(예: `maxWidth = 200.dp`인 제한적 부모) 내부에서 자식 컴포넌트가 `Modifier.size(300.dp)`를 요청하거나 `Modifier.fillMaxSize()`를 요구할 때:
- **유연한 존중 vs 강제 재정의**: 기본 `size` 연산자는 부모의 `maxWidth(200.dp)`를 존중하여 200.dp로 바운딩한다.
- **강제 오버라이드 필요성**: 반면 `requiredSize(300.dp)`는 부모의 제약 조건을 무시하고 자신이 요청한 300.dp를 부모 영역 바깥으로 밀어내며 강제 할당한다.

크기 모디파이어의 동작 특성을 명확히 파악하지 못하면 예상치 못한 자식 노드 잘림(Clipping)이나 레이아웃 왜곡 버그가 발생한다.

---

### 3. 주요 Size Modifier 동작 방식 비교 메커니즘 (How)

```
[Incoming Parent Constraints: 0 <= width <= 200.dp]

1. Modifier.size(300.dp)
   ---> Constraints 변형: minWidth = 200.dp, maxWidth = 200.dp (부모에 의해 Clamped!)

2. Modifier.requiredSize(300.dp)
   ---> Constraints 재정의: minWidth = 300.dp, maxWidth = 300.dp (부모 제약 강제 무시!)

3. Modifier.fillMaxSize()
   ---> Constraints 변형: minWidth = 200.dp, maxWidth = 200.dp (부모 최대 크기로 확장)

4. Modifier.wrapContentSize()
   ---> Constraints 변형: minWidth = 0.dp, maxWidth = 200.dp (최소 제약 해제하여 자식 크기에 맞춤)
```

---

### 4. Size Modifier 활용 코드 예시

```kotlin
@Composable
fun SizeModifierBehaviorDemo() {
    // 200.dp x 200.dp 제약 부모
    Box(
        modifier = Modifier
            .size(200.dp)
            .background(Color.Gray)
    ) {
        // 1. size(300.dp): 부모 max 200.dp 에 갇혀 200.dp 로 측정됨
        Box(
            modifier = Modifier
                .size(300.dp)
                .background(Color.Red.copy(alpha = 0.5f))
        )

        // 2. requiredSize(300.dp): 부모 max 제약을 뚫고 300.dp 로 강제 표시됨!
        Box(
            modifier = Modifier
                .requiredSize(300.dp)
                .background(Color.Blue.copy(alpha = 0.5f))
        )
    }
}
```

---

상위 문서: [Compose Layout, Animation, Accessibility 지침서](compose-layout-animation-accessibility.md)

관련 노트: [Compose layout measures children under parent constraints](compose-layout-constraints.md), [Modifier order changes layout draw and input wrappers](modifier-chain-order.md)

출처: [Constraints in Compose](https://developer.android.com/develop/ui/compose/layouts/constraints)

검증일: 2026-08-05. Compose 공식 가이드의 Constraints 섹션을 대조하여 size vs requiredSize, fillMaxSize 및 wrapContentSize 제약 변형 인터프리터 동작 서술을 정밀 보강했다.
