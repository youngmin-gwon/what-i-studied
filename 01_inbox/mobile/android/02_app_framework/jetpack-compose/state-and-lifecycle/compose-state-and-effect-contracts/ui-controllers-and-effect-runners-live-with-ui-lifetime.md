---
title: ui-controllers-and-effect-runners-live-with-ui-lifetime
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:11:13 +09:00
date created: 2026-07-31 16:53:16 +09:00
---

## UI controller 와 effect runner 는 ViewModel 이 아니라 UI 수명에 둔다

상위 문서: [Compose 상태와 Effect 계약](./compose-state-and-effect-contracts.md)

UI controller 는 UI 트리와 직접 상호작용하는 객체다.

effect runner 는 화면 표시, lifecycle, composition 변화에 반응해 UI 작업을 실행하는 역할이다.

둘의 owner 는 ViewModel 보다 UI 수명에 두는 편이 정확하다.

### UI 수명에 둘 대상

- `SnackbarHostState`
- `DrawerState`, `SheetState`
- `LazyListState`
- `FocusRequester`
- `NavController`
- `LifecycleOwner` 에 등록되는 observer
- 화면 진입·이탈에 따라 취소되어야 하는 `LaunchedEffect`
- listener 등록과 해제를 묶는 `DisposableEffect`

이 객체들은 특정 composition, 화면, window 와 결합되어 있다.

ViewModel 이 이들을 보관하면 화면보다 오래 살아남거나, 재생성된 UI 와 이전 객체가 섞일 수 있다.

```kotlin
@Composable
fun Screen(viewModel: ScreenViewModel, onNavigate: (Destination) -> Unit) {
    val snackbar = remember { SnackbarHostState() }
    val state by viewModel.uiState.collectAsStateWithLifecycle()

    LaunchedEffect(Unit) {
        viewModel.events.collect { event ->
            when (event) {
                is UiEvent.ShowMessage -> snackbar.showSnackbar(event.text)
                is UiEvent.Navigate -> onNavigate(event.destination)
            }
        }
    }

    ScreenContent(state = state, snackbarHostState = snackbar)
}
```

ViewModel 은 화면 정책과 도메인 작업을 관리하고, UI 는 그 결과를 controller 와 effect 로 표현한다.

ViewModel 은 "snackbar 를 보여라"라는 의미 있는 이벤트를 보낼 수 있지만 `SnackbarHostState` 를 직접 호출하지 않는다.

ViewModel 은 navigation 목적지를 결정할 수 있지만 `NavController` 를 소유하지 않는다.

### 수명 선택

작업이 UI 가 사라지면 취소되어야 하면 `LaunchedEffect` 또는 UI scope 를 사용한다.

작업이 사용자의 클릭에서 시작되면 [`rememberCoroutineScope`](https://developer.android.com/develop/ui/compose/side-effects#remembercoroutinescope) 를 사용한다.

등록과 해제가 필요하면 [`DisposableEffect`](https://developer.android.com/develop/ui/compose/side-effects#disposableeffect) 를 사용한다.

화면 데이터의 장기 보존과 비즈니스 작업은 ViewModel 의 수명에 둔다.

이 경계는 ViewModel 을 배제하기 위한 규칙이 아니다.

각 작업이 실제로 누구와 함께 시작되고 끝나야 하는지를 코드에 반영하기 위한 규칙이다.

참고: [UI layer state holders](https://developer.android.com/topic/architecture/ui-layer/stateholders), [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)
