---
title: gradle-optimization-signing
tags: [android, gradle, optimization, signing]
aliases: [Build Performance, Keystore, Proguard, R8]
date modified: 2026-04-05 17:43:25 +09:00
date created: 2026-04-05 16:30:06 +09:00
---

## [[mobile-security]] > [[gradle-optimization-signing]]

### Optimization & Signing

안드로이드 앱의 릴리스를 위한 서명 설정과 배포 사이즈 축소(R8), 빌드 속도 최적화 기법을 다룹니다.

#### 1. 보안 서명 설정 (Signing)

Keystore 비밀번호 유출을 방지하기 위해 `keystore.properties` 파일을 분리하여 관리합니다.

```kotlin
// build.gradle.kts
val keystoreProperties = Properties()
keystoreProperties.load(FileInputStream(rootProject.file("keystore.properties")))

android {
    signingConfigs {
        create("release") {
            storeFile = file(keystoreProperties["storeFile"] as String)
            storePassword = keystoreProperties["storePassword"] as String
            // ...
        }
    }
}
```

#### 2. 코드 및 리소스 최적화 (R8/Proguard)

릴리스 빌드에서는 반드시 **R8**을 통해 미사용 코드를 제거하고 난독화를 수행해야 합니다.

- `isMinifyEnabled = true`: 바이트코드 최적화 및 난독화.
- `isShrinkResources = true`: 미사용 이미지/XML 리소스 자동 제거.

#### 3. 빌드 속도 최적화 (Build Performance)

대규모 프로젝트에서 빌드 시간을 단축하는 핵심 옵션들입니다.

- **Configuration Caching**: 구성(Setup) 단계를 재사용하여 빌드 시작 속도 개선.
- **Incremental Build**: 변경된 부분만 다시 빌드.
- **Build Scan**: `--scan` 옵션으로 어떤 태스크가 병목인지 분석.

#### 연관 문서

- [[gradle-variants-flavors]] - 빌드 타입 기반 설정
- [[mobile-android-foundation-security]] - 서비스 관점 보안
