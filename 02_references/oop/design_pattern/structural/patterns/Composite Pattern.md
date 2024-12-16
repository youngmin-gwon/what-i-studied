---
aliases: []
date created: 2024-12-12 15:52:40 +09:00
date modified: 2024-12-16 12:20:24 +09:00
tags: [design-pattern, gof, oop, structural-pattern]
title: Composite Pattern
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%208.png)

![Untitled](../../../../../_assets/oop/Untitled%209.png)

- 부분으로 전체 계층을 표현하도록 tree structure 로 객체를 구성하는 패턴
- 객체와 객체 구성을 동일하게 사용하게 만들어주는 패턴
- tree data structure
  - nodes(=elements), edges(=relations) 로 구성
  - 각 node 는 여러 개의 children 을 가질 수 있음. 허나 children 은 오직 하나의 parent 만 가질 수 있음
  - node 는 2 개의 타입으로 나눌 수 있음
    - leaf : child 가 하나도 없는 node
    - composite : 하나 이상의 child 를 가지는 node

![Untitled](../../../../../_assets/oop/Untitled%2010.png)

- Flutter 의 "Everything is a widget" 의 아이디어와 같음 (widget 의 child 로 widget 을 가질 수 있음)
- 패턴
  - Component : 구조 안의 객체들의 interface 제공.
  - Leaf : 구조의 leaf 객체. child 를 가지지 않음. 객체의 행동 정의.
  - Composite : children 을 저장 하고 children 과 관련된 행동 정의. leaf 에 각자 일을 할당하고, 중간 결과를 처리한 후 client 에 마지막 결과를 전달하는 역할을 함.

![Untitled](../../../../../_assets/oop/Untitled%2011.png)

- 객체의 " 부분으로서 전체 " 구조를 만들거나, 객체 구성의 차이를 무시하고 싶을 때 사용
- 해당 구조를 적용할만한 대상을 찾는게 어려움 ⇒ 어떠한 객체 그룹을 발견했을 때 해당 패턴을 적용할 수 있는지 검토해보는 것이 좋음
- 예제

![Untitled](../../../../../_assets/oop/Untitled%2012.png)

- 폴더 안에 파일, 폴더 모두 존재할 수 있고, 하위 폴더는 또 다시 폴더, 파일 모두 존재할 수 있는 구조

![Untitled](../../../../../_assets/oop/Untitled%2013.png)

- 적용성
  - tree 같은 객체 구조를 구현할 때 사용
  - 클라이언트 코드가 단순 요소와 복잡한 요소를 모두 균일하게 처리하도록 하기 위해 사용

## Pros

- 기존 코드를 수정하지 않고 새 요소를 추가할 수 있음 ⇒ Open/Closed Principle
- 복잡한 트리 구조를 쉽게 사용할 수 있게 하여 Recursion 계산을 쉽게 만듬

## Cons

- 기능이 너무 다른 클래스에 대해 공통 인터페이스를 제공하는 것은 어려울 수 있음
  - 특정 시나리오에서는 구성 인터페이스를 과도하게 일반화하여 이해하기 어렵게 만듬

## Relationship with other patterns

### [[../../creational/patterns/Builder Pattern]]

- 복잡한 Composite tree 를 생성하기 위해서 Builder 패턴을 사용할 수 있음
  - 재귀적으로 동작하도록 구성 단계를 프로그래밍 할 수 있음

### [[../../behavioral/patterns/Chain of Responsibility Pattern]]

- 종종 Composite 과 함께 사용됨
- Leaf 가 요청을 받으면 모든 상위 구성 요소의 체인을 통해 개체 트리의 루트까지 전달할 수 있음

### [[../../behavioral/patterns/Iterator Pattern]]

- Composite tree 를 순회하기 위해서 Iterator 를 사용

### [[../../behavioral/patterns/Visitor Pattern]]

- Composite tree 의 각 operation 을 수행하기 위해 사용

### [[Flyweight Pattern]]

- Composite tree 의 공유된 Leaf 를 Flyweight 로 구현하여 RAM 자원을 아낄 수 있음

### [[Decorator Pattern]]

- Composite 과 Decorator 는 모두 재귀적 구성을 가지기 때문에 매우 비슷한 구조 다이어그램을 가짐
- Decorator 는 오직 하나의 자식 component 만을 가진 Composite 으로 생각할 수 있음
- Decorator 는 감싸진 객체에 새로운 책임을 추가하는 반면, Composite 는 하위 결과를 " 요약 " 함
- 패턴이 때로 협력도 가능함
  - Decorator 를 사용하여 합성 트리에서 특정 개체의 동작을 확장할 수 있음

### [[../../creational/patterns/Prototype Pattern]]

- Composite 와 Decorator 를 많이 사용하는 디자인은 종종 Prototype 을 사용하여 이점을 얻을수 있음
- Prototype 패턴을 적용하면 복잡한 구조를 처음부터 다시 구성하는 대신 복제할 수 있음
