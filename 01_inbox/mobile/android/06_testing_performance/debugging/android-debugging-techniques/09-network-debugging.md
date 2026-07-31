# Network Debugging

상위 노트: [android-debugging-techniques](01_inbox/mobile/android/06_testing_performance/debugging/android-debugging-techniques.md)

##### Charles Proxy / Fiddler

```xml
<!-- network_security_config.xml -->
<network-security-config>
    <debug-overrides>
        <trust-anchors>
            <certificates src="user" />
        </trust-anchors>
    </debug-overrides>
</network-security-config>
```

```kotlin
// AndroidManifest.xml
<application
    android:networkSecurityConfig="@xml/network_security_config">
```

```bash
# Charles 인증서 설치
# Settings → Security → Install from storage
```

##### OkHttp Interceptor

```kotlin
val loggingInterceptor = HttpLoggingInterceptor { message ->
    Log.d("OkHttp", message)
}.apply {
    level = HttpLoggingInterceptor.Level.BODY
}

val client = OkHttpClient.Builder()
    .addInterceptor(loggingInterceptor)
    .build()
```
