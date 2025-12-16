---
title: apple-storage-and-filesystems
tags: [apple, filesystem, storage]
aliases: []
date modified: 2025-12-16 16:15:48 +09:00
date created: 2025-12-16 16:09:38 +09:00
---

## Storage & Filesystems apple storage filesystem

파일이 어디에 저장되고, 어떻게 보호되는지 쉽게 정리했다. 용어는 [[apple-glossary]].

### 파일 위치
- 앱 컨테이너: Documents(사용자 데이터), Library/Application Support(앱 데이터), Library/Caches(지워도 되는 데이터), tmp(임시).
- App Groups: 여러 앱/확장이 공유하는 컨테이너.
- iCloud Drive: FileProvider/UIDocumentPicker 로 접근. 사용자가 선택한 파일만 접근 가능.

### 보호 등급
- [[apple-glossary#Data Protection Class|Data Protection Class]] 로 잠금 상태와 연계된다. 기본은 Complete Until First Unlock.
- Keychain 항목도 접근 제어 등급을 설정할 수 있다.

### 파일 시스템 종류
- APFS: 스냅샷, 클론, 공간 공유 지원. iOS/macOS 공통.
- Case-sensitive 여부는 볼륨 옵션에 따라 다르다 (앱 빌드 시 주의).

### 저장 용량 관리
- iOS/watchOS 는 공간이 부족할 때 캐시를 지울 수 있다. `isExcludedFromBackup` 로 백업 제외 설정 필요.
- on-disk vs in-memory 캐시 전략을 분리한다.

### 백업/동기화
- iCloud 백업은 사용자가 선택, 일부 폴더 (Caches) 는 제외된다.
- CloudKit 은 앱 데이터베이스, iCloud Drive 는 파일. 혼동하지 말 것.

### 보안/권한
- macOS: 샌드박스 앱은 Security-scoped bookmark 를 통해 사용자가 고른 파일/폴더에만 접근 가능.
- iOS: 사용자가 선택한 사진만 접근하도록 제한 (Photos picker). 전체 라이브러리 접근은 별도 권한이 필요.

### 성능
- 대용량 파일은 스트리밍/청크 업로드 사용.
- 파일 핸들/FD 를 적게 열고, 백그라운드에서 I/O 를 수행한다.

### 디버깅
- `Container` 경로는 Xcode/Devices window 또는 `xcrun simctl get_app_container` 로 확인.
- APFS 스냅샷/기기 백업에서 파일 상태를 검토할 수 있다.

### 링크

[[apple-sandbox-and-security]], [[apple-networking-and-cloud]], [[apple-build-and-distribution]].
