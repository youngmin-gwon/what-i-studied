---
title: Platform signing과 release key는 update와 privilege boundary를 정의한다
tags: [android, android/aosp, android/security]
aliases: [Platform signing, Release keys]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Platform signing과 release key는 update와 privilege boundary를 정의한다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Platform signing key와 release key는 단순 배포 서명이 아니라 system image update, privileged permission, shared UID, platform app 신뢰 경계를 정의한다. 같은 APK라도 어떤 key로 서명되고 어느 partition에 놓이는지에 따라 권한과 업데이트 가능성이 달라진다.

앱 개발에서의 Play App Signing과 플랫폼 이미지 signing은 같은 “서명”이라는 단어를 쓰지만 책임이 다르다. 플랫폼 signing은 기기 image와 OTA, verified boot chain, privileged app policy와 함께 관리해야 한다.

## 실무 규칙

- debug/test key로 만든 image를 production trust boundary로 보지 않는다.
- privileged app 권한은 partition 위치, allowlist, signing key를 함께 본다.
- key rotation은 update path와 rollback protection을 고려한다.
- APK/AAB 배포 서명과 platform image signing을 같은 절차로 문서화하지 않는다.

관련 노트: [AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md), [Android security and privacy](01_inbox/mobile/android/05_security_privacy/android-security-and-privacy.md)
