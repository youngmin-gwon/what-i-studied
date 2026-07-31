# Android Storage Systems

이 문서는 Android 파일 저장소와 공유 저장소 설명의 진입점이다. Scoped Storage, MediaStore, SAF, 앱 전용 파일, 캐시 수명은 정본 노트로 분리했다.

## 정본

- [파일 접근 계약](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)
- [앱 전용 디렉터리는 소유 앱만 쓰는 파일에 사용한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/app-specific-directory-is-for-app-owned-files.md)
- [MediaStore는 공유 미디어를 등록하고 접근한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/mediastore-registers-shared-media.md)
- [SAF는 사용자가 고른 문서와 폴더에 접근한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/saf-grants-access-to-user-selected-documents.md)
- [Scoped Storage는 공유 저장소 직접 접근을 제한한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/scoped-storage-limits-direct-shared-storage-access.md)
- [캐시는 정본이 아니라 재생성 가능한 데이터다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/cache-is-recreatable-data-not-source-of-truth.md)
- [저장소 수명과 백업 경계](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/storage-lifecycle-and-backup.md)
