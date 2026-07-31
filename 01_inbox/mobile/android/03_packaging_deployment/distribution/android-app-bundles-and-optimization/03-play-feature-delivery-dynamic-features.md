# Play Feature Delivery (Dynamic Features)

앱의 특정 기능을 설치 시점이 아닌, 필요할 때(On-demand) 다운로드하도록 구성할 수 있다.

##### 구조 및 호출

```kotlin
// build.gradle.kts (feature module)
plugins {
    id("com.android.dynamic-feature")
}

// 코드에서 동적 모듈 다운로드
val splitInstallManager = SplitInstallManagerFactory.create(context)
val request = SplitInstallRequest.newBuilder()
    .addModule("premium_camera_filter")
    .build()

splitInstallManager.startInstall(request)
    .addOnSuccessListener { /* 모듈 로드 완료 */ }
```
