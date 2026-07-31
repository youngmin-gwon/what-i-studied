# MediaStore API

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
