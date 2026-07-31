# Lifecycle

상위 노트: [[android-jetpack-architecture]]

생명주기를 인식하는 컴포넌트.

```kotlin
class MyObserver : DefaultLifecycleObserver {
    override fun onCreate(owner: LifecycleOwner) {
        // Activity/Fragment onCreate 시
    }
    
    override fun onStart(owner: LifecycleOwner) {
        // onStart 시
    }
    
    override fun onResume(owner: LifecycleOwner) {
        // onResume 시
    }
    
    override fun onPause(owner: LifecycleOwner) {
        // onPause 시
    }
    
    override fun onStop(owner: LifecycleOwner) {
        // onStop 시
    }
    
    override fun onDestroy(owner: LifecycleOwner) {
        // onDestroy 시
    }
}

// 사용
class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        lifecycle.addObserver(MyObserver())
    }
}

// 커스텀 Lifecycle-aware 컴포넌트
// ✅ DefaultLifecycleObserver 사용 (권장)
class MyLocationManager(private val context: Context) : DefaultLifecycleObserver {
    override fun onStart(owner: LifecycleOwner) {
        // 위치 업데이트 시작
    }
    
    override fun onStop(owner: LifecycleOwner) {
        // 위치 업데이트 중지
    }
}

// ❌ @OnLifecycleEvent — Deprecated (Lifecycle 2.4.0+)
// 아래 코드는 더 이상 사용하면 안 됨
// class OldLocationManager : LifecycleObserver {
//     @OnLifecycleEvent(Lifecycle.Event.ON_START)  // ← 리플렉션 기반, deprecated
//     fun start() { }
// }
```
