---
title: callbackflow-requires-awaitclose-for-registration-cleanup
tags: [android, android/async, android/data, android/flow]
aliases: ["callbackFlow는 awaitClose로 등록과 해제를 대칭으로 보장해야 한다"]
date modified: 2026-08-03 18:07:27 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## callbackFlow 는 awaitClose 로 등록과 해제를 대칭으로 보장해야 한다

`callbackFlow` 는 callback 기반 API 를 Flow 로 감싸는 bridge 다. callback 등록은 flow builder 안에서 수행하고, collector 가 취소되거나 flow 가 닫힐 때 `awaitClose` 에서 listener 해제를 보장해야 한다.

Callback thread 에서 값을 보낼 때는 `trySend` 처럼 non-blocking send 를 사용하고 실패 결과를 의식한다. producer 가 너무 빠르면 `buffer`, `conflate`, producer-side throttling 중 하나를 adapter contract 로 선택해야 한다.

`awaitClose` 없이 등록만 하고 끝나는 adapter 는 listener leak 을 만들 수 있다. 또한 같은 callback 을 여러 번 등록하거나 lifecycle 과 무관하게 유지하는 구조도 피해야 한다.

공식 문서: [Kotlin flows on Android](https://developer.android.com/kotlin/flow)
