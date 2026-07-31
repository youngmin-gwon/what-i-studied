---
title: "Gradle 빌드 계약"
tags: ["android", "android/packaging-deployment"]
---

# Gradle 빌드 계약

이 지도는 Android Gradle Plugin의 프로젝트 구조, DSL, identifier, variant, source set, signing 설정을 빌드 의미 단위로 나눈다.

## 정본 노트

- [Android Gradle Plugin은 Android 빌드 규칙을 Gradle에 추가한다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/android-gradle-plugin-adds-android-build-rules-to-gradle.md)
- [Gradle 프로젝트와 모듈 DSL은 서로 다른 책임을 가진다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-project-and-module-dsl-have-different-responsibilities.md)
- [Android 기본 설정은 식별자와 버전 계약을 만든다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/android-default-config-defines-identity-and-version-contracts.md)
- [Build type, product flavor, build variant는 서로 다른 축이다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/build-type-product-flavor-and-build-variant-are-different-axes.md)
- [Source set 우선순위는 variant별 코드와 리소스 충돌을 결정한다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/source-set-priority-decides-variant-code-and-resource-conflicts.md)
- [Signing config는 로컬 서명과 Play 배포 정체성을 연결한다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/signing-config-connects-local-signing-and-play-release-identity.md)
- [AGP DSL 체크리스트는 릴리스 변형의 실제 값을 확인한다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/agp-dsl-checklist-verifies-effective-release-variant-values.md)

관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md), [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)
