# 기본 네트워크와 요청 네트워크는 서로 다른 수명 계약을 가진다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Default network는 시스템이 앱 트래픽에 기본 적용하는 네트워크다. `requestNetwork()`로 요청한 네트워크는 앱이 특정 capability를 요구해 시스템에 연결 유지를 요청하는 별도 수명 계약이며, 권한과 배터리 비용을 동반할 수 있다.

## 실무 규칙

- 일반 HTTP 호출은 앱 default network를 사용한다.
- 특정 Wi-Fi, cellular, not-metered 같은 조건이 필요할 때만 `NetworkRequest`를 만든다.
- `requestNetwork()`는 `CHANGE_NETWORK_STATE` 또는 시스템 설정 수정 권한 조건을 요구할 수 있다.
- 요청이 끝나면 반드시 callback을 unregister해 네트워크 유지와 callback 제한을 해제한다.
- mutable capability인 `VALIDATED`, `CAPTIVE_PORTAL`은 request 조건으로 부적절하다.

## 관련 문서

- [NetworkCallback은 등록 수명과 콜백 데이터의 일관성을 함께 관리해야 한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/networkcallback-lifetime-and-callback-data-consistency-must-be-managed.md)
- [Metered와 Data Saver는 백그라운드 네트워크 비용 정책이다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/metered-and-data-saver-are-background-network-cost-policy.md)

공식 문서: [ConnectivityManager.requestNetwork](https://developer.android.com/reference/android/net/ConnectivityManager#requestNetwork(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback))
