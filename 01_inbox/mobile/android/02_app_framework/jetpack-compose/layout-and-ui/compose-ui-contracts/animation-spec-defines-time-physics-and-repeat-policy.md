---
title: AnimationSpec defines time physics and repeat policy
tags: [android, jetpack-compose, compose/ui]
aliases: [AnimationSpec, spring, tween]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

`AnimationSpec`은 animation이 어떤 시간·물리·반복 규칙으로 target에 도달할지 정의한다. `spring`은 물리 기반, `tween`은 duration/easing 기반, `keyframes`는 시점별 값 기반이다.

`repeatable`과 `infiniteRepeatable`은 반복 정책을 감싸고, `snap`은 보간 없이 즉시 값을 바꾼다. 기본 spec은 API마다 다를 수 있으므로 모든 Compose animation이 무조건 spring이라고 일반화하지 않는다.

Animation spec은 시각 느낌만이 아니라 frame budget과 접근성 선호에도 영향을 준다. 반복 animation과 큰 layout animation은 실제 device에서 측정한다.

관련 노트: [Compose animation API는 변경 단위와 제어 수준으로 선택한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/compose-animation-api-is-selected-by-change-unit-and-control-level.md), [Compose layout과 image 비용은 프레임 예산 안에서 관리한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-layout-and-image-cost-must-be-budgeted.md)

출처: [Customize animations](https://developer.android.com/develop/ui/compose/animation/customize)
