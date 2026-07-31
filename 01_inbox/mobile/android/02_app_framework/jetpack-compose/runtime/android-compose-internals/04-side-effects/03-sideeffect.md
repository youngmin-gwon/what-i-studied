# SideEffect

Compose 상태를 non-Compose 코드에 전달.

```kotlin
@Composable
fun AnalyticsExample(screenName: String) {
    SideEffect {
        // 재구성마다 실행 (상태 변경 후)
        analytics.logScreenView(screenName)
    }
}
```
