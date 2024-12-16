---
aliases: []
date created: 2024-12-12 15:52:49 +09:00
date modified: 2024-12-16 12:20:25 +09:00
tags: [design-pattern, gof, oop, structural-pattern]
title: Decorator Pattern
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%2043.png)

![Untitled](../../../../../_assets/oop/Untitled%2044.png)

- 객체에 동적으로 새로운 책임을 추가할 수 있게 해주는 패턴
- decorator 는 각각 서로 독립적이므로 다양한 동작을 구현하기 위해 추가하고 합쳐질 수 있음
- 상속을 이용한 확장이 실용적이지 못할 때 유용한 패턴
- 코드 복잡성을 증가시킬수 있으므로 사용에 주의 해야함

## Case

- GUI 툴킷이 있다고 가정. 모든 사용자 UI 요소에는 필요 없지만, 어떤 특정 사용자 UI 요소에만 스크롤링이나 테두리 같은 속성을 추가할 필요가 있음.
- Text 를 출력하는 서비스를 제공하는 TextView 클래스가 있다고 가정하자. 이 TextView 에 스크롤 기능이나 두꺼운 테두리가 필요하다면 어떻게 해결해야 할까
  - 직관적인 해결책은 상속
  - 이미 존재하는 클래스를 상속받고, 또 다른 클래스에서 테두리 속성을 상속받으면 이 서브 클래스 인스턴스는 테두리라는 속성을 갖는다
- 하지만 언제 어떻게 테두리를 장식해야할 지 제어해야한다면 난감한 상황이 펼쳐짐
- 모든 TextView 가 아니라 특정 TextView 에만 스크롤이나 테두리 기능이 필요하다면, 상속보다는 장식자 (Decorator) 패턴을 사용하는것이 좋음
  - 테두리를 추가해야하는 객체를 한번 더 감싸는 것

## Structure

![Untitled](Untitled%2045.png)

1. Component
   - 객체를 위한 인터페이스 제공
2. Concrete Component
   - 기본적인 동작 선언
   - decorator 에 의해서 기본 동작은 변경될 수 있음
3. Base Decorator
   - component 인터페이스로 선언된 객체를 감싼 객체를 참조하는 필드를 가짐
   - concrete components 와 decorators 를 모두 가질 수 있음
4. Concrete Decorators
   - component 에 동적으로 추가할 수 있는 행동 선언
5. Client
   - concrete component 를 선언하고 여러 층의 decorator 로 감싸 사용

## Considerations

- Component 는 장식을 추가할 베이스가 되는 역할이므로 작고 가볍게 정의
  - 가급적 인터페이스만 정의
  - 무언가 저장하는 변수를 정의하지 않음
  - 저장할 것이 있으면 서브클래스에서 하자
- 상속 구조를 통해 Decorator 와 Component 가 같은 구조를 갖게 하자
  - 투과적 인터페이스: Decorator 로 계속해서 감싸도 Component 메소드는 계속 사용할 수 있음
- 코드를 수정하지 않고도 준비된 Decorator 를 조합해 기능을 추가할 수 있도록 생각해서 구현
- 비슷한 성질의 작은 클래스가 많아질 수 있다는 단점을 고려
- 구현하려는 내용이 객체의 겉을 변경하려는 것인지 속을 변경하려는 것인지 생각해보자
  - 속을 변경하는 것이라면 전략 패턴을 선택하는 것이 더 적절할 수 있음
- 데코레이터 패턴으로 구현한 다음, 사용이 까다롭게 느껴지거나 자주 쓰는 조합이 있다면 다음 패턴을 사용하는 것을 고려해보자
  - Builder pattern
  - Factory pattern
  - Static factory method
- Decorator 가 다른 Decorator 에 대해 알아야 할 필요가 있다면, Decorator 패턴의 사용 의도와 어긋나는 작업일 수 있음
- 재귀적으로 기능을 갖게하는 방법 외에도, Decorator 를 추가할 때 마다 얻은 아이템을 List 로 관리하는 방법도 있음

## Cautions

- 데코레이터가 여러 개 있다면 순서에 주의
- 코드가 여러 클래스로 흩어져 디버깅이 까다로워지고, 이해하기 어려울 수 있음
- public 메소드가 많다면 Decorator 을 적용하는 것이 바람직하지 않을 수 있음

