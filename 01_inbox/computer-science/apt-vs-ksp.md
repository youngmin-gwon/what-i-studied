---
title: apt-vs-ksp
tags: [computer-science, metaprogramming, apt, ksp, kotlin, java]
aliases: [APT vs KSP, KSP vs APT, kapt vs KSP]
date modified: 2026-08-06 18:08:00 +09:00
date created: 2026-08-06 18:08:00 +09:00
---

# APT vs KSP (어노테이션 프로세서 및 심볼 프로세서 비교)

## 1. 개요 (Overview)

Java 와 Kotlin 생태계에서 컴파일 타임 소스 코드 생성을 전담하는 어노테이션 프로세싱 도구는 자바 표준인 **APT (Annotation Processing Tool / `kapt`)** 와 코틀린 전용으로 발전한 **KSP (Kotlin Symbol Processing)** 로 나뉜다.

---

## 2. APT vs KSP 핵심 기술 비교표

| 비교 항목 | APT / kapt (Java 표준 기반) | KSP (Kotlin Symbol Processing) |
| :--- | :--- | :--- |
| **대상 언어** | Java 중심 (`kapt`를 통해 Kotlin 지원) | **Kotlin 전용 (Kotlin K2 컴파일러 통합)** |
| **작동 원리** | 임시 자바 코드 생성 (**Java Stubs**) 후 스캔 | Kotlin AST(추상 구문 트리) 심볼 직접 분석 |
| **빌드 속도** | **느림** (Java Stub 생성 단계 오버헤드) | **최대 2배 이상 빠름** (Stub 생성 단계 0) |
| **타입 정보 파악** | Kotlin 전용 기능(Nullability, Sealed Class) 미파악 | Kotlin **Nullability(`?`), Sealed Class, Delegate** 완벽 지원 |
| **대표적 활용** | 구형 Dagger2, Room (`kapt`), ButterKnife | 현대 **Room (KSP), kotlinx.serialization, Metro DI** |

---

## 3. 연결 문서 (Related Links)

- [Compile-time Code Generation](compile-time-code-generation.md) - 컴파일 타임 코드 생성의 상위 개념 정의
- [Reflection](reflection.md) - KSP/APT 가 대체하는 런타임 리플렉션의 한계
