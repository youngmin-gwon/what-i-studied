---
title: compose-runtime-links-state-effects-performance-and-tooling
tags: [android, compose/runtime, jetpack-compose]
aliases: [Compose boundary map]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose Runtime 은 State, Effect, 성능, 툴링 경계를 연결한다

Compose Runtime 정본은 모든 API 사용법을 담는 곳이 아니다. Runtime 은 state read, recomposition, Composition identity, phase 모델을 설명하고, 실제 API 선택은 더 좁은 정본으로 보낸다.

`remember`, `**rememberSaveable**(화면 회전이나 프로세스 재시작 후에도 Bundle을 통해 UI 상태를 복원해 주는 저장 API)`, ViewModel, `collectAsStateWithLifecycle` 선택은 state/effect 계약에 둔다. `**LaunchedEffect**(Composition 생명주기에 맞춰 코루틴 작업을 실행하고 Key 변경 또는 Composition 이탈 시 취소하는 Side-Effect API)`, `**DisposableEffect**(Composition 진입 시 리소스를 등록하고 Composition 이탈이나 Key 변경 시 cleanup을 수행하는 Effect API)`, `rememberCoroutine**Scope**(스코프 — 의존성 객체의 생명주기를 특정 DI 컨테이너 수명과 일치시켜 재사용을 제어하는 어노테이션)`, `**produceState**(Flow 같은 외부 비동기 데이터 스트림을 Compose State로 변환하여 공급하는 Effect API)`, `**snapshotFlow**(Compose State의 읽기 변화를 관찰하여 Cold Flow 스트림으로 변환하는 API)` 는 side-effect 와 외부 흐름 경계에서 설명한다.

Stability, strong skipping, state read deferral, `**derivedStateOf**(고빈도 입력 상태 변경 중 최종 결과값이 뒤집힐 때만 Recomposition 스코프를 무효화하는 파생 상태 생성 API)`, heavy work 제거는 performance 계약에 둔다. Navigation, testing, debugging 은 Compose Runtime 예시로 반복하지 않고 해당 분야 정본에 연결한다.

관련 노트: [Compose 상태와 Effect 계약](../../state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md), [Compose 성능 계약](../../performance/compose-performance-contracts/compose-performance-contracts.md)
