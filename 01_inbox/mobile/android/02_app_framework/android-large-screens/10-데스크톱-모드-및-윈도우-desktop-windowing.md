# 데스크톱 모드 및 윈도우 (Desktop Windowing)

상위 노트: [[android-large-screens]]

##### 1. Android 15 Desktop Windowing (New ✅)

Android 15 부터 태블릿에서 여러 앱을 자유로운 크기의 창(Freeform Windows)으로 실행할 수 있는 **데스크톱 윈도우** 기능이 공식 지원됩니다.

- **고정된 가로세로비 설정**: 앱이 자유로운 창 크기 조정을 지원하지 않더라도, `android:screenOrientation` 이나 `android:minAspectRatio` 를 통해 안정적인 비율을 유지할 수 있습니다.
- **Taskbar 활용**: 대화면 하단의 태스크바를 통해 앱 간 드래그 앤 드롭 및 퀵 런칭이 더욱 고도화되었습니다.

##### 2. Samsung DeX & Chrome OS

```kotlin
// 데스크톱 모드 감지
fun isDesktopMode(context: Context): Boolean {
    val uiModeManager = context.getSystemService(Context.UI_MODE_SERVICE) as UiModeManager
    return uiModeManager.currentModeType == Configuration.UI_MODE_TYPE_DESK
}

// 설정 변경 감지
override fun onConfigurationChanged(newConfig: Configuration) {
    super.onConfigurationChanged(newConfig)
    
    if (newConfig.uiMode and Configuration.UI_MODE_TYPE_MASK == Configuration.UI_MODE_TYPE_DESK) {
        // 데스크톱 모드로 전환
        enableDesktopLayout()
    } else {
        // 모바일 모드로 전환
        enableMobileLayout()
    }
}
```
