---
title: Compose UI is a declarative function of state
tags: [android, jetpack-compose, compose/runtime]
aliases: [UI = f(state), Thinking in Compose]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

Compose에서 UI는 기존 View 객체를 찾아 setter로 수정하는 대상이 아니라, 현재 state를 입력으로 계산되는 선언적 결과다. Composable은 data를 받아 UI hierarchy를 emit하고, state가 바뀌면 Compose가 필요한 함수를 다시 호출해 새 설명을 만든다.

이 모델은 “화면 전체를 매번 다시 그린다”는 뜻이 아니다. 개념적으로는 화면을 현재 state에서 다시 계산하지만, Runtime은 변경과 관련된 scope를 고르고 필요한 작업만 수행하려고 한다.

그래서 Composable의 핵심 계약은 명령형 UI 조작이 아니라 current state description이다. ViewModel, repository, effect는 state를 만들거나 외부 작업을 실행하는 owner이고, Composable body는 그 결과를 표현한다.

관련 노트: [Recomposition은 전체 UI redraw가 아니라 필요한 Composable scope 재실행이다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/recomposition-reruns-needed-composable-scopes-not-the-whole-ui.md), [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model)
