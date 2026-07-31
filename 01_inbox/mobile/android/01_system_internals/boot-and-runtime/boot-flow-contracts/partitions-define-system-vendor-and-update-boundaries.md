---
title: "파티션 구조는 system과 vendor의 업데이트 경계를 만든다"
tags: [android, android/system-internals, android/boot-runtime, android/boot]
aliases: ["파티션 구조는 system과 vendor의 업데이트 경계를 만든다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 파티션 구조는 system과 vendor의 업데이트 경계를 만든다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

Android 파티션은 저장소 배치도가 아니라 업데이트, 검증, vendor/system 책임 분리의 경계다. `boot`, `init_boot`, `vendor_boot`, `system`, `system_ext`, `product`, `vendor`, `odm`, `userdata`, `metadata`, `vbmeta`는 서로 다른 수명과 검증 책임을 가진다.

## 판단 기준

- framework와 product 코드는 system 계열 파티션에, SoC/OEM 의존 코드는 vendor/odm 계열에 둔다.
- `vendor_boot`는 GKI 이후 vendor-specific ramdisk와 boot-time vendor 정보를 분리하기 위한 파티션이다.
- `metadata`는 metadata encryption과 snapshot merge 같은 부팅 전후 상태에 쓰일 수 있다.
- `vbmeta`는 여러 파티션의 Verified Boot metadata를 묶는 검증 루트 역할을 한다.

## 관련 문서

- [Dynamic partition은 super 안에서 논리 파티션 크기를 조정한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/dynamic-partitions-resize-logical-images-inside-super.md)
- [fstab은 mount와 검증 플래그를 묶은 부팅 계약이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/fstab-is-boot-time-mount-and-verification-contract.md)

공식 문서: [Partitions overview](https://source.android.com/docs/core/architecture/partitions), [Vendor boot partitions](https://source.android.com/docs/core/architecture/partitions/vendor-boot-partitions)
