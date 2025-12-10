---
title: Mediator Pattern
tags: [behavioral-pattern, design-pattern, gof, oop]
aliases: []
date modified: 2025-12-10 14:26:32 +09:00
date created: 2024-12-12 15:48:17 +09:00
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%2060.png)

![Untitled](../../../../../_assets/oop/Untitled%2061.png)

- **Intermediary/Controller** 라고 불리기도 함.
- 상호작용 로직을 객체로부터 분리하고, Mediator 라는 컨트롤러에 이동시켜, 상호 교류하는 객체들간의 의존성을 줄여주는 패턴.
- 객체 묶음이 어떻게 상호작용 하는지를 묶은 객체를 정의.
- 객체끼리 서로 선언되는 것을 막아**loose coupling** 을 장려함.
- 상호작용을 다양하게 만들어 줌.
-**colleagues**: 서로 상호작용하는 객체들.
  - colleagues 는 서로에 대한 정보가 없고, 오직 mediator 만 알고 있음 ⇒ colleagues 들은 loosely coupled.
- 객체끼리 상호작용 하는 것을 간단화, 추상화 함.
  - 기존의 N:M 의 객체 간 상호작용을, Mediator 를 통해 1:N 의 상호작용으로 만들어줌 ⇒ 이해하고 유지하기 쉬움.
  - colleagues 들은 communication act 는 알아야 하지만, 디테일은 전혀 알 필요가 없음 ⇒ colleagues 들을 바꾸지 않고 Mediator 를 추가하는 것이 가능해짐.

## Structure

![Untitled](../../../../../_assets/oop/Untitled%2062.png)

1. **Mediator**- 컴포넌트들과 상호작용하기 위한 인터페이스 정의.
2.**Concrete Mediator**
   - 컴포넌트를 정의하여 컴포넌트간의 관계를 묶음.
3. (Optional) **Abstract Component or Component Interface**- 유사하게 상호작용하는 컴포넌트가 상속할 수 있는 클래스.
4.**Concrete component or Colleague**- Mediator 가 참고하는 요소.
   - 각각의 colleague 는 다른 colleague 와 소통하기 위해 Mediator 와 소통함.
   - Component 들은 서로를 알고 있어서는 안됨 ⇒ 무조건 Mediator 를 거쳐서 소통해야 함.

## Adaptability

- 다른 클래스와 밀접하게 coupled 되어 있기 때문에 일부 클래스를 변경하기 어려울 때 사용.
- 컴포넌트가 다른 컴포넌트에 너무 의존적이어서 다른 프로그램에서 컴포넌트를 재사용할 수 없을 때 사용.
- 다양한 컨텍스트에서 몇 가지 기본 동작을 재사용하기 위해 수많은 구성 요소 하위 클래스를 만들어야 한 경우 대신 사용.
- 구동 중에 컴포넌트를 추가할 필요가 있을 때 사용.
    💣 모든 communication logic 을 추가하면 God Object 가 될 가능성이 존재함.
- Mediator 는 오직 communication 만 책임진다는 것을 유의하고 사용해야 함.
- 연산, 데이터 변환 등 관계없는 기능이 Mediator 에 없도록 잘 작성해야 함.

## Pros

- 여러 개의 컴포넌트 간 상호작용을 하나로 묶을 수 있다 ⇒**[SRP(Single Responsibility Principle)](../../solid/SRP(Single%20Responsibility%20Principle).md)**.
- 기존 코드 수정 없이 새로운 Mediator 를 추가할 수 있음 ⇒**[OCP(Open Closed Principle)](../../solid/OCP(Open%20Closed%20Principle).md)**.
- 각각의 컴포넌트를 쉽게 재사용할 수 있다.

## Cons

- Mediator 가 God Object 가 될 수도 있음.

## Relationship with other patterns

### [Chain of Responsibility Pattern](Chain%20of%20Responsibility%20Pattern.md), [Command Pattern](Command%20Pattern.md), [Observer Pattern](Observer%20Pattern.md)

- 요청의 sender 와 receiver 을 연결하는 다양한 방법 제시.
  - **CoR**: 잠재적 수신자 중 하나가 처리할 때까지 잠재적 수신자의 동적 사슬을 따라 순차적으로 요청을 전달.
  -**Command**: 발신자와 수신자 간의 단방향 연결을 설정.
  -**Mediator**: 송신자와 수신자 간의 직접 연결을 제거하여 중재자 개체를 통해 간접적으로 통신하도록 함.
  -**Observer** : 수신자가 수신 요청을 동적으로 구독 및 구독 취소할 수 있음.

### [Facade Pattern](../structural/Facade%20Pattern.md)

- 밀접하게 coupled 된 클래스 사이의 상호작용을 정리해준다는 비슷한 역할을 함.
- **Facade**: 간단한 subsystem 인터페이스를 제공하지만, 새로운 기능을 추가하진 않음. subsystem 은 facade 를 모르고 subsystem 객체들은 서로서로 소통함.
-**Mediator**: system 의 컴포넌트간의 상호작용을 중재함. 각각의 컴포넌트는 mediator 만 알고 다른 컴포넌트는 아예 모름.

### [Observer Pattern](Observer%20Pattern.md)

- 차이를 구별하기 어려움.
- 하나를 구현해서 쓰기도 하나, 때로는 두 가지를 동시에 적용하기도 함.
  - Mediator 의 목표는 시스템 구성 요소 집합 간의 상호 종속성 제거 ⇒ 대신 구성 요소는 단일 중재자 개체에 종속됨.
  - Observer 의 목표는 일부 개체가 다른 개체의 종속 역할을 하는 개체 간에 동적 단방향 연결을 설정.
  - 두 가지를 합쳐서 **Observer 에 의존하는 Mediator** 객체를 만들어 내는 것이 대중적임.
    - Mediator 는 Publisher 역할을 하고 Component 는 Mediator 의 이벤트를 구독 및 취소하는 Observer 역할을 함.
    - 이러한 방식으로 Mediator 를 구현하면 Observer 와 매우 유사하게 보일 수 있음.
  - 혼란스러우면 다른 방법으로 Mediator 패턴을 구현할 수 있음.
    - 예를 들어 모든 구성 요소를 동일한 Mediator 개체에 영구적으로 연결할 수 있습니다. 이 구현은 Observer 와 유사하지 않지만 여전히 Mediator 패턴의 인스턴스임.
    - 이제 모든 구성 요소가 Publisher 가 되어 서로 간의 동적 연결을 허용하는 프로그램을 상상해 보기.
      - 중앙 집중식 Mediator 개체는 없고 분산된 Publisher 집합만 있을 것임.
