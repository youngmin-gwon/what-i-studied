---
title: composable-body-must-be-fast-idempotent-and-side-effect-free
tags: [android, compose/runtime, jetpack-compose]
aliases: [side-effect free composable]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Composable body 는 빠르고 멱등하며 side effect 가 없어야 한다

Composable body 는 같은 입력으로 여러 번 실행되어도 같은 UI 설명을 만들어야 한다. DB write, analytics 전송, preference update, repository mutation 처럼 외부에 관찰 가능한 변경을 본문에 넣으면 skip, retry, cancel, 재실행 타이밍에 따라 결과가 흔들린다.

무거운 작업도 본문에 두지 않는다. Compose 는 Composable 을 자주 다시 호출할 수 있으므로 storage read, 큰 list sort, blocking I/O 는 jank 를 만들 수 있다.

외부 작업은 callback 에서 app logic 으로 전달하거나, composition 수명과 맞는 effect API 로 옮긴다. 이 원칙은 purity 라는 미학이 아니라 Runtime 최적화와 correctness 를 위한 실행 계약이다.

```kotlin
// 위반: 본문 실행마다 analytics 가 다시 전송될 수 있다
@Composable
fun ProfileScreen(userId: String) {
    analytics.logScreenView(userId) // recomposition마다 재실행 위험
    Text("Profile $userId")
}

// 수정: 본문은 선언만 하고, 부수효과는 key가 있는 effect로 옮긴다
@Composable
fun ProfileScreen(userId: String) {
    LaunchedEffect(userId) { analytics.logScreenView(userId) }
    Text("Profile $userId")
}
```

첫 번째 코드는 recomposition 이 일어날 때마다(예: 다른 state 변경으로 이 scope 가 재실행될 때) `logScreenView` 가 중복 호출될 수 있다. `LaunchedEffect(userId)` 로 옮기면 `userId` 가 바뀔 때만 한 번 실행된다.

관련 노트: [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](../../state-and-lifecycle/compose-state-and-effect-contracts/launched-effect-owns-composable-cancellable-work.md), [무거운 작업은 composition 안에 두지 않는다](../../performance/compose-performance-contracts/heavy-work-does-not-belong-in-composition.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model), [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)
