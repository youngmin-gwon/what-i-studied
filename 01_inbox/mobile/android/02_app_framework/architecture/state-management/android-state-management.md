---
title: android-state-management
tags: [android, android/architecture, android/state-management]
aliases: ["Android 상태 관리 정본 지도"]
date modified: 2026-08-03 17:28:07 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android 상태 관리 정본 지도

이 폴더는 Android 화면 상태 관리의 정본 노트를 모은다. 기존의 긴 설명형 노트는 이곳의 의미 단위 노트로 흡수하고, 기존 경로는 가능한 한 짧은 경유 노트로 남긴다.

### 읽는 순서

1. [ViewModel은 화면 단위 상태와 외부 작업을 조율한다](viewmodel-screen-orchestration.md)
2. [UI는 상태를 아래로 받고 사용자 행동을 위로 전달한다](unidirectional-data-flow.md)
3. [UiState는 새 collector가 받아도 안전한 현재 화면의 표현이다](uistate-screen-representation.md)
4. [StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다](../../async-flow/flow-state/stateflow-vs-flow.md)
5. [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](../../jetpack-compose/state-and-effects/launched-effect.md)

### 하위 지도

- [Android ViewModel](viewmodel.md)
- [Android UI State](ui-state.md)
- [Android Reducer](reducer.md)
- [Flow와 StateFlow 상태 계약](../../async-flow/flow-state/flow-state.md)
- [Compose 상태와 Effect 계약](../../jetpack-compose/state-and-effects/compose-state-and-effect.md)
