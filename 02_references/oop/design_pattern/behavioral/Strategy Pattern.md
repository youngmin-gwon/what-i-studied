---
title: Strategy Pattern
tags: [behavioral-pattern, design-pattern, gof, oop]
aliases: []
date modified: 2026-07-23 10:21:36 +09:00
date created: 2024-12-12 15:48:00 +09:00
---

## Description

결제 로직을 만든다고 해보자. 처음엔 신용카드만 지원하면 됐는데, PayPal, ApplePay 가 하나씩 추가되면서 `CheckoutService` 안에 `if (type == "card") ... else if (type == "paypal") ...` 같은 분기가 계속 늘어남. 결제 수단이 하나 더 생길 때마다 이미 잘 동작하던 `CheckoutService` 코드를 매번 다시 열어서 고쳐야 하는 게 문제.

**Strategy Pattern** 은 이렇게 "같은 목적을 이루는 여러 방법(알고리즘)" 을 각각 독립된 클래스로 떼어내고, 공통 인터페이스로 묶어서 실행 중에(Runtime) 서로 교체할 수 있게 만드는 행위(Behavioral) 패턴. 위 예시라면 `CreditCardPayment`, `PaypalPayment`, `ApplePayPayment` 를 각각 클래스로 만들고 `PaymentStrategy` 인터페이스로 묶으면, `CheckoutService` 는 셋 중 무엇이 오는지 몰라도 결제를 처리할 수 있음.

![Untitled](../../../../../_assets/oop/Untitled%2014.png)

![Untitled](../../../../../_assets/oop/Untitled%2015.png)

- **핵심**: 여러 알고리즘(전략)을 각각 별도의 클래스로 캡슐화하고, 공통 인터페이스로 교체 가능하게 만듦.
- **목적**:
  1. 알고리즘을 사용하는 코드와 알고리즘의 실제 구현을 분리.
  2. 런타임에 로직을 바꾸거나, if-else 분기가 계속 늘어나는 걸 막고 싶을 때 사용.
  3. 새로운 전략을 추가해도 기존 코드는 건드리지 않도록 하여 **[OCP(Open Closed Principle)](../../solid/OCP(Open%20Closed%20Principle).md)** 를 준수.

## Examples

- **정렬(Sorting)**: 데이터가 적을 땐 `BubbleSort`, 많을 땐 `QuickSort` 를 쓰고 싶다면, 정렬기 코드를 고치는 대신 상황에 맞는 Strategy 를 골라서 넣어주기만 하면 됨.
- **결제(Payment)**: `CreditCard`, `PayPal`, `ApplePay` 를 Strategy 로 만들면, 사용자가 고른 수단에 따라 `CheckoutService` 코드 수정 없이 결제 로직만 교체됨.
- **게임(RPG)**: 무기를 바꾸면 공격 방식도 바뀌어야 함. `SwordAttack`, `BowAttack` 을 Strategy 로 구현하면 캐릭터 클래스를 건드리지 않고도 무기 교체만으로 공격 로직이 즉시 바뀜.

![Untitled](../../../../../_assets/oop/Untitled%2016.png)

## Structure

Context 는 Strategy 인터페이스만 들고 있고, 그 안에 어떤 알고리즘이 들어있는지는 모름. 실제로 어떤 Concrete Strategy 를 쓸지는 Client 가 정해서 Context 에 넘겨줌.

- **Strategy**: Concrete Strategy 들이 공통으로 구현하는 interface. Context 는 이 인터페이스만 앎.
- **Concrete Strategy**: Strategy 인터페이스에 맞춰 실제 알고리즘을 구현한 클래스들 (`PaypalPayment`, `ApplePayPayment` 등).
- **Context**: Strategy 객체를 필드로 들고 있고, 실제 알고리즘 실행을 위임함. 어떤 알고리즘이 들어올지는 신경 쓰지 않기 때문에 런타임에 자유롭게 교체 가능.
- **Client**: 상황에 맞는 Concrete Strategy 를 골라서 Context 에 주입하는 쪽. (실무에서는 이 역할을 [Composition Root](../general/patterns/Composition%20Root.md) 가 담당하는 경우가 많음.)

## Adaptability

다음 상황에서 특히 유용함.

- 같은 일을 하는 방식이 여러 개 있고, 런타임 중에 방식을 전환하고 싶은 경우.
- 동작 하나만 다르고 나머지는 비슷한 클래스가 여러 개 생기고 있는 경우.
- 알고리즘의 구현 세부사항을 클래스의 핵심 로직에서 분리하고 싶은 경우.
- 알고리즘을 고르는 조건문(if-else, switch) 이 점점 커지고 있는 경우.

## Pros

- 알고리즘마다 별도 클래스로 분리하고 공통 인터페이스로 묶기 때문에 **compile-time flexibility** 를 얻음.
  - 게다가 런타임 중에도 전략을 자유롭게 교체할 수 있음.
