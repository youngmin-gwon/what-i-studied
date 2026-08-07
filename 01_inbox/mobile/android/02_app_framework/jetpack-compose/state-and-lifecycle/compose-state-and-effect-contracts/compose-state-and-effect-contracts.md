---
title: compose-state-and-effect-contracts
tags: [android, compose/state, jetpack-compose]
aliases: [Compose 상태와 Effect 계약]
date modified: 2026-08-05 13:49:44 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose 상태와 Effect 계약

Compose 상태 API 와 부작용(Side Effect) 관리 API 는 **데이터의 보유 수명주기(Lifetime)** 와 **작업의 소유자(Owner)** 를 기준으로 엄격히 선택되어야 한다. 이 묶음은 `remember`, `rememberSaveable`, `LaunchedEffect`, `DisposableEffect`, `produceState`, `snapshotFlow` 등 핵심 상태/이펙트 API 의 정본 계약을 바인딩한다.

---

### 수명주기별 상태 및 이펙트 선택 매트릭스 (What / Why / How)

1. **Composition 수명 (Transient UI State)**
   - **API**: `remember { mutableStateOf(…) }`, `rememberCoroutineScope()`, `DisposableEffect`
   - **특징**: Composable 이 화면 트리에 존재하는 동안만 유지됨. 화면 이탈 시 즉시 메모리 파괴.

2. **프로세스 재창조 수명 (Restorable Local UI State)**
   - **API**: `rememberSaveable { mutableStateOf(…) }`
   - **특징**: 화면 회전(Activity Recreation) 및 시스템 프로세스 종료(Process Death) 시에도 Bundle 을 통해 상태 보존.

3. **화면 수명 (Screen/Business State)**
   - **API**: `ViewModel`, `SavedStateHandle`, `collectAsStateWithLifecycle()`
   - **특징**: 화면 설정 변경에도 유지되며 도메인 데이터와 비즈니스 로직을 연결.

---

### 정본 계약 목록

- [Compose 상태 API는 필요한 수명에 맞춰 선택한다](./compose-state-api-selection-by-lifetime.md)
- [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](./launched-effect-owns-composable-cancellable-work.md)
- [등록과 해제가 쌍인 작업은 DisposableEffect로 관리한다](./disposable-effect-pairs-registration-and-cleanup.md)
- [produceState는 외부 상태를 Compose 상태로 변환한다](./produce-state-converts-external-state-to-compose-state.md)
- [rememberCoroutineScope는 수동 제어 UI Coroutine을 소유한다](./remember-coroutine-scope-owns-manually-controlled-ui-coroutines.md)
- [Composable 수명보다 오래 필요한 작은 복원 상태에만 rememberSaveable을 사용한다](./remember-saveable-is-for-small-restorable-ui-state.md)
- [rememberUpdatedState는 effect를 최신 값으로 유지한다](./remember-updated-state-keeps-effect-on-latest-value.md)
- [snapshotFlow는 Compose 상태를 Cold Flow로 변환한다](./snapshot-flow-converts-compose-state-to-cold-flow.md)
- [UI controller와 effect runner는 ViewModel이 아니라 UI 수명에 둔다](./ui-controllers-and-effect-runners-live-with-ui-lifetime.md)
- [ViewModel의 StateFlow는 collectAsStateWithLifecycle로 화면 상태로 변환한다](../../../stateflow-and-sharedflow.md)-becomes-screen-state-with-lifecycle-collection.md)

---

관련 상위 문서: [Jetpack Compose 런타임과 상태 모델의 기본 개념](../../runtime/compose-runtime-and-state-model.md)

검증일: 2026-08-05. Compose State & Side Effect 공식 가이드를 기반으로 수명주기 매트릭스와 계약 목록 구조 서술을 정밀 보강했다.
