---
title: compose-bom-manages-compose-library-version-set
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:20 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## Compose BOM 은 Compose 라이브러리 버전 집합을 관리한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)

관련 노트: [Compose compiler는 BOM이 아니라 Kotlin compiler 흐름에 속한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/compose-compiler-belongs-to-kotlin-compiler-flow-not-bom.md), [Version Catalog는 의존성 좌표와 플러그인 좌표의 이름표다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/version-catalog-names-dependency-and-plugin-coordinates.md)

### 무엇을 관리하는가

Compose BOM 은 여러 Compose 라이브러리에 대응하는 버전 집합을 하나의 플랫폼 버전으로 선택하게 하는 도구다.

BOM 이 앱에 Compose 라이브러리를 자동으로 추가하는 것은 아니다.

사용할 모듈은 각각 dependency 로 선언해야 한다.

```kotlin
dependencies {
    val composeBom = platform(libs.androidx.compose.bom)
    implementation(composeBom)
    androidTestImplementation(composeBom)

    implementation(libs.androidx.compose.foundation)
    implementation(libs.androidx.compose.material3)
}
```

### Version Catalog 연결

```toml
[versions]
androidxComposeBom = "공식 BOM 버전"

[libraries]
androidx-compose-bom = { module = "androidx.compose:compose-bom", version.ref = "androidxComposeBom" }
androidx-compose-foundation = { module = "androidx.compose.foundation:foundation" }
androidx-compose-material3 = { module = "androidx.compose.material3:material3" }
```

Catalog 에는 BOM 자체의 버전만 두고, BOM 이 관리하는 Compose 모듈은 보통 개별 버전을 생략한다.

테스트 configuration 에서 Compose 모듈을 사용한다면 해당 configuration 에도 BOM 을 전달한다.

### 해석과 예외

BOM 은 관련 라이브러리가 함께 잘 동작하도록 테스트된 버전 조합을 제공하지만 절대적인 호환성 보증은 아니다.

새 BOM 이 모든 모듈을 동시에 같은 숫자로 올린다는 뜻도 아니다.

특정 모듈을 예외적으로 올려야 하면 BOM 은 유지하고 해당 dependency 에 버전을 명시한다.

```kotlin
dependencies {
    implementation(platform(libs.androidx.compose.bom))
    implementation("androidx.compose.animation:animation:검토한 버전")
}
```

이 방식은 BOM 과 다른 버전을 의도적으로 선택하므로 전이 의존성 변화와 테스트 범위를 기록한다.

알파·베타 BOM 은 실험 목적이며 운영 사용 여부를 별도로 판단한다.

### Compiler 와의 경계

Compose compiler 는 Compose 라이브러리 BOM 의 구성원이 아니다.

Kotlin 2.0 이상에서는 공식 Compose Compiler Gradle plugin 을 Kotlin compiler 와 함께 관리하는 흐름을 사용한다.

Kotlin 2.0 미만 또는 이전 구성에서는 해당 Kotlin 버전에 맞는 공식 호환성 안내를 확인한다.

### 확인 방법

특정 BOM 의 실제 매핑은 [Compose BOM to library version mapping](https://developer.android.com/develop/ui/compose/bom/bom-mapping) 에서 확인한다.

일반 사용법은 [Compose BOM 공식 안내](https://developer.android.com/develop/ui/compose/bom) 를 기준으로 한다.
