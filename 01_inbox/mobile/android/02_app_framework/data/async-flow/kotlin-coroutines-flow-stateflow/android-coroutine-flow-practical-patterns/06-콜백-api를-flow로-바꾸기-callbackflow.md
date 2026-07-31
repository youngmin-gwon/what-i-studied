# 콜백 API를 Flow로 바꾸기: callbackFlow

위치, 센서, 네트워크 상태처럼 콜백 기반 API는 `callbackFlow`로 감싸면 Flow처럼 다룰 수 있습니다.

```kotlin
fun observeNetworkState(context: Context): Flow<NetworkState> = callbackFlow {
    val callback = object : ConnectivityManager.NetworkCallback() {
        override fun onAvailable(network: Network) {
            trySend(NetworkState.Available)
        }

        override fun onLost(network: Network) {
            trySend(NetworkState.Unavailable)
        }
    }

    val manager = context.getSystemService(ConnectivityManager::class.java)
    manager.registerDefaultNetworkCallback(callback)

    awaitClose {
        manager.unregisterNetworkCallback(callback)
    }
}
```

`awaitClose`는 Flow 수집이 취소될 때 콜백 등록을 해제하는 정리 지점입니다.

---
