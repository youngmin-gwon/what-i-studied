---
title: value-animation-transitions
tags: [android, compose/ui, jetpack-compose]
aliases: [Animatable, animateAsState, updateTransition]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Value animation APIs separate single target transition infinite and coroutine control

### 1. 개념 정의 (What)
값 기반 애니메이션(Value Animation) API들은 **(1) 단일 값 상태 보간(`animate*AsState`), (2) 다중 상태 트랜지션 동기화(`updateTransition`), (3) 무한 반복 애니메이션(`rememberInfiniteTransition`), (4) 코루틴 기반 명령형 제어(`Animatable`)**의 4가지 역할 분담 모델로 정밀히 분리되어 동작하는 가치 보간 엔진이다.

---

### 2. 역할 분담 API 구조의 필요성 (Why)
다양한 모션 요구사항에 맞춤형 제어 메커니즘이 필요하다:
- **`animate*AsState`**: 단순 fire-and-forget 스타일의 단일 속성 보간에 최적화됨.
- **`updateTransition`**: 여러 속성(크기, 색상, 알파, 회전)이 하나의 상태(State) 변경에 발맞추어 한 몸처럼 동기화되어 움직여야 할 때.
- **`Animatable`**: 제스처 드래그 손가락 떼기 시 초기 속도(Velocity)를 이관받아 `snapTo` 또는 `animateTo`로 물리 연산을 연속 제어해야 할 때.

API별 특성을 명확히 구분하여 모션 동기화 실패 및 제스처 튀어오름 현상을 완전 방지한다.

---

### 3. 주요 Value Animation API 세부 메커니즘 (How)

```
+--------------------------+---------------------------------------------------+
| API                      | 주요 사용 목적 및 내부 특징                        |
+--------------------------+---------------------------------------------------+
| animate*AsState          | - 단일 값 변경 감지 시 자동 보간                   |
|                          | - 선언적 fire-and-forget 방식                      |
+--------------------------+---------------------------------------------------+
| updateTransition         | - 다중 속성을 단일 트랜지션 객체로 묶어 동기화     |
|                          | - AnimatedVisibility 하위 삽입 연동 가능          |
+--------------------------+---------------------------------------------------+
| rememberInfiniteTransition| - 무한 루프 애니메이션 (로딩 펄스, 회전 셰이프)     |
+--------------------------+---------------------------------------------------+
| Animatable               | - 코루틴 수동 명령형 제어 (snapTo, animateTo)      |
|                          | - initialVelocity 속도 전달 물리 제스처 연동       |
+--------------------------+---------------------------------------------------+
```

---

### 4. updateTransition 및 Animatable 구현 비교

```kotlin
enum class CardState { Collapsed, Expanded }

// ✅ 1. updateTransition: 다중 속성 동기화 애니메이션
@Composable
fun SyncTransitionCard(cardState: CardState) {
    val transition = updateTransition(targetState = cardState, label = "CardTransition")

    val cardElevation by transition.animateDp(label = "Elevation") { state ->
        when (state) {
            CardState.Collapsed -> 2.dp
            CardState.Expanded -> 12.dp
        }
    }
    val cardBorderAlpha by transition.animateFloat(label = "Alpha") { state ->
        when (state) {
            CardState.Collapsed -> 0.2f
            CardState.Expanded -> 1.0f
        }
    }

    Card(
        elevation = CardDefaults.cardElevation(defaultElevation = cardElevation),
        border = BorderStroke(1.dp, Color.Black.copy(alpha = cardBorderAlpha)),
        modifier = Modifier.size(200.dp)
    ) {
        Text("State: $cardState")
    }
}

// ✅ 2. Animatable: 코루틴 기반 제스처 수동 연동
@Composable
fun GestureAnimatableDemo() {
    val offset = remember { Animatable(0f) }
    val scope = rememberCoroutineScope()

    Box(
        modifier = Modifier
            .offset { IntOffset(offset.value.toInt(), 0) }
            .pointerInput(Unit) {
                detectTapGestures {
                    scope.launch {
                        // snapTo 로 즉시 이동 후 animateTo 로 반환
                        offset.snapTo(100f)
                        offset.animateTo(0f, spring(stiffness = Spring.StiffnessMedium))
                    }
                }
            }
            .size(80.dp)
            .background(Color.Green)
    )
}
```

---

상위 문서: [Compose Layout, Animation, Accessibility 지침서](compose-layout-animation-accessibility.md)

관련 노트: [Compose animation API is selected by change unit and control level](compose-animation-apis.md), [AnimationSpec defines time physics and repeat policy](animation-spec-physics.md)

출처: [Value-based animations in Compose](https://developer.android.com/develop/ui/compose/animation/value-based)

검증일: 2026-08-05. Compose 공식 가이드의 Value-based animation 사양을 대조하여 updateTransition 동기화, Animatable 코루틴 스냅 및 animate*AsState 비교 서술을 정밀 보강했다.
