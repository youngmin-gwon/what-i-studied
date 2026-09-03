---
title: event-stream-signals
tags: [android, android/architecture, android/state-management, android/ui-state]
aliases: ["Snackbar와 Navigation처럼 소비 시점이 중요한 신호만 이벤트 스트림으로 분리한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Snackbar 와 Navigation 처럼 소비 시점이 중요한 신호만 이벤트 스트림으로 분리한다

상위 문서: [Android UI State](ui-state.md)

### 핵심 주장

Snackbar 표시나 Navigation 실행처럼 수신한 순간 UI 동작을 일으키고 반복 재생하면 안 되는 신호는 event stream 으로 분리할 수 있다.

다만 모든 상태 변화를 이벤트로 보내면 새 collector 가 놓친 정보를 복구할 수 없으므로, 소비 시점이 중요한 신호에만 한정한다.

```kotlin
sealed interface SignInEvent {
    data class ShowSnackbar(val message: String) : SignInEvent
    data object NavigateHome : SignInEvent
}
```

[viewmodel](viewmodel.md) 은 이벤트를 발행하고, Composable 은 UI 실행기를 소유해 수집한다.

```kotlin
LaunchedEffect(viewModel) {
    viewModel.events.collect { event ->
        when (event) {
            is SignInEvent.ShowSnackbar -> snackbarHostState.showSnackbar(event.message)
            SignInEvent.NavigateHome -> onNavigateHome()
        }
    }
}
```

`SnackbarHostState` 와 `NavController` 는 event 를 실제 동작으로 소비하는 UI 계층에 둔다.

ViewModel 은 실행기 대신 목적을 전달한다.

### 분리하지 않을 것

- 로딩 중인지 여부
- 현재 입력값과 선택값
- 복원해야 하는 인증 단계
- 새 collector 도 알아야 하는 오류 상태

이 값들은 `UiState` 가 표현한다. event 는 상태의 대체 저장소가 아니라 소비가 발생한 순간에 의미가 있는 신호다.

[sharedflow](../../async-flow/flow-state/stateflow-and-sharedflow.md), Channel 같은 도구의 선택은 재전달 정책과 collector 수명까지 검토한 뒤 정한다.

### 이벤트를 설계하는 질문

- 같은 신호를 새 collector 가 다시 받아도 되는가?
- 신호를 소비하지 않으면 현재 화면이 잘못 표현되는가?
- 재전달, 중복 소비, collector 부재를 어떻게 처리할 것인가?

첫 질문에 예라고 답하면 `UiState` 가 더 적합할 가능성이 크다.

두 번째 질문에 예라고 답하면 event 가 유효할 수 있지만, 복원이 필요한 사실은 별도로 상태에 남긴다.

Navigation 목적지는 event 로 전달할 수 있어도, back stack 과 선택된 route 의 source of truth 는 navigation state 가 소유한다.

Snackbar 는 화면에 남겨야 하는 오류 문구와 달리, 표시 동작을 한 번 요청하는 signal 로 취급한다.

### 테스트 관점

ViewModel 테스트는 event 가 의도한 종류와 payload 를 발행하는지 확인한다.

Composable 테스트는 event 를 실제 snackbar 또는 navigation 호출로 소비하는지 확인하고, 실행기를 ViewModel 에 주입하지 않는다.
