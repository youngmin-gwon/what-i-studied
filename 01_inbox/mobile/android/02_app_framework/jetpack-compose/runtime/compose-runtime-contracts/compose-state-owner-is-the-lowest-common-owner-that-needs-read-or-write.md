---
title: compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write
tags: [android, compose/runtime, jetpack-compose]
aliases: [state down events up, state hoisting]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose State Owner 는 읽거나 쓰는 최하위 공통 소유자다

Compose 에서 state 는 읽고 쓰는 Composable 들의 가장 낮은 공통 owner 에 둔다. 한 Composable 안에서만 쓰는 임시 UI state 는 local `remember`, 여러 child 가 함께 쓰는 state 는 공통 부모, business rule 이 들어간 screen UI state 는 ViewModel 같은 screen-level state holder 가 후보가 된다.

값은 아래로 전달하고 event 는 위로 올린다. 이 흐름은 Composable 을 stateless 에 가깝게 만들고, 테스트와 재사용성을 높인다.

모든 state 를 ViewModel 로 올리는 것도, 모든 state 를 `remember` 에 가두는 것도 안티패턴이 될 수 있다. owner 선택은 수명, business logic, 공유 범위, 복원 필요성으로 결정한다.

```kotlin
// owner: 부모 Composable. 값은 아래로, event는 위로.
@Composable
fun LoginForm() {
    var email by remember { mutableStateOf("") }
    EmailField(value = email, onValueChange = { email = it })
}

@Composable
fun EmailField(value: String, onValueChange: (String) -> Unit) {
    TextField(value = value, onValueChange = onValueChange) // state를 직접 갖지 않는다
}
```

`EmailField` 는 자체 `remember` state 가 없으므로 재사용과 테스트가 쉽고, `email` 을 읽고 쓰는 최소 공통 owner 는 `LoginForm` 하나로 명확하다.

관련 노트: [Compose 상태 API는 필요한 수명에 맞춰 선택한다](../../state-and-lifecycle/compose-state-and-effect-contracts/compose-state-api-selection-by-lifetime.md), [Android 상태 관리 정본 지도](../../../architecture/state-management/android-state-management.md)

출처: [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting), [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
