---
title: Visitor Pattern
tags: [behavioral-pattern, design-pattern, gof, oop]
aliases: []
date modified: 2025-12-09 17:07:10 +09:00
date created: 2024-12-12 15:48:10 +09:00
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%2058.png)

- 알고리즘을 알고리즘을 실행하는 객체로 부터 분리하는 패턴
- 개체 구조의 요소에 대해 수행할 작업을 나타냄
- 작동하는 요소의 클래스를 변경하지 않고 새 작업을 정의할 수 있음
- tree 나 collection 의 복잡한 데이터 구조가 있고, 각 데이터 요소 클래스를 변경하지 않고 기능을 변경하고 싶을 때 사용
- 핵심 아이디어
  - 각각의 특정 복합 객체 클래스에 대해 double-dispatch 작업을 정의하는 것
  - Visitor 패턴의 맥락에서 이를 accept 라고 함
  - client 가 개체 구조를 탐색할 때, 각 요소의 accept 메서드가 호출되어 요청을 특정 방문자 개체에 위임하고 이 개체는 매개변수로 메서드에 전달. 그런 다음, Visitor 개체의 특정 메서드가 호출되어 실제 요청을 수행

## Structure

![Untitled](../../../../../_assets/oop/Untitled%2059.png)

1. ***Visitor***
    - ConcreteElement 를 파라미터로 가질 수 있는 일련의 방문 메소드를 선언하는 인터페이스
    - Overloading 을 취하는 언어라면, 같은 이름을 가질 수도 있지만 Element 타입은 반드시 달라야 함
2. ***ConcreteVisitor***
    - 다른 ConcreteElement 클래스에 맞게 조정된 동일한 동작의 여러 버전을 구현
3. ***Element***
    - Visitor 를 "accept" 메소드 선언하는 인터페이스
    - 선언된 메소드에는 Visitor Interface 유형으로 선언된 매개변수가 하나 있어야 함
4. ***ConcreteElement***
    - accept 메소드 구현
    - 현재 클래스에 해당하는 적절한 Visitor 메서드로 호출을 리디렉션하는 것이 목적
    - 기본 Element 클래스가 이 메서드를 구현하더라도 모든 하위 클래스는 여전히 자체 클래스에서 이 메서드를 재정의하고 Visitor 개체에서 적절한 메서드를 호출해야 함
5. ***Client***
    - 복잡한 컬렉션이나 트리 객체를 포함
    - 일반적으로 클라이언트는 추상 인터페이스를 통해 해당 컬렉션의 개체와 작업하기 때문에 모든 구체적인 요소 클래스를 인식하지 못함

## Adaptability

- 복잡한 객체 구조의 모든 요소에 대한 작업을 실행하고 구체적인 클래스의 인터페이스를 변경하고 싶지 않을 때 사용
- 보조 동작의 비즈니스 논리를 정리할 때 사용
- 클래스 계층의 일부 클래스에서만 의미가 있고 다른 클래스에서는 의미가 없을 때 패턴을 사용
- 객체구조가 거의 바뀌지 않는 경우에만 적용하는 것을 권장

## Pros

- 같은 동작에 대한 여러버전을 하나의 클래스로 이동 시킬 수 있음 ⇒ Single Responsibility Principle
- 기존 코드 수정 없이 새로운 동작을 추가할 수 있음 ⇒ Open/Closed Principle
- 다양한 개체로 작업하는 동안 유용한 정보를 축적할 수 있음
  - 개체 트리와 같은 복잡한 개체 구조를 탐색하고 구조의 각 개체에 방문자를 적용하려는 경우에 유용할 수 있음

## Cons

- Element 계층에 클래스가 추가되거나 제거될 때마다 모든 방문자를 업데이트해야 됨
- 작업해야 하는 요소의 private 필드 및 메서드에 필요한 액세스 권한이 부족할 수 있음

## Relationship with other patterns

### [[Command Pattern]]

- Visitor 를 Command 의 강력한 버전이라고 생각할 수 있음
- Visitor 객체는 다른 클래스의 다양한 객체에서도 작업을 수행할 수 있음

### [[../../structural/patterns/Composite Pattern]]

- Composite Tree 의 연산을 수행할 때 Visitor 를 사용할 수 있음

### [[Iterator Pattern]]

- 복잡한 데이터 구조를 순환하면서 연산을 수행할 때 Visitor 와 Iterator 를 같이 사용할 수 있음

### [[Strategy Pattern]]

- Visitor 를 어떤 의미에서 방문하는 전략이라고 생각할 수 있음
- Visitor 의 목적은 자료 구조의 각 노드를 방문하면서 무언가 한다는 것
- Strategy 는 훨씬 일반적이고 자료 구조와 특별환 연관이 없음
