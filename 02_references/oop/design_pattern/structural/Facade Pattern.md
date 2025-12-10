---
title: Facade Pattern
tags: [design-pattern, gof, oop, structural-pattern]
aliases: []
date modified: 2025-12-09 17:30:06 +09:00
date created: 2024-12-12 15:52:57 +09:00
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%2020.png)

![Untitled](../../../../../_assets/oop/Untitled%2021.png)

- 복잡한 API 나 하위시스템의 함수 묶음을 모은 간단한 인터페이스 제공.
- 클라이언트가 하위 시스템과 소통하기 위해서는 퍼사드만 이용하면 된다.
- 클라이언트와 하위 시스템 간의 의존성을 줄여줌.

![Untitled](../../../../../_assets/oop/Untitled%2022.png)

- **Facade**
  - 어떤 하위시스템 클래스가 요청에 연관되어 있는지 알고, 요청을 하위시스템에 할당하는 역할을 함.
- **Additional Facade**
  - 메인 퍼사드에서 특정한 함수를 추출하고 싶을 때 사용.
- **Subsystem**
  - 특정 카테고리의 기능 구현.
  - 퍼사드에 대한 참조를 전혀 가지고 있지 않음.
- **Client**
  - 하위 시스템 함수를 바로 부르지 않고 퍼사드를 이용해서 기능을 수행함.

## When

1. 복잡한 시스템 연관관계를 간단하게 만든 인터페이스를 제공하고 싶을 때 사용.
2. 하위 시스템을 layer 로 구성하고 싶을 때 사용.
3. 모듈 간의 coupling 을 줄이기 위해서 사용.
4. 매우 큰 기존 API 중 일부만 사용하고 싶을 때 사용.

## Pros

- 복잡한 하위 시스템으로부터 코드를 분리할 수 있음.

## Cons

- 앱의 모든 클래스에 결합된 "god object" 가 될 위험이 있음.

## Relationship with other patterns

### [Adapter Pattern](Adapter%20Pattern.md)

- Facade 는 기존 객체에 새로운 인터페이스를 정의함.
- Adapter 는 기존 존재하는 인터페이스를 유용하게 만들려고 함.

### [Abstract Factory Pattern](../creational/Abstract%20Factory%20Pattern.md)

- Abstract Factory 는 클라이언트 코드에서 서브시스템 객체가 생성되는 방식을 숨기고 싶을 때 Facade 의 대안으로 사용할 수 있음.

### [Flyweight Pattern](Flyweight%20Pattern.md)

- Flyweight 는 조그마한 많은 객체들은 만드는 방법을 보여줌.
- Facade 는 전체 시스템을 상징하는 단일 객체를 만드는 방법을 보여줌.

### [Mediator Pattern](../behavioral/Mediator%20Pattern.md)

- 둘 다 밀접하게 연결된 많은 클래스 간의 협업을 조직하려고 함.
- Facade 는 Subsystem 의 단순화된 인터페이스를 제공하지만, 새로운 기능을 추가하진 않음.
  - Subsystem 은 Facade 의 존재를 모름.
  - Subsystem 의 객체들은 직접적으로 소통할 수 있음.
- Mediator 는 system 구성 요소 간의 소통을 중재함.
  - 구성 요소들은 Mediator 만 알고, 직접 소통하지 않음.

### [Singleton Pattern](../creational/Singleton%20Pattern.md)

- 단일 Facade 객체로 충분하기 때문에 Facade 클래스는 종종 Singleton 으로 변환될 수 있음.

### [Proxy Pattern](Proxy%20Pattern.md)

- 둘 다 복잡한 엔티티를 버퍼링하고 자체적으로 초기화함.
- Proxy 는 서비스 객체와 동일한 인터페이스를 가지고 있어 상호 교환이 가능함.
