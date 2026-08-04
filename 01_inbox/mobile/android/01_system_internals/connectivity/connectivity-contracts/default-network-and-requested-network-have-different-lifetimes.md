---
title: default-network-and-requested-network-have-different-lifetimes
tags: [android, android/connectivity, android/lifecycle]
aliases: [Default Network, Requested Network, NetworkRequest, NetworkCallback Lifecycle]
date modified: 2026-08-04 22:00:00 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## Default Network와 Requested Network는 수명이 다르다

상위 문서: [Connectivity contracts](connectivity-contracts.md)

Android 개발 시 `ConnectivityManager.registerDefaultNetworkCallback()`과 `ConnectivityManager.requestNetwork()`는 완전히 다른 수명주기(Lifecycle) 및 시스템 영향을 갖는다. **Default Network Callback**은 시스템이 전역으로 결정한 네트워크 상태를 단순 관찰(Passive Observer)하는 반면, **Requested Network**는 시스템이 해당 특성의 네트워크 인터페이스 연결을 유지하도록 강제(Active Pinning)하는 명령이다.

### 메커니즘: 관찰자 vs 소유자 모델 비교

1. **Default Network Callback (`registerDefaultNetworkCallback`)**:
   - 시스템 기본 네트워크의 변경(Wi-Fi <-> Cellular 전환)을 단순 수동 수신한다.
   - 물리 네트워크 연결 수명에 일절 영향을 주지 않으므로 전력 소비를 유발하지 않는다.

2. **Requested Network (`requestNetwork`)**:
   - 앱이 특정 조건(`NetworkRequest`)을 명시하여 호출하면, 조건에 부합하는 네트워크(예: Cellular 5G)가 활성화되어 있지 않더라도 시스템이 무선 모뎀을 전원 켜서 연결을 시도한다.
   - 앱이 `unregisterNetworkCallback()`을 호출할 때까지 해당 물리 인터페이스는 절전 모드로 들어가지 못하고 **활성 상태로 고정(Keep-Alive / Pinning)**되므로, 미해제 시 배터리 소모의 원인이 된다.

```mermaid
graph TD
    subgraph Passive Observer (Default Network)
        App1[App] -->|registerDefaultNetworkCallback| CS1[ConnectivityService]
        CS1 -->|System Switches Default| App1
        NoteOver1[네트워크 수명에 영향 없음 / 배터리 안전]
    end

    subgraph Active Pinning (Requested Network)
        App2[App] -->|requestNetwork(Cellular)| CS2[ConnectivityService]
        CS2 -->|Force Power On| Modem[Cellular Radio Modem]
        Modem -->|Keep Alive active| App2
        NoteOver2[unregister 미호출 시 배터리/데이터 지속 누수!]
    end
```

### Kotlin 안전한 NetworkCallback 바인딩 예시

```kotlin
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.NetworkRequest
import androidx.lifecycle.DefaultLifecycleObserver
import androidx.lifecycle.LifecycleOwner

class SafeNetworkRequester(
    private val connectivityManager: ConnectivityManager
) : DefaultLifecycleObserver {

    private var networkCallback: ConnectivityManager.NetworkCallback? = null

    fun requestCellularNetwork() {
        val request = NetworkRequest.Builder()
            .addTransportType(NetworkCapabilities.TRANSPORT_CELLULAR)
            .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
            .build()

        networkCallback = object : ConnectivityManager.NetworkCallback() {
            override fun onAvailable(network: Network) {
                // 바인딩된 셀룰러 네트워크 사용
            }
        }

        // Active Keep-Alive 요청
        connectivityManager.requestNetwork(request, networkCallback!!)
    }

    // Lifecycle ON_STOP 시 반드시 해제하여 배터리 누수 방지
    override fun onStop(owner: LifecycleOwner) {
        networkCallback?.let {
            connectivityManager.unregisterNetworkCallback(it)
            networkCallback = null
        }
    }
}
```

### 관찰 신호: dumpsys connectivity 덤프

```bash
# 활성 NetworkRequest 목록 및 요구자 PID 확인
adb shell dumpsys connectivity | grep -A 10 "NetworkRequests"

# 확인 사항:
# - 앱 패키지명이 requestNetwork 상태로 남아 무선 모뎀을 핀(Pinning)하고 있는지 점검
```

### 관련 문서

- [ConnectivityService는 네트워크를 선택하고 정책을 적용한다](connectivityservice-selects-networks-and-applies-policy.md)
- [NetworkCallback 수명과 콜백 데이터 일관성은 관리되어야 한다](networkcallback-lifetime-and-callback-data-consistency-must-be-managed.md)

공식 문서: [Listen to Network State](https://developer.android.com/training/basics/network-ops/reading-network-state)
