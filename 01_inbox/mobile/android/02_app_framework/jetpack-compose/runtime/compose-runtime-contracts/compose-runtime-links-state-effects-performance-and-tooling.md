---
title: Compose Runtime links state effects performance and tooling
tags: [android, jetpack-compose, compose/runtime]
aliases: [Compose boundary map]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

Compose Runtime 정본은 모든 API 사용법을 담는 곳이 아니다. Runtime은 state read, recomposition, Composition identity, phase 모델을 설명하고, 실제 API 선택은 더 좁은 정본으로 보낸다.

`remember`, `rememberSaveable`, ViewModel, `collectAsStateWithLifecycle` 선택은 state/effect 계약에 둔다. `LaunchedEffect`, `DisposableEffect`, `rememberCoroutineScope`, `produceState`, `snapshotFlow`는 side-effect와 외부 흐름 경계에서 설명한다.

Stability, strong skipping, state read deferral, `derivedStateOf`, heavy work 제거는 performance 계약에 둔다. Navigation, testing, debugging은 Compose Runtime 예시로 반복하지 않고 해당 분야 정본에 연결한다.

관련 노트: [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md), [Compose 성능 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)
