---
title: "Compose 상태 API는 필요한 수명에 맞춰 선택한다"
tags: ["android", "android/app-framework"]
---

# Compose 상태 API는 필요한 수명에 맞춰 선택한다

상위 문서: [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)


Compose 상태 API의 첫 선택 기준은 타입이나 편의성이 아니라 수명이다.

## 판단 기준

1. 이 값이 recomposition 사이에만 필요하면 `remember`를 선택한다.
2. 이 값이 Composable이 composition에 있는 동안만 필요하면 UI 내부에 둔다.
3. Activity 재생성이나 process death 뒤에도 작은 값이 복원되어야 하면 `rememberSaveable`을 검토한다.
4. 여러 Composable이 함께 읽거나 바꿔야 하면 공통 부모로 상태를 hoist한다.
5. 화면 또는 navigation destination보다 오래 살아야 하면 ViewModel이나 상위 owner로 올린다.
6. 앱 재시작 뒤에도 보존해야 하면 DataStore, Room, repository 같은 영속 계층을 선택한다.

## API 선택표

| 필요 수명 | 기본 선택 | 적합한 예 |
| --- | --- | --- |
| recomposition 사이 | `remember` | 펼침 여부, 비밀번호 표시 |
| Composable 수명 | `remember`, UI effect | 임시 애니메이션, UI callback |
| 구성 변경·복원 | `rememberSaveable` | 입력 초안, 탭 key |
| 화면 상태 | ViewModel 또는 state holder | 로딩·성공·오류 상태 |
| 화면 표시 중 Flow 수집 | `collectAsStateWithLifecycle` | `StateFlow<UiState>` |
| 등록과 해제 | `DisposableEffect` | observer, listener |
| key에 따른 coroutine | `LaunchedEffect` | 화면 진입 로드, snackbar |

상태를 오래 살리고 싶다면 현재 Composable에 억지로 보관하지 말고 owner를 높인다.
반대로 UI가 사라질 때 함께 버려야 하는 값은 상위 계층으로 올리지 않는다.

`remember`는 값을 기억하지만 영속 저장소가 아니다.
`rememberSaveable`은 작은 UI 복원 장치이지 도메인 데이터베이스가 아니다.
`ViewModel`은 Composable의 재구성에 흔들리지 않는 화면 상태 owner다.

## Effect 선택도 같은 기준을 따른다

상태 변화나 composition 진입에 맞춰 비동기 작업을 시작해야 하면 [`LaunchedEffect`](https://developer.android.com/develop/ui/compose/side-effects#launchedeffect)를 선택한다.
등록한 자원을 반드시 해제해야 하면 [`DisposableEffect`](https://developer.android.com/develop/ui/compose/side-effects#disposableeffect)를 선택한다.
클릭 시 UI 작업을 시작해야 하면 [`rememberCoroutineScope`](https://developer.android.com/develop/ui/compose/side-effects#remembercoroutinescope)를 선택한다.
화면이 보일 때만 Flow를 읽어야 하면 [`collectAsStateWithLifecycle`](https://developer.android.com/develop/ui/compose/state#other-supported-types-of-state)을 선택한다.

Composable 본문에서 네트워크 요청, listener 등록, 저장 작업을 직접 실행하지 않는다.
본문은 선언하고, effect는 수명에 맞춰 외부 작업을 실행한다.

## 최소 규칙

- 상태의 의미보다 먼저 상태의 owner를 정한다.
- key가 바뀌면 다시 시작되어야 하는 effect에는 그 key를 넣는다.
- 화면을 떠난 뒤에도 필요한 작업은 Compose effect에 숨기지 않는다.
- 여러 화면이 공유하는 값은 한 Composable의 `remember`에 가두지 않는다.
- 큰 데이터와 민감한 데이터는 `rememberSaveable`에 넣지 않는다.

참고: [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state), [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
