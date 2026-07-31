---
title: Compose animation API is selected by change unit and control level
tags: [android, jetpack-compose, compose/ui]
aliases: [Compose animation]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# Compose animation API is selected by change unit and control level

Compose animation API는 “상위 수준이 항상 좋다”가 아니라 무엇이 바뀌는지로 고른다. Visibility 변화는 `AnimatedVisibility`, content 교체는 `AnimatedContent`나 `Crossfade`, 크기 변화는 `animateContentSize`가 후보가 된다.

개별 value만 부드럽게 바꾸면 value animation API를 쓰고, 여러 property가 하나의 state transition에 묶이면 transition API를 쓴다. 코루틴에서 중단, snap, decay, gesture 연동을 직접 제어해야 하면 `Animatable`이 후보가 된다.

Animation 선택은 UX 의도, 상태 owner, 취소 규칙, frame cost를 함께 본다. API 목록을 외우는 것보다 변경 단위와 제어 수준을 먼저 정한다.

관련 노트: [값 애니메이션 API는 단일 target, transition, infinite, coroutine 제어로 나뉜다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/value-animation-apis-separate-single-target-transition-infinite-and-coroutine-control.md), [Compose 성능 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)

출처: [Choose an animation API](https://developer.android.com/develop/ui/compose/animation/choose-api)
