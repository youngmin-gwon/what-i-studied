---
title: "Gradle 프로젝트와 모듈 DSL은 서로 다른 책임을 가진다"
tags: ["android", "android/packaging-deployment"]
---

# Gradle 프로젝트와 모듈 DSL은 서로 다른 책임을 가진다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md)
관련 노트: [Android Gradle Plugin은 Android 빌드 규칙을 Gradle에 추가한다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/android-gradle-plugin-adds-android-build-rules-to-gradle.md), [Version Catalog는 의존성 좌표와 플러그인 좌표의 이름표다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/version-catalog-names-dependency-and-plugin-coordinates.md)

## 파일별 책임

프로젝트 수준은 빌드 전체를 조정하고, 모듈 수준은 실제 Android 산출물을 구성한다.
두 수준의 설정을 섞으면 플러그인 적용 순서와 변형별 값의 소유자가 불명확해진다.

## `settings.gradle.kts`

`pluginManagement`와 `dependencyResolutionManagement`에서 저장소 정책을 정할 수 있다.
`include(":app")`처럼 빌드에 참여할 모듈을 선언하며, 모듈의 `build.gradle.kts`를 직접 구성하지는 않는다.

## 루트 `build.gradle.kts`

루트에서는 플러그인을 버전과 함께 선언하고 `apply false`로 모듈이 선택해 적용하도록 만들 수 있다.

```kotlin
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.kotlin.android) apply false
}
```

`apply false`는 해당 플러그인의 DSL을 루트에 적용한다는 뜻이 아니라, 플러그인 해석을 준비한다는 뜻이다.
실제 Android 앱 모듈은 자신의 `plugins` 블록에서 플러그인을 적용해야 한다.

## 모듈 `build.gradle.kts`

```kotlin
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.example.app"
    compileSdk = <현재 프로젝트 기준>
    defaultConfig {
        applicationId = "com.example.app"
        minSdk = 26
        targetSdk = <현재 프로젝트 기준>
    }
}
```

앱 플러그인은 APK/AAB와 앱 전용 DSL을, 라이브러리 플러그인은 AAR과 라이브러리 전용 DSL을 제공한다.
`namespace`는 생성되는 `R`과 `BuildConfig` 등의 코드 네임스페이스이고, `applicationId`는 앱 식별자다.

## 타입 안전 Kotlin DSL

`build.gradle.kts`에서는 문자열 중심 Groovy 문법보다 IDE 자동 완성과 타입 검사를 활용할 수 있다.
중첩 블록은 각각 다른 AGP 모델을 구성하므로 이름이 비슷한 속성의 의미를 구분해서 읽는다.
플러그인 버전과 API 호환성은 사용하는 Android Studio와 AGP 조합을 기준으로 확인한다.

## 버전 카탈로그

`libs.versions.toml`은 별칭을 통해 의존성과 플러그인 버전을 중앙 관리한다.
별칭은 일관성을 높이지만 AGP, Kotlin, Gradle의 호환성을 자동으로 보장하지는 않는다.

## 참고

Gradle 빌드 구조: https://developer.android.com/build/gradle-build-overview
빌드 의존성 설정: https://developer.android.com/build/dependencies
