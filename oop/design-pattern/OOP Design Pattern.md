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

## 17. Bridge(=handle/body)

- Structural Pattern

![Untitled](Untitled%2046.png)

![Untitled](Untitled%2047.png)

- = handle/body
- 구현부에 추상적인 부분을 분리하여 독립적으로 다양성을 가질 수 있도록 함
    - 추상과 구현 사이에 다리를 연결하여 각각 따로 발전시킨 두 가지를 연결해준다
    - 추상에 구현이 아닌 또 다른 추상을 사용하는 방법을 사용한다
- 여러 구현체를 만들기 위한 추상방법은 주로 상속(inheritance)를 사용하는 것
    - 상속은 잘 사용하면 좋지만 구현부가 추상적 개념에 강하게 종속됨
    - 구현을 compile-time에 제한하기 때문에 run-time에 바꾸는 것이 불가능하다
    - 유연하지 못하게 만든다
    - bridge 패턴은 run-time에 구현체를 교환할 수 있게 만든다
- 문제상황
    - 이식성이 있는 Window를 추상적 개념으로 보고 이를 UI 툴킷을 써서 구현하는 예
- 다음을 참고해서 이해하자
    - 추상은 특정 엔티티를 위한 상위 계층
    - 이 계층은 실제로는 아무런 일을 하지 않고, 구현에게 일을 할당하는 역할만 함
    - OS와 GUI를 생각하면 쉬움
        - GUI는 그저 상위 계층으로 사용자의 명령만 받아서 platform으로 전달하는 역할만 함
        - OS와 GUI는 각기 따로따로 발전할 수 있음
- 구조

![Untitled](Untitled%2048.png)

1. ***Abstraction***
    - ***Refined abstraction***을 위한 interface 정의
    - ***Implementation*** type 객체를 참고하는 역할
2. ***Refined abstraction***
    - ***Abstraction*** interface를 구현
    - 각각 다른 조작 논리를 제공
3. ***Implementation***
    - ***Concrete Implementation***을 위한 interface 정의
    - ***Abstraction***은 오직 이곳에 정의된 method를 통해서만 ***Implementation*** 객체와 소통할 수 있음
4. ***Concrete Implementation***
    - ***Implementation*** interface를 구현
    - platform-specific한 코드를 포함하고 있음
- 적용성
    - monolithic한 class를 여러가지 기능으로 나누고 싶을 때 사용해야 함
        - 작아진 클래스로 기존 코드가 망가지는 것을 방지할 수 있음
        - 코드 유지를 간단하게 만들어줌
        - 좋은 예시: database와 file system처럼 persistence layer에 여러 가지 접근 방식을 사용하려는 경우
    - 추상과 구현 모두 subclass로 확장이 가능해야할 때 사용해야함
    - run-time에 구현을 변경해야 하는 경우 유용함
- 장점
    - 플랫폼 독립적인 클래스 및 앱을 만들 수 있음
    - 클라이언트 코드는 높은 수준의 추상화와 함께 작동. 플랫폼 세부정보에게 정보를 노출하지 않음
    - 각각 새로운 Abstraction, Implementation을 도입할 수 있음 ⇒ Open/Closed Principle
    - Abstraction 에서는 상위 레벨 로직에만 집중하면 되고, Implementation 에서는 플랫폼 세부사항에 집중하면 된다 ⇒ Single Responsibility Principle
- 단점
    - 응집력이 높은 클래스에 패턴을 적용하면 코드를 더 복잡하게 만들 수 있음
- 다른 패턴과의 관계
    - Adapter
        - Bridge는 일반적으로 사전에 설계되어 서로 독립적으로 응용 프로그램의 일부를 개발할 수 있음
        - Adapter는 일반적으로 기존 앱과 함께 사용되어 호환되지 않는 일부 클래스가 잘 작동하도록 함
    - Bridge, State, Strategy, (일부 Adapter)
        - 모두 매우 비슷한 구조를 가지고 있으며, 하위 클래스에 작업을 할당하는 composition을 기반으로 함
        - 하지만 모두 다른 문제를 해결하기 위한 방법임
    - Abstract Factory
        - Bridige 패턴과 함께 사용할 수 있는 패턴
            - Bridge에서 정의한 일부 Abstractions가 특정 Implementations에서만 작동할 수 있을 때 유용함
            - 이 경우 Abstract Factory는 이러한 관계를 캡슐화하고 클라이언트 코드에서 복잡성을 숨길 수 있음
    - Builder
        - Bridge와 함께 조합하여 사용할 수 있음
            - Director 클래스는 추상화의 역할을 하는 반면 다른 Builder는 구현의 역할을 하게 하는 방식

