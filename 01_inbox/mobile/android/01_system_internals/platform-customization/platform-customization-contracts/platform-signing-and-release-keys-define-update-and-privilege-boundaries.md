---
title: platform-signing-and-release-keys-define-update-and-privilege-boundaries
tags: [android, android/aosp, android/security]
aliases: [Platform signing, Release keys]
date modified: 2026-08-03 17:26:33 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Platform signing 과 release key 는 update 와 privilege boundary 를 정의한다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Platform signing key 와 release key 는 단순 배포 서명이 아니라 system image update, privileged permission, shared UID, platform app 신뢰 경계를 정의한다. 같은 APK 라도 어떤 key 로 서명되고 어느 partition 에 놓이는지에 따라 권한과 업데이트 가능성이 달라진다.

앱 개발에서의 Play App Signing 과 플랫폼 이미지 signing 은 같은 "서명"이라는 단어를 쓰지만 책임이 다르다. 플랫폼 signing 은 기기 image 와 OTA, verified boot chain, privileged app policy 와 함께 관리해야 한다.

### 실무 규칙

- debug/test key 로 만든 image 를 production trust boundary 로 보지 않는다.
- privileged app 권한은 partition 위치, allowlist, signing key 를 함께 본다.
- key rotation 은 update path 와 rollback protection 을 고려한다.
- APK/AAB 배포 서명과 platform image signing 을 같은 절차로 문서화하지 않는다.

관련 노트: [AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md), [Android security and privacy](01_inbox/mobile/android/05_security_privacy/android-security-and-privacy.md)
