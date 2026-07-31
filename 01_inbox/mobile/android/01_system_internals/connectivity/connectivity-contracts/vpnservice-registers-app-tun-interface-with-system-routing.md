---
title: "VpnService는 앱이 만든 TUN interface를 시스템 라우팅에 등록한다"
tags: ["android", "android/system-internals"]
---

# VpnService는 앱이 만든 TUN interface를 시스템 라우팅에 등록한다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

`VpnService`는 앱이 사용자 동의와 시스템 권한 아래 가상 네트워크 interface를 만들고, 그 interface로 들어온 패킷을 VPN gateway로 터널링할 수 있게 하는 API다. VPN 앱은 service lifecycle, foreground 실행, tunnel socket 보호, route/DNS 설정을 직접 책임진다.

## 실무 규칙

- manifest service는 `android.permission.BIND_VPN_SERVICE`로 보호하고 `android.net.VpnService` action을 선언한다.
- Android 8.0 이상 background start 제한 때문에 VPN service는 시작 후 foreground service로 승격해야 한다.
- VPN gateway로 가는 socket은 VPN에 다시 들어가지 않도록 `protect()`를 사용한다.
- 사용자가 Settings에서 VPN을 해제하면 `onRevoke()`가 호출될 수 있고, 이 시점의 thread와 routing 상태를 가정하지 않는다.

## 관련 문서

- [Always-on과 lockdown VPN은 연결 실패를 보안 정책으로 바꾼다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/always-on-and-lockdown-vpn-turn-failure-into-security-policy.md)
- [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)

공식 문서: [VPN](https://developer.android.com/develop/connectivity/vpn), [VpnService](https://developer.android.com/reference/android/net/VpnService)
