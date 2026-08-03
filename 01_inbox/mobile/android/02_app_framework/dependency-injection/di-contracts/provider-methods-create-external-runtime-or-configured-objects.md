---
title: provider-methods-create-external-runtime-or-configured-objects
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:43 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Provider method 는 외부 타입, 런타임 값, 설정된 객체를 만들 때 쓴다

`@Provides` 계열 함수는 DI framework 가 생성자를 알 수 없거나 호출해서는 안 되는 객체를 graph 에 넣기 위한 boundary 다. Retrofit, Room database, DataStore, `Context` 로 만드는 system-facing 객체, base URL 같은 configuration 을 묶은 객체가 여기에 들어간다.

Provider method 가 많아지면 graph 가 service locator 처럼 변한다. 먼저 constructor injection 이 가능한 타입인지 확인하고, provider 는 외부 library type 이나 construction policy 가 의미 있는 타입에 제한한다.

관련 노트: [Context boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md).

### 판단 기준

- `@Provides` 는 생성자 주입이 불가능한 외부 라이브러리 클래스, Builder 패턴으로 초기화해야 하는 객체, 또는 런타임 설정 값이 필요한 객체를 생성할 때 사용한다.

### 경계

- 내가 소유한 구체 클래스에 단순히 인스턴스를 반환하는 `@Provides` 를 작성하는 것은 중복(Boilerplate)이므로 피하고, 이러한 경우에는 `@Inject` 생성자나 인터페이스 바인딩(`@Binds`)을 우선한다.
