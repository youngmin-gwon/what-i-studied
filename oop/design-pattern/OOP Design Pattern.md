# OOP Design Pattern

- 일반적인 객체 지향 프로그래밍의 문제 해결 방법
- A quote in the book "Design Patterns: Elements of Reusable Object-Oriented Programming" by GoF

> A design pattern names, abstracts, and identifies the key aspects of a common design structure that make it useful for creating a reusable object-oriented design.
> 디자인 패턴은 대부분의 프로그래밍 상황에서 유용하게 사용하기 위해 공통적으로 사용 되는 디자인 패턴을 명명, 추상화, 명시화 한것이고, 이는  재사용 가능한 객체지향 디자인을 만들기 위함이다.

- (design 이라는 단어 때문에 혼동이 올 수 있으나) UI/UX 문제를 풀기 위한 것이 아님
- 특정 객체지향 문제를 풀기 위한 청사진에 가까움
- 개발 시간을 앞당길 수 있고, 코드를 더욱 유연하고 재사용 가능하게 만들어 줄 수 있음
- 각 패턴을 이해하는게 어렵고, 코드안에서 패턴이 사용될 수 있는 곳을 찾는 곳이 어려움
- 크게 3가지로 나눌 수 있음
    1. [[Creational Pattern]]
    2. [[Structural Pattern]]
    3. [[Behavioral Pattern]]

## Reference

