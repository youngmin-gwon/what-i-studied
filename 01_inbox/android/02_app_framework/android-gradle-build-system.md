---
title: android-gradle-build-system
tags: [android, android/build, android/gradle, android/agp]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android Gradle Build System android android/build android/gradle

Android Gradle Plugin (AGP) 과 빌드 시스템 최적화. 기본은 [android-os-development-guide](android-os-development-guide.md) 참고.

### Gradle 기본 구조

```
MyApp/
├── build.gradle.kts (프로젝트 레벨)
├── settings.gradle.kts
├── gradle.properties
├── app/
│   ├── build.gradle.kts (모듈 레벨)
│   ├── proguard-rules.pro
│   └── src/
└── library/
    └── build.gradle.kts
```

### 프로젝트 레벨 build.gradle.kts

```kotlin
// build.gradle.kts (프로젝트)
plugins {
    id("com.android.application") version "8.2.0" apply false
    id("com.android.library") version "8.2.0" apply false
    id("org.jetbrains.kotlin.android") version "1.9.20" apply false
    id("com.google.dagger.hilt.android") version "2.48" apply false
}

tasks.register("clean", Delete::class) {
    delete(rootProject.buildDir)
}
```

### 모듈 레벨 build.gradle.kts

```kotlin
// app/build.gradle.kts
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("kotlin-kapt")
    id("dagger.hilt.android.plugin")
}

android {
    namespace = "com.example.app"
    compileSdk = 34
    
    defaultConfig {
        applicationId = "com.example.app"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"
        
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        
        // Vector Drawable 지원
        vectorDrawables.useSupportLibrary = true
        
        // BuildConfig 필드 추가
        buildConfigField("String", "API_URL", "\"https://api.example.com\"")
        
        // Manifest placeholder
        manifestPlaceholders["appName"] = "@string/app_name"
    }
    
    buildTypes {
        debug {
            isDebuggable = true
            applicationIdSuffix = ".debug"
            versionNameSuffix = "-DEBUG"
            
            // 리소스 축소 비활성화 (빌드 속도)
            isMinifyEnabled = false
        }
        
        release {
            isDebuggable = false
            isMinifyEnabled = true
            isShrinkResources = true
            
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            
            // 서명 설정
            signingConfig = signingConfigs.getByName("release")
        }
    }
    
    // Product Flavors
    flavorDimensions += listOf("environment", "tier")
    
    productFlavors {
        create("dev") {
            dimension = "environment"
            applicationIdSuffix = ".dev"
            versionNameSuffix = "-dev"
            buildConfigField("String", "API_URL", "\"https://dev-api.example.com\"")
        }
        
        create("prod") {
            dimension = "environment"
            buildConfigField("String", "API_URL", "\"https://api.example.com\"")
        }
        
        create("free") {
            dimension = "tier"
            versionNameSuffix = "-free"
        }
        
        create("paid") {
            dimension = "tier"
            versionNameSuffix = "-paid"
        }
    }
    
    // 빌드 변형 필터링
    variantFilter {
        if (name.contains("devPaid")) {
            ignore = true
        }
    }
    
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
        
        // Java 8+ API desugaring
        isCoreLibraryDesugaringEnabled = true
    }
    
    kotlinOptions {
        jvmTarget = "17"
        
        // Compose 컴파일러 옵션
        freeCompilerArgs += listOf(
            "-opt-in=kotlin.RequiresOptIn",
            "-Xcontext-receivers"
        )
    }
    
    buildFeatures {
        compose = true
        viewBinding = true
        buildConfig = true
    }
    
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.4"
    }
    
    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }
    
    // 테스트 옵션
    testOptions {
        unitTests {
            isIncludeAndroidResources = true
            isReturnDefaultValues = true
        }
    }
}

dependencies {
    // AndroidX
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("androidx.activity:activity-compose:1.8.2")
    
    // Compose
    val composeBom = platform("androidx.compose:compose-bom:2023.10.01")
    implementation(composeBom)
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.ui:ui-tooling-preview")
    debugImplementation("androidx.compose.ui:ui-tooling")
    
    // Hilt
    implementation("com.google.dagger:hilt-android:2.48")
    kapt("com.google.dagger:hilt-compiler:2.48")
    
    // Testing
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.1.5")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
    androidTestImplementation(composeBom)
    
    // Desugaring
    coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.0.4")
}
```

