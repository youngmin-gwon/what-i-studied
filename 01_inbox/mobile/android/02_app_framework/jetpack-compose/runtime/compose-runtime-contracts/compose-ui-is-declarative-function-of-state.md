---
title: compose-ui-is-declarative-function-of-state
tags: [android, compose/runtime, jetpack-compose]
aliases: [Thinking in Compose, UI = f(state)]
date modified: 2026-08-03 18:10:57 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose UI 는 상태의 선언적 함수다

Compose 에서 UI 는 기존 View 객체를 찾아 setter 로 수정하는 대상이 아니라, 현재 state 를 입력으로 계산되는 선언적 결과다. Composable 은 data 를 받아 UI hierarchy 를 emit 하고, state 가 바뀌면 Compose 가 필요한 함수를 다시 호출해 새 설명을 만든다.

이 모델은 "화면 전체를 매번 다시 그린다"는 뜻이 아니다. 개념적으로는 화면을 현재 state 에서 다시 계산하지만, Runtime 은 변경과 관련된 scope 를 고르고 필요한 작업만 수행하려고 한다.

그래서 Composable 의 핵심 계약은 명령형 UI 조작이 아니라 current state description 이다. ViewModel, repository, effect 는 state 를 만들거나 외부 작업을 실행하는 owner 이고, Composable body 는 그 결과를 표현한다.

관련 노트: [Recomposition은 전체 UI redraw가 아니라 필요한 Composable scope 재실행이다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/recomposition-reruns-needed-composable-scopes-not-the-whole-ui.md), [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model)
