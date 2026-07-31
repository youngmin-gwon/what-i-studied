---
title: "Verified Boot와 AVB"
tags: ["android", "android/glossary"]
aliases: ["Android Verified Boot", "AVB"]
---

# Verified Boot와 AVB

정의: Verified Boot와 AVB는 boot image와 partition integrity를 검증해 device software chain of trust를 세우는 boot-time security mechanism이다.

혼동 방지: AVB는 앱 서명 검증과 다르다. 앱 서명은 package install/update trust이고, Verified Boot는 kernel과 system image가 신뢰 가능한 상태로 올라왔는지 검증한다.

정본 링크:
- [AVB boot verification](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md)
- [Verified Boot trust chain](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/verified-boot-establishes-device-software-chain-of-trust.md)