## Adaptability

- 런타임 중 어떤 객체를 사용하는 코드들을 망치지 않고 해당 객체에 행동을 추가하고 싶을 때 사용
- 상속을 이용해서 객체의 행동을 확장하는 것이 불가능하거나 어색할 때 사용

## Pros

- 서브클래스를 만들지 않고 객체를 확장할 수 있음
- 런타임에 특정 객체로 부터의 책임을 추가하거나 제거할 수 있음
- 여러개의 Decorator 들로 객체를 합쳐 행동 조합을 합칠수 있음
- 여러개의 행위를 하던 monolithic 한 클래스를 여러개의 작은 클래스로 나눌수 있게 됨 ⇒ [[../../../solid/SRP(Single Responsibility Principle)]]

## Cons

- wrapper 스택으로 부터 특정 wrapper 를 제거하는 것이 어려움
- 동작이 Decorator 스택의 순서에 의존하지 않는 방식으로 Decorator 를 구현하는 것은 어려움
- 초기 계층 설정에 관한 코드가 깔끔하지 못함

## Relationship with other patterns

### [[Adapter Pattern]], [[Proxy Pattern]]

- Adapter 는 다른 인터페이스를 제공
- Proxy 는 같은 인터페이스를 제공
- Decorator 는 증강된 인터페이스를 제공

### [[Adapter Pattern]]

- Adapter 는 인터페이스를 변환하지만 Decorator 는 인터페이스의 변환없이 객체를 감싼다

### [[../../behavioral/patterns/Chain of Responsibility Pattern]]

- 매우 비슷한 클래스 구조 (recursive composition) 를 가짐

#### Differences

- Chain of Responsibility handler 는 서로 독립적으로 임의의 작업을 실행할 수 있음. 또한 언제든지 요청을 더 이상 전달하지 않을 수 있음
- 데코레이터는 기본 인터페이스와 일관성을 유지하면서 객체의 동작을 확장할 수 있음. 또한 데코레이터는 요청의 흐름을 중단할 수 없음

### [[Composite Pattern]]

- 비슷한 구조 다이어그램을 가짐. 두 패턴 모두 다 재귀 형태를 갖는다
  - Decorator 는 자식이 1 개, Composite 패턴은 자식이 1~n 개 가능
  - Decorator 는 감싸진 객체에 추가적인 책임을 더하는 반면, Composite 은 단지 자식들의 결과를 합산하는 역할만 함
  - 하지만 두개의 패턴을 합칠 수 있음
    - Decorator 를 사용하여 Composite tree 에서 특정 개체의 동작을 확장할 수 있음

### [[Composite Pattern]], [[../../creational/patterns/Prototype Pattern]]

- Composite 과 Decorator 를 많이 사용하는 디자인에서는 Prototype 을 이용하여 이점을 얻을 수 있음
  - Prototype 을 처음부터 다시 구성하는 대신 복잡한 구조를 복제할 수 있음

### [[../../behavioral/patterns/Strategy Pattern]]

- Decorator 는 외부를 바꾸고, Strategy 는 속을 바꾸는 역할을 함

### [[Proxy Pattern]]

#### 1. Commons

- 두 패턴 모두 한 개체가 일부 작업을 다른 개체에 위임해야 하는 구성 원칙을 기반으로 함
- (Proxy 패턴에서 원본에 해당하는) ConcreteComponent 는 (Proxy 패턴에서 Proxy 에 해당하는) Decorator 를 통해 호출되는 몇 가지 동작을 구현
- 공통 기본 클래스 (common base class) 로부터 상속

#### 2. Differences

- 의도에서 차이가 남
  - 데코레이터는 기능을 추가하거나, (좀 더 일반적으로는) ConcreteComponent 의 핵심 기능에 추가 기능을 동적으로 선택할 수 있는 옵션을 제공
  - 프록시는 세부적으로 정의된 하우스키핑 코드 (housekeeping code) 를 원본으로부터 분리하는 역할
- Proxy 는 일반적으로 자체적으로 서비스 개체의 수명 주기를 관리
- Decorator 의 구성은 항상 클라이언트에 의해 제어됨
