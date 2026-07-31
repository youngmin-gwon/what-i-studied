# Timber (구조화된 로깅)

상위 노트: [[android-debugging-techniques]]

```kotlin
// build.gradle.kts
dependencies {
    implementation("com.jakewharton.timber:timber:5.0.1")
}

// Application
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        if (BuildConfig.DEBUG) {
            Timber.plant(Timber.DebugTree())
        } else {
            Timber.plant(CrashReportingTree())
        }
    }
}

class CrashReportingTree : Timber.Tree() {
    override fun log(priority: Int, tag: String?, message: String, t: Throwable?) {
        if (priority == Log.ERROR || priority == Log.WARN) {
            // Firebase Crashlytics 등에 전송
            FirebaseCrashlytics.getInstance().log(message)
            t?.let { FirebaseCrashlytics.getInstance().recordException(it) }
        }
    }
}

// 사용
Timber.d("User logged in: %s", userId)
Timber.e(exception, "Failed to load data")
```
