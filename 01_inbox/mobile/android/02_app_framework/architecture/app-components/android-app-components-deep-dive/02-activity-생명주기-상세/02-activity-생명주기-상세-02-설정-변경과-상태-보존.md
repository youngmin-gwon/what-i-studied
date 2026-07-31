# 설정 변경과 상태 보존

화면 회전이나 언어 변경 시 Activity 가 재생성된다.

```kotlin
// ViewModel 사용 (권장)
class MyViewModel : ViewModel() {
    val data = MutableLiveData<String>()
}

class MyActivity : AppCompatActivity() {
    private val viewModel: MyViewModel by viewModels()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // ViewModel 의 데이터는 설정 변경 시에도 유지됨
        viewModel.data.observe(this) { value ->
            // UI 업데이트
        }
    }
}

// onSaveInstanceState 사용 (간단한 데이터)
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putString("key", "value")
}

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    savedInstanceState?.getString("key")?.let {
        // 복원된 데이터 사용
    }
}
```

더 자세한 내용은 [android-viewmodel](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel.md) 참고.
