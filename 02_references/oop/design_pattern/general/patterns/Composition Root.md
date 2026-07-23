---
title: Composition Root
tags: [design-pattern, general-pattern, oop, architecture, dependency-injection]
aliases: [Composition Root Pattern]
date modified: 2026-07-23
date created: 2026-07-23
---

## Description

**Composition Root** 는 애플리케이션에서 구체 클래스들을 조립해서 객체 그래프를 만드는 **단 하나의 지점**을 의미함. Mark Seemann 이 *Dependency Injection Principles, Practices, and Patterns* 에서 정리한 용어로, GoF 책에는 나오지 않지만 GoF 패턴이 실무에서 어떻게 배선(wiring)되는지를 설명해 줌.

- **핵심**: 구현체(concrete class)를 아는 코드를 없애는 게 아니라, 그 코드를 시스템의 가장 바깥쪽 한 곳으로 몰아내는 것.
- **왜 필요한가**: `interface PaymentStrategy` 를 아무리 잘 추상화해도, 어딘가에서는 반드시 `PaypalStrategy()` 를 생성해야 함. 이 생성 코드를 도메인 곳곳에 흩어놓지 않고 한 곳에 모으는 것이 목적.
- **DI Container 와의 관계**: Android 의 [Metro](https://github.com/ZacSweers/metro), Dagger/Hilt, Koin, Spring 의 `ApplicationContext` 는 모두 Composition Root 를 프레임워크가 대신 구현해 준 것. `@Provides`/`@Binds` 선언이 곧 Composition Root 의 배선 정보임.

## 왜 GoF 예제만 보면 헷갈리는가

GoF 다이어그램은 대부분 이렇게 끝남.

```
Client → ConcreteStrategy 생성 → Context 에 전달
```

"결국 Client 가 Concrete 를 아는데, 뭐가 분리된 거지?" 라는 의문이 자연스럽게 듦. GoF 책은 1994년에 쓰였고 DI Container 라는 개념 자체가 없었기 때문에, "이 생성 코드를 어디에 둘 것인가" 를 설명하지 않고 넘어감.

현대 아키텍처는 이 지점을 명확히 함.

```
Composition Root            ← 구현체를 아는 유일한 곳 (DI Module)
      ↓ 생성 + 주입
Application / Domain Layer  ← 인터페이스만 의존
```

즉 GoF 패턴이 숨기는 건 "구현체를 아는 사람" 이 아니라 **"구현체를 아는 위치의 개수"**. [DIP(Dependency Inversion Principle)](../../../solid/DIP(Dependency%20Inversion%20Principle).md) 도 같은 이야기 — 고수준 모듈이 저수준 모듈을 몰라도 된다는 것이지, 아무도 몰라도 된다는 뜻이 아님.

## Android 예시 (Metro)

[Metro](https://github.com/ZacSweers/metro) 는 컴파일 타임에 동작하는 Kotlin DI 컴파일러 플러그인. `@DependencyGraph` 가 Composition Root 역할을 함.

```kotlin
// Domain: 구현을 모름, 인터페이스만 의존
@Inject
class CheckoutViewModel(private val strategy: PaymentStrategy)

// Composition Root: 여기만 구현을 앎
@DependencyGraph(AppScope::class)
interface AppGraph {
    val checkoutViewModel: CheckoutViewModel

    @Provides
    fun providePaymentStrategy(
        samsung: SamsungBillingStrategy,
        google: GoogleBillingStrategy,
    ): PaymentStrategy =
        if (Build.MANUFACTURER == "Samsung") samsung else google
}

// 앱 시작 지점
val graph = createGraph<AppGraph>()
```

`AppGraph` 밖에서는 아무도 `SamsungBillingStrategy` 라는 이름을 몰라도 됨. Metro 를 안 쓰는 프로젝트라면 `Application` 클래스나 `AppContainer` 가 같은 역할을 함 — 프레임워크가 있든 없든 "구현체를 아는 코드는 한 곳" 이라는 원칙은 동일함.

## GoF 패턴 재분류

DI 시대에 GoF 23개 패턴이 실무에서 어떤 위치에 있는지 3그룹으로 나누면 다음과 같음.

| 그룹 | 의미 | 해당 패턴 |
| :--- | :--- | :--- |
| **1. 언어가 흡수** | 언어 기능만으로 대체됨. DI 와 무관 | [Builder](../../creational/Builder%20Pattern.md), [Iterator](../../behavioral/Iterator%20Pattern.md), [Prototype](../../creational/Prototype%20Pattern.md) |
| **2. DI Container 가 흡수** | 패턴이 사라진 게 아니라 Container 내부가 그 패턴으로 구현되어 있음 | [Factory Method](../../creational/Factory%20Method%20Pattern.md), [Abstract Factory](../../creational/Abstract%20Factory%20Pattern.md), [Observer](../../behavioral/Observer%20Pattern.md), [Singleton](../../creational/Singleton%20Pattern.md) |
| **3. 여전히 설계의 핵심** | 객체 관계/생명주기를 다루는 패턴이라 언어·프레임워크로 대체 불가 | [Strategy](../../behavioral/Strategy%20Pattern.md), [Template Method](../../behavioral/Template%20Method%20Pattern.md), [Command](../../behavioral/Command%20Pattern.md), [Adapter](../../structural/Adapter%20Pattern.md), [Decorator](../../structural/Decorator%20Pattern.md), [Composite](../../structural/Composite%20Pattern.md), [Facade](../../structural/Facade%20Pattern.md), [Bridge](../../structural/Bridge%20Pattern.md), [Proxy](../../structural/Proxy%20Pattern.md), [Memento](../../behavioral/Memento%20Pattern.md), [State](../../behavioral/State%20Pattern.md), [Chain of Responsibility](../../behavioral/Chain%20of%20Responsibility%20Pattern.md), [Mediator](../../behavioral/Mediator%20Pattern.md), [Visitor](../../behavioral/Visitor%20Pattern.md), [Interpreter](../../behavioral/Interpreter%20Pattern.md), [Flyweight](../../structural/Flyweight%20Pattern.md) |

각 패턴 문서의 `Modern Applicability` 절은 이 표의 분류를 근거로, Android(Metro) 에서 그 패턴이 실제로 어떻게 배선되는지를 다룸.

## 결론

> GoF 패턴의 상당수는 "사라진 것" 이 아니라, 언어와 프레임워크가 그 구현을 흡수했거나, 적용 범위가 더 좁고 명확해진 것이다.

작고 순수한 로직(정렬 알고리즘 등)은 함수로 충분하지만, 생명주기·트랜잭션·DI 가 얽히는 "서비스형" 코드는 여전히 인터페이스와 Composition Root 조합이 필요함.

## Relationship with other patterns

### [DIP(Dependency Inversion Principle)](../../../solid/DIP(Dependency%20Inversion%20Principle).md)

- DIP 는 "고수준 모듈이 저수준 모듈에 의존하지 않는다" 는 원칙, Composition Root 는 그 원칙을 "어디서 조립할 것인가" 로 구체화한 실천 방법.

### [Factory Method Pattern](../../creational/Factory%20Method%20Pattern.md), [Abstract Factory Pattern](../../creational/Abstract%20Factory%20Pattern.md)

- DI Container(`AppGraph`, `ApplicationContext`) 자체가 거대한 Factory 이자 Composition Root 의 실제 구현체.
