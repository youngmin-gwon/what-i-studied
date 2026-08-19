---
title: fileprovider-grants-narrow-uri-access-instead-of-file-path-sharing
tags: [android, android/app-components, android/architecture, android/security]
aliases: ["FileProvider는 파일 경로 공유 대신 좁은 URI 접근을 허용한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## FileProvider는 파일 경로 공유 대신 좁은 URI 접근을 허용한다

`FileProvider` 는 안드로이드 7.0 (API 24) 이후 파일 공유의 보안 표준(Strict Mode 적용)으로, **원시 파일 경로(`file://`)를 외부에 직접 노출하는 대신 보안이 강화된 `content://` URI 를 생성하고, 임시 일회성 접근 권한(`FLAG_GRANT_READ_URI_PERMISSION`)을 좁게 부여하는 특수 `ContentProvider` 의 하위 클래스**다.

---

### 1. 개념 및 핵심 명제 (What)

- **`file://` URI 공유 금지**:
  외부 앱에 `file:///sdcard/photo.jpg` 와 같은 원시 경로를 Intent 로 넘기면 `FileUriExposedException` 이 발생한다.
- **임시 권한 부여 (`FLAG_GRANT_READ_URI_PERMISSION`)**:
  `FileProvider.getUriForFile()` 로 생성된 `content://` URI 는 해당 Intent 를 수신하는 대상 패키지에 대해서만 대상 파일 읽기/쓰기 임시 권한을 부여하고, 컴포넌트가 종료되면 권한이 자동으로 회수된다.

---

### 2. 코드 예시 (FileProvider 설정 및 Intent 전달)

```kotlin
val photoFile = File(context.filesDir, "images/sample.jpg")

val photoUri: Uri = FileProvider.getUriForFile(
    context,
    "${context.packageName}.fileprovider",
    photoFile
)

val shareIntent = Intent(Intent.ACTION_SEND).apply {
    type = "image/jpeg"
    putExtra(Intent.EXTRA_STREAM, photoUri)
    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION) // 좁은 임시 읽기 권한 부여
}
context.startActivity(Intent.createChooser(shareIntent, "이미지 공유"))
```

---

### 3. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component.md)
- 공식 가이드: [Share Files with FileProvider](https://developer.android.com/training/secure-file-sharing/setup-sharing)

검증일: 2026-08-05. FileProvider 보안 스펙 확인 완료.
