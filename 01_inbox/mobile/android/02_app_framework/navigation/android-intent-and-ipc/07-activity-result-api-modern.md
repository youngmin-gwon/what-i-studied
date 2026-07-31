# Activity Result API (Modern)

상위 노트: [[android-intent-and-ipc]]

`startActivityForResult()` / `onActivityResult()` 는 **deprecated** 되었다. 현대적 대안은 `ActivityResultContracts` 이다.

```kotlin
class MyActivity : AppCompatActivity() {

    // 1. 콜백 등록 (onCreate 전에)
    private val pickImage = registerForActivityResult(
        ActivityResultContracts.PickVisualMedia()
    ) { uri: Uri? ->
        uri?.let { handleSelectedImage(it) }
    }
    
    private val requestPermission = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted: Boolean ->
        if (isGranted) {
            // 권한 허용됨
        } else {
            // 권한 거부됨
        }
    }
    
    private val takePicture = registerForActivityResult(
        ActivityResultContracts.TakePicture()
    ) { success: Boolean ->
        if (success) {
            // 사진 촬영 성공
        }
    }

    // 2. 실행
    fun onPickImageClick() {
        pickImage.launch(
            PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly)
        )
    }
    
    fun onRequestCameraClick() {
        requestPermission.launch(Manifest.permission.CAMERA)
    }
}
```

**주요 Contract 종류:**

| Contract | 용도 | 반환 |
|----------|------|------|
| `PickVisualMedia` | Photo Picker (권한 불필요!) | `Uri?` |
| `PickMultipleVisualMedia` | 다중 선택 | `List<Uri>` |
| `TakePicture` | 카메라 촬영 | `Boolean` |
| `RequestPermission` | 단일 권한 요청 | `Boolean` |
| `RequestMultiplePermissions` | 다중 권한 요청 | `Map<String, Boolean>` |
| `OpenDocument` | SAF 파일 선택 | `Uri?` |
| `CreateDocument` | SAF 파일 생성 | `Uri?` |
| `GetContent` | 컨텐츠 선택 | `Uri?` |

##### 커스텀 Contract

```kotlin
class PickUserContract : ActivityResultContract<Unit, User?>() {
    override fun createIntent(context: Context, input: Unit): Intent {
        return Intent(context, UserPickerActivity::class.java)
    }
    
    override fun parseResult(resultCode: Int, intent: Intent?): User? {
        if (resultCode != Activity.RESULT_OK) return null
        return intent?.getParcelableExtra("selected_user")
    }
}

// 사용
private val pickUser = registerForActivityResult(PickUserContract()) { user ->
    user?.let { selectedUser = it }
}
```