[Flutter Design Patterns: 1 - Singleton](https://medium.com/flutter-community/flutter-design-patterns-1-singleton-437f04e923ce)

---

## 20. Chain of Responsibility(=Chain of Command)

- Behavioral Pattern

## 21. Visitor

- Behavioral Pattern

![Untitled](Untitled%2058.png)

- 알고리즘을 알고리즘을 실행하는 객체로 부터 분리하는 패턴
- 개체 구조의 요소에 대해 수행할 작업을 나타냄
- 작동하는 요소의 클래스를 변경하지 않고 새 작업을 정의할 수 있음
- tree나 collection의 복잡한 데이터 구조가 있고, 각 데이터 요소 클래스를 변경하지 않고 기능을 변경하고 싶을 때 사용
- 핵심 아이디어
    - 각각의 특정 복합 객체 클래스에 대해 double-dispatch 작업을 정의하는 것
    - Visitor 패턴의 맥락에서 이를 accept라고 함
    - client가 개체 구조를 탐색할 때, 각 요소의 accept 메서드가 호출되어 요청을 특정 방문자 개체에 위임하고 이 개체는 매개변수로 메서드에 전달. 그런 다음, Visitor 개체의 특정 메서드가 호출되어 실제 요청을 수행
- 분석

![Untitled](Untitled%2059.png)

- ***Visitor***
    - ConcreteElement를 파라미터로 가질 수 있는 일련의 방문 메소드를 선언하는 인터페이스
    - Overloading을 취하는 언어라면,  같은 이름을 가질 수도 있지만 Element 타입은 반드시 달라야 함
- ***ConcreteVisitor***
    - 다른 ConcreteElement 클래스에 맞게 조정된 동일한 동작의 여러 버전을 구현
- ***Element***
    - Visitor를 “accept” 메소드 선언하는 인터페이스
    - 선언된 메소드에는 Visitor Interface 유형으로 선언된 매개변수가 하나 있어야 함
- ***ConcreteElement***
    - accpet 메소드 구현
    - 현재 클래스에 해당하는 적절한 Visitor 메서드로 호출을 리디렉션하는 것이 목적
    - 기본 Element 클래스가 이 메서드를 구현하더라도 모든 하위 클래스는 여전히 자체 클래스에서 이 메서드를 재정의하고 Visitor 개체에서 적절한 메서드를 호출해야 함
- ***Client***
    - 복잡한 컬렉션이나 트리 객체를 포함
    - 일반적으로 클라이언트는 추상 인터페이스를 통해 해당 컬렉션의 개체와 작업하기 때문에 모든 구체적인 요소 클래스를 인식하지 못함
- 적용성
    - 복잡한 객체 구조의 모든 요소에 대한 작업을 실행하고 구체적인 클래스의 인터페이스를 변경하고 싶지 않을 때 사용
    - 보조 동작의 비즈니스 논리를 정리할 때 사용
    - 클래스 계층의 일부 클래스에서만 의미가 있고 다른 클래스에서는 의미가 없을 때 패턴을 사용
    - 객체구조가 거의 바뀌지 않는 경우에만 적용하는 것을 권장
- 장점
    - 같은 동작에 대한 여러버전을 하나의 클래스로 이동 시킬 수 있음 ⇒ Single Responsibility Principle
    - 기존 코드 수정 없이 새로운 동작을 추가할 수 있음 ⇒ Open/Closed Principle
    - 다양한 개체로 작업하는 동안 유용한 정보를 축적할 수 있음
        - 개체 트리와 같은 복잡한 개체 구조를 탐색하고 구조의 각 개체에 방문자를 적용하려는 경우에 유용할 수 있음
- 단점
    - Element 계층에 클래스가 추가되거나 제거될 때마다 모든 방문자를 업데이트해야 됨
    - 작업해야 하는 요소의 private 필드 및 메서드에 필요한 액세스 권한이 부족할 수 있음
- 다른 패턴과의 관계
    - Command
        - Visitor를 Command의 강력한 버전이라고 생각할 수 있음
        - Visitor 객체는 다른 클래스의 다양한 객체에서도 작업을 수행할 수 있음
    - Composite
        - Composite Tree의 연산을 수행할 때 Visitor를 사용할 수 있음
    - Iterator
        - 복잡한 데이터 구조를 순환하면서 연산을 수행할 때 Visitor와 Iterator를 같이 사용할 수 있음
    - Strategy
        - Visitor를 어떤 의미에서 방문하는 전략이라고 생각할 수 있음
        - Visitor의 목적은 자료 구조의 각 노드를 방문하면서 무언가 한다는 것
        - Strategy는 훨씬 일반적이고 자료 구조와 특별환 연관이 없음

## 23. Observer

- Behavioral Pattern

![Untitled](Untitled%2063.png)

- Dependents/Publish-Subscribe 라고 불리기도 함
- Reactive Programming 아이디어가 어떻게 차용되었는지 확인할 수 있는 패턴
- 객체 간 1:N 의존성을 정의하여, 객체의 상태가 바뀌었을 때 모든 구독 객체들은 알림을 받을 수 있게 됨
- 이 디자인 패턴이 생기게 된 배경
    - 한 객체의 변화가 다른 것들의 변화를 일으키는 tightly coupled 객체들 때문에 생기게 됨
- 패턴 안의 객체들은 두 가지 역할을 수행함
    1.  Subject ⇒ Publisher
        - 알림을 배포하는 주체
        - 알림을 구독, 취소할 수 있게 하는 방법도 제공함
    2. Observer (= Subscriber)
        - 알림을 받아 변화하는 객체
- observers가 누구인지 몰라도 변하게 하는 것이 가능함 ⇒ loosely coupled하게 만듬
- 구현할 때 고려할 점들
    - 옵저버는 상태를 갖지 않아도 된다
    - Notify를 누가 호출해야 할까?
    - Update 메소드의 인자
    - Observer의 행위가 Subject에 영향을 주는 경우
- 구조

![Untitled](Untitled%2064.png)

- ***Publisher(Subject)***
    - Subscriber를 붙이고 때는 interface 제공
    - Observers 목록을 보관함
- (Optional) ***ConcretePublishers***
    - 관심 상태를 저장하고, 상태 변했을 때 Observers에 알림 전송
- ***Subscriber(Observer)***
    - 알림(notification) 인터페이스 선언
- ***ConcreteSubscribers***
    - 알림(notification) 인터페이스 적용
    - subject의 상태와 일관되게 유지할 수 있도록 처리

- Observer vs Mediator
    - Mediator의 가장 큰 목적은 N:M의 관계를 1:N으로 변환하는 것. Observer는 몇몇의 객체는 다른 객체에 종속체 처럼 행동하며,  객체간 동적인 one way 연결을 허용.
    
- 사용
    - 한 객체의 변화가 다른 객체들의 변화를 만들어야할 때 사용
    - 오직 정해진 시간 동안만 어떠한 객체들의 변화를 관찰해야될 때 사용

- 장점
    - 기존 코드 변경 없이, 새로운 Subscriber를 추가할 수 있음 ⇒ Open/Closed Principle
    - 객체간의 관계를 runtime에 만들 수 있다
- 단점
    - Subscriber가 무작위 순서로 전달 받게 된다
- 다른 패턴과의 관계
    - Chain of Responsibility, Command, Observer
        - 요청의 sender와 receiver을 연결하는 다양한 방법 제시
            - CoR : 잠재적 수신자 중 하나가 처리할 때까지 잠재적 수신자의 동적 사슬을 따라 순차적으로 요청을 전달
            - Command : 발신자와 수신자 간의 단방향 연결을 설정
            - Mediator : 송신자와 수신자 간의 직접 연결을 제거하여 중재자 개체를 통해 간접적으로 통신하도록 함
            - Observer : 수신자가 수신 요청을 동적으로 구독 및 구독 취소할 수 있음
    - Observer
        - 차이를 구별하기 어려움
        - 하나를 구현해서 쓰기도 하나, 때로는 두 가지를 동시에 적용하기도 함
            - Mediator의 목표는 시스템 구성 요소 집합 간의 상호 종속성 제거 ⇒ 대신 구성 요소는 단일 중재자 개체에 종속됨
            - Observer의 목표는 일부 개체가 다른 개체의 종속 역할을 하는 개체 간에 동적 단방향 연결을 설정
            - 두 가지를 합쳐서 Observer에 의존하는 Mediator 객체를 만들어 내는 것이 대중적임
                - Mediator는 Publisher 역할을 하고 Component는 Mediator의 이벤트를 구독 및 취소하는 Observer 역할을 함
                - 이러한 방식으로 Mediator를 구현하면 Observer와 매우 유사하게 보일 수 있음
            - 혼란스러우면 다른 방법으로 Mediator 패턴을 구현할 수 있음
                - 예를 들어 모든 구성 요소를 동일한 Mediator 개체에 영구적으로 연결할 수 있습니다. 이 구현은 Observer와 유사하지 않지만 여전히 Mediator 패턴의 인스턴스임
                - 이제 모든 구성 요소가 Publisher가 되어 서로 간의 동적 연결을 허용하는 프로그램을 상상해 보기
                    - 중앙 집중식 Mediator 개체는 없고 분산된 Publisher 집합만 있을 것임