# callbackFlow

상위 노트: [android-coroutines-flow](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow.md)

콜백 기반 API 를 Flow 로 변환한다.

```kotlin
fun locationUpdates(): Flow<Location> = callbackFlow {
    val locationManager = context.getSystemService<LocationManager>()
    val listener = object : LocationListener {
        override fun onLocationChanged(location: Location) {
            trySend(location)  // 콜백 → Flow
        }
    }
    
    locationManager?.requestLocationUpdates(
        LocationManager.GPS_PROVIDER, 1000L, 0f, listener
    )
    
    awaitClose {
        // Flow 가 취소될 때 정리
        locationManager?.removeUpdates(listener)
    }
}

// 사용
viewModelScope.launch {
    locationUpdates()
        .conflate()  // 처리 못 한 이전 값은 버림
        .collect { location ->
            _currentLocation.value = location
        }
}
```
