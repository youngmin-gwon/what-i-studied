---
title: platform-security-contracts
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:14:17 +09:00
date created: 2026-08-01 00:03:59 +09:00
---

## Android 플랫폼 보안 경계 계약

Android 플랫폼 보안은 앱 UID sandbox, Binder IPC 경계, SELinux mandatory access control, Verified Boot chain of trust 가 서로 다른 지점을 보호하는 계층형 모델이다.

### 정본 노트

- [Android app sandbox는 UID와 프로세스 경계로 앱을 격리한다](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)
- [SELinux는 Linux 사용자 권한을 넘어 mandatory policy를 강제한다](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/selinux-enforces-mandatory-policy-beyond-linux-user-permissions.md)
- [Verified Boot는 기기 소프트웨어의 chain of trust를 만든다](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/verified-boot-establishes-device-software-chain-of-trust.md)

관련 지도: [Android 권한 계약](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md), [무결성과 attestation 계약](01_inbox/mobile/android/05_security_privacy/integrity-and-attestation/integrity-contracts/integrity-contracts.md)
