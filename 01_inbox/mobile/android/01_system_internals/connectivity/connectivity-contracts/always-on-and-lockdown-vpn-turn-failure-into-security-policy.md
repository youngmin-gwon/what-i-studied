---
title: always-on-and-lockdown-vpn-turn-failure-into-security-policy
tags: ["android", "android/system-internals"]
aliases: []
date modified: 2026-08-03 17:24:26 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## Always-on 과 lockdown VPN 은 연결 실패를 보안 정책으로 바꾼다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Always-on VPN 은 부팅 후 VPN service 를 계속 유지하려는 시스템 정책이고, lockdown VPN 은 VPN 을 우회하는 트래픽을 차단하는 더 강한 정책이다. 이 모드에서는 VPN 연결 실패가 단순 네트워크 오류가 아니라 전체 앱 연결 차단으로 이어질 수 있다.

### 실무 규칙

- always-on 을 지원하지 못하는 VPN 앱은 manifest metadata 로 명시적으로 opt-out 한다.
- lockdown 모드에서는 allowlist/disallowlist 와 enterprise policy 가 사용자 네트워크 경험을 크게 바꾼다.
- VPN service 는 앱 업데이트, reboot, network handover 이후 재연결을 견뎌야 한다.
- 연결 실패 알림과 사용자 복구 경로를 UX 요구사항으로 둔다.

### 관련 문서

- [VpnService는 앱이 만든 TUN interface를 시스템 라우팅에 등록한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/vpnservice-registers-app-tun-interface-with-system-routing.md)
- [Android 보안 샌드박스](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)

공식 문서: [VPN always-on](https://developer.android.com/develop/connectivity/vpn#always-on), [DevicePolicyManager.setAlwaysOnVpnPackage](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAlwaysOnVpnPackage(android.content.ComponentName,%20java.lang.String,%20boolean))
