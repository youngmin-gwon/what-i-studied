# WindowSizeClass

상위 노트: [android-large-screens](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens.md)

화면 크기에 따라 레이아웃 조정.

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.compose.material3:material3-window-size-class:1.1.2")
}

@Composable
fun AdaptiveLayout() {
    val windowSizeClass = calculateWindowSizeClass(this)
    
    when (windowSizeClass.widthSizeClass) {
        WindowWidthSizeClass.Compact -> {
            // 스마트폰: 단일 패널
            SinglePaneLayout()
        }
        WindowWidthSizeClass.Medium -> {
            // 작은 태블릿: 리스트-디테일
            ListDetailLayout()
        }
        WindowWidthSizeClass.Expanded -> {
            // 큰 태블릿: 3패널
            ThreePaneLayout()
        }
    }
}
```
