---
title: Composition Root
tags: [design-pattern, general-pattern, oop, architecture, dependency-injection]
aliases: [Composition Root Pattern]
date modified: 2026-07-23
date created: 2026-07-23
---

## Description

**Composition Root** 는 애플리케이션에서 객체 그래프(구체 클래스들의 조합)를 조립하는 **단 하나의 지점**을 의미함. Mark Seemann 이 *Dependency Injection Principles, Practices, and Patterns* 에서 정리한 용어이며, GoF 책에는 등장하지 않지만 GoF 패턴들이 실무에서 어떻게 배선(wiring)되는지 이해하는 데 핵심적인 개념임.

- **핵심**: 구현체(concrete class)를 아는 코드를 없애는 것이 아니라, 그 코드를 시스템의 가장 바깥쪽 한 곳으로 몰아내는 것.
- **왜 필요한가**: `interface PaymentStrategy` 를 아무리 잘 추상화해도, 어딘가에서는 반드시 `new PaypalStrategy()` 를 호출해야 함. 이 호출을 도메인/애플리케이션 코드 곳곳에 흩어 놓지 않고 한 곳(Composition Root)에 모아두는 것이 목적.
- **DI Container 와의 관계**: Spring 의 `ApplicationContext`, Android 의 Hilt/Koin Container 는 사실상 Composition Root 를 프레임워크가 대신 구현해 준 것. 개발자가 명시적으로 `new` 하는 대신, `@Bean`/`@Provides`/`@Module` 선언이 Composition Root 의 배선 정보 역할을 함.

## 왜 GoF 예제만 보면 헷갈리는가

GoF 책의 다이어그램은 대부분 다음과 같이 끝남.

```
Client → new ConcreteStrategy() → Context
```

여기서 "Client 가 결국 Concrete 를 아는데, 뭐가 분리된 거지?" 라는 의문이 생김. 이 의문은 타당함 — GoF 책은 1994년에 쓰여졌고, 당시엔 DI Container 도 IoC 도 거의 없었기 때문에 "이 `new` 를 어디서 해야 하는가" 를 거의 설명하지 않음.

현대 아키텍처에서는 이 지점이 명확함.

```
Composition Root (main / DI Container 설정)
        ↓ new ConcreteXxx(...)
Application / Domain Layer
        ↓ (인터페이스만 의존)
Concrete 구현을 모르는 코드
```

즉 GoF 패턴이 숨기는 것은 "구현체를 아는 사람" 이 아니라 "구현체를 아는 위치의 개수" 임. [DIP(Dependency Inversion Principle)](../../../solid/DIP(Dependency%20Inversion%20Principle).md) 도 같은 맥락 — 고수준 모듈이 저수준 모듈을 몰라도 된다는 것이지, 아무도 몰라도 된다는 뜻이 아님.

## Android 예시 (Hilt)

```kotlin
// Domain/Application: 구현을 모름
class CheckoutViewModel @Inject constructor(
    private val strategy: PaymentStrategy
) : ViewModel()

// Composition Root: 여기만 구현을 앎
@Module
@InstallIn(SingletonComponent::class)
object PaymentModule {
    @Provides
    fun providePaymentStrategy(
        samsung: SamsungBillingStrategy,
        google: GoogleBillingStrategy
    ): PaymentStrategy =
        if (Build.MANUFACTURER == "Samsung") samsung else google
}
```

Hilt 를 쓰지 않는 수동 DI 라면, `Application` 클래스나 `AppContainer` 가 그 역할을 대신함. 어느 경우든 "구현체를 아는 코드는 딱 한 곳" 이라는 원칙은 동일함.

## Spring 예시

```java
// Application: 구현을 모름
@Service
class CheckoutService {
    private final PaymentStrategy strategy;
}

// Composition Root: Spring Context / @Configuration
@Configuration
class PaymentConfig {
    @Bean
    PaymentStrategy paymentStrategy(PaypalStrategy paypal, StripeStrategy stripe,
                                     @Value("${payment.provider}") String provider) {
        return provider.equals("paypal") ? paypal : stripe;
    }
}
```

