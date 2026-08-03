---
title: structured-concurrency-parent-owns-child-lifetime
tags: [android, android/async, android/coroutines, android/data]
aliases: ["Structured concurrency는 부모 scope가 자식 작업의 수명을 소유하게 한다"]
date modified: 2026-08-03 18:07:23 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Structured concurrency 는 부모 scope 가 자식 작업의 수명을 소유하게 한다

Structured concurrency 는 coroutine 을 독립 작업 목록이 아니라 부모 - 자식 수명 트리로 다루는 규칙이다. 부모 scope 가 취소되면 자식 작업도 취소되고, 부모는 자식이 끝나기 전 완료되지 않는다.

Android 에서는 작업의 owner 에 맞춰 `viewModelScope`, `lifecycleScope`, WorkManager 같은 boundary 를 고른다. `GlobalScope` 는 이 소유권 트리 밖에서 작업을 시작하므로 취소와 실패의 책임을 흐리게 만든다.

`coroutineScope` 는 자식 실패를 부모 실패로 전파하는 기본 구조이고, `supervisorScope` 는 실패 전파를 끊어야 하는 명시적 격리 boundary 다. 둘 다 수명을 없애는 도구가 아니라 수명과 실패 전파를 다르게 묶는 도구다.

공식 문서: [Coroutines basics](https://kotlinlang.org/docs/coroutines-basics.html), [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/)
