---
title: "의존성 변경 체크리스트는 그래프, ABI, 테스트, 배포 위험을 함께 본다"
tags: ["android", "android/packaging-deployment"]
---

# 의존성 변경 체크리스트는 그래프, ABI, 테스트, 배포 위험을 함께 본다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)
관련 노트: [Android CI/CD 게이트는 빠른 검증과 릴리스 검증을 분리한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/android-cicd-gates-separate-fast-validation-and-release-validation.md), [Gradle 의존성 관리는 요청 버전이 아니라 해석 그래프를 관리한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/gradle-dependency-management-controls-resolution-graph-not-requested-versions.md)

## 변경 전

- 변경 대상이 라이브러리, 플랫폼, plugin, compiler tool 중 무엇인지 분류한다.
- 현재 Kotlin, AGP, Gradle, Compose BOM의 조합과 해석 그래프를 기록한다.
- 해당 변경을 지원하는 공식 문서의 호환성 조건을 확인한다.
- PR에서 실행할 빠른 게이트와 릴리스에서 실행할 전체 게이트를 구분한다.

## Version Catalog

- `gradle/libs.versions.toml`에 좌표와 버전이 중복되지 않는가.
- `[libraries]`와 `[plugins]`를 올바른 configuration에서 사용하는가.
- Catalog의 요청 버전과 실제 Gradle 해석 버전을 혼동하지 않는가.
- 번들이 실제 공동 변경 단위를 표현하는가.

## Compose

- Compose BOM을 `platform(...)`으로 필요한 configuration에 전달했는가.
- Compose 라이브러리 dependency에는 불필요한 개별 버전을 넣지 않았는가.
- BOM이 라이브러리를 자동 추가하지 않는다는 점을 반영했는가.
- 예외 버전 override가 있다면 이유와 테스트를 남겼는가.
- compiler는 BOM이 아니라 Kotlin과 공식 plugin 흐름으로 검증했는가.

## 코드 생성과 직렬화

- processor가 KAPT와 KSP 중 어느 방식을 공식 지원하는가.
- KSP 전환을 성능 수치가 아니라 실제 CI 측정으로 판단했는가.
- Serialization plugin과 format 런타임 dependency를 모두 선언했는가.
- 직렬화 모델의 스키마 변경과 외부 입력 검증을 테스트했는가.

## CI/CD

- 검사, 테스트, 컴파일, 산출물, 배포 게이트가 분리되어 있는가.
- 서명과 배포 secret이 로그와 PR job에서 보호되는가.
- release artifact가 검증된 입력에서 만들어지고 추적 가능한가.
- 실패한 테스트와 flaky 재시도가 구분되어 보고되는가.
- 변경 이유와 되돌림 조건을 PR 설명에 남겼는가.

## 공식 기준

- [Compose BOM](https://developer.android.com/develop/ui/compose/bom)
- [Compose compiler plugin](https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler)
- [Gradle Version Catalog](https://docs.gradle.org/current/userguide/version_catalogs.html)
- [KSP](https://kotlinlang.org/docs/ksp-overview.html)
