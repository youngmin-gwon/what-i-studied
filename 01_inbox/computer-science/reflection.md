---
title: reflection
tags: [computer-science, reflection, java, kotlin, metaprogramming]
aliases: [Reflection, 런타임 리플렉션, 리플렉션]
date modified: 2026-08-06 18:08:00 +09:00
date created: 2026-08-06 17:26:00 +09:00
---

# Reflection (런타임 리플렉션)

## 1. 개요 (Overview)

**Reflection (런타임 리플렉션)** 은 자바(Java)나 코틀린(Kotlin) 등 프로그래밍 언어에서 **애플리케이션이 실행 중(Runtime)인 상태에서 자기 자신의 객체 구조, 클래스 타입, 필드, 메서드, 어노테이션 정보 등을 동적으로 조회하고 조작할 수 있도록 지원하는 메타프로그래밍 기술**이다.

컴파일 시점에 결정되지 않은 객체의 정보에 접근하거나, 객체의 `private` 멤버에 강제로 접근하여 값을 읽고 수정할 때 사용된다.

---

### 초보자를 위한 쉽게 이해하는 비유

* **일반적인 정적 코드 실행 (Static Call)**:
  - 공장에서 미리 정해진 주문서(컴파일 결과)대로 정품 부품을 순서대로 조립하는 방식 (매우 빠르고 안전함).
* **런타임 리플렉션 (Reflection)**:
  - 실행 중에 상자가 들어오면 **엑스레이(X-Ray)로 내부 필드 구조를 하나하나 스캔한 뒤, 상자를 열고 private 부품을 몰래 꺼내 조작하는 방식** (느리고, 엑스레이 스캔 비용이 크며, 망가질 위험이 존재함).

---

## 2. Java Reflection vs Kotlin Reflection

Java 의 표준 `java.lang.reflect` 와 코틀린 전용 `kotlin.reflect` 의 구조적 차이점 및 라이브러리 용량 특성은 독립된 [Java vs Kotlin Reflection 비교 문서](java-vs-kotlin-reflection.md)를 참고한다.

---

## 3. Kotlin 이 런타임 리플렉션을 지양하는 이유와 언어적 대안

Kotlin 생태계에서는 **`kotlin-reflect` 사용을 가급적 피하고 컴파일 타임으로 해결**하는 패턴을 권장한다.

1. **`kotlin-reflect.jar` 파일 용량 부담**:
   - 코틀린 리플렉션 라이브러리를 프로젝트에 포함하면 APK/AAB 빌드 용량이 약 2.5MB 이상 증가한다.
2. **`inline` + `reified` 키워드를 통한 런타임 타입 추상화**:
   - Java 에서는 generic 타입 파라미터가 런타임에 소거(Type Erasure)되어 `Class<T>`를 얻으려면 리플렉션을 써야 했다.
   - Kotlin 은 **`inline fun <reified T> getGenericType()`** 문법을 통해 리플렉션 없이 컴파일 타임에 타입을 구체화(Reify)하여 리플렉션 오버헤드를 0으로 만든다.
3. **KSP 기반 컴파일 타임 코드 생성**:
   - [Compile-time Code Generation](compile-time-code-generation.md)을 활용하여 `kotlinx.serialization`이나 Metro/Hilt DI 처럼 리플렉션 없는 초고속 빌드를 지향한다.

---

## 4. 리플렉션의 주요 활용과 심각한 단점

### 1) 주요 활용 분야
- **구형 의존성 주입 (DI)**: Spring Framework, Guice 등 런타임 탐색.
- **구형 직렬화**: [java.io.Serializable](../mobile/android/01_system_internals/binder-ipc.md) 객체 자동 변환.

### 2) 심각한 단점
- **런타임 성능 오버헤드**: 직접 호출 대비 수십 배 이상 느리며 [ART 런타임](../mobile/android/01_system_internals/art.md) 최적화를 방해함.
- **가비지 컬렉션(GC) 폭증**: 메타데이터 객체 남발로 [Garbage Collection](garbage-collection.md) 팝업 유발.
- **타입 안전성 파괴**: 오타 발생 시 런타임 크래시 유발.

---

## 5. 리플렉션의 대안: 컴파일 타임 코드 생성 (KSP / APT & Metro DI)

현대적인 모바일 및 웹 개발(Android/Kotlin)에서는 런타임 리플렉션의 단점을 극복하기 위해 **[Compile-time Code Generation (컴파일 타임 코드 생성)](compile-time-code-generation.md)** 기술로 완전히 전환되었다.

- **KSP (Kotlin Symbol Processing) / APT (Annotation Processing)**:
  - 자세한 메커니즘과 두 도구의 차이점은 [APT vs KSP](apt-vs-ksp.md) 및 [Compile-time Code Generation](compile-time-code-generation.md) 문서를 참고한다.
- **현대 DI 프레임워크 (Metro DI / Dagger / Hilt)**:
  - 런타임 리플렉션 0% 로 초고속 객체 주입을 보장한다.

---

## 6. 연결 문서 (Related Links)

- [Java vs Kotlin Reflection](java-vs-kotlin-reflection.md) - Java 와 Kotlin Reflection 패키지 세부 비교
- [Compile-time Code Generation](compile-time-code-generation.md) - 리플렉션을 대체하는 코드 생성 메커니즘
- [APT vs KSP](apt-vs-ksp.md) - 어노테이션 및 심볼 프로세서 비교
- [Serializable](../mobile/android/01_system_internals/binder-ipc.md) - 리플렉션 기반 구형 직렬화와 컴파일 타임 kotlinx.serialization 비교
- [Garbage Collection](garbage-collection.md) - 리플렉션 객체 생성으로 인해 유발되는 GC 팝업
- [ART (Android Runtime)](../mobile/android/01_system_internals/art.md) - 리플렉션 실행 시 컴파일 최적화가 제약되는 안드로이드 런타임
