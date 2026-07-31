---
title: "Compose compiler는 BOM이 아니라 Kotlin compiler 흐름에 속한다"
tags: ["android", "android/packaging-deployment"]
---

# Compose compiler는 BOM이 아니라 Kotlin compiler 흐름에 속한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)
관련 노트: [Compose BOM은 Compose 라이브러리 버전 집합을 관리한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/compose-bom-manages-compose-library-version-set.md), [KSP는 Kotlin-first 코드 생성이고 kapt는 유지보수 모드다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/ksp-is-kotlin-first-code-generation-and-kapt-is-maintenance-mode.md)

## 구분

Compose UI 라이브러리의 버전 관리와 Compose compiler의 버전 관리는 서로 다른 축이다.
Compose BOM은 `ui`, `foundation`, `material` 같은 라이브러리의 버전 집합을 다룬다.
Compiler는 Kotlin 코드를 Compose에 맞게 컴파일하는 빌드 도구이므로 BOM으로 정렬되지 않는다.

## Kotlin 2.0 이상

Kotlin 2.0부터는 Compose compiler가 Kotlin compiler와 함께 릴리스·관리되는 흐름이다.
Gradle에서는 공식 `org.jetbrains.kotlin.plugin.compose` plugin을 적용하는 구성을 우선 검토한다.
정확한 plugin 버전과 적용 위치는 프로젝트의 Kotlin 버전 및 Android Gradle Plugin 조합을 공식 문서에서 확인한다.

```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}
```

위 예시는 방향을 보여 주는 형태이며, 실제 버전은 프로젝트의 version catalog와 plugin 관리 규칙에 맞춘다.
Kotlin, AGP, Gradle, Compose compiler plugin의 조합은 한 번에 올리지 말고 호환성을 검증한다.

## Kotlin 2.0 미만 또는 전환 중인 프로젝트

이전 구성에서는 Kotlin 버전에 맞는 Compose compiler extension을 공식 호환성 표에서 찾아야 한다.
현재 프로젝트가 어떤 방식인지 먼저 확인한 뒤 plugin 방식과 기존 설정을 혼합하지 않는다.
`composeOptions.kotlinCompilerExtensionVersion` 같은 이전 설정을 정리할 때는 컴파일 로그와 테스트를 확인한다.

## 검증 항목

- Compose compiler plugin이 필요한 모듈에만 적용되었는가.
- Kotlin plugin 버전과 compiler plugin 버전의 공식 조합인가.
- BOM 버전과 compiler 버전을 같은 숫자로 맞추려는 잘못된 규칙이 없는가.
- Compose UI 컴파일, 단위 테스트, instrumented test가 모두 통과하는가.
- 업그레이드 후 generated source와 경고가 예상 범위인가.

업그레이드 PR에는 이전 설정을 제거했는지와 새 plugin이 실제로 적용된 모듈을 함께 기록한다.
컴파일 실패가 나면 BOM을 바꾸기보다 Kotlin·plugin·AGP 조합부터 분리해 확인한다.
버전 번호를 문서의 예시로 고정하지 않고 프로젝트의 lockfile과 공식 릴리스 안내를 기준으로 갱신한다.

최신 버전 번호는 문서에 상수로 복사해 두기보다 릴리스 시점의 공식 문서를 기준으로 갱신한다.
현재 기준은 [Compose compiler Gradle plugin](https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler)과
[Compose BOM 안내](https://developer.android.com/develop/ui/compose/bom)를 함께 읽는다.
