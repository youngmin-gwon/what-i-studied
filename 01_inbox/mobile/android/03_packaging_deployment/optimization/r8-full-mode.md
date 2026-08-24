---
title: r8-full-mode
tags: ["android", "r8", "fullmode", "optimization", "agp", "performance"]
aliases: ["R8 Full Mode", "R8 풀 모드", "R8 Configuration Analyzer", "android.enableR8.fullMode", "R8 최적화 모드"]
date created: 2026-08-24 15:05:00 +09:00
date modified: 2026-08-24 15:05:00 +09:00
---

## R8 Full Mode와 Configuration Analyzer (R8 Full Mode & Rules Analysis)

### 개요

**R8 Full Mode(풀 모드)** 는 기존 호환 모드(Compatibility Mode)의 보수적인 제약을 해제하고, 더 공격적인 코드 수축(Shrinking), 인라이닝(Inlining), 클래스 병합(Class Merging), 인자 제거(Argument Removal)를 적용하는 R8 최적화 실행 모드이다.

**AGP 8.0부터 기본값(Default)으로 활성화**되었으며, 과거 마이그레이션 과정에서 임시로 설정했던 `android.enableR8.fullMode=false` 플래그가 남아있다면 이를 제거하고 최신 릴리스 테스트로 검증해야 한다.

```mermaid
flowchart TD
    Rules["ProGuard Keep Rules"] --> Mode{"R8 실행 모드"}
    
    Mode -->|Compat Mode| LowOpt["보수적 최적화<br/>(클래스 Keep 시 Default Constructor 등 과도 보호)"]
    Mode -->|Full Mode (AGP 8.0+ 기본)| HighOpt["공격적 최적화<br/>(미사용 인자 제거 + 단일 구현체 클래스 병합 + 강력 인라이닝)"]
    
    HighOpt --> Analyzer["R8 Configuration Analyzer<br/>(최적화를 가로막는 병목 규칙 시각화 리포트)"]
```

---

### 1. Compat Mode vs Full Mode 의 핵심 차이

| 비교 항목 | Compat Mode (호환 모드 / 과거 기본값) | Full Mode (풀 모드 / AGP 8.0+ 기본값) |
|---|---|---|
| **기본 생성자 처리** | 클래스가 `-keep`되면 명시되지 않은 기본 생성자(`<init>()`)도 자동으로 보호함 | 명시되지 않은 생성자는 사용되지 않을 경우 엄격히 제거 |
| **미사용 인자 제거** | 메서드 시그니처를 보수적으로 유지 | 호출부에서 사용되지 않는 매개변수 바이트코드를 완전 삭제 |
| **클래스 병합 (Class Merging)** | 제한적 병합 수행 | 단일 구현 인터페이스나 1:1 상속 클래스를 하나로 적극 병합 |
| **DEX 크기 절감률** | 기준선 (Baseline) | **추가 5~15% 이상의 바이트코드 크기 축소 달성** |

---

### 2. R8 Configuration Analyzer: 최적화 차단 규칙 발굴

넓은 와일드카드(`-keep class com.example.** { *; }`)나 서드파티 라이브러리의 방어적인 Keep 규칙은 R8 의 최적화를 심각하게 가로막는다.

**R8 Configuration Analyzer** 는 병합된 전체 Keep 규칙이 수축률(Shrinking), 최적화(Optimization), 난독화(Obfuscation)에 미치는 부정적 영향을 수치화하고 시각적 HTML 리포트로 분석해 준다.

```bash
# AGP 9.3+ 단독 분석 태스크 실행 (APK 빌드 없이 초고속 리포트 생성)
./gradlew :app:analyzeReleaseR8Config

# 생성되는 HTML 리포트 위치
# app/build/reports/r8/r8-config-analyzer-release.html
```

---

### 3. 프로젝트 설정 확인 가이드

```properties
# gradle.properties

# [권장] AGP 8.0+에서는 Full Mode가 기본값이므로 해당 줄이 없어야 함.
# 만약 아래와 같이 비활성화 옵션이 남아있다면 즉시 제거하고 릴리스 회귀 테스트를 수행할 것!
# android.enableR8.fullMode=false (삭제 대상)
```

---

### 4. 관측 가능 증거 (Observable Evidence)

릴리스 빌드 시 생성되는 `configanalyzer.html` 또는 R8 매핑 보고서에서 규칙의 실효성을 관측할 수 있다:

```bash
# R8 최종 실효 규칙 파일 확인
cat app/build/outputs/mapping/release/configuration.txt | head -n 30
```

---

### 상위 및 연관 문서

- [R8 Keep 규칙과 최적화 경계](r8-keep-rules.md)
- [D8과 R8 컴파일러 및 덱싱(Dexing) 메커니즘](d8-and-r8.md)
- [R8 릴리스 검증 및 De-obfuscation](r8-validation.md)
- [빌드 최적화 계약](build-optimization.md)
