---
title: gradle-performance-tuning
tags: [android, build, gradle, performance]
aliases: [빌드 성능 최적화]
date modified: 2026-04-06 19:10:00 +09:00
date created: 2026-04-06 18:57:55 +09:00
---

## [[android-gradle-build-system]] > [[gradle-performance-tuning]]

### Gradle Performance Tuning: Optimized Build Pipeline

대규모 안드로이드 프로젝트에서 빌드 시간은 개발 생산성에 직결됩니다. 본 문서는 Gradle 빌드 속도를 획기적으로 단축하기 위한 전략과 최신 성능 기법을 분석합니다.

---

#### ⚡ 1. 핵심 성능 기능 활성화 (Core Speed-ups)

`gradle.properties` 에 다음 설정을 추가하여 기본 성능을 강화합니다.

```properties
# 병렬 프로젝트 실행
org.gradle.parallel=true

# 빌드 구성 캐싱 (매우 중요)
org.gradle.configuration-cache=true

# JVM 데몬 메모리 확장
org.gradle.jvmargs=-Xmx6g -XX:+UseParallelGC -Dfile.encoding=UTF-8

# 증분 빌드 활성화
org.gradle.caching=true
```

---

#### 🔍 2. 빌드 프로파일링 & 분석 (Build Scanning)

어떤 태스크가 시간을 가장 많이 잡아먹는지 확인하는 것이 최적화의 첫걸음입니다.

- **Build Scan**: `./gradlew assembleDebug --scan`
  - Gradle Enterprise 또는 클라우드 리포트를 통해 태스크 종속성, 네트워크 지연, 캐시 미스 이유를 시각적으로 확인.
- **Profile Report**: `./gradlew assembleDebug --profile`
  - `build/reports/profile` 에 로컬 HTML 리포트 생성.

---

#### 🎯 3. 단계별 최적화 전략

| 단계 | 전략 | 효과 |
| :--- | :--- | :--- |
| **Configuration** | 불필요한 연산 제거, Configuration Cache 사용 | 빌드 시작 시간 5-10초 단축 |
| **Dependency** | Version Catalog 를 통한 의존성 관리, 불필요한 동적 버전(`+`) 제거 | 네트워크 지연 및 해결 속도 개선 |
| **Execution** | 증분 컴파일(Incremental), 원격 캐싱(Remote Cache) | 재빌드(Incremental Build) 시간 70% 단축 |
| **JVM** | 적절한 `-Xmx` 할당 및 가비지 컬렉터(ParallelGC) 설정 | GC 오버헤드로 인한 빌드 멈춤 방지 |

---

#### 🛡️ 4. 증분 빌드와 캐시 (Incremental vs Caching)

- **Incremental Build**: 이미 처리된 입력값은 건너뛰고 변경된 파일만 컴파일.
- **Configuration Cache**: `settings.gradle`, `build.gradle` 의 실행 결과를 캐싱하여 'Configuring' 단계를 생략. (Kotlin K2 컴파일러와 함께 최상의 궁합)
- **Remote Build Cache**: CI 환경과 로컬 팀원 간에 빌드 아티팩트를 공유하여 'Clean Build' 시간을 획기적으로 절약.

---

#### 📚 See Also
- [[android-gradle-build-system]] - 안드로이드 빌드 시스템 허브
- [[android-gradle-dsl-reference]] - `build.gradle.kts` 상세 문법
- [[android-cicd-patterns]] - 자동화된 CI/CD 파이프라인
