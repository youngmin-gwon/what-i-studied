---
title: "fstab은 mount와 검증 플래그를 묶은 부팅 계약이다"
tags: [android, android/system-internals, android/boot-runtime, android/init]
aliases: ["fstab은 mount와 검증 플래그를 묶은 부팅 계약이다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# fstab은 mount와 검증 플래그를 묶은 부팅 계약이다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

Android의 fstab은 어떤 block device를 어디에 mount할지뿐 아니라 `wait`, `slotselect`, `avb`, `logical`, `first_stage_mount`, `fileencryption`, `checkpoint` 같은 boot-time policy를 함께 선언한다.

## 판단 기준

- `first_stage_mount`는 second stage init이 vendor/system rc와 정책을 읽기 전에 필요한 파티션을 올린다.
- `slotselect`는 A/B slot suffix를 mount 대상 선택에 반영한다.
- `avb`는 mount 경로와 Verified Boot 검증 경계를 연결한다.
- `/data` mount는 file-based encryption, metadata encryption, checkpoint와 함께 부팅 성공 여부에 영향을 준다.

## 관련 문서

- [파티션 구조는 system과 vendor의 업데이트 경계를 만든다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/partitions-define-system-vendor-and-update-boundaries.md)
- [FBE의 CE와 DE 저장소는 잠금 해제 전후 접근 가능성이 다르다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/fbe-ce-and-de-separate-storage-availability.md)
