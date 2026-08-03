---
title: connectivity-contracts
tags: ["android", "android/system-internals"]
aliases: ["Android connectivity contracts"]
date modified: 2026-08-03 17:24:25 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## 연결성 계약

Android 연결성은 물리 네트워크 종류보다 capability, validation, cost, policy, user choice, VPN overlay, DNS/security 설정이 함께 결정하는 실행 계약이다.

### 계층 구분

- app API: `ConnectivityManager`, `Network`, `NetworkCapabilities`, `LinkProperties`, `NetworkCallback`, `WifiManager`, `VpnService` 처럼 앱 코드가 직접 부르는 표면. 앱은 이 계층의 상태만 직접 읽고 바꿀 수 있다.
- framework service: `ConnectivityService` 는 system_server 안에서 여러 네트워크 후보를 모아 default network 와 정책을 계산하는 조율자다. 이 계층의 시작/조율 세부(어떻게 system_server 가 이 service 를 띄우는지)는 [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md) 이 정본이므로 이 묶음에서는 반복하지 않는다.
- native service: `netd` 는 framework 의 라우팅/DNS/firewall/tethering 결정을 실제 kernel 동작으로 옮기는 native daemon 이다. 앱은 netd 를 직접 호출하지 않는다.
- kernel/HAL: iptables/nftables/eBPF 기반 라우팅·필터링, Wi-Fi/radio driver, modem HAL 은 netd 아래에서 동작하며 OEM/커널 버전에 따라 구현이 달라질 수 있다.

### 읽는 순서

1. `Network`/`NetworkCapabilities`/`LinkProperties` 로 앱이 실제로 무엇을 관찰하는지 본다.
2. `ConnectivityService` 가 여러 네트워크 후보를 어떻게 default/requested 로 나누는지 본다.
3. `NetworkCallback` 수명 관리로 관찰이 언제 끊기거나 새는지 본다.
4. validated/captive portal 로 "연결됨"과 "인터넷 됨"의 차이를 본다.
5. metered/Data Saver/cellular 로 비용 정책을, Wi-Fi API 로 스캔·제안·연결 권한 경계를 본다.
6. VPN(VpnService, always-on/lockdown)으로 라우팅을 덮어쓰는 계층을 본다.
7. Private DNS/Network Security Config 로 DNS 와 TLS 보안 경계를 분리해서 본다.
8. netd/TrafficStats/tethering 으로 framework 아래 native 집행 계층을 본다.
9. 문제가 생기면 네트워크 디버깅 노트로 앱 상태와 system 상태를 대조한다.

### 문제 분류 기준

- "인터넷 연결이 안 되거나 느리다" → [Validated와 captive portal](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/validated-and-captive-portal-are-observed-internet-states.md), [Network은 연결 인스턴스다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-is-connection-instance-and-transport-is-only-one-capability.md)
- "특정 조건(Wi-Fi, not-metered)의 네트워크를 골라 써야 한다" → [기본/요청 네트워크 수명](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/default-network-and-requested-network-have-different-lifetimes.md), [NetworkCallback 수명 관리](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/networkcallback-lifetime-and-callback-data-consistency-must-be-managed.md)
- "배터리/데이터 사용량 정책 문제" → [Metered와 Data Saver](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/metered-and-data-saver-are-background-network-cost-policy.md), [TrafficStats](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/trafficstats-observes-uid-usage-not-cost-policy.md)
- "Wi-Fi 스캔/연결/주변기기 권한 문제" → [Wi-Fi API 분리](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/wifi-apis-separate-scan-suggestion-request-and-local-connectivity.md)
- "VPN 이 연결되지 않거나 다른 앱 트래픽까지 막는다" → [VpnService](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/vpnservice-registers-app-tun-interface-with-system-routing.md), [Always-on/lockdown VPN](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/always-on-and-lockdown-vpn-turn-failure-into-security-policy.md)
- "TLS/인증서/cleartext 오류" → [Network Security Config](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-security-config-declares-app-trust-cleartext-and-pinning-policy.md), [Private DNS](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/private-dns-encrypts-dns-but-does-not-replace-app-tls-validation.md)
- "라우팅/방화벽/테더링이 이상하다" → [netd 집행 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/netd-enforces-routing-dns-firewall-and-tethering-operations.md), [테더링](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/tethering-bridges-upstream-and-downstream-through-system-service.md)
- "원인이 불명확하다" → [네트워크 디버깅](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-debugging-compares-app-api-state-with-system-network-state.md) 에서 앱 API 상태와 system state 대조부터 시작한다.

### 비슷해 보이는 노트의 차이

- **ConnectivityService vs netd**: ConnectivityService 는 "어떤 네트워크를 쓸지" 결정하는 framework 정책 계층이고, netd 는 그 결정을 실제 routing/DNS/firewall 동작으로 옮기는 native 집행 계층이다.
- **default network vs requested network**: default 는 시스템이 앱에 암묵적으로 적용하는 네트워크이고, requested 는 앱이 `NetworkRequest` 로 명시적으로 요구해 별도 수명을 갖는 네트워크다.
- **Private DNS vs Network Security Config**: Private DNS 는 DNS 질의 자체의 암호화를 다루고, Network Security Config 는 앱이 맺는 TLS 연결의 신뢰/pinning/cleartext 정책을 다룬다. 둘 다 있어야 하고 서로 대체하지 않는다.
- **TrafficStats vs Metered/Data Saver**: TrafficStats 는 사용량을 관찰만 하는 API 이고, Metered/Data Saver 는 그 사용을 실제로 제한하는 시스템 정책이다.
- **VpnService vs Always-on/lockdown VPN**: VpnService 는 앱이 TUN interface 를 만드는 메커니즘이고, always-on/lockdown 은 그 VPN 을 시스템이 얼마나 강제로 유지·차단하는지의 정책 모드다.

### 관련 지도

- [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)
- [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
- [디버깅 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)

### 정본 노트
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

### 중복 방지 규칙

- system_server 가 ConnectivityService 같은 framework service 를 어떻게 시작/조율하는지는 boot-and-runtime 정본으로 두고, 이 묶음은 "무엇을 결정하는 service 인가"만 다룬다.
- Binder transaction/thread pool 비용은 IPC 정본으로 두고, 이 묶음은 ConnectivityService/netd 가 Binder 위에서 통신한다는 사실만 연결한다.
- 앱 sandbox, permission 세부는 security/privacy 정본으로 두고, 이 묶음은 연결성 API 가 요구하는 permission 이름만 언급한다.
- 배터리/백그라운드 작업 제약의 일반 정책은 performance/background-work 정본으로 두고, 이 묶음은 metered/Data Saver 가 그 정책의 network 입력이라는 연결만 다룬다.
