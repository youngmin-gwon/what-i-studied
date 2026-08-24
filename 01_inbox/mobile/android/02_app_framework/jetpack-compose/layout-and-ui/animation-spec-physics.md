---
title: animation-spec-physics
tags: [android, compose/ui, jetpack-compose]
aliases: [AnimationSpec, spring, tween, keyframes]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## AnimationSpec defines time physics and repeat policy

### 1. 개념 정의 (What)
`AnimationSpec<T>`는 애니메이션이 시작 값에서 목표 값으로 변화하는 **시간 곡선(Easing), 물리 기반 바운스(Physics-based Motion), 보간 알고리즘, 및 반복 정책(Repeat Policy)을 정의하는 핵심 인터페이스 및 설정 모델**이다.

---

### 2. AnimationSpec 분류의 필요성 (Why)
모든 애니메이션에 고정된 지속 시간(Duration) 기반 이징(Easing)을 적용하면 UI가 인위적이고 딱딱하게 느껴진다.
- **물리 기반 모션 (`spring`)**: 현실 세계의 스프링 질량-스프링-댐핑 물리 법칙을 모사하여, 사용자가 제스처를 멈췄을 때 속도의 연속성을 유지하면서 자연스러운 튕김(Bounce)을 제공한다.
- **시간 기반 모션 (`tween`)**: 특정 초(ms) 동안 일정한 보간 곡선(EaseIn, EaseOut)에 맞춰 진행된다.
- **키프레임 모션 (`keyframes`)**: 특정 시간(ms) 구간마다 정밀한 중간 지점 값과 이징 곡선을 할당한다.

상황에 맞는 `AnimationSpec`을 적용함으로써 자연스럽고 생동감 넘치는 사용자 경험을 연출한다.

---

### 3. 주요 AnimationSpec 세부 메커니즘 (How)

```
1. spring(dampingRatio, stiffness) [기본 최우선 물리 스펙]
   - dampingRatio: 튕김 정도 (DampingRatioHighBouncy, DampingRatioNoBouncy)
   - stiffness: 강성/속도 (StiffnessHigh, StiffnessLow, StiffnessVeryLow)
   - 특징: 지속 시간(Duration)을 정하지 않으며, 속도 연속성을 보장함!

2. tween(durationMillis, delayMillis, easing)
   - durationMillis: 진행 기간 지정 (예: 300ms)
   - easing: FastOutSlowInEasing, LinearOutSlowInEasing

3. keyframes { durationMillis = 1000; 0.dp at 0; 200.dp at 400 with FastOutLinearInEasing }

4. repeatable(iterations, animationSpec, repeatMode) / infiniteRepeatable(...)
```

---

### 4. AnimationSpec 적용 코드 예시

```kotlin
@Composable
fun AnimationSpecDemo(isExpanded: Boolean) {
    // 1. Spring Physics Spec: 자연스러운 스프링 모션 적용
    val springWidth by animateDpAsState(
        targetValue = if (isExpanded) 300.dp else 100.dp,
        animationSpec = spring(
            dampingRatio = Spring.DampingRatioMediumBouncy,
            stiffness = Spring.StiffnessLow
        )
    )

    // 2. Keyframes Spec: 정밀 타임라인 지정
    val keyframeAlpha by animateFloatAsState(
        targetValue = if (isExpanded) 1f else 0f,
        animationSpec = keyframes {
            durationMillis = 800
            0.0f at 0
            0.8f at 200 using LinearOutSlowInEasing
            0.2f at 600
            1.0f at 800
        }
    )

    Box(
        modifier = Modifier
            .width(springWidth)
            .height(80.dp)
            .alpha(keyframeAlpha)
            .background(Color.DarkGray)
    )
}
```

---

상위 문서: [Compose Layout, Animation, Accessibility 지침서](compose-layout-animation-accessibility.md)

관련 노트: [Compose animation API is selected by change unit and control level](compose-animation-apis.md), [Value animation APIs separate single target transition infinite and coroutine control](value-animation-transitions.md)

출처: [Customize Compose animations](https://developer.android.com/develop/ui/compose/animation/customize)

검증일: 2026-08-05. Compose 공식 가이드의 Customize animations 사양을 대조하여 spring, tween, keyframes, repeatable 모션 및 Easing 물리 모델 서술을 정밀 보강했다.
