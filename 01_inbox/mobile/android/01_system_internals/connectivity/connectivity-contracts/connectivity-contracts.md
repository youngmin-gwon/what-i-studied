# 연결성 계약

Android 연결성은 물리 네트워크 종류보다 capability, validation, cost, policy, user choice, VPN overlay, DNS/security 설정이 함께 결정하는 실행 계약이다.

## 정본 노트
- [ConnectivityService는 네트워크 선택과 정책 적용의 system service다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivityservice-selects-networks-and-applies-policy.md)
- [Network는 특정 연결 인스턴스이고 transport는 그 속성 중 하나다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-is-connection-instance-and-transport-is-only-one-capability.md)
- [기본 네트워크와 요청 네트워크는 서로 다른 수명 계약을 가진다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/default-network-and-requested-network-have-different-lifetimes.md)
- [NetworkCallback은 등록 수명과 콜백 데이터의 일관성을 함께 관리해야 한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/networkcallback-lifetime-and-callback-data-consistency-must-be-managed.md)
- [Metered와 Data Saver는 백그라운드 네트워크 비용 정책이다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/metered-and-data-saver-are-background-network-cost-policy.md)
- [Validated와 captive portal은 인터넷 가능성의 관측 상태다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/validated-and-captive-portal-are-observed-internet-states.md)
- [Wi-Fi API는 스캔, 제안, 요청, 로컬 연결을 분리한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/wifi-apis-separate-scan-suggestion-request-and-local-connectivity.md)
- [Cellular 연결은 사용자 요금제와 시스템 정책의 영향을 받는다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/cellular-connectivity-is-shaped-by-plan-and-system-policy.md)
- [VpnService는 앱이 만든 TUN interface를 시스템 라우팅에 등록한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/vpnservice-registers-app-tun-interface-with-system-routing.md)
- [Always-on과 lockdown VPN은 연결 실패를 보안 정책으로 바꾼다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/always-on-and-lockdown-vpn-turn-failure-into-security-policy.md)
- [Private DNS는 DNS 질의를 암호화하지만 앱 TLS 검증을 대체하지 않는다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/private-dns-encrypts-dns-but-does-not-replace-app-tls-validation.md)
- [Network Security Config는 앱의 trust, cleartext, pinning 정책을 선언한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-security-config-declares-app-trust-cleartext-and-pinning-policy.md)
- [netd는 framework 요청을 routing, DNS, firewall, tethering 동작으로 집행한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/netd-enforces-routing-dns-firewall-and-tethering-operations.md)
- [TrafficStats는 UID 단위 사용량 관찰이지 비용 정책 결정자가 아니다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/trafficstats-observes-uid-usage-not-cost-policy.md)
- [테더링은 개인 hotspot 기능이 아니라 upstream과 downstream을 잇는 system service다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/tethering-bridges-upstream-and-downstream-through-system-service.md)
- [네트워크 디버깅은 앱 API 상태와 system network state를 대조한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-debugging-compares-app-api-state-with-system-network-state.md)
