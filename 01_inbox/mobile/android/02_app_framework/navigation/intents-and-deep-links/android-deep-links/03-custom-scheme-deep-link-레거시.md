# Custom Scheme Deep Link (레거시)

```xml
<!-- AndroidManifest.xml -->
<activity android:name=".DetailActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:scheme="myapp"
            android:host="detail"
            android:pathPrefix="/" />
    </intent-filter>
</activity>
```

```kotlin
// 수신 처리
class DetailActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        intent?.data?.let { uri ->
            // myapp://detail/123 → pathSegments[0] = "123"
            val itemId = uri.lastPathSegment
            loadItem(itemId)
        }
    }
}
```
