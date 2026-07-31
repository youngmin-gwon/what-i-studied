# Android 연결성과 네트워크 지도

Android 네트워크는 Wi-Fi, cellular, Ethernet, VPN 같은 transport를 그대로 앱에 노출하는 구조가 아니다. 앱은 `ConnectivityManager`가 제공하는 `Network`, `NetworkCapabilities`, `LinkProperties`, 정책 상태를 보고 현재 작업에 맞는 연결성을 판단해야 한다.

## 정본 노트
- [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)
