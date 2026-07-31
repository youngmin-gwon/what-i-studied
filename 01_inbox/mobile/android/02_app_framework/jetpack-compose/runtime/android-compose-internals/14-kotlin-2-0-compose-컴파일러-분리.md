# Kotlin 2.0+ Compose 컴파일러 분리

상위 노트: [android-compose-internals](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals.md)

>[!WARNING] **Kotlin 2.0 마이그레이션 필수 변경**
>Kotlin 2.0 부터 Compose 컴파일러 플러그인이 Kotlin 에 **내장**되었다. 별도의 `compose-compiler` 의존성과 `kotlinCompilerExtensionVersion` 설정이 **삭제**되어야 한다.

```kotlin
// ❌ Kotlin 1.x (이전 방식)
android {
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.4"  // 삭제 대상
    }
}

// ✅ Kotlin 2.0+ (현대 방식)
plugins {
    alias(libs.plugins.kotlin.compose)  // Compose 컴파일러 플러그인
}
// composeOptions 블록 자체가 불필요
```

**마이그레이션 체크리스트:**

1. `build.gradle.kts` 에서 `composeOptions { kotlinCompilerExtensionVersion }` 제거
2. `plugins` 블록에 `kotlin-compose` 플러그인 추가
3. `libs.versions.toml` 에서 Compose Compiler 버전 참조 제거
