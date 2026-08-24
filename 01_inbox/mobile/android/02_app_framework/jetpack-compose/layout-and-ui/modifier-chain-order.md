---
title: modifier-chain-order
tags: [android, compose/ui, jetpack-compose]
aliases: [Modifier order, Modifier chaining]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Modifier order changes layout draw and input wrappers

### 1. 개념 정의 (What)
`Modifier`의 체이닝 순서는 단순한 스타일 속성의 나열이 아니며, **각 Modifier 체인 요소가 상위 Wrapper 노드로 연결되어 측정(Measurement), 제약 조건 변경, 그래픽 그리기(Draw Scope), 사용자 패킷 입력(Pointer Input)을 감싸는 중첩 래퍼 트리를 순서대로 형성하는 구조적 메커니즘**이다.

---

### 2. Modifier 체이닝 순서의 중요성 (Why)
체이닝 순서에 따라 시각적 및 기능적 결과가 완전히 달라진다:
- `Modifier.padding(16.dp).clickable { ... }`: 패딩 영역을 **포함하여** 클릭 제스처가 감지됨.
- `Modifier.clickable { ... }.padding(16.dp)`: 패딩 영역을 **제외한** 터치 영역만 클릭 제스처가 감지됨.

동일한 `background`와 `padding`이라도 선후 순서에 따라 컴포넌트 외부 배경색이 칠해질지, 패딩 내부 콘텐츠 배경색이 칠해질지가 결정된다.

---

### 3. 내부 동작 및 체인 래핑 메커니즘 (How)

```
[Outer Modifier: Modifier.padding(16.dp)]
   |  Layout Phase: Constraints 여백 차감 후 하향 전달
   v
[Inner Modifier: Modifier.background(Color.Blue)]
   |  Draw Phase: 남은 영역에 파란색 배경 그리기
   v
[Content: Text("Hello")]
```

1. **Modifier Node Tree 구조**: Compose 1.3+부터 Modifier는 `Modifier.Node` 객체의 체인 구조체로 컴파일 타임 및 런타임에 인라인 래핑된다.
2. **측정 순서 (Top-down)**: 체인의 맨 왼쪽(Outer) Modifier부터 오른쪽(Inner) Modifier 방향으로 Constraints 제약 조건이 변형되어 내려간다.
3. **그리기 순서 (Bottom-up / Inside-out)**: 그리기 및 배치 패스에서는 Inner에서 Outer 방향으로 래퍼 스코프가 실행된다.

---

### 4. Modifier 순서 차이 비교 코드 사례

```kotlin
@Composable
fun ModifierOrderComparison() {
    Row(horizontalArrangement = Arrangement.spacedBy(16.dp)) {
        // 1. padding -> background -> size
        // 배경색이 패딩 안쪽 100x100 영역에만 칠해짐
        Box(
            modifier = Modifier
                .padding(16.dp)
                .background(Color.Red)
                .size(100.dp)
        )

        // 2. background -> padding -> size
        // 배경색이 패딩 영역을 포함한 전체 사각형에 칠해짐
        Box(
            modifier = Modifier
                .background(Color.Blue)
                .padding(16.dp)
                .size(100.dp)
        )
    }
}
```

---

상위 문서: [Compose Layout, Animation, Accessibility 지침서](compose-layout-animation-accessibility.md)

관련 노트: [Compose layout measures children under parent constraints](compose-layout-constraints.md), [Size modifiers interpret requested size inside incoming constraints](size-modifiers-constraints.md)

출처: [Compose modifiers](https://developer.android.com/develop/ui/compose/modifiers)

검증일: 2026-08-05. Compose 공식 가이드의 Modifier order 단락을 대조하여 Modifier.Node 체인 래핑, Top-down 제약 전달 및 터치/그리기 스코프 순서 영향 서술을 정밀 보강했다.
