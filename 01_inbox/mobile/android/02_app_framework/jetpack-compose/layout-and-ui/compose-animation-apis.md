---
title: compose-animation-apis
tags: [android, compose/ui, jetpack-compose]
aliases: [Compose animation API selection, High-level vs Low-level Animation]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Compose animation API is selected by change unit and control level

### 1. 개념 정의 (What)
Compose의 애니메이션 API 패밀리는 단일 API로 통합되어 있지 않으며, **애니메이션을 적용하는 대상 단위(High-level Layout/Content 변경 vs Low-level 단일 값 보간)**와 **개발자의 제어 세분성 수준(Control Level)**에 따라 최적의 API 계층을 체계적으로 선택해야 하는 애니메이션 아키텍처 체계다.

---

### 2. 애니메이션 API 선택 계층의 필요성 (Why)
간단한 버튼 가시성 전환에 저수준 `Animatable` 코루틴 제어를 사용하면 코드가 지나치게 길어지고, 반대로 제스처 추종 애니메이션에 고수준 `AnimatedVisibility`를 적용하면 세분화된 물리 움직임을 제어할 수 없다.

적절한 API 레벨을 선택함으로써 코드 가독성, 개발 생산성 및 모션 성능의 최적 조화를 달성한다.

---

### 3. API 선택 트리 및 계층 구조 (How)

```
[애니메이션 대상 및 제어 수준 선택 트리]
                           |
            +--------------+--------------+
            |                             |
  [High-level Content 애니메이션]   [Low-level Value 애니메이션]
            |                             |
    +-------+-------+             +-------+-------+
    |               |             |               |
 [가시성 전환]   [콘텐츠 교체]  [단일 값 보간]  [다중 상태 동기화]
AnimatedVisibility  Crossfade /  animate*AsState updateTransition
               AnimatedContent                    |
                                            [코루틴 수동 제어]
                                               Animatable
```

1. **High-level Layout APIs**: `AnimatedVisibility`, `AnimatedContent`, `Crossfade` - UI 노드의 추가/제거 및 레이아웃 구조 변화를 자동 트랜지션 처리.
2. **Value-based APIs**: `animateFloatAsState`, `animateDpAsState` - 단일 값의 상태 변화에 따라 값을 시간에 따라 자동 보간.
3. **Multi-state Sync APIs**: `updateTransition` - 하나의 상태 변화에 반응하여 여러 개의 애니메이션 값(예: 알파, 크기, 회전)을 동기화하여 동시 구동.
4. **Low-level Imperative APIs**: `Animatable`, `TargetBasedAnimation` - 코루틴 제스처 추적, 핑퐁 모션, 커스텀 물리 효과 수동 제어.

---

### 4. API 선택 수준별 코드 비교 가이드

```kotlin
// ✅ 1. High-level: 컨텐츠 가시성 전환 (AnimatedVisibility)
@Composable
fun VisibilityAnimationDemo(visible: Boolean) {
    AnimatedVisibility(
        visible = visible,
        enter = fadeIn() + expandVertically(),
        exit = fadeOut() + shrinkVertically()
    ) {
        Text("Visible Content Card")
    }
}

// ✅ 2. Low-level Value: 단일 Dp 값 보간 (animateDpAsState)
@Composable
fun CornerRadiusAnimationDemo(isRound: Boolean) {
    val cornerRadius by animateDpAsState(
        targetValue = if (isRound) 32.dp else 4.dp,
        animationSpec = spring(stiffness = Spring.StiffnessLow)
    )

    Box(
        modifier = Modifier
            .size(100.dp)
            .clip(RoundedCornerShape(cornerRadius))
            .background(Color.Magenta)
    )
}
```

---

상위 문서: [Compose Layout, Animation, Accessibility 지침서](compose-layout-animation-accessibility.md)

관련 노트: [AnimationSpec defines time physics and repeat policy](animation-spec-physics.md), [Value animation APIs separate single target transition infinite and coroutine control](value-animation-transitions.md)

출처: [Animation in Compose](https://developer.android.com/develop/ui/compose/animation/introduction)

검증일: 2026-08-05. Compose 공식 가이드의 Animation API 선택 트리를 대조하여 High-level vs Low-level, updateTransition 및 Animatable 계층 구조 서술을 정밀 보강했다.
