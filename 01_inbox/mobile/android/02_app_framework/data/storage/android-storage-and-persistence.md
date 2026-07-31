# Android 저장소와 영속성

이 문서는 Android 저장소 선택의 진입점이다. 저장 매체 자체는 `02_app_framework/data/storage`에서 다루고, 암호화·키·백업처럼 보안 경계가 핵심인 내용은 `05_security_privacy/secure-storage`의 정본으로 연결한다.

## 판단 순서

1. [Android 저장소는 데이터 수명과 소유권으로 선택한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/choose-storage-by-data-lifetime-and-ownership.md)
2. [저장소 선택은 파일의 소유권과 공개 목적을 먼저 묻는다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-storage-is-selected-by-owner-and-public-purpose.md)
3. [DataStore는 작은 설정과 현재 상태를 저장한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/datastore-stores-small-settings-and-current-state.md)
4. [Room은 누적되고 조회되는 로컬 데이터를 저장한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/room-stores-accumulated-queryable-local-data.md)
5. [앱 전용 디렉터리는 소유 앱만 쓰는 파일에 사용한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/app-specific-directory-is-for-app-owned-files.md)
6. [MediaStore는 공유 미디어를 등록하고 접근한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/mediastore-registers-shared-media.md)
7. [SAF는 사용자가 고른 문서와 폴더에 접근한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/saf-grants-access-to-user-selected-documents.md)
8. [Android 민감 데이터는 암호화와 키 소유권을 함께 설계한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)
9. [백업과 복원은 데이터 경계를 명시적으로 설계해야 한다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/backup-restore-requires-explicit-data-boundaries.md)

## 하위 지도

- [영속 저장소 계약](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)
- [파일 접근 계약](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)
- [보안 저장소 계약](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)
- [저장소 수명과 백업 경계](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/storage-lifecycle-and-backup.md)
