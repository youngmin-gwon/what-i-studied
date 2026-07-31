# Network는 특정 연결 인스턴스이고 transport는 그 속성 중 하나다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

`Network`는 현재 사용할 수 있는 특정 연결 인스턴스다. `NetworkCapabilities`는 그 연결이 인터넷 가능, 검증됨, 계량제 아님, captive portal, Wi-Fi/cellular/VPN transport 같은 속성을 갖는지 표현하고, `LinkProperties`는 IP 주소, DNS, route 같은 link layer 구성을 담는다.

## 실무 규칙

- `TRANSPORT_WIFI`만 보고 인터넷 가능성을 판단하지 않는다.
- `NET_CAPABILITY_INTERNET`은 인터넷을 제공할 의도가 있다는 뜻이고, `NET_CAPABILITY_VALIDATED`는 시스템이 실제 인터넷 도달성을 관측했다는 뜻이다.
- DNS 서버, route, interface name이 필요하면 `LinkProperties`를 본다.
- Wi-Fi SSID 같은 location-sensitive 정보는 권한과 redaction 정책의 영향을 받는다.

## 관련 문서

- [Validated와 captive portal은 인터넷 가능성의 관측 상태다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/validated-and-captive-portal-are-observed-internet-states.md)
- [Private DNS는 DNS 질의를 암호화하지만 앱 TLS 검증을 대체하지 않는다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/private-dns-encrypts-dns-but-does-not-replace-app-tls-validation.md)

공식 문서: [ConnectivityManager.getNetworkCapabilities](https://developer.android.com/reference/android/net/ConnectivityManager#getNetworkCapabilities(android.net.Network))
