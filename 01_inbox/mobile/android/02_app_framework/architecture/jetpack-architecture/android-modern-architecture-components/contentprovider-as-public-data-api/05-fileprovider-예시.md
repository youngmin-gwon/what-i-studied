# FileProvider 예시

일반 앱에서 가장 자주 만나는 ContentProvider 계열은 직접 Provider를 구현하는 것이 아니라 `FileProvider`를 사용하는 경우입니다.

```xml

<provider android:name="androidx.core.content.FileProvider"
    android:authorities="${applicationId}.fileprovider" android:exported="false"
    android:grantUriPermissions="true">
    <meta-data android:name="android.support.FILE_PROVIDER_PATHS"
        android:resource="@xml/file_paths" />
</provider>
```

```kotlin
val uri = FileProvider.getUriForFile(
    context,
    "${context.packageName}.fileprovider",
    pdfFile,
)

val intent = Intent(Intent.ACTION_SEND).apply {
    type = "application/pdf"
    putExtra(Intent.EXTRA_STREAM, uri)
    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
}
context.startActivity(Intent.createChooser(intent, "공유"))
```

> [!IMPORTANT]
> 파일 경로(`/storage/.../invoice.pdf`)를 다른 앱에 직접 넘기는 방식은 안전하지 않습니다. `content://` URI와 임시 권한을 주는
`FileProvider`가 현대 Android의 표준 방식입니다.

---
