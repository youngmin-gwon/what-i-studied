---
title: callbackFlow는 awaitClose로 등록과 해제를 대칭으로 보장해야 한다
tags: [android, android/data, android/async, android/flow]
aliases: ["callbackFlow는 awaitClose로 등록과 해제를 대칭으로 보장해야 한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# callbackFlow는 awaitClose로 등록과 해제를 대칭으로 보장해야 한다

`callbackFlow`는 callback 기반 API를 Flow로 감싸는 bridge다. callback 등록은 flow builder 안에서 수행하고, collector가 취소되거나 flow가 닫힐 때 `awaitClose`에서 listener 해제를 보장해야 한다.

Callback thread에서 값을 보낼 때는 `trySend`처럼 non-blocking send를 사용하고 실패 결과를 의식한다. producer가 너무 빠르면 `buffer`, `conflate`, producer-side throttling 중 하나를 adapter contract로 선택해야 한다.

`awaitClose` 없이 등록만 하고 끝나는 adapter는 listener leak을 만들 수 있다. 또한 같은 callback을 여러 번 등록하거나 lifecycle과 무관하게 유지하는 구조도 피해야 한다.

공식 문서: [Kotlin flows on Android](https://developer.android.com/kotlin/flow)
