---
title: android-gradle-dsl-reference
tags: [android, gradle, kts, dsl]
aliases: [Gradle Kotlin DSL 가이드]
date modified: 2026-04-07 10:50:00 +09:00
date created: 2026-04-05 09:20:00 +09:00
---

## [[android-gradle-build-system]] > [[android-gradle-dsl-reference]]

### Gradle Kotlin DSL: Type-Safe Build Configuration

프로젝트 수준과 모듈 수준의 `build.gradle.kts` 설정 파일에서 자주 쓰이는 상세 문법과 구조를 정리합니다.

---

#### 🧩 1. Project-level DSL (Global Settings)

```kotlin
// root build.gradle.kts
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.kotlin.android) apply false
}
```

---

#### 📦 2. Module-level DSL (App/Library)

```kotlin
// app/build.gradle.kts
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.example.app"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.example.app"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "1.0.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }

    kotlinOptions {
        jvmTarget = "21"
    }
}
```

---

#### 💡 3. Version Catalog (libs.versions.toml)

최근에는 하드코딩 대신 `libs` 접근자를 사용하는 것이 표준입니다.

```toml
[versions]
agp = "8.7.0"
kotlin = "2.0.21"

[libraries]
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "core-ktx" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
```

---

#### 📚 See Also
- [[android-gradle-build-system]] - 전체 빌드 시스템 개요
- [[gradle-performance-tuning]] - 성능 최적화 설정
- [[gradle-variants-flavors]] - 멀티 환경(Flavors) 구성
