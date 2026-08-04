---
title: connectivity-contracts
tags: [android, android/connectivity]
aliases: [Android connectivity contracts]
date modified: 2026-08-04 15:50:00 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## Connectivity contracts

이 문서는 Android 연결성 파이프라인을 API 사용법이 아닌 **실행 및 보안 계약(Execution & Security Contracts)** 관점에서 정리한 정본 인덱스다. 핵심 질문은 "어떤 네트워크 인스턴스가 활성화되어 있으며, 어떤 eBPF/라우팅 정책과 백그라운드 제한이 적용되고 있는가"이다.

상위 문서: [Android connectivity runtime](../android-connectivity.md)

### 읽는 순서

1. **네트워크 선택 및 생명주기 정본**: [ConnectivityService 원리](connectivityservice-selects-networks-and-applies-policy.md), [Network vs Transport](network-is-connection-instance-and-transport-is-only-one-capability.md), [Default vs Requested Network](default-network-and-requested-network-have-different-lifetimes.md), [NetworkCallback 관리](networkcallback-lifetime-and-callback-data-consistency-must-be-managed.md)로 시스템 네트워크 선택 아키텍처를 이해한다.
2. **인터넷 검증 및 백그라운드 정책**: [Validated와 Captive Portal](validated-and-captive-portal-are-observed-internet-states.md), [Metered와 Data Saver](metered-and-data-saver-are-background-network-cost-policy.md), [셀룰러 정책](cellular-connectivity-is-shaped-by-plan-and-system-policy.md), [TrafficStats 통계](trafficstats-observes-uid-usage-not-cost-policy.md)로 비용 및 네트워크 가용성 통제를 본다.
3. **네이티브 실행 및 보안 커널 계약**: [netd 엔진 역할](netd-enforces-routing-dns-firewall-and-tethering-operations.md), [VpnService TUN 등록](vpnservice-registers-app-tun-interface-with-system-routing.md), [Always-on과 Lockdown VPN](always-on-and-lockdown-vpn-turn-failure-into-security-policy.md), [Tethering 브리징](tethering-bridges-upstream-and-downstream-through-system-service.md)으로 라우팅과 터널링을 이해한다.
4. **보안 통신 및 Wi-Fi 세분화**: [Network Security Config](network-security-config-declares-app-trust-cleartext-and-pinning-policy.md), [Private DNS의 역할](private-dns-encrypts-dns-but-does-not-replace-app-tls-validation.md), [Wi-Fi APIs 세분화](wifi-apis-separate-scan-suggestion-request-and-local-connectivity.md), [네트워크 디버깅 기법](network-debugging-compares-app-api-state-with-system-network-state.md)을 확인한다.

### 문제 분류 기준

- **인터넷 미연결 / Captive Portal 문제**: [Validated와 Captive Portal](validated-and-captive-portal-are-observed-internet-states.md), [ConnectivityService 원리](connectivityservice-selects-networks-and-applies-policy.md)
- **백그라운드 통신 차단 / 배터리 절약 에러**: [Metered와 Data Saver](metered-and-data-saver-are-background-network-cost-policy.md), [netd 엔진 역할](netd-enforces-routing-dns-firewall-and-tethering-operations.md)
- **VPN 연결 실패 / 차단 이슈**: [Always-on과 Lockdown VPN](always-on-and-lockdown-vpn-turn-failure-into-security-policy.md), [VpnService TUN 등록](vpnservice-registers-app-tun-interface-with-system-routing.md)
- **Cleartext HTTP 차단 및 SSL 에러**: [Network Security Config](network-security-config-declares-app-trust-cleartext-and-pinning-policy.md), [Private DNS의 역할](private-dns-encrypts-dns-but-does-not-replace-app-tls-validation.md)
- **Wi-Fi / IoT 기기 직접 연결**: [Wi-Fi APIs 세분화](wifi-apis-separate-scan-suggestion-request-and-local-connectivity.md), [Default vs Requested Network](default-network-and-requested-network-have-different-lifetimes.md)
