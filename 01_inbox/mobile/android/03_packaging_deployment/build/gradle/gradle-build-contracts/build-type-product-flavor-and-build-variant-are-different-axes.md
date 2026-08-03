---
title: build-type-product-flavor-and-build-variant-are-different-axes
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:33 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## Build type, product flavor, build variant 는 서로 다른 축이다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md)

관련 노트: [Source set 우선순위는 variant별 코드와 리소스 충돌을 결정한다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/source-set-priority-decides-variant-code-and-resource-conflicts.md), [AGP DSL 체크리스트는 릴리스 변형의 실제 값을 확인한다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/agp-dsl-checklist-verifies-effective-release-variant-values.md)

### 세 개념의 관계

Build type 은 개발 생명주기 단계와 패키징 규칙을 나타낸다.

Product flavor 는 제품, 시장, 환경처럼 기능과 콘텐츠가 다른 축을 나타낸다.

Build variant 는 각 flavor dimension 의 선택과 build type 을 조합한 실제 빌드 단위다.

### Build type

새 Android 모듈에는 보통 `debug` 와 `release` 가 기본 제공된다.

debug 는 디버깅과 기본 debug keystore 사용을, release 는 배포 설정과 release 서명을 중심으로 구성한다.

`staging` 처럼 별도 단계가 필요하면 기존 build type 을 초기값으로 복사해 차이를 명시한다.

```kotlin
android {
    buildTypes {
        debug {
            applicationIdSuffix = ".debug"
        }
        create("staging") {
            initWith(getByName("debug"))
            applicationIdSuffix = ".staging"
        }
        release {
            isDebuggable = false
        }
    }
}
```

### Product flavor

flavor 는 `productFlavors` 블록에 선언하고 하나의 flavor dimension 에 소속시킨다.

예를 들어 `dev` 와 `prod` 는 environment 차이를, `free` 와 `paid` 는 제품 등급 차이를 나타낸다.

여러 dimension 을 사용하면 각 dimension 에서 하나씩 선택되므로 조합 수가 곱셈으로 증가한다.

```kotlin
flavorDimensions += listOf("environment")
productFlavors {
    create("dev") { dimension = "environment" }
    create("prod") { dimension = "environment" }
}
```

### Variant 이름과 선택

두 flavor 와 두 build type 이면 `devDebug`, `devRelease`, `prodDebug`, `prodRelease` 가 생긴다.

variant 는 직접 선언하는 객체라기보다 type 과 flavor 의 규칙을 조합해 AGP 가 만든 결과다.

IDE 의 Build Variants 창이나 Gradle 태스크로 선택한 variant 를 빌드한다.

### 설계 기준

- 기능 차이는 flavor, 최적화·서명 차이는 build type 에 둔다.
- 조합이 폭발하면 dimension 수와 배포 목적을 다시 검토한다.
- 각 variant 가 실제로 필요한지 CI 와 배포 매트릭스로 확인한다.

### 참고

공식 변형 안내: https://developer.android.com/build/build-variants

빌드 구성 개요: https://developer.android.com/build