## 18. Builder

- Creational Pattern

## 19. Flyweight

- Structural Pattern

![Untitled](Untitled%2052.png)

- 각 객체의 모든 데이터를 보관하는 대신 여러 개체 간에 공통된 state를 공유하여 RAM을 적개 사용하는 패턴
    - 성능 최적화를 위한 패턴
    - RAM 차지로 인한 성능 문제가 있을 때만 적용
    - 다른 의미 있는 방법이 없을 때 사용
- 슈팅 게임을 만든다고 생각했을 때 총알, 미사일 등을 모두 각각의 객체로 만들어서 사용하게 되면 어마어마한 램 공간을 사용하게 된다 ⇒ 이럴 때 Flyweight 패턴을 적용해 볼 수 있다
- 몇가지를 제외하고 비슷하게 여러 개 사용되는 객체에 적용
- 객체를 두가지로 나눠서 사용
    - Intrisic state: 변하지 않는 데이터 ⇒ Flyweight 에 저장
    - Extrinsic state: 각 인스턴스마다 변하는 데이터 ⇒ Context 에 저장
- Flyweight는 객체 내부에 Extrinsic state 저장을 중단할는 대신, 이 상태를 의존하는 특정 메소드에 Extrinsic state를 전달하는 방법 제시
- 분석

![Untitled](Untitled%2053.png)

1. ***Flyweight***
    - Intrinsic state를 포함하는 곳
    - 변하지 않으니 Intrinsic state는 immutable 해야함
    - method로 extrinsic state가 전달 됨
    - 이 객체는 많은 다른 context에서 공유가 가능해야함
2. ***FlyweightFactory***
    - Flyweight 객체를 만들고 관리하는 곳
    - Client가 Factory를 호출할 때 특정 Flyweight 객체가 존재하는지 확인
        - 존재하지 않으면 새 인스턴스 생성한 다음 반환
3. ***Context***
    - Extrinsic state를 포함하는 곳
        - Extrinsic state는 유일 값
4. ***Client***
    - Flyweight의 Extrinsic state를 저장, 계산, 유지하는 역할
- 사용성
    - 프로그램이 사용 가능한 RAM에 거의 맞지 않는 엄청난 수의 객체를 지원해야 하는 경우에만 사용
- 장점
    - 비슷한 객체를 많이 사용할 때, RAM을 아낄 수 있음
- 단점
    - flyweight 메서드를 호출할 때마다 컨텍스트 데이터 중 일부를 다시 계산해야 하는 경우 CPU와 RAM의 trade-off 가 있음
- 다른 패턴과의 관계
    - 코드가 복잡해짐

## 20. Chain of Responsibility(=Chain of Command)

- Behavioral Pattern

![Untitled](Untitled%2054.png)

- 일련의 핸들러를 따라 요청을 전달할 수 있는 패턴
- 요청을 받으면 각 핸들러는 요청을 처리할지 아니면 체인의 다음 핸들러로 전달할지 결정
- 문제 상황
    - 온라인 주문 시스템을 구축한다고 가정해보자. 많은 기능들이 필요하겠지만 유저에 대한 인증이나, Admin 권한을 가진 사용자의 경우 모든 주문을 조회한다던지 하는 기능들이 필요할것이다.
    
    시스템이 비대해져가면서 비밀번호 brute force 어택을 막기 위한 기능, 요청에 대한 validation, 같은 요청에 대해 cache를 반환하는 기능이 필요할수도 있다.
    
    이 상태에서 또 다른 기능을 추가하면 로직은 복잡해진다. 하나를 변경할 때 다른 기능에 영향을 줄 수도 있고, 만약 이 기능들중 일부분의 기능이 다른 기능구현에 필요하다면 중복코드가 발생한다. 이렇게 되면 시스템을 관리하며 유지보수하기가 매우 힘들어진다
    
    ![Untitled](Untitled%2055.png)
    
- 해결책
    - 다른 행동 패턴들과 유사하게 책임 연쇄 패턴도 핸들러라는 단일 객체를 사용한다. 위의 문제점과 같은 상황에서는 각 단계별 행동들이 단일 메소드를 가지는 클래스가 되고, 요청은 단일 메소드의 인자가 된다.
    - 책임 연쇄 패턴은 핸들러들을 연결하여 체인 형태로 구성한다. 체인에서 각 핸들러들은 다음 핸들러를 참조하는 필드를 가지고 있으며, 요청을 처리하고 넘긴다.
    - 또 하나의 특징이 있는데 마치 알고리즘에서 더 탐색할 필요가 없는 그래프 경로를 탐색하지 않는 가지치기 처럼, 각 핸들러는 요청을 다음 핸들러에 넘길지 말지 결정할 수 있다.

