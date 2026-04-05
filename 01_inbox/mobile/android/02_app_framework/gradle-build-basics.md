---
title: gradle-build-basics
tags: [android, build, gradle]
aliases: [Gradle Plugins, plugins block, 안드로이드 빌드 기초]
date modified: 2026-04-05 17:43:22 +09:00
date created: 2026-04-05 16:29:59 +09:00
---

## [[mobile-security]] > [[gradle-build-basics]]

### Gradle Build Basics & Plugins

안드로이드 빌드 시스템의 핵심인 Gradle 의 기본 구조와 플러그인 설정 방식을 다룹니다.

#### 프로젝트 구조

```text
MyApp/
├── build.gradle.kts (프로젝트 레벨)
├── settings.gradle.kts (모듈 포함 설정)
├── gradle.properties (JVM 및 빌드 옵션)
├── gradle/libs.versions.toml (Version Catalog)
└── app/
    └── build.gradle.kts (모듈 레벨 스크립트)
```

#### Plugins 블록 (기능 활성화)

`plugins` 블록은 빌드 과정에 특수 기능(코드 생성, DSL 확장 등)을 추가하는 선언적 상단부입니다.

##### 1. alias 방식 (권장 ✅)

`libs.versions.toml` 에 정의된 플러그인을 참조하여 버전을 중앙에서 관리합니다.

```kotlin
// build.gradle.kts
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.hilt)
}
```

##### 2. id 방식 (직접 선언)

플러그인을 직접 명시합니다. 버전이 없는 내장 플러그인이나 일회성 테스트에 사용합니다.

```kotlin
plugins {
    id("kotlin-kapt") 
    id("com.google.devtools.ksp") version "2.0.0-1.0.21"
}
```

#### 주요 플러그인 역할

| 플러그인 | 역할 |
| :--- | :--- |
| **android-application** | APK 빌드 기능 및 `android { … }` DSL 활성화 |
| **kotlin-android** | Kotlin 코드 컴파일러 활성화 |
| **kotlin-compose** | `@Composable` 함수 인식 및 최적화 |
| **hilt** | `@HiltAndroidApp` 등 의존성 주입 코드 자동 생성 |

---
#### 연관 문서
- [[gradle-dependency-management]] - Version Catalog 및 의존성 관리
- [[gradle-variants-flavors.md]] - 빌드 변형 설정
- [[android-gradle-build-system]] - Gradle MOC
