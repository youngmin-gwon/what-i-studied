# Entry Point (Hilt 가 관리하지 않는 클래스)

```kotlin
@EntryPoint
@InstallIn(SingletonComponent::class)
interface AnalyticsEntryPoint {
    fun analytics(): Analytics
}

class CustomContentProvider : ContentProvider() {
    
    private val analytics: Analytics by lazy {
        val appContext = context?.applicationContext ?: throw IllegalStateException()
        val hiltEntryPoint = EntryPointAccessors.fromApplication(
            appContext,
            AnalyticsEntryPoint::class.java
        )
        hiltEntryPoint.analytics()
    }
    
    override fun onCreate(): Boolean {
        analytics.logEvent("ContentProvider_Created")
        return true
    }
}
```
