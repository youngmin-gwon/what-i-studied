# ConnectivityManager

상위 노트: [[android-connectivity-and-networking]]

### 네트워크 요청

```kotlin
val connectivityManager = getSystemService(ConnectivityManager::class.java)

// 현재 활성 네트워크
val activeNetwork = connectivityManager.activeNetwork
val capabilities = connectivityManager.getNetworkCapabilities(activeNetwork)

if (capabilities?.hasTransport(NetworkCapabilities.TRANSPORT_WIFI) == true) {
    // Wi-Fi 연결
}

// 네트워크 콜백
val request = NetworkRequest.Builder()
    .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    .addTransportType(NetworkCapabilities.TRANSPORT_WIFI)
    .build()

connectivityManager.registerNetworkCallback(request, object : NetworkCallback() {
    override fun onAvailable(network: Network) {
        // 네트워크 사용 가능
    }
    
    override fun onLost(network: Network) {
        // 네트워크 끊김
    }
    
    override fun onCapabilitiesChanged(
        network: Network,
        capabilities: NetworkCapabilities
    ) {
        val bandwidth = capabilities.linkDownstreamBandwidthKbps
    }
})
```

### Network Selection

**우선순위** (Android 9+):

1. **Default**: Wi-Fi > Ethernet > Mobile
2. **사용자 선택**: 설정에서 우선 네트워크 지정
3. **앱 요구사항**: `NetworkRequest` 로 특정 네트워크 요청

**예시**:

```kotlin
// 계량제가 아닌 네트워크 (Wi-Fi)만
val request = NetworkRequest.Builder()
    .addCapability(NetworkCapabilities.NET_CAPABILITY_NOT_METERED)
    .build()

connectivityManager.requestNetwork(request, callback)
```

---
