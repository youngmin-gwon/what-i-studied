---
title: di-binding-creation
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 15:22:00 +09:00
date created: 2026-08-06 15:22:00 +09:00
---

## DI Binding and Creation Contracts

### DI는 전역 객체 접근이 아니라 조립 경계다
Dependency Injection의 핵심은 필요한 객체를 소비자가 직접 만들거나 전역 registry에서 꺼내지 않고, 바깥 composition root에서 연결해 넣는 것이다. 생성 책임이 compiler-generated graph나 module 선언으로 이동할 뿐, 소비자가 전역 룩업을 하는 것이 아니다.

### 소비자는 의존성을 생성하지 말고 생성자로 요구한다
객체 생성 정책, 테스트 대체와 lifetime을 사용 코드에서 분리해야 한다. 의존성을 생성자로 요구해야 객체가 유효해지기 전에 필요한 dependency가 모두 채워진다.

### Constructor injection은 기본 binding 경로다
DI graph 에 타입을 넣는 기본 방법은 constructor injection 이다. 생성자에 필요한 dependency 가 드러나면 graph 는 타입 간 연결을 정적으로 추적할 수 있다. 런타임에 동적인 인자가 필요하다면 **Assisted Injection**을 고려해야 한다 (ex. `@AssistedInject`와 `@AssistedFactory`).

### Binds는 interface와 implementation을 연결한다
`@Binds` 계열 binding 은 이미 constructor injection 으로 만들 수 있는 implementation 을 interface 타입으로 노출하는 선언이다. 생성 코드를 추가하지 않는다.

### Provider method는 외부 타입, 런타임 값, 설정된 객체를 만들 때 쓴다
`@Provides` 계열 함수는 DI framework 가 생성자를 알 수 없거나 호출해서는 안 되는 객체를 graph 에 넣기 위한 boundary 다 (ex. Retrofit, Room database).

### Qualifier는 같은 타입의 서로 다른 의미를 구분한다
같은 `String`이나 `CoroutineDispatcher`가 여러 의미로 존재하면 타입만으로는 알 수 없다. `@Qualifier`는 같은 타입의 값을 의미별로 분리하는 식별 어노테이션이다.

### 누락된 바인딩과 Graph Compilation Error
의존성 그래프 구성 시 필요한 binding이 빠졌거나 (Missing Binding) 주입할 수 없는 경우, 컴파일 타임 의존성 주입 프레임워크(Dagger/Hilt 등)는 Graph Compilation Error를 띄워 런타임 이전에 실패를 보장한다.