- 각 알고리즘의 코드, 내부 데이터, 의존성을 서로 격리할 수 있음.
- 새 Concrete Strategy 를 기존 코드 수정 없이 추가할 수 있음 ⇒ [OCP(Open Closed Principle)](../../solid/OCP(Open%20Closed%20Principle).md).

## Cons

- Context 를 사용하는 쪽에서 각 Concrete Strategy 의 차이를 알고 적절히 선택해야 함.
- 알고리즘이 거의 바뀌지 않는다면, 굳이 Strategy 패턴으로 나눌 이유가 없음.
- 대부분의 언어가 함수를 값처럼 다룰 수 있기 때문에(함수 타입, 람다), 아주 작은 전략이라면 클래스 대신 함수 하나로 충분한 경우가 많음.

## Relationship with other patterns

### [Bridge Pattern](structural/Bridge%20Pattern.md), [State Pattern](State%20Pattern.md), (일부분 [Adapter Pattern](structural/Adapter%20Pattern.md))

- 구조가 비슷함 (다른 객체에 실제 작업을 위임하는 구조).
- 하지만 각각 풀려는 문제가 다름.
- 패턴은 특정 방식으로 코드를 구조화하기 위한 단순한 레시피가 아님.
	- **해결해야 하는 문제를 다른 개발자와 소통하기 위한 방법으로 패턴을 사용해야 함.**

### [Decorator Pattern](structural/Decorator%20Pattern.md)

- Decorator 는 객체의 **겉** 을 바꾸는 역할, Strategy 는 객체의 **속** 을 바꾸는 역할.

### [Command Pattern](Command%20Pattern.md)

- 둘 다 객체를 파라미터로 갖기 때문에 비슷해 보일 수 있지만, 의도가 다름.
	- **Command**: 연산 자체를 객체로 바꾸려는 의도 ⇒ 실행을 연기하거나, 대기열에 쌓거나, 실행 기록을 저장하거나, 원격으로 전송하는 등의 작업이 가능해짐.
	- **Strategy**: 같은 일을 하는 여러 알고리즘을 자유롭게 교체하려는 의도.

### [Template Method Pattern](Template%20Method%20Pattern.md)

- **Template Method** 는 상속 기반. 알고리즘 중 수정이 필요한 일부분만 서브클래스에서 확장.
- **Strategy** 는 구성(Composition) 기반. 아예 다르게 동작하는 전략 객체를 갈아 끼워서 행위를 바꿈.
- 그래서 Template Method 는 class level, Strategy 는 object level 에서 동작함.
	- Template Method 는 static 이라 compile-time-safe, Strategy 는 런타임에 바뀌므로 runtime-safe.
- Template Method 는 공통 로직을 서브클래스끼리 공유하지만, Strategy 는 각 구현이 완전히 독립적이라 공유되는 코드가 없음.

### [State Pattern](State%20Pattern.md)

- State 는 Strategy 를 확장한 패턴으로 볼 수 있음.
	- 둘 다 구성(Composition) 기반이고, helper 객체가 Context 의 동작을 바꿔줌.
- **Strategy** 는 상속을 대체하려는 목적, **State** 는 조건문을 대체하려는 목적.

## Modern Applicability (DI/Composition Root)

[Composition Root](../general/patterns/Composition%20Root.md) 관점에서 보면 Strategy 는 **3그룹: 여전히 설계의 핵심** 에 속함. 단, 크기에 따라 갈림.

- 정렬 알고리즘처럼 순수한 전략 → 함수/람다로 충분.
- Payment, Auth, Retry 처럼 로깅·DI·생명주기가 얽힌 전략 → "알고리즘" 이 아니라 사실상 **서비스** 라 `interface` + 클래스가 자연스러움.

**"그래도 결국 누군가는 concrete 를 알아야 하지 않나?"** GoF 다이어그램은 여기서 멈춰서 오해를 줌. Strategy 가 없애는 건 "아는 사람" 이 아니라 **"아는 위치의 개수"**. `CheckoutViewModel` 은 Paypal 인지 모르고, [Composition Root](../general/patterns/Composition%20Root.md) 한 곳만 알면 됨.

**Android 예시 (Metro)** — 스토어별로 결제 전략이 갈리는 경우.

```kotlin
interface PaymentStrategy {
    fun pay(amount: Int)
}

@Inject class SamsungBillingStrategy : PaymentStrategy { /* ... */ }
@Inject class GoogleBillingStrategy : PaymentStrategy { /* ... */ }

@Inject
class CheckoutViewModel(private val strategy: PaymentStrategy) // 구체 구현을 모름

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
```

`AppGraph` 가 Composition Root. 스토어가 늘어나도(Huawei 등) `CheckoutViewModel` 은 수정하지 않음 ⇒ [OCP(Open Closed Principle)](../../solid/OCP(Open%20Closed%20Principle).md) 유지. Strategy 가 사라진 게 아니라 "누가 결정하는가" 가 `AppGraph` 라는 명시적 지점으로 이동했을 뿐.
