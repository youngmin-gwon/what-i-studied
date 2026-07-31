# Memory Leak 디버깅

상위 노트: [[android-debugging-techniques]]

##### LeakCanary

```kotlin
// build.gradle.kts
dependencies {
    debugImplementation("com.squareup.leakcanary:leakcanary-android:2.12")
}

// 자동으로 누수 감지
// 알림으로 결과 표시
```

##### 수동 분석

```kotlin
// 의심되는 객체 추적
class MyActivity : AppCompatActivity() {
    companion object {
        private val instances = mutableListOf<WeakReference<MyActivity>>()
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        instances.add(WeakReference(this))
        
        // 주기적으로 확인
        instances.removeAll { it.get() == null }
        Log.d("Leak", "Active instances: ${instances.size}")
    }
}
```
