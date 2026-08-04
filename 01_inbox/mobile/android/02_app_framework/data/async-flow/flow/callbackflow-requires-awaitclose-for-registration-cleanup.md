---
title: callbackflow-requires-awaitclose-for-registration-cleanup
tags: [android, android/async, android/data, android/flow]
aliases: ["callbackFlow는 awaitClose로 등록과 해제를 대칭으로 보장해야 한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## callbackFlow 는 awaitClose 로 등록과 해제를 대칭으로 보장해야 한다

`callbackFlow` 는 callback 기반 API 를 Flow 로 감싸는 bridge 다. callback 등록은 flow builder 안에서 수행하고, collector 가 취소되거나 flow 가 닫힐 때 `awaitClose` 에서 listener 해제를 보장해야 한다.

Callback thread 에서 값을 보낼 때는 `trySend` 처럼 non-blocking send 를 사용하고 실패 결과를 의식한다. producer 가 너무 빠르면 `buffer`, `conflate`, producer-side throttling 중 하나를 adapter contract 로 선택해야 한다.

`awaitClose` 없이 등록만 하고 끝나는 adapter 는 listener leak 을 만들 수 있다. 또한 같은 callback 을 여러 번 등록하거나 lifecycle 과 무관하게 유지하는 구조도 피해야 한다.

```kotlin
fun locationUpdates(client: FusedLocationProviderClient): Flow<Location> = callbackFlow {
    val callback = object : LocationCallback() {
        override fun onLocationResult(result: LocationResult) {
            result.lastLocation?.let { trySend(it) }
        }
    }
    client.requestLocationUpdates(request, callback, Looper.getMainLooper())
    awaitClose { client.removeLocationUpdates(callback) } // collector 취소 시 반드시 호출된다
}
```

`callbackFlow` 블록이 `awaitClose` 를 호출하지 않고 정상 종료하면 kotlinx.coroutines 는 `IllegalStateException` 을 던지며 "`awaitClose { ... }` should be used in the end of callbackFlow block" 이라고 명시적으로 알려준다. `awaitClose` 를 호출했더라도 그 블록 안에서 `removeLocationUpdates` 를 빼먹으면 예외는 나지 않는 대신, collector 가 취소된 뒤에도 `requestLocationUpdates` 로 등록한 `callback` 이 시스템 서비스에 남아 화면을 떠났다가 다시 들어올 때마다 이전 callback 이 누적되어 같은 위치가 중복으로 emit 되는 형태로 leak 이 드러난다.

공식 문서: [Kotlin flows on Android](https://developer.android.com/kotlin/flow)
