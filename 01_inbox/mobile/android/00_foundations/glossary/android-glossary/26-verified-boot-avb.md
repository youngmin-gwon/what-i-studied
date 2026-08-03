---
title: 26-verified-boot-avb
tags: ["android", "android/glossary"]
aliases: ["Android Verified Boot", "AVB"]
date modified: 2026-08-03 17:21:05 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Verified Boot(AVB)는 부팅 과정에서 시스템 이미지의 무결성을 암호학적으로 검증한다

정의: Verified Boot 와 AVB 는 boot image 와 partition integrity 를 검증해 device software chain of trust 를 세우는 boot-time security mechanism 이다.

혼동 방지: AVB 는 앱 서명 검증과 다르다. 앱 서명은 package install/update trust 이고, Verified Boot 는 kernel 과 system image 가 신뢰 가능한 상태로 올라왔는지 검증한다.

정본 링크:

- [AVB boot verification](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md)
- [Verified Boot trust chain](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/verified-boot-establishes-device-software-chain-of-trust.md)
