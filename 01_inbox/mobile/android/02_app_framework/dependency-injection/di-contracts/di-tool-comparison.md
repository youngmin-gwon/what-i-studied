---
title: di-tool-comparison
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 15:22:00 +09:00
date created: 2026-08-06 15:22:00 +09:00
---

## DI Tool Comparison and Engine Contracts

### Dagger와 Hilt
**Dagger**는 compile time에 dependency graph를 생성하고 검증하는 정적 DI engine이다. Android component 생성 시점과 표준 hierarchy 통합은 **Hilt**를 통해 공식적으로 지원된다. Dagger 자체는 정적 graph 엔진이지 Android lifecycle 정책을 강제하지는 않는다.

### Koin
**Koin** classic DSL은 Kotlin 코드로 definition을 선언하고 container가 런타임에 dependency를 resolve한다. 런타임 resolution 편의성을 제공하며, compiler plugin이나 module verify()를 쓰면 빌드 타임 검증을 앞당길 수 있다.

### Metro
**Metro**는 Kotlin compiler plugin 기반의 compile-time DI로, get_it 식 전역 locator가 아니라 graph가 생성자를 호출하고 binding을 검증하게 두는 도구다.

### Compile-time DI와 Runtime DI의 실패 시점
Dagger/Hilt, Metro 같은 compile-time DI는 누락 binding, cycle을 build 단계에서 드러낸다. 반면 runtime resolution 성격이 강한 구성은 해당 실행 경로에서 처음 예외가 발생할 수 있다.

### DSL 문법은 ownership과 lifetime 계약을 바꾸지 않는다
Koin DSL, Compose 등의 DSL 문법은 선언을 쉽게 하지만 owner와 lifetime을 자동으로 올바르게 만들어 주지는 않는다. 언제 생성되고 사라지는지 별도로 설계해야 한다.
