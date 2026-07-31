# Storage Access Framework (SAF)

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
