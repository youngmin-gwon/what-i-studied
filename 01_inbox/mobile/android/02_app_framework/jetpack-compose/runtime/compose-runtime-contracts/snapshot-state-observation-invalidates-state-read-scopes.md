---
title: snapshot-state-observation-invalidates-state-read-scopes
tags: [android, compose/runtime, jetpack-compose]
aliases: [Automatic State Observation, Snapshot State]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Snapshot State 관찰은 State 를 읽은 scope 를 무효화 대상으로 만든다

Compose Runtime 은 `MutableState` 같은 observable state 의 read 를 추적한다. 어떤 Composable scope 가 state value 를 읽었는지 기록하고, 값이 바뀌면 그 read scope 를 invalidation 대상으로 삼는다.

중요한 것은 state 가 어디에서 만들어졌는가보다 어디에서 읽혔는가다. 부모에서 `state.value` 를 먼저 읽어 plain value 로 자식에게 넘기면 부모가 관찰 scope 가 될 수 있고, 자식에서 직접 읽으면 더 아래 scope 가 관찰 대상이 된다.

그렇다고 "항상 State 객체를 자식에게 넘기라"는 뜻은 아니다. reusable Composable 에는 plain value 와 event callback 을 넘기는 편이 보통 더 좋고, 실제 재실행 범위는 read 위치, 파라미터 안정성, skipping 조건이 함께 결정한다.

```kotlin
// 부모가 읽음: count가 바뀔 때마다 Parent 전체가 invalidate 대상이다
@Composable
fun Parent(count: MutableState<Int>) {
    Child(value = count.value) // 이미 읽은 plain Int를 전달
}

// 자식이 읽음: count가 바뀌어도 Parent는 그대로, Child scope만 invalidate된다
@Composable
fun Parent(count: MutableState<Int>) {
    Child(count = count)
}

@Composable
fun Child(count: MutableState<Int>) {
    Text("${count.value}")
}
```

두 버전 모두 최종 화면은 같지만, `count.value` 를 어디서 읽느냐에 따라 invalidation 대상 scope 가 `Parent` 인지 `Child` 인지가 갈린다.

관련 노트: [Compose 상태 읽기 위치는 recomposition 범위를 결정한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-state-read-location-controls-recomposition-scope.md), [Automatic State Observation이 Flutter rebuild 사고와 Compose를 가른다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/automatic-state-observation-is-the-compose-flutter-rebuild-difference.md)

출처: [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state), [Compose phases](https://developer.android.com/develop/ui/compose/phases)
