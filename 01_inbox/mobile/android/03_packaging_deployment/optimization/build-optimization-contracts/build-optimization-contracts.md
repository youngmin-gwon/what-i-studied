---
title: build-optimization-contracts
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:55 +09:00
date created: 2026-07-31 17:32:53 +09:00
---

## R8 와 Gradle 빌드 최적화 계약

이 지도는 배포 산출물 최적화와 개발 빌드 속도를 분리한다. R8 은 릴리즈 산출물의 크기, 난독화, 최적화 계약이고, Gradle 성능은 개발 피드백 루프의 계약이다.

### 정본 노트

- [R8은 릴리즈 코드의 수축, 최적화, 난독화를 수행한다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-shrinks-optimizes-and-obfuscates-release-builds.md)
- [R8 keep 규칙은 최적화 경계다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/keep-rules-are-optimization-boundaries.md)
- [R8 Full Mode와 Configuration Analyzer는 막힌 최적화를 드러낸다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-full-mode-and-configuration-analyzer-expose-blocked-optimization.md)
- [리소스 수축은 코드 수축 후 미사용 리소스를 제거한다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/resource-shrinking-removes-unused-resources-after-code-shrinking.md)
- [R8 결과물은 크기와 런타임 회귀로 검증한다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-output-must-be-validated-with-size-and-runtime-regression.md)
- [Gradle 빌드 성능은 앱 런타임 성능과 다르다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/gradle-build-performance-is-not-app-runtime-performance.md)
- [증분 빌드, 캐시, 구성 캐시는 빌드 작업량을 줄인다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/incremental-build-cache-and-configuration-cache-reduce-build-work.md)

관련 지도: [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md), [Play 릴리스와 배포 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)
