---
title: Observer Pattern
tags: [behavioral-pattern, design-pattern, gof, oop]
aliases: []
date modified: 2025-12-09 17:24:30 +09:00
date created: 2024-12-12 15:47:43 +09:00
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%2063.png)

- **Dependents/Publish-Subscribe** 라고 불리기도 함.
- Reactive Programming 아이디어가 어떻게 차용되었는지 확인할 수 있는 패턴.
- 객체 간 1:N 의존성을 정의하여, 객체의 상태가 바뀌었을 때 모든 구독 객체들은 알림을 받을 수 있게 됨.
- 이 디자인 패턴이 생기게 된 배경
  - 한 객체의 변화가 다른 것들의 변화를 일으키는 tightly coupled 객체들 때문에 생기게 됨.
- 패턴 안의 객체들은 두 가지 역할을 수행함
  1. **Subject ⇒ Publisher**
      - 알림을 배포하는 주체.
      - 알림을 구독, 취소할 수 있게 하는 방법도 제공함.
  2. **Observer (= Subscriber)**
      - 알림을 받아 변화하는 객체.
- observers 가 누구인지 몰라도 변하게 하는 것이 가능함 ⇒ **loosely coupled** 하게 만듬.

## Consideration

- 옵저버는 상태를 갖지 않아도 된다.
- Notify 를 누가 호출해야 할까?
- Update 메소드의 인자.
- Observer 의 행위가 Subject 에 영향을 주는 경우.

## Structure

![Untitled](../../../../../_assets/oop/Untitled%2064.png)

1. ***Publisher(Subject)***
    - Subscriber 를 붙이고 떼는 interface 제공.
    - Observers 목록을 보관함.
2. (Optional) ***ConcretePublishers***
    - 관심 상태를 저장하고, 상태 변했을 때 Observers 에 알림 전송.
3. ***Subscriber(Observer)***
    - 알림 (notification) 인터페이스 선언.
4. ***ConcreteSubscribers***
    - 알림 (notification) 인터페이스 적용.
    - subject 의 상태와 일관되게 유지할 수 있도록 처리.

## [Observer Pattern](Observer%20Pattern.md) vs [Mediator Pattern](Mediator%20Pattern.md)

- Mediator 의 가장 큰 목적은 N:M 의 관계를 1:N 으로 변환하는 것. Observer 는 몇몇의 객체는 다른 객체에 종속체 처럼 행동하며, 객체 간 동적인 one way 연결을 허용.

## Adaptability

- 한 객체의 변화가 다른 객체들의 변화를 만들어야 할 때 사용.
- 오직 정해진 시간 동안만 어떠한 객체들의 변화를 관찰해야 될 때 사용.

## Pros

- 기존 코드 변경 없이, 새로운 Subscriber 를 추가할 수 있음 ⇒ **[OCP(Open Closed Principle)](../../../solid/OCP(Open%20Closed%20Principle).md)**.
- 객체 간의 관계를 runtime 에 만들 수 있다.

## Cons

- Subscriber 가 무작위 순서로 전달 받게 된다.

## Relationship with other patterns

### [Chain of Responsibility Pattern](Chain%20of%20Responsibility%20Pattern.md), [Command Pattern](Command%20Pattern.md)

- 요청의 sender 와 receiver 을 연결하는 다양한 방법 제시.
  - **CoR** : 잠재적 수신자 중 하나가 처리할 때까지 잠재적 수신자의 동적 사슬을 따라 순차적으로 요청을 전달.
  - **Command** : 발신자와 수신자 간의 단방향 연결을 설정.
  - **Mediator** : 송신자와 수신자 간의 직접 연결을 제거하여 중재자 개체를 통해 간접적으로 통신하도록 함.
  - **Observer** : 수신자가 수신 요청을 동적으로 구독 및 구독 취소할 수 있음.

### [Mediator Pattern](Mediator%20Pattern.md)

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
