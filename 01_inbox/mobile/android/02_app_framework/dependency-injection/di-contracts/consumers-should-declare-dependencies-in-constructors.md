---
title: "소비자는 의존성을 생성하지 말고 생성자로 요구한다"
tags: ["android", "android/app-framework"]
---

# 소비자는 의존성을 생성하지 말고 생성자로 요구한다

DI가 잘 동작하려면 Repository, UseCase, state holder 같은 일반 Kotlin 객체가 내부에서 concrete dependency를 직접 만들지 않아야 한다. 소비자는 필요한 dependency를 생성자 파라미터로 선언하고, graph가 그 생성자를 호출하게 둔다.

직접 생성이 섞이면 fake 교체, scope 통제, configuration 주입, dependency graph 검증이 깨진다. Android framework class처럼 생성자를 framework가 호출하는 타입은 예외이며, 이때는 Hilt entry point, factory, assisted injection 같은 별도 boundary가 필요하다.

관련 노트: [ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [Hilt integration](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/hilt-is-official-android-dagger-integration.md).

## 판단 기준

- 소비하는 객체는 `new`나 팩토리 메서드를 직접 호출하지 않고 생성자 파라미터로만 의존성을 선언해야 한다. 이를 통해 결합도를 낮추고 테스트 시 Fake 객체 주입을 용이하게 한다.

## 경계

- Activity, Fragment 등 시스템이 생성자를 호출하는 안드로이드 프레임워크 컴포넌트는 예외적으로 `@AndroidEntryPoint` 등을 통해 필드 주입을 사용해야 한다.
