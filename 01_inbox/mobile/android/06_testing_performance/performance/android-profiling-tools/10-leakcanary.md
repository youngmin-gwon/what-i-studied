# LeakCanary

상위 노트: [android-profiling-tools](01_inbox/mobile/android/06_testing_performance/performance/android-profiling-tools.md)

메모리 누수 자동 감지.

```kotlin
// build.gradle.kts
dependencies {
    debugImplementation("com.squareup.leakcanary:leakcanary-android:2.12")
}

// 자동으로 누수 감지 및 알림
// 커스터마이징
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        LeakCanary.config = LeakCanary.config.copy(
            dumpHeap = true,
            retainedVisibleThreshold = 3
        )
    }
}
```
