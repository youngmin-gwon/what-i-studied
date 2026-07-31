# Version Catalog는 의존성 좌표와 플러그인 좌표의 이름표다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)
관련 정본: [Gradle 프로젝트와 모듈 DSL은 서로 다른 책임을 가진다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-project-and-module-dsl-have-different-responsibilities.md)

## 역할

Version Catalog는 여러 모듈에서 반복되는 의존성 좌표, 플러그인 좌표, 버전 이름을 한 곳에서 관리하는 Gradle 기능이다.
기본 파일은 `gradle/libs.versions.toml`이며 Gradle이 자동으로 읽어 `libs` 접근자를 제공한다.

```toml
[versions]
agp = "버전"
kotlin = "버전"
core = "버전"

[libraries]
androidx-core-ktx = { module = "androidx.core:core-ktx", version.ref = "core" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }

[bundles]
test = ["junit", "truth"]
```

## 네 영역

- `[versions]`는 여러 항목이 참조할 버전 값을 이름으로 둔다.
- `[libraries]`는 라이브러리의 group, name 또는 module 좌표를 정의한다.
- `[plugins]`는 Gradle plugin id와 버전을 정의한다.
- `[bundles]`는 함께 선언할 라이브러리 별칭을 묶는다.

Kotlin DSL에서는 `libs.androidx.core.ktx`, `libs.plugins.android.application`처럼 사용한다.
별칭의 하이픈과 일부 구분자는 타입 안전 접근자로 변환되므로 이름을 짧고 예측 가능하게 짓는다.
IDE 자동 완성은 편의 기능이며, Catalog가 최종 버전 선택을 강제한다는 뜻은 아니다.

## 라이브러리와 플러그인 구분

`[libraries]` 항목은 `implementation`, `api`, `ksp`, `kapt`, 테스트 configuration 등에 전달할 좌표다.
`[plugins]` 항목은 `plugins { alias(...) }`에서 빌드 로직을 적용하는 id다.
플러그인은 앱 런타임 라이브러리로 넣는 것이 아니며, 필요한 라이브러리 의존성은 별도로 선언한다.

```kotlin
plugins {
    alias(libs.plugins.android.application)
}

dependencies {
    implementation(libs.androidx.core.ktx)
}
```

## 운영 규칙

- 버전 키는 제품 영역보다 기술 이름 중심으로 일관되게 짓는다.
- Catalog에는 좌표와 버전처럼 정적인 정보만 두고 조건문은 빌드 스크립트에 둔다.
- 번들은 실제로 함께 쓰이는 항목에만 사용한다.
- 업그레이드 PR에서는 변경된 해석 그래프와 테스트 결과를 함께 검토한다.

## 공식 문서

- [Gradle Version Catalog](https://docs.gradle.org/current/userguide/version_catalogs.html)
- [Gradle 의존성 기본](https://docs.gradle.org/current/userguide/dependency_management_basics.html)
