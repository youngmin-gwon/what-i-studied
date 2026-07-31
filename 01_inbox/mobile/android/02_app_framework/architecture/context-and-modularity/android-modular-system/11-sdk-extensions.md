# SDK Extensions

상위 노트: [android-modular-system](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system.md)

Android 11+ 에서 SDK 를 모듈식으로 업데이트.

```kotlin
// SDK Extension 레벨 확인
val extensionVersion = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
    SdkExtensions.getExtensionVersion(Build.VERSION_CODES.R)
} else {
    0
}

// 특정 기능 사용 가능 여부
if (extensionVersion >= 5) {
    // Android 11 Extension 5 기능 사용
    useNewFeature()
}
```

```kotlin
// build.gradle.kts
android {
    compileSdkExtension = 5
}
```
