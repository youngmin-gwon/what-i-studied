---
title: launched-effect-owns-composable-cancellable-work
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:11:07 +09:00
date created: 2026-07-31 16:53:16 +09:00
---

## Composable 과 함께 취소되어야 하는 작업은 LaunchedEffect 로 시작한다

상위 문서: [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)

`LaunchedEffect` 는 composition 에 들어올 때 coroutine 을 시작하고, key 가 바뀌거나 Composable 이 사라지면 작업을 취소한다.

### 사용 기준

다음 조건을 모두 만족하는 작업에 적합하다.

- 작업의 시작점이 UI composition 또는 UI state 변화다.
- 작업이 특정 key 에 종속된다.
- key 가 바뀌면 이전 작업을 취소하고 새 작업을 시작해야 한다.
- Composable 이 제거되면 작업도 더 이상 의미가 없다.

```kotlin
@Composable
fun DetailRoute(itemId: String, onLoad: (String) -> Unit) {
    LaunchedEffect(itemId) {
        onLoad(itemId)
    }
}
```

`itemId` 가 바뀌면 기존 effect 가 취소되고 새 effect 가 시작된다.

화면 진입 시 한 번만 실행하는 작업은 고정 key 를 사용할 수 있지만, 실제로 고정 수명이 맞는지 확인한다.

effect 내부에서 읽는 값이 최신이어야 하면서 재시작은 피해야 한다면 [`rememberUpdatedState`](https://developer.android.com/develop/ui/compose/side-effects#rememberupdatedstate) 를 검토한다.

### 적합한 작업

- 화면 진입에 따른 UI-local 로드 트리거
- key 변경에 따른 검색 또는 미리보기 갱신
- snackbar, navigation 같은 일회성 UI 이벤트 처리
- animation 시작
- Compose 상태를 읽어 UI 수명 동안 관찰하는 작업

Composable 본문에서 suspend 함수를 직접 호출하지 않는다.

recomposition 마다 네트워크 요청이나 저장이 반복될 수 있기 때문이다.

### ViewModel 과의 경계

화면 데이터의 source of truth 와 장기 비즈니스 작업은 ViewModel 또는 repository 가 소유한다.

`LaunchedEffect` 는 그 작업을 UI 수명에 맞춰 요청하거나 UI 결과를 소비하는 경계로 둔다.

화면이 사라져도 끝까지 실행되어야 하는 저장·동기화 작업은 `LaunchedEffect` 에 두지 않는다.

```kotlin
@Composable
fun Screen(viewModel: ScreenViewModel) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    LaunchedEffect(Unit) {
        viewModel.onScreenEntered()
    }
    ScreenContent(state)
}
```

`LaunchedEffect` 는 effect 의 owner 를 Composable 로 만든다.

`viewModelScope` 는 작업의 owner 를 ViewModel 로 만든다.

둘 중 어떤 수명이 요구되는지 먼저 결정한다.

참고: [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects#launchedeffect), [Lifecycle-aware coroutines](https://developer.android.com/topic/libraries/architecture/coroutines)
