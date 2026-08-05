---
title: compose-state-api-selection-by-lifetime
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 16:53:16 +09:00
---

## Compose 상태 API 는 필요한 수명에 맞춰 선택한다

상위 문서: [Compose 상태와 Effect 계약](./compose-state-and-effect-contracts.md)
배경 지식: [프로세스 생명주기 및 상태](../../../../../../operating-systems/process-states-lifecycle.md)

Compose 상태 API 의 첫 선택 기준은 타입이나 편의성이 아니라 수명이다.

### 판단 기준

1. 이 값이 recomposition 사이에만 필요하면 `remember` 를 선택한다.
2. 이 값이 Composable 이 composition 에 있는 동안만 필요하면 UI 내부에 둔다.
3. Activity 재생성이나 process death 뒤에도 작은 값이 복원되어야 하면 `**rememberSaveable**(화면 회전이나 프로세스 재시작 후에도 Bundle을 통해 UI 상태를 복원해 주는 저장 API)` 을 검토한다.
4. 여러 Composable 이 함께 읽거나 바꿔야 하면 공통 부모로 상태를 hoist 한다.
5. 화면 또는 navigation destination 보다 오래 살아야 하면 ViewModel 이나 상위 owner 로 올린다.
6. 앱 재시작 뒤에도 보존해야 하면 DataStore, Room, repository 같은 영속 계층을 선택한다.

### API 선택표

| 필요 수명 | 기본 선택 | 적합한 예 |
| --- | --- | --- |
| recomposition 사이 | `remember` | 펼침 여부, 비밀번호 표시 |
| Composable 수명 | `remember`, UI effect | 임시 애니메이션, UI callback |
| 구성 변경·복원 | `rememberSaveable` | 입력 초안, 탭 key |
| 화면 상태 | ViewModel 또는 state holder | 로딩·성공·오류 상태 |
| 화면 표시 중 Flow 수집 | `collectAsStateWithLifecycle` | `StateFlow<UiState>` |
| 등록과 해제 | `**DisposableEffect**(Composition 진입 시 리소스를 등록하고 Composition 이탈이나 Key 변경 시 cleanup을 수행하는 Effect API)` | observer, listener |
| key 에 따른 coroutine | `**LaunchedEffect**(Composition 생명주기에 맞춰 코루틴 작업을 실행하고 Key 변경 또는 Composition 이탈 시 취소하는 Side-Effect API)` | 화면 진입 로드, snackbar |

상태를 오래 살리고 싶다면 현재 Composable 에 억지로 보관하지 말고 owner 를 높인다.

반대로 UI 가 사라질 때 함께 버려야 하는 값은 상위 계층으로 올리지 않는다.

`remember` 는 값을 기억하지만 영속 저장소가 아니다.

`rememberSaveable` 은 작은 UI 복원 장치이지 도메인 데이터베이스가 아니다.

`ViewModel` 은 Composable 의 재구성에 흔들리지 않는 화면 상태 owner 다.

### Effect 선택도 같은 기준을 따른다

상태 변화나 composition 진입에 맞춰 비동기 작업을 시작해야 하면 [`LaunchedEffect`](https://developer.android.com/develop/ui/compose/side-effects#launchedeffect) 를 선택한다.

등록한 자원을 반드시 해제해야 하면 [`DisposableEffect`](https://developer.android.com/develop/ui/compose/side-effects#disposableeffect) 를 선택한다.

클릭 시 UI 작업을 시작해야 하면 [`rememberCoroutine**Scope**(스코프 — 의존성 객체의 생명주기를 특정 DI 컨테이너 수명과 일치시켜 재사용을 제어하는 어노테이션)`](https://developer.android.com/develop/ui/compose/side-effects#remembercoroutinescope) 를 선택한다.

화면이 보일 때만 Flow 를 읽어야 하면 [`collectAsStateWithLifecycle`](https://developer.android.com/develop/ui/compose/state#other-supported-types-of-state) 을 선택한다.

Composable 본문에서 네트워크 요청, listener 등록, 저장 작업을 직접 실행하지 않는다.

본문은 선언하고, effect 는 수명에 맞춰 외부 작업을 실행한다.

### 최소 규칙

- 상태의 의미보다 먼저 상태의 owner 를 정한다.
- key 가 바뀌면 다시 시작되어야 하는 effect 에는 그 key 를 넣는다.
- 화면을 떠난 뒤에도 필요한 작업은 Compose effect 에 숨기지 않는다.
- 여러 화면이 공유하는 값은 한 Composable 의 `remember` 에 가두지 않는다.
- 큰 데이터와 민감한 데이터는 `rememberSaveable` 에 넣지 않는다.

참고: [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state), [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
