# Validated와 captive portal은 인터넷 가능성의 관측 상태다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

`VALIDATED`와 `CAPTIVE_PORTAL`은 네트워크가 실제 인터넷에 도달 가능한지 시스템이 관측한 상태다. Wi-Fi에 연결됐거나 IP를 받았다는 사실만으로 앱 서버에 도달할 수 있다고 보면 안 된다.

## 판단 기준

- captive portal은 사용자가 로그인이나 약관 동의를 해야 인터넷이 열리는 상태일 수 있다.
- validation 상태는 시간이 지나며 바뀔 수 있으므로 callback으로 관찰한다.
- requestNetwork 조건으로 captive portal이나 validated 같은 mutable capability를 요구하지 않는다.
- 앱 자체 backend reachability는 별도 health check와 오류 UI로 다룬다.

## 관련 문서

- [Network는 특정 연결 인스턴스이고 transport는 그 속성 중 하나다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-is-connection-instance-and-transport-is-only-one-capability.md)
- [네트워크 디버깅은 앱 API 상태와 system network state를 대조한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-debugging-compares-app-api-state-with-system-network-state.md)

공식 문서: [NetworkCapabilities](https://developer.android.com/reference/android/net/NetworkCapabilities)
