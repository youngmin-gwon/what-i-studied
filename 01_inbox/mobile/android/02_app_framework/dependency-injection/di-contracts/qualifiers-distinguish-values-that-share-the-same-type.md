---
title: Qualifier는 같은 타입의 서로 다른 의미를 구분한다
tags: ["android", "android/app-framework"]
---

# Qualifier는 같은 타입의 서로 다른 의미를 구분한다

DI graph는 타입만으로 binding을 찾는 경우가 많다. 같은 `String`, `CoroutineDispatcher`, `OkHttpClient`, `Context`가 여러 의미로 존재하면 타입만으로는 어떤 값을 넣어야 하는지 알 수 없다.

Qualifier는 같은 타입의 값을 의미별로 분리하는 이름표다. `@ApplicationContext`와 `@ActivityContext`, `@IoDispatcher`와 `@MainDispatcher`처럼 lifetime이나 역할이 다른 값을 구분할 때 사용한다.

관련 노트: [Context boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md).

## 판단 기준

- 동일한 타입(예: String, Retrofit, Dispatcher)이지만 사용 목적이 다른 경우, `@Qualifier` (예: `@Named`) 어노테이션을 생성하여 DI 그래프가 어떤 인스턴스를 주입할지 명확히 식별하게 해야 한다.

## 경계

- 여러 구현체가 존재하지 않고 단일 용도로만 사용되는 커스텀 클래스에는 Qualifier를 남용하지 않으며, 안드로이드 Context나 코루틴 Dispatcher 같은 범용 타입의 충돌 방지용으로 제한적으로 사용한다.
