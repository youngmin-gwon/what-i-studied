---
title: "등록과 해제가 쌍인 작업은 DisposableEffect로 관리한다"
tags: ["android", "android/app-framework"]
---

# 등록과 해제가 쌍인 작업은 DisposableEffect로 관리한다

상위 문서: [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)


외부 시스템에 등록한 listener, observer, callback은 같은 수명 안에서 반드시 해제해야 한다.
이런 작업은 `DisposableEffect`로 감싼다.

## 동작

`DisposableEffect`는 composition에 들어오면 등록 블록을 실행한다.
key가 바뀌면 기존 effect의 `onDispose`를 먼저 실행하고 새 등록을 수행한다.
Composable이 composition에서 제거되면 `onDispose`가 실행된다.

```kotlin
@Composable
fun ObserveLifecycle(owner: LifecycleOwner, onEvent: (Lifecycle.Event) -> Unit) {
    DisposableEffect(owner) {
        val observer = LifecycleEventObserver { _, event -> onEvent(event) }
        owner.lifecycle.addObserver(observer)
        onDispose { owner.lifecycle.removeObserver(observer) }
    }
}
```

등록에 사용한 동일한 객체를 해제에 사용해야 한다.
key에는 등록 대상의 identity와 effect 동작을 바꾸는 값을 넣는다.
등록 대상이 바뀌면 이전 대상에서 해제하고 새 대상에 다시 등록되어야 한다.

## 적합한 작업

- `LifecycleObserver` 등록과 제거
- 센서 callback 등록과 해제
- 외부 SDK attach와 detach
- BroadcastReceiver 등록과 해제
- window, back handler, listener의 수명 연결

정리할 자원이 없다면 `DisposableEffect`를 선택하지 않는다.
단순한 외부 상태 동기화에는 [`SideEffect`](https://developer.android.com/develop/ui/compose/side-effects#sideeffect)를 검토한다.
coroutine의 시작과 취소가 핵심이면 [`LaunchedEffect`](https://developer.android.com/develop/ui/compose/side-effects#launchedeffect)가 맞다.

## UI 수명 경계

등록한 객체가 UI controller라면 Composable 또는 별도 UI state holder가 소유한다.
ViewModel이 `NavController`, `SnackbarHostState`, `FocusRequester` 같은 UI 객체를 장기 보관하지 않게 한다.
등록이 화면 전체 수명에 걸쳐야 한다면 effect를 너무 작은 child Composable 안에 두지 않는다.

`DisposableEffect`는 등록·해제의 누락을 줄이지만, 등록 대상의 thread-safety나 callback 중복까지 자동으로 해결하지 않는다.
callback에서 최신 값을 읽어야 하면 key를 불필요하게 바꾸기보다 `rememberUpdatedState`를 사용한다.

## 체크리스트

- 등록과 해제가 한 effect 안에 함께 있는가?
- `onDispose`가 등록에 사용한 동일한 객체를 해제하는가?
- 대상이 바뀌었을 때 key가 effect를 재생성하는가?
- UI 전용 객체가 ViewModel로 새어 나가지 않는가?
- dispose 이후 callback이 더 이상 UI를 만지지 않는가?

참고: [DisposableEffect](https://developer.android.com/develop/ui/compose/side-effects#disposableeffect), [Lifecycle in Jetpack Compose](https://developer.android.com/topic/libraries/architecture/lifecycle)
