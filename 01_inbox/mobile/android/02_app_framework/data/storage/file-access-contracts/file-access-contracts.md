---
title: 파일 접근 계약
tags: [android, android/data, android/storage, android/file-access-contracts]
aliases: ["파일 접근 계약"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 파일 접근 계약

파일 접근은 파일의 형식보다 소유권과 공개 목적을 먼저 본다. 앱이 소유하는 파일, 사용자가 고르는 문서, 갤러리에 공개되는 미디어는 서로 다른 계약이다.

## 정본 노트

- [저장소 선택은 파일의 소유권과 공개 목적을 먼저 묻는다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-storage-is-selected-by-owner-and-public-purpose.md)
- [앱 전용 디렉터리는 소유 앱만 쓰는 파일에 사용한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/app-specific-directory-is-for-app-owned-files.md)
- [MediaStore는 공유 미디어를 등록하고 접근한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/mediastore-registers-shared-media.md)
- [SAF는 사용자가 고른 문서와 폴더에 접근한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/saf-grants-access-to-user-selected-documents.md)
- [Photo Picker는 필요한 미디어 접근 범위를 줄인다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/photo-picker-minimizes-media-access.md)
- [Scoped Storage는 공유 저장소 직접 접근을 제한한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/scoped-storage-limits-direct-shared-storage-access.md)
- [캐시는 정본이 아니라 재생성 가능한 데이터다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/cache-is-recreatable-data-not-source-of-truth.md)

상위 지도: [Android 저장소와 영속성](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-persistence.md)
