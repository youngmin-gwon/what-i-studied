---
title: Adapter Pattern
tags: [design-pattern, gof, oop, structural-pattern]
aliases: []
date modified: 2025-12-09 17:36:01 +09:00
date created: 2024-12-12 14:59:28 +09:00
---

## Description

![Untitled](../../../../../_assets/oop/adapter_overview.png)

![Untitled](../../../../../_assets/oop/adapter_before.png)

![Untitled](../../../../../_assets/oop/adapter_after.png)

다른 인터페이스 클라이언트가 기대하는대로 인터페이스를 변환함

함께 할 수 없는 클래스들을 함께 일할 수 있게 만들어줌

가장 일반적이고, 가장 유용하게 사용할 수 있는 디자인 패턴 중 하나

- eg. 형태가 맞지 않은 3rd party library 를 Adapter 를 생성하여 사용할 수 있게 만들어 줌

외부 데이터 저장소 혹은 방식이 다를 때 interface 에 맞는 각각의 adapter 를 만들어 동일한 형식의 데이터로 만들어 줄 수 있음

Adapter 로 감싸고, interface 만 노출하여 기존의 코드를 재사용 가능하게 만들어 줌

code abstraction 을 하므로 domain layer 의 unit test 를 보다 쉽게 만들어 줌

    - 아침에 커피를 마시기 위해 통상적으로 해야할 일

        - (커피 구입과정 제외) 그라인딩 → 브루잉 → 커피 완성

    - 커피 머신을 이용하는 경우

        - 커피 머신 가동 → 커피 완성

    - 위의 과정이 abstraction ⇒ 커피 머신 내부에서 어떻게 동작하는지는 알 필요 없이 커피 머신만 가동시키면 커피를 뽑아낼 수 있음

## Structure

![Untitled](adapter_structure.png)

(같은 아이디어를 공유하지만) 크게 `1. object`, `2.class` adapter 구조로 나눌 수 있음

- Target or ITarget 은 Client 가 사용하는 interface 정의
- Client 는 Target 과 소통함
- Adapted 은 Adapter 를 연결하여 변환할 것 (ex. 3rd party library)
- Adapter 는 Adapted 의 interface 역할을 하여 Adapted 를 Target 과 이어줌

### Difference

- **class** 는 Adapted 로 부터 Target interface 로 전달하기 위해 **상속**을 이용 ⇒ Adapted 의 concrete operation 이 Target 의 구현으로 부터 바로 호출됨
  - 구현하고자 하는 언어가 multiple inheritance 를 지원해야 구현할 수 있음
- **object** 는 Adapted 로 부터 Target interface 로 전달하기 위해 **객체 구조**를 이용

Github 에 작성한 예시에서 object implementation 을 사용한 이유

- Dart 는 multiple inheritance 를 지원하지 않음
- object adapter 는 runtime 에 연결되기 때문에 더욱 유연하다 (=loosely-coupled) ⇒ [SOLID](../../../solid/SOLID.md) 원칙 중 [LSP(Liskov substitution principle)](../../../solid/LSP(Liskov%20substitution%20principle).md) 원칙에 부합함
  - class adapter 는 쉽게 override 만 하면 된다는 장점이 있음

![Untitled](../../../../../_assets/oop/adapter_impl.png)

## Adaptability

- 기존 클래스를 사용하고 싶지만 인터페이스가 나머지 코드와 호환되지 않을 때 사용
- 상위 클래스에 추가할 수 없는 몇 가지 공통 기능이 없는 여러 기존 하위 클래스를 재사용하려는 경우 패턴을 사용

## Pros

- [SRP(Single Responsibility Principle)](../../../solid/SRP(Single%20Responsibility%20Principle).md)
- [OCP(Open Closed Principle)](../../../solid/OCP(Open%20Closed%20Principle).md)

## Cons

- 새로운 인터페이스와 클래스를 추가해야하기 때문에 코드 복잡도 증가
  - 때로는 service 클래스를 쉽게 변경하는 것이 더 간단할 때도 있음

## Relationship with other patterns

### [Bridge Pattern](Bridge%20Pattern.md)

- 일반적으로 사전에 설계되어 서로 독립적으로 응용 프로그램의 일부를 개발할 수 있음
- 일반적으로 기존 앱과 함께 사용되어 호환되지 않는 일부 클래스가 잘 작동하도록 함

### [Decorator Pattern](Decorator%20Pattern.md)

- Adapter 는 기존 객체의 인터페이스를 변경하지만, Decorator 는 인터페이스를 변경하지 않고 기존 객체를 강화함
- Decorator 는 재귀적 구조를 가지지만, Adapter 는 불가능함

### [Proxy Pattern](Proxy%20Pattern.md)

- Adapter 는 감싼 객체에 다른 인터페이스를 제공함
- Proxy 는 감싼 객체에 같은 인터페이스를 제공함
- Decorator 는 감싼 객체에 강화된 인터페이스를 제공함

### [Facade Pattern](Facade%20Pattern.md)

- Facade 는 기존 객체에 새로운 인터페이스를 정의함
- Adapter 는 기존 존재하는 인터페이스를 유용하게 만들려고 함

## Difference with Bridge, State, Strategy, Adapter Pattern

- 어떤 면에서는 매우 비슷한 구조를 가지고 있음
  - subclass 에 작업을 맡긴다는 구조가 비슷함
- 사용 목적이 다름
