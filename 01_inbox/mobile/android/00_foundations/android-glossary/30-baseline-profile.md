# Baseline Profile

상위 노트: [[android-glossary]]

**정의**: 앱에서 자주 사용되는 코드 경로를 기록한 파일

**상세**:

설치 시 이 프로파일을 기반으로 AOT 컴파일하여 첫 실행부터 빠른 성능을 제공한다. Jetpack Compose 앱에서 특히 효과적이다.

**생성**:

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.profileinstaller:profileinstaller:1.3.0")
}

// 벤치마크로 프로파일 생성
./gradlew :app:generateBaselineProfile
```

**관련**: [android-zygote-and-runtime](../01_system_internals/android-zygote-and-runtime.md)

---
