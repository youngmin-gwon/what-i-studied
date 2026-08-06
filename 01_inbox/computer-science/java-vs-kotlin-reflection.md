---
title: java-vs-kotlin-reflection
tags: [computer-science, reflection, java, kotlin, metaprogramming]
aliases: [Java vs Kotlin Reflection, java.lang.reflect vs kotlin.reflect]
date modified: 2026-08-06 18:08:00 +09:00
date created: 2026-08-06 18:08:00 +09:00
---

# Java vs Kotlin Reflection (`java.lang.reflect` vs `kotlin.reflect`)

## 1. 개요 (Overview)

런타임 메타데이터를 동적으로 스캔하는 리플렉션 기술은 Java 의 표준 API 인 **`java.lang.reflect`** 와 Kotlin 언어 전용 공식 패키지인 **`kotlin.reflect`** 로 나뉜다.

---

## 2. Java vs Kotlin Reflection 비교표

| 비교 항목 | Java Reflection (`java.lang.reflect`) | Kotlin Reflection (`kotlin.reflect`) |
| :--- | :--- | :--- |
| **패키지 명** | `java.lang.reflect.*` | `kotlin.reflect.*` |
| **핵심 메타 클래스** | `Class`, `Field`, `Method`, `Constructor` | `KClass`, `KProperty`, `KFunction`, `KParameter` |
| **Kotlin 언어 이해도** | Nullability, Data Class, Delegate 파악 불가 | **Nullability(`?`), Property Delegate, Sealed Class 완벽 파악** |
| **라이브러리 포함** | JDK 기본 포함 (추가 용량 0) | **`kotlin-reflect.jar` (약 2.5MB 파일 추가 필요)** |
| **권장 사용 여부** | 구형 자바 프레임워크 호환성 유지 | **사용 극구 지양 (inline reified 및 KSP 대체 권장)** |

---

## 3. 연결 문서 (Related Links)

- [Reflection](reflection.md) - 런타임 리플렉션의 상위 정의 및 단점
- [APT vs KSP](apt-vs-ksp.md) - 리플렉션을 대체하는 컴파일 타임 코드 생성 도구 비교
