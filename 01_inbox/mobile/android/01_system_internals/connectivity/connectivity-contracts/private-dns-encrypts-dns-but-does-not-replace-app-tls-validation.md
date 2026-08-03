---
title: private-dns-encrypts-dns-but-does-not-replace-app-tls-validation
tags: ["android", "android/system-internals"]
aliases: []
date modified: 2026-08-03 17:24:40 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## Private DNS 는 DNS 질의를 암호화하지만 앱 TLS 검증을 대체하지 않는다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Private DNS 는 시스템 DNS resolver 가 DNS-over-TLS 로 질의를 암호화하도록 하는 플랫폼 기능이다. 이는 DNS 감청과 변조 위험을 줄이지만, 앱의 HTTPS/TLS 검증, certificate pinning, backend authentication 을 대체하지 않는다.

### 판단 기준

- 사용자가 설정한 Private DNS provider 는 앱이 임의로 통제하지 않는다.
- 앱은 `LinkProperties.isPrivateDnsActive()` 와 `getPrivateDnsServerName()` 으로 현재 네트워크의 Private DNS 상태를 관찰할 수 있다.
- DNS-over-TLS 가 켜져도 SNI, IP, traffic pattern 등 다른 metadata 가 모두 사라지는 것은 아니다.
- 앱의 보안 연결 정책은 Network Security Config 와 TLS library 설정에서 다룬다.
- DNS 실패는 captive portal, VPN, Private DNS provider 장애, network validation 실패와 함께 봐야 한다.

### 관련 문서

- [Network Security Config는 앱의 trust, cleartext, pinning 정책을 선언한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-security-config-declares-app-trust-cleartext-and-pinning-policy.md)
- [네트워크 디버깅은 앱 API 상태와 system network state를 대조한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-debugging-compares-app-api-state-with-system-network-state.md)

공식 문서: [LinkProperties Private DNS API](https://developer.android.com/reference/android/net/LinkProperties#getPrivateDnsServerName()), [Android DNS Resolver](https://source.android.com/docs/core/ota/modular-system/dns-resolver)
