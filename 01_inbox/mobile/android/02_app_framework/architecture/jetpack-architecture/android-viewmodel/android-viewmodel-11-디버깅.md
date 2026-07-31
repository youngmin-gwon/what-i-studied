# 디버깅

상위 노트: [android-viewmodel](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel.md)

```kotlin
class DebugViewModel : ViewModel() {
    init {
        Log.d("ViewModel", "Created: ${this.hashCode()}")
    }
    
    override fun onCleared() {
        super.onCleared()
        Log.d("ViewModel", "Cleared: ${this.hashCode()}")
    }
}

// Activity
class MainActivity : AppCompatActivity() {
    private val viewModel: DebugViewModel by viewModels()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d("Activity", "ViewModel hash: ${viewModel.hashCode()}")
        // 화면 회전해도 같은 해시코드 출력됨
    }
}
```
