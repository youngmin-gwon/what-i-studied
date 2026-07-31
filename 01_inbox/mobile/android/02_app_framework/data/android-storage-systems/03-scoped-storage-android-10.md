# Scoped Storage (Android 10+)

상위 노트: [[android-storage-systems]]

앱이 자신의 파일만 직접 접근하고, 다른 파일은 MediaStore/SAF 를 통해 접근한다.

##### MediaStore API

미디어 파일 (이미지, 비디오, 오디오, 다운로드) 접근.

**이미지 저장:**

```kotlin
fun saveImageToGallery(bitmap: Bitmap, displayName: String) {
    val contentValues = ContentValues().apply {
        put(MediaStore.Images.Media.DISPLAY_NAME, displayName)
        put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            put(MediaStore.Images.Media.RELATIVE_PATH, Environment.DIRECTORY_PICTURES)
            put(MediaStore.Images.Media.IS_PENDING, 1)
        }
    }
    
    val resolver = contentResolver
    val uri = resolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, contentValues)
    
    uri?.let {
        resolver.openOutputStream(it)?.use { outputStream ->
            bitmap.compress(Bitmap.CompressFormat.JPEG, 95, outputStream)
        }
        
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            contentValues.clear()
            contentValues.put(MediaStore.Images.Media.IS_PENDING, 0)
            resolver.update(it, contentValues, null, null)
        }
    }
}
```

**이미지 읽기:**

```kotlin
fun loadImagesFromGallery(): List<Uri> {
    val images = mutableListOf<Uri>()
    val projection = arrayOf(
        MediaStore.Images.Media._ID,
        MediaStore.Images.Media.DISPLAY_NAME,
        MediaStore.Images.Media.DATE_ADDED
    )
    
    val sortOrder = "${MediaStore.Images.Media.DATE_ADDED} DESC"
    
    contentResolver.query(
        MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
        projection,
        null,
        null,
        sortOrder
    )?.use { cursor ->
        val idColumn = cursor.getColumnIndexOrThrow(MediaStore.Images.Media._ID)
        
        while (cursor.moveToNext()) {
            val id = cursor.getLong(idColumn)
            val uri = ContentUris.withAppendedId(
                MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
                id
            )
            images.add(uri)
        }
    }
    
    return images
}
```

**비디오 저장:**

```kotlin
@RequiresApi(Build.VERSION_CODES.Q)
fun saveVideoToGallery(videoFile: File, displayName: String) {
    val contentValues = ContentValues().apply {
        put(MediaStore.Video.Media.DISPLAY_NAME, displayName)
        put(MediaStore.Video.Media.MIME_TYPE, "video/mp4")
        put(MediaStore.Video.Media.RELATIVE_PATH, Environment.DIRECTORY_MOVIES)
    }
    
    val uri = contentResolver.insert(
        MediaStore.Video.Media.EXTERNAL_CONTENT_URI,
        contentValues
    )
    
    uri?.let {
        contentResolver.openOutputStream(it)?.use { outputStream ->
            videoFile.inputStream().use { inputStream ->
                inputStream.copyTo(outputStream)
            }
        }
    }
}
```

##### Storage Access Framework (SAF)

사용자가 직접 파일/폴더를 선택하도록 한다.

**파일 선택:**

```kotlin
class MainActivity : AppCompatActivity() {
    private val openDocumentLauncher = registerForActivityResult(
        ActivityResultContracts.OpenDocument()
    ) { uri: Uri? ->
        uri?.let {
            // 선택된 파일 읽기
            contentResolver.openInputStream(it)?.use { inputStream ->
                val text = inputStream.bufferedReader().readText()
                // 사용
            }
        }
    }
    
    fun selectDocument() {
        openDocumentLauncher.launch(arrayOf("text/plain", "application/pdf"))
    }
}
```

**파일 생성:**

```kotlin
private val createDocumentLauncher = registerForActivityResult(
    ActivityResultContracts.CreateDocument("text/plain")
) { uri: Uri? ->
    uri?.let {
        contentResolver.openOutputStream(it)?.use { outputStream ->
            outputStream.write("Hello, SAF!".toByteArray())
        }
    }
}

fun createNewDocument() {
    createDocumentLauncher.launch("myfile.txt")
}
```

**폴더 선택 (트리 접근):**

```kotlin
private val openDocumentTreeLauncher = registerForActivityResult(
    ActivityResultContracts.OpenDocumentTree()
) { uri: Uri? ->
    uri?.let { treeUri ->
        // 영구 권한 획득
        contentResolver.takePersistableUriPermission(
            treeUri,
            Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_WRITE_URI_PERMISSION
        )
        
        // 폴더 내 파일 나열
        val documentFile = DocumentFile.fromTreeUri(this, treeUri)
        documentFile?.listFiles()?.forEach { file ->
            Log.d("SAF", "File: ${file.name}")
        }
    }
}
```
