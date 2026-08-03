---
title: gradle-dependency-management-controls-resolution-graph-not-requested-versions
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:25 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## Gradle 의존성 관리는 요청 버전이 아니라 해석 그래프를 관리한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)

관련 노트: [Version Catalog는 의존성 좌표와 플러그인 좌표의 이름표다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/version-catalog-names-dependency-and-plugin-coordinates.md), [의존성 변경 체크리스트는 그래프, ABI, 테스트, 배포 위험을 함께 본다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-change-checklist-reviews-graph-abi-tests-and-release-risk.md)

### 목적

Gradle 의존성 관리는 앱 코드가 필요로 하는 모듈을 선언하고, 의존성 그래프를 해석하고, 실제 아티팩트를 내려받는 과정이다.

의존성 선언은 `build.gradle.kts` 의 `dependencies` 블록에 둔다.

어떤 configuration 에 넣느냐가 컴파일·런타임·테스트에서의 노출 범위를 결정한다.

```kotlin
dependencies {
    implementation(libs.androidx.core.ktx)
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
}
```

### 해석 순서

1. 프로젝트와 외부 저장소에서 요청된 모듈을 수집한다.
2. 모듈의 전이 의존성을 따라 그래프를 만든다.
3. 버전 충돌과 플랫폼·제약 조건을 반영해 선택 버전을 결정한다.
4. 선택된 variant 와 아티팩트를 내려받아 configuration 에 제공한다.

Version Catalog 에 적힌 버전은 요청값과 별칭을 중앙화할 뿐, 최종 해석 버전을 무조건 고정하지 않는다.

플랫폼이나 다른 전이 의존성이 더 높은 버전을 요청하면 해석 결과가 달라질 수 있다.

### 중앙화 원칙

- 저장소 선언과 콘텐츠 필터는 `settings.gradle.kts` 에서 일관되게 관리한다.
- 반복되는 좌표와 버전은 `gradle/libs.versions.toml` 에 모은다.
- 함께 사용하도록 설계된 모듈 집합은 플랫폼 또는 BOM 으로 관리한다.
- 재현성이 필요하면 의존성 잠금과 의존성 그래프 검사를 별도로 검토한다.
- 무분별한 동적 버전보다 검토 가능한 고정 버전을 우선한다.

Version Catalog 와 플랫폼은 역할이 다르다.

Catalog 는 선언 이름과 요청 버전을 정리하고, 플랫폼은 관련 모듈의 버전 제약을 그래프 해석에 제공한다.

둘은 함께 사용할 수 있지만 어느 하나가 다른 하나를 대체하지 않는다.

### 점검 명령

```bash
./gradlew :app:dependencies
./gradlew :app:dependencyInsight --dependency compose
```

첫 명령은 configuration 별 그래프를 보고, 두 번째 명령은 특정 모듈이 선택된 이유를 좁혀 본다.

업그레이드 후에는 실제 해석 결과와 테스트를 함께 확인한다.

### 공식 문서

- [Gradle 의존성 관리 개요](https://docs.gradle.org/current/userguide/dependency_management_basics.html)
- [Gradle 의존성 관리 상세](https://docs.gradle.org/current/userguide/core_dependency_management.html)
- [Gradle 의존성 모범 사례](https://docs.gradle.org/current/userguide/best_practices_dependencies.html)
