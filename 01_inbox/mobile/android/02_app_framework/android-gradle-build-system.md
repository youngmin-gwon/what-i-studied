---
title: android-gradle-build-system
tags: [android, gradle, build, hub]
aliases: [Gradle MOC, 빌드 시스템 허브]
---

# [[mobile-security]] > [[android-gradle-build-system]]

## Gradle Build System (MOC)

안드로이드 프로젝트의 빌드, 자동화, 의존성 관리의 중심인 Gradle 시스템에 대한 지식 지도입니다. 대규모 프로젝트의 빌드 속도 개선과 유지보수 효율성을 목표로 합니다.

---

### 🏗️ Build Foundation (빌드 기초)

Gradle의 핵심 구조와 설정 방식을 다룹니다.

- [[gradle-build-basics]]: 프로젝트/모듈 구조 및 **Plugins 블록** (alias vs id).
- [[gradle-dependency-management]]: **Version Catalog (toml)**, **Compose BOM** 및 Kapt vs KSP 비교.
- [[android-gradle-dsl-reference]]: `build.gradle.kts` 상세 문법 가이드.

---

### 📦 Variability & Packaging (변형 및 패키징)

다양한 제품군과 서명을 관리하는 방법입니다.

- [[gradle-variants-flavors]]: **Build Types** (Debug/Release) 및 **Product Flavors** 환경 구축.
- [[gradle-optimization-signing]]: **Keystore** 보안 서명 및 **R8/Proguard** 코드 축소/난독화.

---

### ⚡ Performance & CI/CD (성능 및 자동화)

대규모 프로젝트 빌드 최적화와 파이프라인 구축입니다.

- [[gradle-performance-tuning]]: Configuration Caching, 빌드 스캔 및 태스크 병목 분석.
- [[android-cicd-patterns]]: GitHub Actions/Jenkins를 활용한 자동 빌드 및 배포.

---

### 📚 연관 문서
- [[android-os-development-guide]]: OS 개발 관점의 빌드
- [[android-jetpack-architecture]]: 아키텍처와 라이브러리 상관 관계
- [[google-play-deployment]]: 스토어 배포 프로세스
