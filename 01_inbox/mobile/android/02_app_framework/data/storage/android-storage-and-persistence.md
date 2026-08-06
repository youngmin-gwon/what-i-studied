---
title: android-storage-and-persistence
tags: [android, android/data, android/storage]
aliases: ["Android Storage and Persistence"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android 저장소는 수명과 소유권 보안 경계에 따라 다른 계약을 가진다

배경 지식: [리눅스 파일 시스템](../../../../../linux/filesystems.md)

Android storage 는 저장 대상의 수명, 소유권, 공개 목적, 보안 경계를 먼저 나눈다. Room, DataStore, app-specific file, MediaStore, SAF, Photo Picker, secure storage 는 서로 대체재가 아니라 다른 계약이다.

### 판단 순서

1. [데이터 수명과 소유권으로 저장소를 선택한다](./persistence-contracts/choose-storage-by-data-lifetime-and-ownership.md)
2. [파일은 소유권과 공개 목적을 먼저 판단한다](./file-access-contracts/file-storage-is-selected-by-owner-and-public-purpose.md)
3. [DataStore는 작은 설정과 현재 상태를 저장한다](./persistence-contracts/datastore-stores-small-settings-and-current-state.md)
4. [Room은 누적되고 조회되는 로컬 데이터를 저장한다](./persistence-contracts/room-stores-accumulated-queryable-local-data.md)
5. [앱 전용 디렉터리는 앱 소유 파일에 사용한다](./file-access-contracts/app-specific-directory-is-for-app-owned-files.md)
6. [MediaStore는 공유 미디어를 등록한다](./file-access-contracts/mediastore-registers-shared-media.md)
7. [SAF는 사용자가 고른 문서와 폴더에 접근한다](./file-access-contracts/saf-grants-access-to-user-selected-documents.md)
8. [Photo Picker는 미디어 접근 범위를 줄인다](./file-access-contracts/photo-picker-minimizes-media-access.md)
9. [민감 데이터는 암호화와 키 소유권을 함께 설계한다](../../../05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)
10. [백업과 복원은 데이터 경계를 명시한다](../../../05_security_privacy/secure-storage/storage-lifecycle-and-backup/backup-restore-requires-explicit-data-boundaries.md)

### 정본 지도

- [영속 저장소 계약](./persistence-contracts/persistence-contracts.md)
- [파일 접근 계약](./file-access-contracts/file-access-contracts.md)
- [보안 저장소 계약](../../../05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)
- [Android Data Layer Map](../android-data-layer-map.md)
