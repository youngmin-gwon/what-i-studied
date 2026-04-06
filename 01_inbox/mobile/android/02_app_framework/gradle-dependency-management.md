---
title: gradle-dependency-management
tags: [android, dependency, gradle]
aliases: [Compose BOM, kapt vs ksp, toml, Version Catalog]
date modified: 2026-04-05 17:43:23 +09:00
date created: 2026-04-05 16:30:04 +09:00
---

## [[mobile-security]] > [[gradle-dependency-management]]

### Dependency Management: Modern Patterns

안드로이드의 의존성 관리는 휴먼 에러를 방지하고 속도를 향상시키기 위해 **Version Catalog**와 **BOM** 방식으로 진화했습니다.

#### 1. Version Catalog (`toml`) 권장 ✅

`libs.versions.toml` 파일을 통해 버전을 한 곳에서 관리하는 방식입니다. `buildSrc` 대비 빌드 캐싱 성능이 뛰어납니다.

```toml
# gradle/libs.versions.toml
[versions]
compose = "1.6.0"
hilt = "2.50"

[libraries]
compose-ui = { module = "androidx.compose.ui:ui", version.ref = "compose" }
hilt-android = { module = "com.google.dagger:hilt-android", version.ref = "hilt" }

[bundles]
compose = ["compose-ui", "compose-material3"]
```

#### 2. Compose BOM (Bill of Materials)

BOM 은 구글에서 테스트가 완료된 호환되는 라이브러리 세트를 제공합니다. 개별 버전을 일일이 명시할 필요가 없습니다.

```kotlin
dependencies {
    val composeBom = platform(libs.compose.bom)
    implementation(composeBom)
    
    implementation(libs.compose.ui) // 버전 생략 가능
}
```

#### 3. Kapt vs KSP

어노테이션 프로세싱(코드 생성) 도구의 차이입니다.

- **Kapt**: Java 기반으로 동작하며 빌드 속도가 상대적으로 느림 (Legacy).
- **KSP (Kotlin Symbol Processing)**: Kotlin 네이티브 지원으로 **최대 2 배 이상 빠름**. 최신 라이브러리(Room, Hilt 등)는 KSP 사용이 필수적입니다.

#### 연관 문서

- [[gradle-build-basics]] - 빌드 기초
- [[android-jetpack-architecture]] - 라이브러리 활용 아키텍처
