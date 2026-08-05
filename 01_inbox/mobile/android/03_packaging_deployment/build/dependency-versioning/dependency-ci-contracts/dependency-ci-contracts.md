---
title: dependency-ci-contracts
tags: ["android", "android/packaging-deployment", "dependency"]
aliases: ["의존성, 버전, CI 계약"]
date created: 2026-07-31 17:52:17 +09:00
date modified: 2026-08-05 16:15:00 +09:00
created: 2026-07-31 17:52:17 +09:00
updated: 2026-08-05 16:15:00 +09:00
---

## 의존성, 버전, CI 계약

상위 문서: [Android 패키징과 배포 지도](../../../android-packaging-deployment.md)

이 지도는 Gradle **Dependency Resolution**(전이적 의존성 그래프 해석 엔진), **Version Catalog**(`libs.versions.toml`: 중앙 의존성 좌표 관리), Compose **BOM**(Bill of Materials: 라이브러리 버전 집합) 및 Compiler, **KSP**(Kotlin Symbol Processing: 고성능 코드 생성기)/kapt 코드 생성, kotlinx.serialization, 그리고 CI/CD 품질 게이트 운영 계약을 다룬다.

```mermaid
flowchart LR
    Catalog["Version Catalog (libs.versions.toml)"] --> Resolution["Gradle Resolution Engine"]
    Resolution --> BOM["Compose BOM / Platform"]
    Resolution --> KSP["KSP Code Generator"]
    BOM --> CIGate["CI Fast Gate / Release Gate"]
    KSP --> CIGate
```

### 정본 노트
- [Gradle 의존성 관리는 요청 버전이 아니라 해석 그래프를 관리한다](gradle-dependency-management-controls-resolution-graph-not-requested-versions.md)
- [Version Catalog는 의존성 좌표와 플러그인 좌표의 이름표다](version-catalog-names-dependency-and-plugin-coordinates.md)
- [Compose BOM은 Compose 라이브러리 버전 집합을 관리한다](compose-bom-manages-compose-library-version-set.md)
- [Compose compiler는 BOM이 아니라 Kotlin compiler 흐름에 속한다](compose-compiler-belongs-to-kotlin-compiler-flow-not-bom.md)
- [KSP는 Kotlin-first 코드 생성이고 kapt는 유지보수 모드다](ksp-is-kotlin-first-code-generation-and-kapt-is-maintenance-mode.md)
- [kotlinx serialization은 컴파일러 플러그인과 런타임 포맷을 함께 요구한다](kotlinx-serialization-requires-compiler-plugin-and-runtime-format.md)
- [Android CI/CD 게이트는 빠른 검증과 릴리스 검증을 분리한다](android-cicd-gates-separate-fast-validation-and-release-validation.md)
- [의존성 변경 체크리스트는 그래프, ABI, 테스트, 배포 위험을 함께 본다](dependency-change-checklist-reviews-graph-abi-tests-and-release-risk.md)

이 지도의 CI/CD 노트는 "어떤 게이트를 언제 도는가"(Fast Gate vs Release Gate 구분)만 다루며, 그 게이트를 실제 파이프라인 단계·Fastlane·서명 자격증명·빌드 매트릭스로 구현하는 방법은 별도 클러스터 [Android CI/CD 구현 계약](../../ci-cd-contracts/ci-cd-contracts.md) 이 다룬다.

관련 지도: [Gradle 빌드 계약](../../gradle/gradle-build-contracts/gradle-build-contracts.md), [Play 릴리스와 배포 계약](../../../distribution/release-distribution-contracts/release-distribution-contracts.md), [Android CI/CD 구현 계약](../../ci-cd-contracts/ci-cd-contracts.md)

### 관측 가능 증거 (Observable Evidence)
```bash
# 의존성 그래프 및 충돌 분석
./gradlew app:dependencies --configuration releaseRuntimeClasspath
./gradlew app:dependencyInsight --dependency okhttp --configuration releaseRuntimeClasspath
```
