---
title: 06-저장소-무제한-scoped-storage-2019
tags: []
aliases: []
date modified: 2026-07-31 15:42:26 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## 저장소: 무제한 → Scoped Storage (2019)

상위 노트: [02-주요-기술-전환](01_inbox/mobile/android/00_foundations/history/android-evolution-history/02-%EC%A3%BC%EC%9A%94-%EA%B8%B0%EC%88%A0-%EC%A0%84%ED%99%98.md)

**Phase 1: 무제한 접근** (~Android 9)

```java
// READ_EXTERNAL_STORAGE만 있으면
// /sdcard의 모든 파일 읽기 가능
File photo = new File("/sdcard/DCIM/photo.jpg");
```

**문제**:

- 프라이버시 침해 (모든 사진 접근 가능)
- 앱 삭제 후에도 잔여 파일

**Phase 2: Scoped Storage** (Android 10+)

```kotlin
// MediaStore API 사용 필수
val uri = MediaStore.Images.Media.EXTERNAL_CONTENT_URI
contentResolver.query(uri, ...) // 권한 있는 파일만
```

**Phase 3: Photo Picker** (Android 13, 2022)

```kotlin
// 시스템 UI로 사진 선택
val intent = Intent(MediaStore.ACTION_PICK_IMAGES)
startActivityForResult(intent, REQUEST_CODE)
// → READ_MEDIA_IMAGES 권한 불필요
```
