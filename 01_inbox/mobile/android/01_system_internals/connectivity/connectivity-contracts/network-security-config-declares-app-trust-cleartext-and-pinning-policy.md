---
title: network-security-config-declares-app-trust-cleartext-and-pinning-policy
tags: ["android", "android/system-internals"]
aliases: []
date modified: 2026-08-03 17:24:38 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## Network Security Config 는 앱의 trust, cleartext, pinning 정책을 선언한다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Network Security Config 는 앱의 도메인별 trust anchors, cleartext 허용, certificate pinning, debug override 같은 연결 보안 정책을 XML 로 선언한다. 이는 HTTP client 코드의 옵션이 아니라 앱 manifest 에 연결되는 플랫폼 보안 설정이다.

### 실무 규칙

- Android 9(API 28) 이상 target 앱은 기본적으로 cleartext 가 비활성화된다.
- cleartext 허용은 domain 별로 최소화하고 임시 테스트 설정을 release 에 남기지 않는다.
- custom CA 를 추가하면 Certificate Transparency 동작과 pinning 우회 여부를 함께 검토한다.
- pinning 에는 backup pin 과 교체 계획이 필요하다. pin 만료는 장애 방지책이지만 보안 약화 지점이기도 하다.
- Android 17(API 37) 이상 target 에서는 ECH 관련 `domainEncryption` 정책도 검토 대상이 된다.

### 관련 문서

- [Android 보안 샌드박스](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)
- [Private DNS는 DNS 질의를 암호화하지만 앱 TLS 검증을 대체하지 않는다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/private-dns-encrypts-dns-but-does-not-replace-app-tls-validation.md)

공식 문서: [Network security configuration](https://developer.android.com/privacy-and-security/security-config)

기준일: 2026-07-31. ECH 와 localhost 기본 정책은 API 37 이상 문서 기준이므로 target SDK 변경 시 재확인한다.
