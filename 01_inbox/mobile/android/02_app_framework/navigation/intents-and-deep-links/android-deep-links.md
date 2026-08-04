---
title: android-deep-links
tags: [android, android/intents, android/navigation]
aliases: ["Android Deep Links"]
date modified: 2026-08-03 18:11:04 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Deep Link 는 외부 URI 를 앱 내부 destination 으로 들어오게 하는 계약이다

Android Deep Link 문서는 외부 URI 가 앱 내부 destination 으로 들어오는 계약을 정리한다. 핵심은 URI 수신, 검증, 인증 상태, back stack 구성, App Link verification 을 분리하는 것이다.

### 정본 지도

- [Deep Link 계약](./deep-link-contracts/deep-link-contracts.md)
- [Android 딥 링크는 외부 URI 계약이다](./deep-link-contracts/deep-link-is-external-uri-contract.md)
- [Android App Link는 검증된 HTTPS 딥 링크다](./deep-link-contracts/app-link-is-verified-https-deep-link.md)
- [외부 URI는 navigation 전에 allowlist와 canonicalization을 거쳐야 한다](./deep-link-contracts/external-uri-must-be-validated-before-navigation.md)