## GoF 패턴이 Composition Root/DI 시대에 재배치되는 방식

| 그룹 | 패턴 | 설명 |
| :--- | :--- | :--- |
| 1. 언어 기능이 흡수 | [Builder Pattern](../../creational/Builder%20Pattern.md), [Iterator Pattern](../../behavioral/Iterator%20Pattern.md), [Prototype Pattern](../../creational/Prototype%20Pattern.md) | Named argument, `for-in`, 언어 차원의 복사(`copy()`, `data class`) 로 상당 부분 대체됨. DI 와 무관. |
| 2. DI Container/Framework 가 흡수 | [Factory Method Pattern](../../creational/Factory%20Method%20Pattern.md), [Abstract Factory Pattern](../../creational/Abstract%20Factory%20Pattern.md), [Observer Pattern](../../behavioral/Observer%20Pattern.md), [Singleton Pattern](../../creational/Singleton%20Pattern.md) | 패턴이 사라진 게 아니라, Container(`BeanFactory`, Hilt `Component`) 가 내부적으로 그 패턴을 구현하고 있음. |
| 3. 여전히 설계의 핵심 | [Strategy Pattern](../../behavioral/Strategy%20Pattern.md), [Template Method Pattern](../../behavioral/Template%20Method%20Pattern.md), [Command Pattern](../../behavioral/Command%20Pattern.md), [Adapter Pattern](../../structural/Adapter%20Pattern.md), [Decorator Pattern](../../structural/Decorator%20Pattern.md), [Composite Pattern](../../structural/Composite%20Pattern.md), [Facade Pattern](../../structural/Facade%20Pattern.md), [Bridge Pattern](../../structural/Bridge%20Pattern.md), [Proxy Pattern](../../structural/Proxy%20Pattern.md), [Memento Pattern](../../behavioral/Memento%20Pattern.md), [State Pattern](../../behavioral/State%20Pattern.md), [Chain of Responsibility Pattern](../../behavioral/Chain%20of%20Responsibility%20Pattern.md), [Mediator Pattern](../../behavioral/Mediator%20Pattern.md), [Visitor Pattern](../../behavioral/Visitor%20Pattern.md), [Interpreter Pattern](../../behavioral/Interpreter%20Pattern.md), [Flyweight Pattern](../../structural/Flyweight%20Pattern.md) | 객체 관계/생명주기를 설계하는 패턴이라 언어 기능만으로는 대체 불가. 다만 "작고 순수한 행동" 은 함수/람다로 표현 가능. |

## 결론

> GoF 패턴의 상당수는 "사라진 것" 이 아니라, 언어와 프레임워크가 그 구현을 흡수했거나, 적용 범위가 더 좁고 명확해진 것이다.

각 개별 패턴 문서의 **Modern Applicability (DI/Composition Root)** 절에서는 이 문서의 분류를 기준으로, 해당 패턴이 Android(Hilt)/Spring 에서 구체적으로 어떻게 배선되는지를 다룸.

## Relationship with other patterns

### [DIP(Dependency Inversion Principle)](../../../solid/DIP(Dependency%20Inversion%20Principle).md)

- DIP 는 "고수준 모듈이 저수준 모듈에 의존하지 않는다" 는 원칙 수준의 이야기이고, Composition Root 는 그 원칙을 실제 코드에서 "어디서 조립할 것인가" 로 구체화한 것.

### [Factory Method Pattern](../../creational/Factory%20Method%20Pattern.md), [Abstract Factory Pattern](../../creational/Abstract%20Factory%20Pattern.md)

- DI Container(`ApplicationContext`, Hilt `Component`) 자체가 거대한 Factory 이자 Composition Root 의 실제 구현체.
