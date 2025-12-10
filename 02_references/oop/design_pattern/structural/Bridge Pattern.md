---
title: Bridge Pattern
tags: [design-pattern, gof, oop, structural-pattern]
aliases: []
date modified: 2025-12-09 17:03:12 +09:00
date created: 2024-12-12 15:52:30 +09:00
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%2046.png)

![Untitled](../../../../../_assets/oop/Untitled%2047.png)

- 구현부에 추상적인 부분을 분리하여 독립적으로 다양성을 가질 수 있도록 함.
  - 추상과 구현 사이에 다리를 연결하여 각각 따로 발전시킨 두 가지를 연결해준다.
  - 추상에 구현이 아닌 또 다른 추상을 사용하는 방법을 사용한다.
- 여러 구현체를 만들기 위한 추상 방법은 주로 상속 (inheritance) 를 사용하는 것.
  - 상속은 잘 사용하면 좋지만 구현부가 추상적 개념에 강하게 종속됨.
  - 구현을 compile-time 에 제한하기 때문에 run-time 에 바꾸는 것이 불가능하다.
  - 유연하지 못하게 만든다.
  - bridge 패턴은 run-time 에 구현체를 교환할 수 있게 만든다.

## Case

### Situation

- 이식성이 있는 Window 를 추상적 개념으로 보고 이를 UI 툴킷을 써서 구현하는 예.
- 다음을 참고해서 이해하자.
  - 추상은 특정 엔티티를 위한 상위 계층.
  - 이 계층은 실제로는 아무런 일을 하지 않고, 구현에게 일을 할당하는 역할만 함.
  - OS 와 GUI 를 생각하면 쉬움.
    - GUI 는 그저 상위 계층으로 사용자의 명령만 받아서 platform 으로 전달하는 역할만 함.
    - OS 와 GUI 는 각기 따로따로 발전할 수 있음.

## Structure

![Untitled](../../../../../_assets/oop/Untitled%2048.png)

1. ***Abstraction***
    - ***Refined abstraction***을 위한 interface 정의.
    - ***Implementation*** type 객체를 참고하는 역할.
2. ***Refined abstraction***
    - ***Abstraction*** interface 를 구현.
    - 각각 다른 조작 논리를 제공.
3. ***Implementation***
    - ***Concrete Implementation***을 위한 interface 정의.
    - ***Abstraction***은 오직 이곳에 정의된 method 를 통해서만 ***Implementation*** 객체와 소통할 수 있음.
4. ***Concrete Implementation***
    - ***Implementation*** interface 를 구현.
    - platform-specific 한 코드를 포함하고 있음.

## Adaptability

- monolithic 한 class 를 여러 가지 기능으로 나누고 싶을 때 사용해야 함.
  - 작아진 클래스로 기존 코드가 망가지는 것을 방지할 수 있음.
  - 코드 유지를 간단하게 만들어줌.
  - 좋은 예시: database 와 file system 처럼 persistence layer 에 여러 가지 접근 방식을 사용하려는 경우.
- 추상과 구현 모두 subclass 로 확장이 가능해야 할 때 사용해야 함.
- run-time 에 구현을 변경해야 하는 경우 유용함.

## Pros

- 플랫폼 독립적인 클래스 및 앱을 만들 수 있음.
- 클라이언트 코드는 높은 수준의 추상화와 함께 작동. 플랫폼 세부정보에게 정보를 노출하지 않음.
- 각각 새로운 Abstraction, Implementation 을 도입할 수 있음 ⇒ **[OCP(Open Closed Principle)](../../solid/OCP(Open%20Closed%20Principle).md)**.
- Abstraction 에서는 상위 레벨 로직에만 집중하면 되고, Implementation 에서는 플랫폼 세부사항에 집중하면 된다 ⇒ **[SRP(Single Responsibility Principle)](../../solid/SRP(Single%20Responsibility%20Principle).md)**.

## Cons

- 응집력이 높은 클래스에 패턴을 적용하면 코드를 더 복잡하게 만들 수 있음.

## Relationship with other patterns

### [Adapter Pattern](Adapter%20Pattern.md)

- Bridge 는 일반적으로 사전에 설계되어 서로 독립적으로 응용 프로그램의 일부를 개발할 수 있음.
- Adapter 는 일반적으로 기존 앱과 함께 사용되어 호환되지 않는 일부 클래스가 잘 작동하도록 함.

### [State Pattern](../behavioral/State%20Pattern.md), [Strategy Pattern](../behavioral/Strategy%20Pattern.md), (일부 [Adapter Pattern](Adapter%20Pattern.md))

- 모두 매우 비슷한 구조를 가지고 있으며, 하위 클래스에 작업을 할당하는 composition 을 기반으로 함.
- 하지만 모두 다른 문제를 해결하기 위한 방법임.

### [Abstract Factory Pattern](../creational/Abstract%20Factory%20Pattern.md)

- Bridge 패턴과 함께 사용할 수 있는 패턴.
  - Bridge 에서 정의한 일부 Abstractions 가 특정 Implementations 에서만 작동할 수 있을 때 유용함.
  - 이 경우 Abstract Factory 는 이러한 관계를 캡슐화하고 클라이언트 코드에서 복잡성을 숨길 수 있음.

### [Builder Pattern](../creational/Builder%20Pattern.md)

- Bridge 와 함께 조합하여 사용할 수 있음.
  - Director 클래스는 추상화의 역할을 하는 반면 다른 Builder 는 구현의 역할을 하게 하는 방식.
