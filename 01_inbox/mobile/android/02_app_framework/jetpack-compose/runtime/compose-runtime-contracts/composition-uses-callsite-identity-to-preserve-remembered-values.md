---
title: composition-uses-callsite-identity-to-preserve-remembered-values
tags: [android, compose/runtime, jetpack-compose]
aliases: [positional memoization, Slot Table]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Composition 은 호출 위치 식별자(Callsite Identity)를 사용해 remember 값을 보존한다

Composition 은 Composable 호출의 위치와 구조를 이용해 `remember` 값, group, node 관계를 보존한다. 같은 `remember` 코드라도 호출 위치가 다르면 서로 다른 저장공간이 된다.

조건문, 반복문, list item 에서는 호출 구조와 key 가 identity 에 영향을 준다. item identity 를 안정적으로 주지 않으면 위치 변화가 값 보존과 재사용을 흐릴 수 있다.

```kotlin
// key 없음: index 기반 callsite identity. 맨 앞에 item을 삽입하면
// 모든 하위 항목의 remember 상태가 밀려서 엉뚱한 값과 매칭될 수 있다.
items.forEach { item -> ItemRow(item) }

// key 있음: item.id가 identity가 되어 삽입/삭제/이동에도
// 각 ItemRow의 remember 상태(예: 펼침 여부)가 올바른 item을 따라간다.
items.forEach { item -> key(item.id) { ItemRow(item) } }
```

`LazyColumn` 의 `items(list, key = { it.id })` 도 같은 원리다. key 를 생략하면 목록이 재정렬될 때 `remember { mutableStateOf(false) }` 로 만든 펼침 상태가 다른 item 으로 옮겨붙는 것을 관찰할 수 있다.

Slot Table, group, Composer 같은 용어는 Runtime 이해를 위한 내부 모델이다. 디컴파일된 함수 signature 나 내부 자료구조를 앱 코드가 의존하는 API 처럼 쓰지 않는다.

관련 노트: [remember는 일반 cache가 아니라 Composition에 귀속된 저장공간이다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/remember-is-composition-scoped-storage-not-general-cache.md), [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-compiler-output-enables-restart-and-skip-control.md)

출처: [Lifecycle of composables](https://developer.android.com/develop/ui/compose/lifecycle)
