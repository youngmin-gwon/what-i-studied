---
title: value-animation-apis-separate-single-target-transition-infinite-and-coroutine-control
tags: [android, compose/ui, jetpack-compose]
aliases: [Animatable, animateAsState, updateTransition]
date modified: 2026-08-03 18:10:35 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Value animation APIs separate single target transition infinite and coroutine control

`animate*AsState` 는 단일 target value 를 상태처럼 관찰해 자동 보간한다. 별도 lifecycle 제어가 거의 필요 없고 target 만 바뀌는 간단한 값에 맞다.

`updateTransition` 은 하나의 state change 에 여러 animated value 가 함께 반응해야 할 때 쓴다. `rememberInfiniteTransition` 은 loading shimmer 처럼 composition 에 있는 동안 계속 반복되는 값을 만든다.

`Animatable` 은 coroutine 에서 `animateTo`, `snapTo`, `animateDecay` 같은 명령을 직접 호출해 gesture, cancellation, interruption, sequential animation 을 제어할 때 쓴다. 이 경우 작업 owner 와 cancellation 은 effect/coroutine scope 와 함께 설계한다.

관련 노트: [AnimationSpec은 시간, 물리, 반복 정책을 정의한다](./animation-spec-defines-time-physics-and-repeat-policy.md), [사용자 이벤트로 시작하고 수동 제어할 coroutine은 rememberCoroutineScope로 실행한다](../../state-and-lifecycle/compose-state-and-effect-contracts/remember-coroutine-scope-owns-manually-controlled-ui-coroutines.md)

출처: [Value-based animations](https://developer.android.com/develop/ui/compose/animation/value-based), [Animation quick guide](https://developer.android.com/develop/ui/compose/animation/quick-guide)