### 서명 설정

```kotlin
// 보안을 위해 keystore.properties 파일 사용
val keystorePropertiesFile = rootProject.file("keystore.properties")
val keystoreProperties = Properties()
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}

android {
    signingConfigs {
        create("release") {
            storeFile = file(keystoreProperties["storeFile"] as String)
            storePassword = keystoreProperties["storePassword"] as String
            keyAlias = keystoreProperties["keyAlias"] as String
            keyPassword = keystoreProperties["keyPassword"] as String
        }
    }
}
```

```properties
# keystore.properties (gitignore 에 추가!)
storeFile=../release.keystore
storePassword=myStorePassword
keyAlias=myKeyAlias
keyPassword=myKeyPassword
```

### 의존성 관리

#### Version Catalog (권장)

```toml
# gradle/libs.versions.toml
[versions]
kotlin = "1.9.20"
compose = "1.5.4"
hilt = "2.48"

[libraries]
androidx-core = { module = "androidx.core:core-ktx", version = "1.12.0" }
androidx-lifecycle-viewmodel = { module = "androidx.lifecycle:lifecycle-viewmodel-ktx", version = "2.6.2" }
compose-ui = { module = "androidx.compose.ui:ui", version.ref = "compose" }
compose-material3 = { module = "androidx.compose.material3:material3", version = "1.1.2" }
hilt-android = { module = "com.google.dagger:hilt-android", version.ref = "hilt" }
hilt-compiler = { module = "com.google.dagger:hilt-compiler", version.ref = "hilt" }

[bundles]
compose = ["compose-ui", "compose-material3"]

[plugins]
android-application = { id = "com.android.application", version = "8.2.0" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
hilt = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
```

```kotlin
// build.gradle.kts 에서 사용
dependencies {
    implementation(libs.androidx.core)
    implementation(libs.bundles.compose)
    implementation(libs.hilt.android)
    kapt(libs.hilt.compiler)
}
```

#### buildSrc 패턴

```kotlin
// buildSrc/src/main/kotlin/Dependencies.kt
object Versions {
    const val kotlin = "1.9.20"
    const val compose = "1.5.4"
}

object Libs {
    const val androidxCore = "androidx.core:core-ktx:1.12.0"
    const val composeUi = "androidx.compose.ui:ui:${Versions.compose}"
}

// build.gradle.kts 에서 사용
dependencies {
    implementation(Libs.androidxCore)
    implementation(Libs.composeUi)
}
```

### 멀티 모듈 프로젝트

```
MyApp/
├── app/                    # 앱 모듈
├── feature/
│   ├── home/              # 기능 모듈
│   └── profile/
├── core/
│   ├── ui/                # 공통 UI
│   ├── data/              # 데이터 레이어
│   └── domain/            # 도메인 레이어
└── library/
    └── analytics/         # 라이브러리 모듈
```

```kotlin
// settings.gradle.kts
include(":app")
include(":feature:home")
include(":feature:profile")
include(":core:ui")
include(":core:data")
include(":core:domain")
include(":library:analytics")
```

```kotlin
// app/build.gradle.kts
dependencies {
    implementation(project(":feature:home"))
    implementation(project(":feature:profile"))
    implementation(project(":core:ui"))
}

// feature/home/build.gradle.kts
dependencies {
    implementation(project(":core:ui"))
    implementation(project(":core:domain"))
}
```

### 빌드 최적화

#### gradle.properties

```properties
# Gradle 데몬
org.gradle.daemon=true
org.gradle.jvmargs=-Xmx4g -XX:MaxMetaspaceSize=1g -XX:+HeapDumpOnOutOfMemoryError

# 병렬 빌드
org.gradle.parallel=true
org.gradle.workers.max=4

# 빌드 캐시
org.gradle.caching=true

# Configuration on demand
org.gradle.configureondemand=true

# Kotlin
kotlin.code.style=official
kotlin.incremental=true
kotlin.incremental.java=true

# AndroidX
android.useAndroidX=true
android.enableJetifier=false

# R8
android.enableR8.fullMode=true

# Non-transitive R classes
android.nonTransitiveRClass=true
android.nonFinalResIds=true
```

#### Build Cache

