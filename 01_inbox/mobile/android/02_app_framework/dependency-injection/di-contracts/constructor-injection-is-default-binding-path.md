---
title: constructor-injection-is-default-binding-path
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Constructor injection 은 기본 binding 경로다

DI graph 에 타입을 넣는 기본 방법은 constructor injection 이다. 생성자에 필요한 dependency 가 드러나면 graph 는 타입 간 연결을 정적으로 추적할 수 있고, 테스트에서도 생성자가 요구하는 협력 객체가 명확해진다.

`@Provides`나 factory가 먼저 떠오른다면 그 타입을 직접 소유하지 않는지, 런타임 값이 필요한지, interface binding이 빠진 것은 아닌지 확인한다. 소유한 일반 클래스는 constructor injection으로 시작하는 편이 가장 단순하다.

### 최소 예시

```kotlin
class UserRepository @Inject constructor(
    private val api: UserApi,
    private val cache: UserCache,
)
```

Dagger 계열 graph는 `UserRepository`가 요청되면 두 constructor parameter의 binding을 찾은 뒤 생성 코드를 만든다. 별도 module은 필요하지 않지만 `UserApi`와 `UserCache`의 생성 경로는 있어야 한다.

### 실패와 관찰 신호

`UserApi` binding을 지우면 build에서 대략 `[Dagger/MissingBinding] UserApi cannot be provided without an @Provides-annotated method` 같은 dependency trace가 나온다. 정확한 문구는 버전에 따라 달라도, 어느 entry point에서 누락 key까지 도달했는지 trace를 읽는다. runtime container라면 같은 누락이 해당 객체를 처음 resolve할 때 예외로 나타날 수 있다.

공식 문서: [Dependency injection in Android](https://developer.android.com/training/dependency-injection)

생성자에 request/session 같은 런타임 값이 섞이면 모든 값을 graph binding으로 만들기보다 assisted factory나 명시적 factory parameter로 분리한다.

상위 문서: [DI 계약](./di-contracts.md)
