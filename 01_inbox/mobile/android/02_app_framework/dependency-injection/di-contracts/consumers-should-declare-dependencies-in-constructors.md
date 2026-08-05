---
title: consumers-should-declare-dependencies-in-constructors
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## 소비자는 의존성을 생성하지 말고 생성자로 요구한다

DI 가 잘 동작하려면 Repository, UseCase, state holder 같은 일반 Kotlin 객체가 내부에서 concrete dependency 를 직접 만들지 않아야 한다. 소비자는 필요한 dependency 를 생성자 파라미터로 선언하고, graph 가 그 생성자를 호출하게 둔다.

직접 생성이 섞이면 fake 교체, scope 통제, configuration 주입, dependency graph 검증이 깨진다. Android framework class 처럼 생성자를 framework 가 호출하는 타입은 예외이며, 이때는 **Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) entry point, factory, assisted injection 같은 별도 boundary 가 필요하다.

관련 노트: [ViewModel](../../architecture/state-management/viewmodel/viewmodel.md), [Hilt integration](./hilt-is-official-android-dagger-integration.md).

### 판단 기준

- 소비하는 객체는 `new` 나 팩토리 메서드를 직접 호출하지 않고 생성자 파라미터로만 의존성을 선언해야 한다. 이를 통해 결합도를 낮추고 테스트 시 Fake 객체 주입을 용이하게 한다.

### 경계

- Activity, Fragment 등 시스템이 생성자를 호출하는 안드로이드 프레임워크 컴포넌트는 예외적으로 `@AndroidEntryPoint` 등을 통해 필드 주입을 사용해야 한다.
