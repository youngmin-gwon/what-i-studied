---
title: gradle-variants-flavors
tags: [android, gradle, build-variants]
aliases: [Build Types, Product Flavors, 빌드 변형]
---

# [[mobile-security]] > [[gradle-variants-flavors]]

## Build Variants: Types & Flavors

안드로이드는 하나의 소스 코드에서 서로 다른 특징(개발용, 운영용, 유료/무료 등)을 가진 여러 가지 APK/AAB를 생성할 수 있는 강력한 빌드 변형 시스템을 제공합니다.

### 1. Build Types (빌드 타입)

빌드 타입은 주로 앱의 **패키징 방식**과 보안 설정을 결정합니다.

```kotlin
buildTypes {
    debug {
        isDebuggable = true
        applicationIdSuffix = ".debug"
        isMinifyEnabled = false // 빌드 속도를 위해 코드 축소 비활성화
    }
    
    release {
        isMinifyEnabled = true  // R8 코드 축소 및 난독화 활성화
        isShrinkResources = true // 미사용 리소스 제거
        proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        signingConfig = signingConfigs.getByName("release")
    }
}
```

### 2. Product Flavors (제품 버전)

플래버는 앱의 **기능적 차이**나 환경(API 주소 등)을 구분합니다. `dimension`을 통해 여러 조합(Dimension)을 구성할 수 있습니다.

```kotlin
flavorDimensions += listOf("environment", "tier")

productFlavors {
    create("dev") {
        dimension = "environment"
        buildConfigField("String", "API_URL", "\"https://dev-api.example.com\"")
    }
    create("prod") {
        dimension = "environment"
        buildConfigField("String", "API_URL", "\"https://api.example.com\"")
    }
    create("free") {
        dimension = "tier"
    }
}
```

### 3. Build Variant Generation

결과물은 `[Flavor][Type]` 조합으로 생성됩니다:
- `devFreeDebug`, `devFreeRelease`, `prodFreeDebug`, `prodFreeRelease` ...

---
### 연관 문서
- [[gradle-optimization-signing]] - 서명 및 성능 최적화
- [[gradle-build-basics]] - 빌드 기초
