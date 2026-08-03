---
title: Recomposition은 전체 UI 재그리가 아니라 필요한 Composable scope 재실행이다
tags: [android, compose/runtime, jetpack-compose]
aliases: [Recomposition]
date modified: 2026-08-03 16:46:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

# Recomposition은 전체 UI 재그리가 아니라 필요한 Composable scope 재실행이다

Recomposition 은 입력이나 관찰 중인 state 변화에 대응해 Composable 함수를 다시 실행하는 과정이다. 다시 실행은 UI 전체 redraw 와 같지 않고, Compose 는 변경 가능성이 있는 함수나 lambda 만 실행하고 나머지는 skip 할 수 있다.

Recomposition 은 자주 일어날 수 있고, animation 중에는 매 frame 가까이 실행될 수 있다. 횟수 자체를 버그로 보지 말고, 실행되는 work 가 무겁거나 불필요하게 넓은지 측정해야 한다.

공식 mental model 은 recomposition 이 skip 될 수 있고, 낙관적으로 진행되며, Composable 실행 순서와 빈도에 의존하지 말아야 한다고 설명한다. 따라서 본문 실행을 외부 상태 변경의 트리거로 삼으면 안 된다.

관련 노트: [Composable body는 빠르고 idempotent하며 side-effect free 해야 한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-body-must-be-fast-idempotent-and-side-effect-free.md), [Compose 상태 읽기 위치는 recomposition 범위를 결정한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-state-read-location-controls-recomposition-scope.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model), [Lifecycle of composables](https://developer.android.com/develop/ui/compose/lifecycle)