![Untitled](Untitled%2056.png)

- 패턴 사용시 여러 핸들러를 하나의 체인으로 연결하고 클라이언트가 해당 체인을 따라 요청을 전달할 수 있음 ⇒ **각 핸들러는 요청을 수신하고 처리 및/또는 추가로 전달**
- 요청 추가/제거/재정렬/처리순서 변경 할 수 있음
- 여러 종류의 요청을 다양한 방식으로 처리할 것이 예상되지만, 요청이나 처리 순서가 컴파일 타임에 정해지지 않는 경우 사용 해야함
- 주의해야 할 점
    - 요청 수행이 보장되지 않음
    - 발신자와 수신자 사이에 느슨한 결합을 도입하고 요청이 체인의 모든 핸들러에 의해 처리될 수 있기 때문에 실제로 처리된다는 보장이 없음
- 분석

![Untitled](Untitled%2057.png)

- ***Handler***
    - 요청을 처리하기 위한 인터페이스 정의
    - 모든 핸들러가 BaseHandler를 상속받아 사용한다면 하지 않아도 됨
- ***BaseHandler***
    - chain 다음 객체의 reference를 가짐
    - default 행위를 정의함
    - 모든 핸들러 클래스 공통 보일러플레이트 코드 포함
- ***ConcreteHandler***
    - 요청을 실제 처리하는 코드 정의
        - 해당 객체에서 처리하거나 다음으로 넘기거나 하는 방식
        - 핸들러는 초기화 된 이후로는 immutable함
- ***Client***
    - 필요에 따라 핸들러 체인을 만들고 요청을 보냄
- 적용성
    - 프로그램이 다양한 방식으로 다양한 종류의 요청을 처리할 것으로 예상되지만 정확한 요청 유형과 순서를 미리 알 수 없는 경우 사용
    - 특정 순서로 여러 핸들러를 실행해야 하는 경우 사용
    - 핸들러 세트와 그 순서가 런타임에 변경되어야 하는 경우 사용
- 장점
    - 요청 처리 순서를 제어할 수 있음
    - 작업을 수행하는 클래스에서 작업을 호출하는 클래스를 분리할 수 있음 ⇒ Single Responsibility Principle
    - 기존 코드를 손상시키지 않고 새 핸들러를 도입할 수 있음 ⇒ Open/Closed Principle
- 단점
    - 일부 요청은 처리되지 않을 수 있음
- 다른 패턴과의 관계
    - Command, Mediator, Observer
        - 모두 요청의 발신자와 수신자를 연결하는 다양한 방법을 다룸
            - CoR : 잠재적 수신자 중 하나가 처리할 때까지 잠재적 수신자의 동적 사슬을 따라 순차적으로 요청을 전달
            - Command : 발신자와 수신자 간의 단방향 연결을 설정
            - Mediator : 송신자와 수신자 간의 직접 연결을 제거하여 중재자 개체를 통해 간접적으로 통신하도록 함
            - Observer : 수신자가 수신 요청을 동적으로 구독 및 구독 취소할 수 있음
    - Composite
        - CoR은 주로 Composite과 함께 사용됨
            - 이 경우 leaf component가 요청을 받으면 모든 상위 component의 체인을 통해 component tree의 root까지 전달할 수 있음
    - Command
        - CoR의 핸들러를 Command를 이용해서 구현할 수 있음
        - 이 경우, 요청으로 표시되는 동일한 컨텍스트 개체에 대해 다양한 작업을 실행할 수 있음
        - 다른 방법
            - request 자체를 command로 구현
            - 이 경우, 체인으로 연결된 일련의 다른 컨텍스트에서 동일한 작업을 실행할 수 있음
    - Decorator
        - 매우 비슷한 클래스 구조를 가지고 있음
            - 재귀 구성을 이용해서 연속된 객체의 연산을 수행함
        - 하지만 결정적으로 다른 점이 있음
            - CoR : 서로 독립적으로 임의의 작업을 실행할 수 있음. 언제든지 요청을 다음으로 전달하지 않고 끝낼 수 있음
            - Decorator : 기본 인터페이스와 일관성을 유지하면서 객체의 동작을 확장함. 요청 중간에 끝내는 것이 불가능

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