# 모듈별 빌드 파일 (`build.gradle.kts`) 설정

상위 노트: [baseline-profile-and-macrobenchmark](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark.md)

기존 프로젝트의 멀티 모듈 의존성 구조를 존중하여 독립된 테스트 모듈 `:baselineprofile`을 등록하고 `:app` 모듈과 연결합니다.

### 3-1. 프로젝트 루트 `settings.gradle.kts`
새로운 빌드 타겟으로 `:baselineprofile`을 선언합니다.
```kotlin
include(":baselineprofile")
```

### 3-2. 독립형 `:baselineprofile/build.gradle.kts`
`com.android.test` 플러그인을 사용하여 최적화를 캡처할 독립형 테스트 타겟으로 설정합니다.

```kotlin
plugins {
    alias(libs.plugins.android.test)              // com.android.test
    alias(libs.plugins.androidx.baselineprofile)      // androidx.baselineprofile
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.benefit.virtualmate.baselineprofile"
    compileSdk = 35

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }
    kotlinOptions {
        jvmTarget = "21"
    }

    defaultConfig {
        minSdk = 28 // Macrobenchmark 측정은 API 28 이상 권장
        targetSdk = 37
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    targetProjectPath = ":app" // 최적화 대상 애플리케이션 모듈 바인딩
}

dependencies {
    // libs.versions.toml에 등록한 테스트 전용 번들 주입
    implementation(libs.bundles.baselineprofile.generator)
    implementation(libs.androidx.espresso.core) // 간혹 필요한 에스프레소 기본 의존성
}
```

### 3-3. 애플리케이션 `:app/build.gradle.kts`
생성된 프로필 파일이 릴리즈에 자동 번들링되도록 플러그인을 연동하고, 앱 전용 인프라 구성 패키지(`app-infrastructure` 번들)를 주입합니다.

```kotlin
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.androidx.baselineprofile) // 1) 플러그인 추가
    // ...
}

dependencies {
    // 2) baselineProfile 구성을 사용해 생성기 모듈과 바인딩
    baselineProfile(project(":baselineprofile"))

    // 3) 앱 전용 기본 인프라/최적화 구성 번들 추가 (ProfileInstaller 및 SplashScreen 포함)
    implementation(libs.bundles.app.infrastructure)
}
```

---
