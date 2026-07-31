# Flipper (Meta)

상위 노트: [android-debugging-techniques](01_inbox/mobile/android/06_testing_performance/debugging/android-debugging-techniques.md)

강력한 디버깅 플랫폼.

```kotlin
// build.gradle.kts
dependencies {
    debugImplementation("com.facebook.flipper:flipper:0.212.0")
    debugImplementation("com.facebook.soloader:soloader:0.10.5")
    debugImplementation("com.facebook.flipper:flipper-network-plugin:0.212.0")
    debugImplementation("com.facebook.flipper:flipper-leakcanary2-plugin:0.212.0")
}

// Application
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        SoLoader.init(this, false)
        
        if (BuildConfig.DEBUG && FlipperUtils.shouldEnableFlipper(this)) {
            val client = AndroidFlipperClient.getInstance(this)
            client.addPlugin(InspectorFlipperPlugin(this, DescriptorMapping.withDefaults()))
            client.addPlugin(NetworkFlipperPlugin())
            client.addPlugin(DatabasesFlipperPlugin(this))
            client.addPlugin(LeakCanary2FlipperPlugin())
            client.start()
        }
    }
}
```
