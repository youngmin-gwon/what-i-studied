---
title: storage-lifecycle-and-backup
tags: []
aliases: []
date modified: 2026-08-03 18:14:42 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

## 저장소 생명주기와 백업 계약

### 저장소 수명과 백업 경계

이 지도는 저장된 데이터가 언제 접근 가능한지, 언제 사라져도 되는지, 어떤 경계를 넘어 백업·복원될 수 있는지를 다룬다.

#### 정본 노트

- [FBE는 CE와 DE로 저장소 가용 시점을 나눈다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/fbe-ce-and-de-separate-storage-availability.md)
- [Direct Boot는 최소한의 device-protected 데이터만 요구한다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/direct-boot-requires-minimal-device-protected-data.md)
- [백업과 복원은 데이터 경계를 명시적으로 설계해야 한다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/backup-restore-requires-explicit-data-boundaries.md)
- [캐시는 정본이 아니라 재생성 가능한 데이터다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/cache-is-recreatable-data-not-source-of-truth.md)
- [Scoped Storage와 암호화는 서로 다른 경계를 보호한다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/scoped-storage-and-encryption-protect-different-boundaries.md)

관련 지도: [Android 저장소와 영속성](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-persistence.md), [보안 저장소 계약](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)
