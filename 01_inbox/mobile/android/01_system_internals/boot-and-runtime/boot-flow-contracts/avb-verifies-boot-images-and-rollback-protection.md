---
title: "AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다"
tags: [android, android/system-internals, android/boot-runtime, android/boot]
aliases: ["AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

Android Verified Boot는 부팅 경로에서 실행되는 이미지가 신뢰 가능한 소스에서 왔는지 확인하고, 알려진 취약 버전으로 되돌리는 공격을 막기 위한 구조다. AVB는 `vbmeta`, partition footer, libavb, dm-verity, rollback index를 통해 이 계약을 구현한다.

## 판단 기준

- green/yellow/orange/red 상태는 사용자가 보는 경고뿐 아니라 Android에 전달되는 보안 상태다.
- dm-verity는 부팅 후 block 읽기 시점의 무결성 검증과 연결된다.
- rollback protection은 새 보안 패치 수준에서 만든 신뢰를 이전 취약 이미지가 재사용하지 못하게 한다.
- bootloader unlock은 검증 실패와 별개의 위험 상태이며 사용자 데이터 삭제와 연결된다.

## 관련 문서

- [Bootloader는 검증된 slot을 고르고 Android에 bootconfig를 넘긴다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/bootloader-selects-verified-slot-and-passes-bootconfig.md)
- [Verified Boot는 기기 소프트웨어의 chain of trust를 만든다](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/verified-boot-establishes-device-software-chain-of-trust.md)

공식 문서: [Android Verified Boot](https://source.android.com/docs/security/features/verifiedboot/avb), [Boot flow](https://source.android.com/docs/security/features/verifiedboot/boot-flow)
