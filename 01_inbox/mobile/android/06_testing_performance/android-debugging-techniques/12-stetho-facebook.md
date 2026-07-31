# Stetho (Facebook)

상위 노트: [[android-debugging-techniques]]

웹 브라우저로 앱 디버깅.

```kotlin
// build.gradle.kts
dependencies {
    debugImplementation("com.facebook.stetho:stetho:1.6.0")
    debugImplementation("com.facebook.stetho:stetho-okhttp3:1.6.0")
}

// Application
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        if (BuildConfig.DEBUG) {
            Stetho.initializeWithDefaults(this)
        }
    }
}

// OkHttp 에 연결
val client = OkHttpClient.Builder()
    .addNetworkInterceptor(StethoInterceptor())
    .build()
```

```
# Chrome 에서
chrome://inspect/#devices
```