```kotlin
// settings.gradle.kts
buildCache {
    local {
        isEnabled = true
        directory = File(rootDir, "build-cache")
        removeUnusedEntriesAfterDays = 7
    }
}
```

#### Dependency Analysis Plugin

```kotlin
// build.gradle.kts (프로젝트)
plugins {
    id("com.autonomousapps.dependency-analysis") version "1.28.0"
}

dependencyAnalysis {
    issues {
        all {
            onAny {
                severity("fail")
            }
        }
    }
}
```

```bash
# 사용하지 않는 의존성 찾기
./gradlew buildHealth
```

### ProGuard/R8

```proguard
# proguard-rules.pro

# Keep 규칙
-keep class com.example.app.model.** { *; }
-keepclassmembers class * implements android.os.Parcelable {
    static ** CREATOR;
}

# Retrofit
-keepattributes Signature
-keepattributes *Annotation*
-keep class retrofit2.** { *; }

# Gson
-keepattributes Signature
-keep class com.google.gson.** { *; }
-keep class * implements com.google.gson.TypeAdapter
-keep class * implements com.google.gson.TypeAdapterFactory
-keep class * implements com.google.gson.JsonSerializer
-keep class * implements com.google.gson.JsonDeserializer

# Coroutines
-keepnames class kotlinx.coroutines.internal.MainDispatcherFactory {}
-keepnames class kotlinx.coroutines.CoroutineExceptionHandler {}

# 디버깅 정보 유지
-keepattributes SourceFile,LineNumberTable
-renamesourcefileattribute SourceFile
```

### 커스텀 Gradle Task

```kotlin
// app/build.gradle.kts
tasks.register("printVersionName") {
    doLast {
        println("Version: ${android.defaultConfig.versionName}")
    }
}

// APK 파일명 커스터마이징
android {
    applicationVariants.all {
        outputs.all {
            val output = this as com.android.build.gradle.internal.api.BaseVariantOutputImpl
            output.outputFileName = "MyApp-${versionName}-${buildType.name}.apk"
        }
    }
}

// 빌드 시간 측정
class BuildTimeListener : BuildListener, TaskExecutionListener {
    private var startTime: Long = 0
    
    override fun beforeExecute(task: Task) {
        startTime = System.currentTimeMillis()
    }
    
    override fun afterExecute(task: Task, state: TaskState) {
        val duration = System.currentTimeMillis() - startTime
        if (duration > 1000) {
            println("${task.name} took ${duration}ms")
        }
    }
}

gradle.addListener(BuildTimeListener())
```

### 빌드 변형 (Build Variants)

```kotlin
// 빌드 변형별 리소스
src/
├── main/
├── debug/
│   └── res/
│       └── values/
│           └── strings.xml (디버그 전용)
├── release/
└── dev/
    └── res/
        └── values/
            └── config.xml (dev flavor 전용)

// 빌드 변형별 코드
src/
├── main/kotlin/
├── debug/kotlin/
│   └── DebugUtils.kt
└── release/kotlin/
    └── ReleaseUtils.kt
```

### Gradle 명령어

```bash
# 빌드
./gradlew assembleDebug
./gradlew assembleRelease
./gradlew bundleRelease # AAB 생성

# 특정 변형 빌드
./gradlew assembleDevDebug
./gradlew assembleProdRelease

# 설치
./gradlew installDebug
./gradlew installRelease

# 테스트
./gradlew test
./gradlew connectedAndroidTest

# 린트
./gradlew lint
./gradlew lintDebug

# 의존성 확인
./gradlew dependencies
./gradlew app:dependencies --configuration releaseRuntimeClasspath

# 빌드 캐시 정리
./gradlew clean
./gradlew cleanBuildCache

# 빌드 스캔
./gradlew build --scan

# 프로파일링
./gradlew assembleDebug --profile
```

### 빌드 성능 분석

```bash
# Build Analyzer (Android Studio)
# Build → Analyze Build Performance

# Gradle Profiler
gradle-profiler --benchmark --project-dir . assembleDebug

# Build Scan
./gradlew build --scan
# https://scans.gradle.com 에서 결과 확인
```

### 더 보기

[android-os-development-guide](android-os-development-guide.md), [android-jetpack-architecture](android-jetpack-architecture.md), [android-dependency-injection](android-dependency-injection.md), [android-testing-and-quality](../06_testing_performance/android-testing-and-quality.md)
