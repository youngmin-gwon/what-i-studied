# Scoped Storage

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 앱별로 외부 저장소 접근을 제한하는 정책

**상세**:

Android 10 부터 도입되어 앱은 자신의 디렉토리와 MediaStore 로만 접근 가능하다. 다른 앱 파일이나 임의 경로 접근이 차단된다.

**접근 방식**:

```kotlin
// 1. 앱 전용 디렉토리 (권한 불필요)
val appFiles = context.getExternalFilesDir(null)
// /sdcard/Android/data/com.example/files/

// 2. MediaStore (사진/비디오/오디오)
val uri = MediaStore.Images.Media.EXTERNAL_CONTENT_URI
contentResolver.query(uri, ...)

// 3. Storage Access Framework (파일 선택)
val intent = Intent(Intent.ACTION_OPEN_DOCUMENT)
intent.type = "*/*"
startActivityForResult(intent, REQUEST_CODE)
```

**관련**: [android-security-sandbox](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-sandbox.md), [android-storage-systems](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems.md)

---
