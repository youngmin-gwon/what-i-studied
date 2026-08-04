---
title: compose-state-and-effect-contracts
tags: [android, compose/state, jetpack-compose]
aliases: [Compose 상태와 Effect 계약]
date modified: 2026-08-03 18:11:05 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose 상태와 Effect 계약

Compose 상태 API 는 값의 수명과 작업의 owner 를 기준으로 고른다. `remember`, `rememberSaveable`, ViewModel, effect API 를 편의성 기준으로 섞지 않는다.

### 정본 노트

- [Compose 상태 API는 필요한 수명에 맞춰 선택한다](./compose-state-api-selection-by-lifetime.md)
- [Composable 수명보다 오래 필요한 작은 복원 상태에만 rememberSaveable을 사용한다](./remember-saveable-is-for-small-restorable-ui-state.md)
- [ViewModel의 StateFlow는 lifecycle-aware collection으로 화면 상태가 된다](./viewmodel-stateflow-becomes-screen-state-with-lifecycle-collection.md)
- [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](./launched-effect-owns-composable-cancellable-work.md)
- [등록과 해제가 쌍인 작업은 DisposableEffect로 관리한다](./disposable-effect-pairs-registration-and-cleanup.md)
- [사용자 이벤트로 시작하고 수동 제어할 coroutine은 rememberCoroutineScope로 실행한다](./remember-coroutine-scope-owns-manually-controlled-ui-coroutines.md)
- [Effect를 재시작하지 않고 최신 값을 읽어야 할 때 rememberUpdatedState를 사용한다](./remember-updated-state-keeps-effect-on-latest-value.md)
- [외부 비동기·구독 상태를 Compose State로 바꿀 때 produceState를 사용한다](./produce-state-converts-external-state-to-compose-state.md)
- [Compose State를 cold Flow로 바꿔 관찰·연산할 때 snapshotFlow를 사용한다](./snapshot-flow-converts-compose-state-to-cold-flow.md)
- [UI 컨트롤러와 Effect 실행기는 UI 수명에 둔다](./ui-controllers-and-effect-runners-live-with-ui-lifetime.md)

관련 Runtime 지도: [Compose runtime and state model](../../runtime/compose-runtime-and-state-model.md)

관련 상태 관리 지도: [Android 상태 관리 정본 지도](../../../architecture/state-management/android-state-management.md)

관련 성능 지도: [Compose 성능 계약](../../performance/compose-performance-contracts/compose-performance-contracts.md)
