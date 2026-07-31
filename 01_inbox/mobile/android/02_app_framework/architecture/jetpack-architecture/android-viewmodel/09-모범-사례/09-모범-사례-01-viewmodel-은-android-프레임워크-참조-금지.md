# ViewModel 은 Android 프레임워크 참조 금지

```kotlin
// ❌ 나쁜 예
class BadViewModel(private val context: Context) : ViewModel() {
    fun showToast() {
        Toast.makeText(context, "Message", Toast.LENGTH_SHORT).show()
    }
}

// ✅ 좋은 예
class GoodViewModel : ViewModel() {
    private val _showToast = MutableLiveData<String>()
    val showToast: LiveData<String> = _showToast
    
    fun triggerToast() {
        _showToast.value = "Message"
    }
}

class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        viewModel.showToast.observe(this) { message ->
            Toast.makeText(this, message, Toast.LENGTH_SHORT).show()
        }
    }
}
```

**예외:** `AndroidViewModel` 은 `Application` 컨텍스트를 받을 수 있음

```kotlin
class MyViewModel(application: Application) : AndroidViewModel(application) {
    private val context: Context
        get() = getApplication()
    
    // Application 컨텍스트는 메모리 누수 없음
    fun getString(resId: Int): String {
        return context.getString(resId)
    }
}
```
