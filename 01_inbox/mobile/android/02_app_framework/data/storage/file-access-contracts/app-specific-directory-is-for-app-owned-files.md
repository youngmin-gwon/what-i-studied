---
title: app-specific-directory-is-for-app-owned-files
tags: [android, android/data, android/file-access-contracts, android/storage]
aliases: ["앱 전용 디렉터리: 소유 앱만 쓰는 파일"]
date modified: 2026-08-03 18:07:57 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 앱 전용 디렉터리: 소유 앱만 쓰는 파일

상위 문서: [파일 접근 계약](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)

관련 노트: [캐시는 정본이 아니라 재생성 가능한 데이터다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/cache-is-recreatable-data-not-source-of-truth.md)

앱 전용 디렉터리는 파일의 소유자와 수명이 앱에 묶인 저장 영역이다.

사용자나 다른 앱이 갤러리에서 직접 볼 필요가 없는 파일에 우선 적용한다.

### 대표 API

```kotlin
val permanentFile = File(context.filesDir, "analysis/result.json")
val temporaryFile = File(context.cacheDir, "preview.jpg")
val externalFile = File(
    context.getExternalFilesDir(Environment.DIRECTORY_DOCUMENTS),
    "export.zip"
)
val externalCache = File(context.externalCacheDir, "download.part")
```

`filesDir` 는 앱 내부의 영구 파일 영역이다.

`cacheDir` 는 다시 생성할 수 있는 임시 파일 영역이다.

`getExternalFilesDir()` 는 외부 저장소에 있는 앱 전용 영역이다.

`getExternalCacheDir()` 는 외부 저장소의 앱 전용 캐시 영역이다.

### 수명과 공개 범위

- 앱을 삭제하면 앱 전용 파일도 함께 제거된다.
- 내부 앱 전용 파일은 다른 앱이 직접 읽을 수 없다.
- 앱 전용 외부 파일도 공유 컬렉션의 일반 미디어가 아니다.
- 캐시는 저장 공간 부족 시 시스템이 삭제할 수 있다.
- 캐시에 복구할 수 없는 원본 데이터나 비밀값을 넣지 않는다.

이미지나 영상이라는 형식만으로 MediaStore 를 선택하지 않는다.

사용자에게 공개할 필요가 없고 앱 내부 처리에만 쓰면 앱 전용 디렉터리가 맞다.

### 적용 예

- 운동 분석 중간 산출물
- 네트워크 다운로드의 재생성 가능한 사본
- 이미지 리사이즈와 업로드 전 임시 파일
- 앱 내부 export 를 만들기 위한 작업 파일

반대로 사용자가 갤러리에서 계속 보거나 다른 앱으로 공유해야 하는 결과물은

[MediaStore로 공유 미디어 저장](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/mediastore-registers-shared-media.md) 을 검토한다.

사용자가 직접 파일 위치를 정해야 한다면

[SAF로 사용자 선택 파일 다루기](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/saf-grants-access-to-user-selected-documents.md) 가 더 적합하다.

### 구현 원칙

저장소 객체가 오래 살아야 하면 Activity 가 아닌 Application Context 를 전달한다.

파일 경로를 문자열로 조립하지 말고 Context 가 제공하는 디렉터리를 사용한다.

큰 파일은 메모리에 한 번에 올리지 말고 스트림으로 복사한다.

작업 완료 후 임시 파일을 삭제하고, 실패 시에도 정리하도록 `finally` 를 둔다.

파일 이름에는 사용자 입력을 그대로 경로로 사용하지 않는다.

영구 파일과 캐시를 별도 하위 디렉터리로 나누면 삭제 정책을 적용하기 쉽다.

앱 전용 디렉터리는 권한을 덜 요구한다는 장점만으로 선택하는 것이 아니다.

파일의 소유권, 공개 필요성, 삭제 시점이 앱 생명주기와 일치하는지가 핵심이다.
