---
title: remember-updated-state-keeps-effect-on-latest-value
tags: [android, compose/state, jetpack-compose]
aliases: [rememberUpdatedState]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## rememberUpdatedState 는 effect 를 최신 값으로 유지한다

`rememberUpdatedState` 는 long-lived effect 를 재시작하지 않으면서 effect 내부에서 최신 값을 읽어야 할 때 쓴다. 대표적인 경우는 timeout, lifecycle observer, 외부 callback 등록처럼 수명은 유지하되 callback lambda 만 최신이어야 하는 작업이다.

Effect key 에 넣어야 하는 값을 `rememberUpdatedState` 로 숨기면 안 된다. 값이 바뀔 때 작업 자체를 다시 시작해야 한다면 그 값은 key 가 되어야 한다.

따라서 이 API 의 질문은 "최신 값을 쓰고 싶은가"가 아니라 "이 값 변화가 effect 재시작 이유인가"다. 재시작 이유가 아니면 `rememberUpdatedState`, 재시작 이유면 key 를 선택한다.

```kotlin
@Composable
fun TimeoutMessage(onTimeout: () -> Unit) {
    val currentOnTimeout by rememberUpdatedState(onTimeout)
    LaunchedEffect(Unit) { // key가 Unit이므로 onTimeout이 바뀌어도 delay는 재시작되지 않는다
        delay(5000)
        currentOnTimeout() // 5초 뒤 시점의 최신 onTimeout을 호출한다
    }
}
```

`onTimeout` 을 `rememberUpdatedState` 없이 `LaunchedEffect` 안에서 직접 참조하면, 이 Composable 이 처음 만들어졌을 때의 람다를 그대로 capture 해서 5초 뒤에도 오래된 값을 호출한다. `rememberUpdatedState` 는 effect 를 재시작하지 않고도 실행 시점의 최신 `onTimeout` 을 읽게 해준다.

관련 노트: [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](./launched-effect-owns-composable-cancellable-work.md), [등록과 해제가 쌍인 작업은 DisposableEffect로 관리한다](./disposable-effect-pairs-registration-and-cleanup.md)

출처: [Side-effects in Compose - rememberUpdatedState](https://developer.android.com/develop/ui/compose/side-effects#rememberupdatedstate)
