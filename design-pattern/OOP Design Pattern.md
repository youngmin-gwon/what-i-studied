# OOP Design Pattern

## 0. OOP Design Pattern

- 일반적인 객체 지향 프로그래밍의 문제 해결 방법
- A quote in the book "Design Patterns: Elements of Reusable Object-Oriented Programming" by GoF

> A design pattern names, abstracts, and identifies the key aspects of a common design structure that make it useful for creating a reusable object-oriented design.
> 

> 디자인 패턴은 대부분의 프로그래밍 상황에서 유용하게 사용하기 위해 공통적으로 사용 되는 디자인 패턴을 명명, 추상화, 명시화 한것이고, 이는  재사용 가능한 객체지향 디자인을 만들기 위함이다.
> 
- (design 이라는 단어 때문에 혼동이 올 수 있으나) UI/UX 문제를 풀기 위한 것이 아님
- 특정 객체지향 문제를 풀기 위한 청사진에 가까움
- 개발 시간을 앞당길 수 있고, 코드를 더욱 유연하고 재사용 가능하게 만들어 줄 수 있음
- 각 패턴을 이해하는게 어렵고, 코드안에서 패턴이 사용될 수 있는 곳을 찾는 곳이 어려움
- 크게 3가지로 나눌 수 있음
    1. Creational Pattern : 객체의 생성에 관련된 패턴. 객체의 생성절차를 추상화 하는 패턴
        - 시스템이 어떤 구체적인 클래스를 사용하는 지에 대한 정보를 캡슐화 한다
        - 이들 클래스의 인스턴스들이 어떻게 만들고 어떻게 서로 맞붙는지에 대한 부분을 완전히 가린다
        - 종류
            1. 싱글턴 패턴(Singleton) : 한 클래스에 한 객체만 존재하도록 제한한다
            2. 프로토타입 패턴(Prototype) : 기존 객체를 복제함으로써 객체를 생성
            3. 빌더 패턴(Builder) : 생성(construction)과 표기(representation)를 분리해 복잡한 객체를 생성
            4. 팩토리 메서드 패턴(Factory Method) : 생성할 객체의 클래스를 국한하지 않고 객체를 생성
            5. 추상 팩토리 패턴(Abstract Factory) : 동일한 주제의 다른 팩토리를 묶어 줌
    2. Structural Pattern : 클래스나 객체를 조합해 더 큰 구조를 만드는 패턴
        - 서로 독립적으로 개발한 클래스 라이브러리를 마치 하나인 것처럼 사용할 수 있음
        - 여러 인터페이스를 합성하여 서로 다른 인터페이스들의 통일된 추상을 제공
        - 인터페이스나 구현을 복합하는 것이 아니라 객체를 합성하는 방법을 제공
        - 종류
            1. 어댑터 패턴(Adapter) : 인터페이스가 호환되지 않는 클래스들을 함께 사용할 수 있도록, 타 클래스의 인터페이스를 기존 인터페이스에 덧씌운다
            2. 브리지 패턴(Bridge) : 추상화와 구현을 분리해 둘을 각각 따로 발전시킬 수 있다
            3. 합성 패턴(Composite) : 0개, 1개 혹은 그 이상의 객체를 묶어 하나의 객체로 사용할 수 있다
            4. 데코레이터 패턴(Decorator) : 기존 객체의 메서드에 새로운 행동을 추가하거나 오버라이드 할 수 있다
            5. 퍼사드 패턴(Facade) : 많은 분량의 코드에 접근할 수 있는 단순한 인터페이스를 제공한다
            6. 플라이웨이트 패턴(Flyweight) : 다수의 유사한 객체를 생성, 조작하는 비용을 절감할 수 있다
            7. 프록시 패턴(Proxy) : 접근 조절, 비용 절감, 복잡도 감소를 위해 접근이 힘든 객체에 대한 대역을 제공한다
    3. Behavioral Pattern : 객체나 클래스 사이의 알고리즘이나 책임 분배에 관련된 패턴
        - 객체가 수행할 수 없는 작업을 여러 개의 객체로 어떻게 분배 하며 객체 사이의 결합도 최소화에 중점을 둠
        - 주로 클래스에 적용 하는지 아니면 객체에 적용 하는지에 따라 구분되는 패턴
        - 종류
            1. 책임연쇄 패턴(Chain of Responsibility) : 책임들이 연결되어 있어 내가 책임을 못 질 것 같으면 다음 책임자에게 자동으로 넘기는 구조
            2. 커맨드 패턴(Command) : 명령어를 각각 구현하는 것 보다는 하나의 추상 클래스에 메서드를 만들고 각 명령이 들어오면 그에 맞는 서브 클래스가 선택되어 실행
            3. 인터프리터 패턴(Interpreter) : 문법 규칙을 클래스화한 구조를 갖는 SQL 언어나 통신 프로토콜 같은 것을 개발할 때 사용
            4. 이터레이터 패턴(Iterator) : 반복이 필요한 자료구조를 모두 동일한 인터페이스를 통해 접근할 수 있도록 메서드를 이용해 자료구조를 활용할 수 있도록 해줌
            5. 옵저버 패턴(Observer) : 어떤 클래스에 변화가 일어났을 때, 이를 감지하여 다른 클래스에 통보해 줌
            6. 전략 패턴(Strategy) : 알고리즘 군을 정의하고 각각의 클래스로 캡슐화한 다음, 필요할 때 서로 교환해서 사용할 수 있게 해줌
            7. 템플릿 메서드 패턴(Template method) : 상위 클래스에서는 추상적으로 표현하고 그 구체적인 내용은 하위 클래스에서 결정됨
            8. 방문자 패턴(Visitor) : 각 클래스의 데이터 구조로부터 처리 기능을 분리하여 별도의 visitor 클래스로 만들어 놓고 해당 클래스의 메서드가 각 클래스를 돌아다니며 특정 작업을 수행
            9. 중재자 패턴(Mediator) : 클래스간의 복잡한 상호작용을 캡슐화하여 한 클래스에 위임해서 처리함
            10. 상태 패턴(State) : 동일한 동작을 객체의 상태에 따라 다르게 처리해야 할 때 사용
            11. 기념품 패턴(Memento) : ctrl + z 같은 undo 기능 개발할 때 유용한 디자인 패턴. 클래스 설계 관점에서 객체의 정보를 저장

참고한 곳

[Flutter Design Patterns: 1 - Singleton](https://medium.com/flutter-community/flutter-design-patterns-1-singleton-437f04e923ce)

## 1. Singleton

- Creational pattern
- 하나의 인스턴스만을 만들어 사용하기 위한 패턴
- 커넥션 풀, 스레드 풀, 디바이스 설정 객체 등의 경우 인스턴스를 여러 개 만들게 되면 자원을 낭비하게 되거나 버그를 발생시킬 수 있으므로 오직 하나만 생성하고 그 인스턴스를 사용하도록 하는 것이 이 패턴의 목적
- class 의 instance 를 만드는 것이 비용이 클 때 사용할 수 있음. ex) 클래스를 인스턴스화 할 때 외부 데이터를 가져오는 시간이 많이 드는 경우
- 같은 객체를 반복해서 사용해야될 때 사용할 수 있음
- 하나의 인스턴스만을 사용하게 하도록 하기 위해 인스턴스 생성에 특별한 제약을 걸어둬야 함 → 생성자에 private 접근 제어자를 지정하고, 유일한 단일 객체를 반환할 수 있도록 정적 메소드를 지원해야 함. 또한 유일한 단일 객체를 참조할 정적 참고변수가 필요함.
- 고려대상
    - 필요할 때만 사용하기 위해서 lazy construction 을 고려해야함.
    - 대부분의 경우 singleton class 를 생성하기 위해 parameters가 필요하지 않아야 함 ⇒ parameter를 받는 다는 것은 조건에 따라 다른 객체가 생성된다는 의미이고 이것은 더이상 singleton 이라고 할 수 없음
    - multi-threaded 환경에서 safe하게 사용할 수 있도록 해야함(만약, singleton이 mutable data를 가지고 있다면 예상하지 못한 결과를 만들어낼 수 있음)
    - 때로는, singleton은 anti-pattern이라는 것을 숙지해야함(OOP SOLID principle 에서 single responsibility principle을 위배함)
    - 타입으로 제공되는 인터페이스가 있지 않다면 singleton 을 복제하는 것이 불가능하기 때문에 unit test를 어렵게 함

---

## 2. Adapter(=Wrapper)

- Structural Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%201.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%202.png)

- = wrapper
- 다른 인터페이스 클라이언트가 기대하는대로 인터페이스를 변환함
- 함께 할 수 없는 클래스들을 함께 일할 수 있게 만들어줌
- 가장 일반적이고, 가장 유용하게 사용할 수 있는 디자인 패턴 중 하나
    - 예) 형태가 맞지 않은 3rd party library를 Adapter를 생성하여 사용할 수 있게 만들어 줌
- 외부 데이터 저장소 혹은 방식이 다를 때 interface에 맞는 각각의 adapter를 만들어 동일한 형식의 데이터로 만들어 줄 수 있음
- Adapter로 감싸고, interface만 노출하여 기존의 코드를 재사용 가능하게 만들어 줌
- code abstraction 을 하므로 domain layer의 unit test 를 보다 쉽게 만들어 줌
    - 아침에 커피를 마시기 위해 통상적으로 해야할 일
        - (커피 구입과정 제외) 그라인딩 → 브루잉 → 커피 완성
    - 커피 머신을 이용하는 경우
        - 커피 머신 가동 → 커피 완성
    - 위의 과정이 abstraction ⇒  커피 머신  내부에서 어떻게 동작하는지는 알 필요 없이 커피 머신만 가동시키면 커피를 뽑아낼 수 있음
- 디자인 구조

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%203.png)

- (같은 아이디어를 공유하지만) 크게 **1. object**, **2.class** adapter 구조로 나눌 수 있음
    - Target or ITarget은 Client가 사용하는 interface 정의
    - Client는 Target과 소통함
    - Adaptee은 Adapter를 연결하여 변환할 것(ex. 3rd party library)
    - Adapter는 Adaptee의 interface 역할을 하여 Adaptee를  Target과 이어줌
- 차이점
    - **class** 는 Adaptee로 부터 Target interface로 전달하기 위해 **상속**을 이용   ⇒ Adaptee의 concrete operation 이 Target의 구현으로 부터 바로 호출됨
        - 구현하고자 하는 언어가 multiple inheritance 를 지원해야 구현할 수 있음
    - **object** 는  Adaptee로 부터 Target interface로 전달하기 위해 **객체 구조**를 이용
- Github에 작성한 예시에서 object implementation 을 사용한 이유
    - Dart는 multiple inheritance를 지원하지 않음
    - object adapter는 runtime에 연결되기 때문에 더욱 유연하다(=loosely-coupled) ⇒ SOLID 원칙 중 Liskov substitution 원칙에 부합함
        - class adapter 는 쉽게 override 만 하면 된다는 장점이 있음

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%204.png)

- 적용성
    - 기존 클래스를 사용하고 싶지만 인터페이스가 나머지 코드와 호환되지 않을 때 사용
    - 상위 클래스에 추가할 수 없는 몇 가지 공통 기능이 없는 여러 기존 하위 클래스를 재사용하려는 경우 패턴을 사용
- 장점
    - Single Responsibility Principle
    - Open/Closed Principle
- 단점
    - 새로운 인터페이스와 클래스를 추가해야하기 때문에 코드 복잡도 증가
        - 때로는 service 클래스를 쉽게 변경하는 것이 더 간단할 때도 있음
- 다른 패턴과의 관계
    - Bridge
        - 일반적으로 사전에 설계되어 서로 독립적으로 응용 프로그램의 일부를 개발할 수 있음
        - 일반적으로 기존 앱과 함께 사용되어 호환되지 않는 일부 클래스가 잘 작동하도록 함
    - Decorator
        - Adapter는 기존 객체의 인터페이스를 변경하지만, Decorator는 인터페이스를 변경하지 않고 기존 객체를 강화함
        - Decorator는 재귀적 구조를 가지지만, Adapter는 불가능함
    - Proxy
        - Adapter는 감싼 객체에 다른 인터페이스를 제공함
        - Proxy는 감싼 객체에 같은 인터페이스를 제공함
        - Decorator는 감싼 객체에 강화된 인터페이스를 제공함
    - Facade
        - Facade는 기존 객체에 새로운 인터페이스를 정의함
        - Adapter는 기존 존재하는 인터페이스를 유용하게 만들려고 함
- Bridge, State, Strategy, Adapter 차이
    - 어떤 면에서는 매우 비슷한 구조를 가지고 있음
        - subclass에 작업을 맡긴다는 구조가 비슷함
    - 사용 목적이 다름

---

## 3. Template Method

- Behavioral design pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%205.png)

- 알고리즘의 구조를 바꾸지 않고 하위 클래스들이 알고리즘의 몇몇 단계를 재정의하게 함
- 불변하는 알고리즘의 전체 틀을 기준으로 세부사항을 다양하게 만들고자 할 때 사용하게 됨
- 코드 재사용을 위한 핵심적인 기술 → DRY Principle (Don't Repeat Yourself)
    - 여러 단계로 구성된 알고리즘(데이터 가져오기 → 처리 → 계산 결과 제공)이 있을 때 어떤 경우 요구사항은 "3rd-party API로 데이터 가져오기 → 데이터 처리 → 콘솔창에 계산 결과 제공" 일 수 있고, 또 다른 경우 "내장 파일로 데이터 가져오기 → 데이터 처리 → 이메일로 계산 결과 제공" 일 수 있음
    - **세부정보는 다르지만 전체 알고리즘 구조는 같다**: "데이터 가져오기 → 처리 → 계산결과 제공"
    - 이러한 경우 template method 는 유용함 : 각 단계 세부 정보는 변경 할 수 있지만 전체 구조는 지켜야 함
- **변하지 않는 기능은 슈퍼 클래스에 만들어 두고** **자주 변경하며 확장할 기능은 서브 클래스에 만드는 방식**으로 구동
- 디자인 구조

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%206.png)

- 설명
    - AbstractClass: 알고리즘의 뼈대를 설명하는 templateMethod 포함. primitive operations 나 AbstractClass 혹은 다른 객체들에 정의된 operations 을 호출함
    - ConcreteClass: 변하지 않는 알고리즘 단계를 구현하기 위해 AbstractClass에 의존
- Template Method 기능 타입들
    - primitive operations : 하위 클래스에서 반드시 구현되어야 하는 추상 함수. default implementation 을 제공하고 필요한 경우 하위 클래스에서 재정의 될 수 있는 concrete operations.
    - final operations: 하위 클래스에 의해 override 될 수 없는 concrete operations
    - hook operations: 필요한 경우 하위 클래스가 확장할 수 있는 default behavior을 제공하는 concrete operations. 대부분의 경우 default가 아무것도 안하는 것임
    - template method itself: final 로 정의 될 수 있기 때문에 하위 클래스에 의해 override 될 수 없음

- template method는 operations 중 어떤 것이 hook operation인지 abstract operations인지 알려줄 필요가 있음 ⇒ override 되어야 하는 경우 접두사로 "Do-"를 붙여 hook 인지 알려줄 수 있음
- Hollywood Principle

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%207.png)

> Don't call us, we will call you
> 
- Template method 는 high-level component로 간주됨 → clients 나 알고리즘의 concrete operations 가 template method에 의해 호출된다는 의미
    - abstraction은 details에 의존하면 안되고, details가 abstractions에 의존해야함 ⇒ Dependency Inversion principle in SOLID
- 적용
    
    ![template_method.png](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/template_method.png)
    
- 적용성
    - 알고리즘의 특정 단계만 확장하고 전체 알고리즘이나 해당 구조는 확장하지 않도록 할 때 사용
    - 전체적으로 같지만, 약간의 차이만 있는 알고리즘을 적용할 때 사용
- 장점
    1. 중복코드를 줄일수 있다(=DRY)
    2. 자식 클래스의 역할을 줄여 핵심 로직의 관리가 용이하다
    3. 좀더 코드를 객체지향적으로 구성할 수 있다
    4. 클라이언트가 큰 알고리즘의 특정 부분만 재정의하도록 하여 알고리즘의 다른 부분에 발생하는 변경 사항의 영향을 덜 받도록 할 수 있음
- 단점
    1. 추상 메소드가 많아지면 클래스 관리가 복잡해진다
    2. Subclass에서 default 구현을 무시하여 Liskov Substitution Principle을 위반할 수도 있음
    3. 클래스간의 관계와 코드가 꼬여버릴 염려가 있다
    4. 일부 클라이언트는 알고리즘이 제공한 skeleton에 의해 제한될 수 있음
- 다른 패턴과의 관계
    - Factory Method
        - Factory Method는 Template Method를 구체화 한것. 동시에 Factory Method는 큰 Template Method의 한 단계 역할을 할 수 있음
    - Strategy
        - Template Method는 상속을 기반으로 함 ⇒ 이 메서드를 사용하면 하위 클래스에서 해당 부분을 확장하여 알고리즘의 일부를 변경할 수 있음
        - Strategy은 구성을 기반으로 함 ⇒ 해당 동작에 해당하는 다른 전략을 제공하여 개체 동작의 일부를 변경할 수 있음
        - Concrete Algorithm이 선택될 때 차이가 있음
            - Template Method는 template을 상속하기 때문에 컴파일 타임에 정해짐
            - Strategy는 런타임에 정해지기 때문에 동적으로 알고리즘 할당 가능
        - Template Method는 공통된 기능을 공유하도록 설계되어 있지만, Strategy 패턴은 모든 implementation이 독립적이고 공유되는 코드가 없다

## 4. Composite

- Structural pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%208.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%209.png)

- 부분으로 전체 계층을 표현하도록 tree structure 로 객체를 구성하는 패턴
- 객체와 객체 구성을 동일하게 사용하게 만들어주는 패턴
- tree data structure
    - nodes(=elements), edges(=relations)로 구성
    - 각 node는 여러 개의 children을 가질 수 있음. 허나 children은 오직 하나의 parent만 가질 수 있음
    - node는 2개의 타입으로 나눌 수 있음
        - leaf : child가 하나도 없는 node
        - composite : 하나 이상의 child를 가지는 node

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2010.png)

- Flutter 의 "Everything is a widget" 의 아이디어와 같음 (widget 의 child로 widget을 가질 수 있음)
- 패턴
    - Component : 구조 안의 객체들의 interface 제공.
    - Leaf : 구조의 leaf 객체. child 를 가지지 않음. 객체의 행동 정의.
    - Composite : children을 저장 하고 children과 관련된 행동 정의. leaf에 각자 일을 할당하고, 중간 결과를 처리한 후 client에 마지막 결과를 전달하는 역할을 함.

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2011.png)

- 객체의 "부분으로서 전체" 구조를 만들거나, 객체 구성의 차이를 무시하고 싶을 때 사용
- 해당 구조를 적용할만한 대상을 찾는게 어려움 ⇒ 어떠한 객체 그룹을 발견했을 때 해당 패턴을 적용할 수 있는지 검토해보는 것이 좋음
- 예제

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2012.png)

- 폴더 안에 파일, 폴더 모두 존재할 수 있고, 하위 폴더는 또 다시 폴더, 파일 모두 존재할 수 있는 구조

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2013.png)

- 적용성
    - tree 같은 객체 구조를 구현할 때 사용
    - 클라이언트 코드가 단순 요소와 복잡한 요소를 모두 균일하게 처리하도록 하기 위해 사용
- 장점
    - 기존 코드를 수정하지 않고 새 요소를 추가할 수 있음 ⇒ Open/Closed Principle
    - 복잡한 트리 구조를 쉽게 사용할 수 있게 하여 Recursion 계산을 쉽게 만듬
- 단점
    - 기능이 너무 다른 클래스에 대해 공통 인터페이스를 제공하는 것은 어려울 수 있음
        - 특정 시나리오에서는 구성 인터페이스를 과도하게 일반화하여 이해하기 어렵게 만듬
- 다른 패턴과의 관계
    - Builder
        - 복잡한 Composite tree를 생성하기 위해서 Builder 패턴을 사용할 수 있음
            - 재귀적으로 동작하도록 구성 단계를 프로그래밍 할 수 있음
    - Chain of Responsibility
        - 종종 Composite과 함께 사용됨
        - Leaf 가 요청을 받으면 모든 상위 구성 요소의 체인을 통해 개체 트리의 루트까지 전달할 수 있음
    - Iterator
        - Composite tree를 순회하기 위해서 Iterator를 사용
    - Visitor
        - Composite tree의 각 operation을 수행하기 위해 사용
    - Flyweight
        - Composite tree의 공유된 Leaf를 Flyweight로 구현하여 RAM 자원을 아낄 수 있음
    - Decorator
        - Composite과 Decorator는 모두 재귀적 구성을 가지기 때문에 매우 비슷한 구조 다이어그램을 가짐
        - Decorator는 오직 하나의 자식 component만을 가진 Composite으로 생각할 수 있음
        - Decorator는 감싸진 객체에 새로운 책임을 추가하는 반면, Composite는 하위 결과를 "요약"함
        - 패턴이 때로 협력도 가능함
            - Decorator를 사용하여 합성 트리에서 특정 개체의 동작을 확장할 수 있음
    - Prototype
        - Composite와 Decorator를 많이 사용하는 디자인은 종종 Prototype을 사용하여 이점을 얻을수 있음
        - Prototype 패턴을 적용하면 복잡한 구조를 처음부터 다시 구성하는 대신 복제할 수 있음

## 5. Strategy(=Policy)

- Behavioral pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2014.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2015.png)

- = policy
- 알고리즘 집단을 만들고, 각각을 캡슐화 한 후, 집단의 각각을 교환가능하게 만드는 것이 목적
- 가장 실용적인 디자인 패턴 중 하나
- 객체 내부에서 다른 계산로직을 사용하거나 알고리즘을 run-time 중 동적으로 바꾸고 싶을 때 사용
- 예시
    - Sorting algorithms: 각각의 정렬 알고리즘을 추출하여 각각의 클래스로 만들고 sort() 할 수 있는 interface를 만들어 사용
    - Payment strategies : 각각의 결제 방법을 클래스로 만들고 사용자의 선택에 따라 알고리즘 수행
    - Damage calculation in RPG : 각기 다른 동작에 따라 데미지를 계산하는 알고리즘이 있고 각 공격의 문맥에 따라 다른 데미지를 계산하는 알고리즘을 적용

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2016.png)

- 분석
    - Strategy: Concrete Strategies에서 공통적으로 사용되는 interface를 정의. 어떤 strategy를 사용할지는 context에서 정해질 것임
    - Concrete Strategies: Strategy interface에 맞춰 알고리즘 정의
    - Context: Strategy 객체를 가지고 있음. 어떤 알고리즘이 사용될지에 대해서는 독립적 ⇒ 동적으로 바뀔 수 있음
    - Client: Concrete Strategies 중 특정한 알고리즘을 선택하고 Context로 넘김
- 새로운 알고리즘을 추가함으로 로직을 바꿀 필요가 없으므로 SOLID 중 Open-Closed Principle (O in SOLID) 를 성립하게 만들어줌 [확장에는 열려있고, 수정에는 닫혀있음]
- 적용성
    - 다양한 알고리즘을 사용하고 런타임 중에 한 알고리즘에서 다른 알고리즘으로 전환할 수 있도록 하려는 경우
    - 일부 동작을 실행하는 방식만 다른 유사한 클래스가 많이 있는 경우 사용
    - 사용자에게 중요하지 않을 수 있는 알고리즘의 구현 세부 정보에서 클래스의 비즈니스 논리를 분리하기 위해 사용
    - 알고리즘의  전환 사이 대규모 조건문이 있는 경우 사용
- 장점
    - 연관 있는 알고리즘들을 각각의 추출된 class 에 정의한 후 공통 interface 를 정의 ⇒ compile-time flexibility 를 줌
        - run-time 중 추출된 클래스를 동적으로 교환할 수 있음
    - 코드, 내부 데이터, 다양한 알고리즘의 dependencies 를 isolate할 수 있음
    - 간단한 interface를 사용하여 동적으로 알고리즘 수행 혹은 알고리즘 교체를 할 수 있음
    - 새로운 ConcreteStrategy를 코드 수정없이 추가할 수 있음 ⇒ Open/Closed Principle
- 단점
    - 사용하는 곳에서 반드시 각 ConcreteStrategy의 차이를 알고 적절하게 사용해야 함
    - 알고리즘이 거의 바뀌지 않는다면, 복잡하게 Stategy패턴을 사용할 이유가 없음
    - 대부분의 언어에서 Functional type support를 하기 때문에 굳이 코드베이스를 크게 만들이유가 없다
- 다른 패턴과의 관계
    - Bridge, State, (일부분 Adapter)
        - 구조가 비슷함(다른 객체에 실제 작업을 위임하는 구조)
        - 모두 다른 문제를 풀기 위한 방법
            - 패턴은 특정 방식으로 코드를 구조화하기 위한 단순한 레시피가 아님
            - **해결해야하는 문제를 다른 개발자와 소통하기 위한 방법으로 패턴을 사용해야 함**
    - Decorator
        - Decorator는 객체의 겉을 바꾸는 역할, Strategy는 객체의 속을 바꾸는 역할
    - Command
        - 둘다 객체를 파라미터로 갖기 때문에 비슷해보일 수 있음
        - 하지만, 다른 의도로 사용됨
            - Command: 연산을 객체로 바꾸려는 의도 ⇒ 작업 실행을 연기하고, 대기열에 추가하고, 명령 기록을 저장하고, 원격 서비스에 명령을 보내는 등의 작업을 수행할 수 있음
            - Strategy:  같은 일을 하는 다른 알고리즘을 자유롭게 교체해서 사용하기 위한 의도
    - Template method
        - Template Method 패턴은 상속 기반. subclass에서 수정이 필요한 알고리즘 일부분을 확장하는 방법
        - Strategy 패턴은 구성 기반. 다르게 동작하는 전략을 제공해서 객체의 행위를 변경하는 방법
        - Template Method는 class level에서 동작하고, Strategy는 object level에서 동작함 ⇒ Template Method는 static 하기 때문에 compile-time-safe, Strategy는 runtime-safe 함
        - Template Method 패턴은 공통된 기능을 공유하도록 설계되어 있지만, Strategy 패턴은 모든 implementation이 독립적이고 공유되는 코드가 없다
    - State
        - State는 Strategy를 확장한 패턴으로 간주됨
            - 둘 모두 구성 기반
            - helper 객체가 context를 변경하는 것을 도와 줌
            - Strategy는
        - Strategy는 상속을 대체하려는 목적
        - State는 코드내의 조건문들을 대체하려는 목적

## 6. State

- Behavioral pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2017.png)

- 객체의 내부 상태가 바뀌었을 때 행동을 바꿀 수 있게 해주는 패턴
- 상태 전이를 위한 조건 로직이 지나치게 복잡한 경우 이를 해소하기 위한 방법
- Finite-state machine을 이해해야 아이디어를 이해할 수 있음
    
    ![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2018.png)
    
    - Jira 예시
    - task가 들어갈 수 있는 유한한 상태가 있음
    - 모든 상태는 유일하고, 다르게 행동함
    - 이러한 상태는 다른 상태로 언제든지 변할 수 있음
        - 하지만, 현재 상태에서 변할 수 있게 정해진 상태로만 변경할 수 있음
- 조건문을 이용해서 구현할 수 있겠지만, 이런 경우 새로운 상태를 추가하는 것이 매우 어려워 짐
    - state pattern을 이용하면 새 상태를 추가하는 것이 매우 쉬워지고, 상태 변경도 명백해진다
- 분석

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2019.png)

1. Context
    - 현재 상태를 가리키는 ConcreteState 인스턴스를 보관
    - ConcreteState 구현에 대해서는 전혀 모름(=State interface 이용)
    - 현재 상태를 바꾸기 위해서 setter 메소드를 가짐
2. State
    - 특정한 state의 행동과 상태를 캡슐화하기 위한 인터페이스 제공
3. ConcreteStates
    - Context와 관련된 상태의 행동을 정의
    - State 객체들은 Context 정보를 위해, 또는 state 변화를 위해 Context를 참조할 수도 있음
4. Client
    - 현재 상태를 알기 위해 Context를 사용
    - 상태 변화 명령을 내림
    - 필요하다면 Context의 초기 상태를 정의

- 적용성
    - 상태가 많고, 자주 변경되며, 상태에 따라서 다르게 동작하는 경우 사용되야 함
    - 유사한 상태 및 전환에 걸쳐 중복 코드가 많은 경우 사용
    - 상태에 따른 조건이 까다로울 때 사용
- 예시
    - e-commerce application에서 주문 상태 관리
    - 현재 상태에 적절한 신호등 색 보여주기
    - Medium 기사 상태(draft, submitted, published…)
- 장점
    - 특정 상태에 관련된 코드를 분리된 클래스로 만들어줌 ⇒ Single Responsibility Principle
    - 새 상태를 코드 수정없이 추가할 수 있음 ⇒ Open/Closed Principle
    - 조건문을 없애 코드를 더욱 간단하게 만들 수 있음
- 단점
    - 상태가 많이 바뀌지 않고, 상태가 많이 없을 때는 패턴 적용하는 것이 과함
- 다른 패턴과의 관계
    - Bridge, State, (일부분 Adapter)
        - 구조가 비슷함(다른 객체에 실제 작업을 위임하는 구조)
        - 모두 다른 문제를 풀기 위한 방법
            - 패턴은 특정 방식으로 코드를 구조화하기 위한 단순한 레시피가 아님
            - **해결해야하는 문제를 다른 개발자와 소통하기 위한 방법으로 패턴을 사용해야 함**
    - Strategy
        - State는 Strategy를 확장한 패턴으로 간주됨
            - 둘 모두 구성 기반
            - helper 객체가 context를 변경하는 것을 도와 줌
            - Strategy는 Strategy는 상속을 대체하려는 목적
            - State는 코드내의 조건문들을 대체하려는 목적

## 7. Facade

- Structural pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2020.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2021.png)

- 복잡한 API나 하위시스템의 함수 묶음을 모은 간단한 인터페이스 제공
- 클라이언트가 하위 시스템과 소통하기 위해서는 퍼사드만 이용하면 된다
- 클라이언트와 하위 시스템간의 의존성을 줄여줌

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2022.png)

- Facade
    - 어떤 하위시스템 클래스가 요청에 연관되어 있는지 알고, 요청을 하위시스템에 할당하는 역할을 함
- Additional Facade
    - 메인 퍼사드에서 특정한 함수를 추출하고 싶을 때 사용
- Subsystem
    - 특정 카테고리의 기능 구현
    - 퍼사드에 대한 참조를 전혀 가지고 있지 않음
- Client
    - 하위 시스템 함수를 바로 부르지 않고 퍼사드를 이용해서 기능을 수행함
- 사용하는 경우
    1. 복잡한 시스템 연관관계를 간단하게 만든 인터페이스를 제공하고 싶을 때 사용
    2. 하위 시스템을 layer로 구성하고 싶을 때 사용
    3. 모듈간의 coupling을 줄이기 위해서 사용
    4. 매우 큰 기존 API 중 일부만 사용하고 싶을 때 사용 
- 장점
    - 복잡한 하위 시스템으로부터 코드를 분리할 수 있음
- 단점
    - 앱의 모든 클래스에 결합된 “god object”가 될 위험이 있음
- 다른 패턴과의 관계
    - Adapter
        - Facade는 기존 객체에 새로운 인터페이스를 정의함
        - Adapter는 기존 존재하는 인터페이스를 유용하게 만들려고 함
    - Abstract Factory
        - Abstract Factory는 클라이언트 코드에서 서브시스템 객체가 생성되는 방식을 숨기고 싶을 때 Facade의 대안으로 사용할 수 있음
    - Flyweight
        - Flyweight는 조그마한 많은 객체들은 만드는 방법을 보여줌
        - Facade는 전체 시스템을 상징하는 단일 객체를 만드는 방법을 보여줌
    - Mediator
        - 둘 다 밀접하게 연결된 많은 클래스 간의 협업을 조직하려고 함
        - Facade는 Subsystem의 단순화된 인터페이스를 제공하지만, 새로운 기능을 추가하진 않음
            - Subsystem은 Facade의 존재를 모름
            - Subsystem의 객체들은 직접적으로 소통할 수 있음
        - Mediator는 system 구성요소 간의 소통을 중재함
            - 구성요소들은 Mediator만 알고, 직접 소통하지 않음
    - Singleton
        - 단일 Facade 객체로 충분하기 때문에 Facade 클래스는 종종 Singleton으로 변환될 수 있음
    - Proxy
        - 둘 다 복잡한 엔티티를 버퍼링하고 자체적으로 초기화함
        - Proxy는 서비스 객체와 동일한 인터페이스를 가지고 있어 상호 교환이 가능함

## 8. Interpreter

- Behavioral Pattern
- 언어를 주고, 문법의 표현을 정의하여 해당 언어로 된 기술 문장을 해석하는 번역기를 함께 정의하는 패턴
- 규칙을 정의하고 이에 맞춰서 프로세스를 해석하는 패턴
- 규칙 관리가 쉬워짐
- 분석

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2023.png)

1. AbstractExpression
    - 추상 구문 트리에 속한 모든 노드에 해당하는 클래스들이 공통으로 가져야 할 `interpret()`연산을 추상 연산으로 정의
2. TerminalExpression
    - 문법에 정의한 터미널 기호와 관련된 해석 방법을 구현
    - 문장을 구성하는 모든 터미널 기호에 대해서 해당 클래스를 만들어야 함
    - 사칙 연산에서 숫자의 역할
3. NonterminalExpression
    - nonterminal 기호에 대한 `interpret()` 연산 구현
    - 사칙 연산에서 연산자 역할
4. Context
    - Expression 인스턴스에 공유되는 번역기에 대한 포괄적인 정보를 포함
5. Client
    - 언어로 정의한 특정 문장을 나타내는 추상 구문 트리
    - 추상 구문 트리는 NonterminalExpression과 TerminalExpression 클래스의 인스턴스로 구성
    - 이 인스턴스의 `interpret()`연산을 호출
- Composite vs Interpreter
    - Composite 패턴은 오직 static한 시스템 특성을 정의하거나 구조를 정의하기 위해서 사용됨
    - Interpreter 패턴은 언어를 상징하고, 행위를 정의하고, 트리 안의 구성 노드들의 해석 방법을 제시하고, 문맥을 공유하기 위해 사용됨
    - Interpreter 패턴은 문장을 구성하기 위해서 Composite 패턴을 사용함
- 비교적 간단한 언어(e.g. RegEx, bar codes, 사칙 연산)를 해석하기 위해서만 사용됨
- 성능이 중요한 고려사항이 아닐때만 사용해야함
- 어떤 언어의 문법을 10개 이하의 클래스로 구현할 수 있다면, Interpreter 패턴을 사용하는 것이 좋다.
    - 검색 조건식을 통해 객체나 데이터베이스를 검색하는 것
- 사용 예시
    - Specification과 Query Object 패턴은 Interpreter 패턴을 매우 적극적으로 사용하는 예다. 두 패턴은 모두 단순한 문법과 객체의 조합을 이용해 검색 조건식을 모델화하는 것으로, 검색 조건식과 그 표현을 분리하는 데 유용하게 쓰일 수 있다. 예를 들어, Query Object 패턴은 쿼리를 일반화해 모델로 만들기 때문에 데이터베이스에 실제로 쿼리할 때 사용되는 SQL로 쉽게 변환할 수 있다.
    - 인터프리터는 시스템 설정을 런타임에 변경하기 위해 사용되는 경우도 많다. 예를 들어, 시스템에서 사용자 인터페이스를 통해 사용자가 원하는 설정을 쿼리 형태로 입력받은 다음, 그 쿼리를 나타내는 해석 가능한 객체 구조를 동적으로 생성할 수 있다. 이런 식으로 인터프리터는 시스템 내의 모든 동작이 정적이어서, 동적으로 설정할 수 없는 경우에는 불가능한 훨씬 더 큰 강력함과 융통성을 제공할 수 있다.
- 고려사항
    - Interpreter 패턴은 단순한 언어를 해석할 때 유용한 패턴임
        - 문법을 클래스 몇 개로 모델화 할 수 있을 때, 그 언어는 단순하다고 말함
        - 단순한 언어의 문장이나 수식은 그 문법을 정의하는 클래스들의 인스턴스를 조합해 표현할 수 있음 ⇒ 이때는 보통, Composite 패턴을 이용
    - Interpreter 패턴을 구현하는 것은 Composite 패턴보다 약간 더 복잡할 뿐이지만, 가장 어려운 점은 어떤 경우에 인터프리터가 필요한지를 아는 것임
    - 언어가 복잡하거나 반대로 아주 단순한 경우에는 Interpreter가 필요 없음 ⇒ 어떤 언어의 문법을 10개 이하의 클래스로 구현할 수 있다면 선택해볼만 함

## 9. Iterator

- Behavioral Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2024.png)

- 컬렉션 구현 방법을 노출시키지 않으면서도 그 집합체안에 들어있는 모든 항목을 순회 접근할 수 있게 해 주는 방법을 제공해 주는 패턴
    - 무언가 많이 모여 있는 것을 하나씩 지정해서 순서대로 처리하는 패턴
- Iterator 패턴을 사용하면 집합체 내에서 어떤 식으로 일이 처리되는지 몰라도 그 안에 들어있는 항목들에 대해서 반복작업을 수행 할 수 있다
- 실생활 사례
    
    ![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2025.png)
    
    - 며칠 동안 로마를 방문하여 주요 명소와 명소를 모두 방문할 계획입니다. 그러나 일단 거기에 가면 콜로세움조차 찾을 수 없는 원을 그리며 걷는 데 많은 시간을 낭비할 수 있습니다.
    
    반면에 스마트폰용 가상 가이드 앱을 구입하여 내비게이션에 사용할 수 있습니다. 그것은 똑똑하고 저렴하며 원하는만큼 흥미로운 장소에 머물 수 있습니다.
    
    세 번째 대안은 여행 예산의 일부를 지출하고 그의 손등처럼 도시를 아는 현지 가이드를 고용할 수 있다는 것입니다. 가이드는 귀하의 취향에 맞게 여행을 조정하고 모든 명소를 보여주고 흥미 진진한 이야기를 많이 들려줄 수 있습니다. 그것은 훨씬 더 재미있을 것입니다. 그러나 슬프게도 더 비쌉니다.
    
    머리 속에서 태어난 임의의 방향, 스마트폰 내비게이터 또는 인간 가이드와 같은 이 모든 옵션은 로마에 있는 방대한 명소와 명소 컬렉션을 반복하는 역할을 합니다.
- 분석

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2026.png)

1. IterableCollection
    - Iterator를 생성하기 위한 인터페이스
    - 컬렉션과 호환되는 Iterator를 얻기 위한 하나 이상의 메서드를 선언
        - ConcreteCollection이 다양한 종류의 Iterator를 반환할 수 있도록 메서드의 반환 유형은 Iterator 인터페이스로 선언
2. ConcreteCollection
    - 특정 ConcreteIterator의 새 인스턴스를 반환하기 위해 Iterator 생성을 구현
        - 클라이언트가 요청할 때마다 특정 ConcreteIterator 클래스의 새 인스턴스를 반환
3. Iterator
    - Collection에 접근하고 순차 순회 하기 위한 인터페이스
    - 컬렉션 순회에 필요한 작업(다음 요소 가져오기, 현재 위치 검색, 반복 다시 시작 등)을 선언
4. ConcreteIterator
    - iterator 인터페이스를 구현
    - 컬렉션을 순회하기 위한 특정 알고리즘을 구현
    - 자체적으로 순회 진행을 추적해야 함
        - 이를 통해 여러 Iterator가 서로 독립적으로 동일한 컬렉션을 순회할 수 있음
- 적용성
    - collection 데이터 타입이 내부적으로 복잡하고, 복잡성을 client에 보여주고 싶지 않을 때 이 패턴을 사용하라
    - 순회 코드의 중복을 줄이기 위해 이 패턴을 사용하라
    - 구조의 타입이 알려져 있지 않거나, 서로 다른 데이터 구조를 순회하고 싶을 때 사용하라
    - 일일이 접근하는 작업을 컬렉션 객체가 아닌 반복자 객체에서 맡게 됨
        - 집합체 인터페이스 구현이 간단해짐
        - 집합체에서는 반복작업에 손을 떼고 원래 자신이 할일에만 전념할 수 있음
        
        ⇒ SRP, DRY 준수하게 됨
        
    - 같은 collection을 다른 규칙으로 순회하는 방법이 필요할 때, 하나의 인터페이스를 부풀리는 것이 아니라 iterator 클래스를 하나 더 구현하기만 하면 되기 때문에 유용하게 사용할 수 있음
    - 데이터 구조 구현을 확정할 수 없지만, 순회하는 방법이 필요할때 유용함
- 장점
    - 장황한 순회 알고리즘을 별도의 클래스로 추출하여 클라이언트 코드와 컬렉션을 정리할 수 있음 ⇒ Single Responsibility Principle
    - 기존 코드 수정 없이 새로운 유형의 컬렉션 및 반복자를 추가할 수 있음 ⇒ Open/Closed Principle
    - 각 iterator 객체에는 고유한 반복 상태가 포함되어 있으므로 동일한 collection을 병렬로 순회 할 수 있음
    - 원할 때 순회를 중단/재개 할 수 있음
- 단점
    - 간단한 Collection만 사용한다면 과한 패턴
    - 일부 특수 컬렉션의 요소를 직접 살펴보는 것보다 덜 효율적일 수 있음
- 다른 패턴과의 관계
    - Composite
        - Composite와 Iterator를 함께 사용하여, Composite tree를 순회 하게 할 수 있음
    - Factory Method
        - Factory Method와 Iterator를 함께 사용하여, 컬렉션 하위 클래스가 컬렉션과 호환되는 다양한 유형의 반복자를 반환하도록 할 수 있음
    - Memento
        - Memento와 Iterator를 함께 사용하여, 현재 상태를 알고, 또 필요한 경우 되돌릴 수 있음
    - Visitor
        - Visitor와 Iterator를 함께 사용하여, 모두 다른 클래스이더라도, 복잡한 데이터 구조를 순회하고 요소에 대해 일부 작업을 실행할 수 있음

## 10. Factory Method(=Virtual Constructor)

- Creational pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2027.png)

- = Virtual Constructor
- 객체를 만드는 인터페이스를 제공하지만, 서브클래스에서 어떤 클래스를 초기화 할지 정하는 패턴
- 예시
    - Logistic에 관련된 앱을 만들었다. 처음에는 Truck만 신경쓰면 되어서 Truck을 코드 전체에 작성했다
    - Logistic이 잘 되어서 Ship도 추가하고 싶다. 허나 Ship을 추가하기 위해 코드 베이스 전체를 수정해야 할 것이다
    - Transport 인터페이스를 만들고 Factory Method 패턴을 사용해서 하위 클래스에서 Truck인지, Ship인지 정하게 만든다
- 장점
    - 객체를 사용할 클래스에서 직접 객체를 만들게 되는 문제를 해결할 수 있음
    - subclassing함으로 compile-time 유연성을 가질 수 있음
    - 코드에서 application에 특정된 클래스의 직접 바인딩을 제거할 수 있다. 덕분에 코드는 인터페이스만 신경쓰면 된다
    - 분석
    
    ![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2028.png)
    
    - Creator
        - Product 객체를 반환하는 Factory Method 정의
        - Factory Method는 서브클래스들이 구현하도록 추상으로 정의할 수 있음
        - 혹은 ConcreteProduct를 제공하는 Factory Method의 default 구현을 제공할 수도 있음
    - ConcreteCreator
        - Factory Method를 오버라이드하고 ConcreteProduct 인스턴스를 반환
            - factory method는 매번 새로운 인스턴스를 만들 필요가 없다는 것 주목
    - Product
        - Factory Method가 생성하는 모든 객체에 대한 인터페이스 정의
    - ConcreteProduct
        - Product 인터페이스 구현
        - 각 객체의 인스턴스는 특정한 ConcreteCreator 에 의해서 반환됨
- 적용성
    - 목적: 실제로 product를 사용하는 곳과 product를 생성하는 곳을 분리하기 위함
        - 새 concrete product를 추가해야되는 경우, 오직 factory method를 오버라이드하는 새로운 ConcreteCreator도 생성되야 한다는 것을 인지
    - 새로운 인스턴스를 계속 생성할 필요가 없는 경우 적용할 수 있음
        - 이미 생성된 객체를 추적하는 cache layer나 저장소를 둬서 반환할 수 있도록 설정하는 방식으로 가능
    - 추후에 어떠한 타입의 객체를 사용해야 하는지 모를 때 사용
- 장점
    - product를 생성하는 곳을 한 곳으로 이동시킬 수 있음 ⇒ Single Responsibility Principle
    - 코드 수정 없이 새로운 product를 추가할 수 있음 ⇒ Open/Closed Principle
    - Creator와 ConcreteProduct간의 결합도를 줄일 수 있음
- 단점
    - 패턴을 구현하기 위해 많은 새 하위 클래스를 도입해야 하므로 코드가 더 복잡해질 수 있음
        - 가장 좋은 시나리오는 생성자 클래스의 기존 계층 구조에 패턴을 도입하는 경우
- 다른 패턴과의 관계
    - Abstract factory, Prototype, Builder
        - 모두 Factory Method를 기반으로 발전 됨
        - Factory Method보다 자유롭지만, 복잡함
    - Abstract factory
        - Abstract Factory는 Factory Method의 세트를 기반으로 만들어짐
    - Iterator
        - Factory Method와 Iterator를 함께 사용하여, 컬렉션 하위 클래스가 컬렉션과 호환되는 다양한 유형의 반복자를 반환하도록 할 수 있음
    - Prototype
        - Prototype은 상속을 기반으로 하지 않지만  복제된 객체의 복잡한 초기화가 필요
        - Factory Method는 상속을 기반으로 하지만 초기화 단계가 필요하지 않음
    - Template Method
        - Factory Method는 Template Method를 구체화 한것. 동시에 Factory Method는 큰 Template Method의 한 단계 역할을 할 수 있음

## 11. Abstract Factory(=Kit)

- Creational pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2029.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2030.png)

- = Kit
- concrete class를 구체화 하지 않고 관계있는 혹은 의존적인 객체들의 군집을 만들기 위한 인터페이스 제공
- 객체 군집을 만드는 것을 캡슐화 ⇒ 객체 생성을 추상화 하게 됨
- 사용
    - 객체가 생성되거나 구성, 표현되는 방식과 무관하게 시스템을 독립적으로 만들고자 할 때
    - 여러 제품군 중 하나를 선택해서 시스템을 설정해야 하고 한번 구성한 제품을 다른 것으로 대체할 수 있을 때
    - 관련된 제품 객체들이 함께 사용되도록 설계되었고, 이 부분에 대한 제약이 외부에도 지켜지도록 하고 싶을 때
    - 제품에 대한 클래스 라이브러리를 제공하고, 그들의 구현이 아닌 인터페이스를 노출시키고 싶을 때
- 가장 쉬운 예: 상황에 따라 Android or iOS Theme 을 보여줌
- Factory Method 패턴과 유사한데 차이점은?
    - Abstract Factory 는 관계되어 있는 객체의 “Family”를 만드는 방법을 제공함
    - Factory Method 는 쉽게 Abstract Factory의 subset이라고 생각해도 됨
- Abstract Factory 패턴은 객체 생성을 더욱 유동적으로 할 수 있게 만듬
    1. Compile-time flexibility
        - 객체 만드는 방법은 사용부분으로부터 독립적으로 선언, 변경될 수 있다: 단지 subclass를 새로 선언하면 된다
    2. Run-time flexibility
        - factory object는 동적으로 변화될 수 있다
- application-specific한 binding을 제거해줌
- 연관되어 있는 객체 군집을 사용해야할 때, 하지만 어떻게 만들어지는지 신경 쓰지 않아야 하고, concrete class에 의존하지 않아야할때, 고려해야할 패턴
- 딱딱하게 생각하지말자. GoF의 패턴을 조금씩 변형해 사용하는 경우가 많다
    - ConcreteFactory가 의 AbstractFactory역할도 맡도록 구현하는 경우도 있음
    - Factory이면서 Product인 경우도 있음
    - Factory를 Product에 주입하지 않고 Factory가 Product를 생산하는 경우도 있음
- 구성

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2031.png)

1. Abstract Factory
    - abstract product를 생성하는 interface 선언
2. Concrete Factory
    - concrete product 객체들을 생성하는 operations를 적용
    - **각각의 Concrete Factory는 오직 하나의 varient와 일치한다**
3. Product
    - product 객체의 interface 선언
4. Concrete Product
    - 상응하는 Concrete Factory에 의해 만들어지는 product 채택
5. Client
    - Abstract factory만 사용하여 product 사용
- 적용
    - 코드가 관련 제품의 다양한 제품군과 함께 작동해야 하지만 해당 제품의 구체적인 클래스에 의존하고 싶지 않을 때 사용해야 함
        - 미리 정의되지 않았거나 단순히 미래의 확장성을 허용하기 위해
- 장점
    - product를 생성하는 곳을 한 곳으로 이동시킬 수 있음 ⇒ Single Responsibility Principle
    - 코드 수정 없이 새로운 product를 추가할 수 있음 ⇒ Open/Closed Principle
    - Creator와 ConcreteProduct간의 결합도를 줄일 수 있음
- 단점
    - 새로운 종류의 Product를 제공하기 어려울 수 있다
- 다른 패턴과의 관계
    - Prototype, Builder
        - 모두 Factory Method를 기반으로 발전 됨
        - Factory Method보다 자유롭지만, 복잡함
    - Builder
        - Builder는 복잡한 객체를 단계별로 생성하는 패턴
        - Abstract Factory는 관계있는 객체의 family를 만드는 패턴
        - Abstract Factory는 객체를 바로 생성하지만, Builder는 객체 생성까지 추가적인 시간이 필요함
    - FactoryMethod
        - Abstract Factory는 Factory Method의 세트를 기반으로 만들어짐
    - Facade
        - 클라이언트 코드에서 서브시스템 객체가 생성되는 방식을 숨기고 싶을 때 Facade의 대안으로 사용할 수 있음
    - Bridge
        - Abstract Factory와 Bridge 패턴을 함께 사용할 수 있음
            - Bridge에서 정의한 일부 추상화가 특정 구현에서만 작동할 수 있을 때 유용함
            - Abstract Factory는 관계를 캡슐화하고 클라이언트 코드에서 복잡성을 숨길 수 있음
    - Singleton
        - Abstract Factory는 Singleton 패턴으로 적용될 수 있음
    

cf) Factory 용어 의미 비교

1. Factory
    - 무언가를 생성하는 function, method, class를 의미하는 모호한 용어
    - 대부분의 경우, factory는 객체를 생성하지만, 때때로 file, 데이터베이스의 record를 생성하기도 함
    - 주로 사용하는 상황 예시
        - 프로그램의 GUI를 생성하는 function 혹은 method
        - User를 생성하는 클래스
        - 특정 방식으로 클래스 생성자를 호출하는 정적 메서드.
        - Creational 디자인 패턴 중 하나
2. Creation method
    - 객체를 생성하는 메소드
        - 팩토리 메소드 패턴의 모든 결과가 "생성 메소드"이지만 반드시 그 반대는 아님을 의미
    - 동일 의미
        - *Martin Fowler*가 *Refactoring*에서 언급했던 factory method
        - *Joshua Bloch*가 *Effective Java*에서 언급했던 static factory method
    - 실제로 생성 메서드는 생성자 호출을 둘러싼 래퍼일 뿐임
        - 하지만, 생성자 변경 사항에서 코드를 분리하는 데 도움이 될 수 있음
        - 또한, 새로 만드는 대신 기존 개체를 반환하는 특정 논리를 포함할 수도 있음
    - 많은 사람이 factory method 라고 부름 ⇒ 새로운 객체를 만드는 메소드 이기 때문
    - factory method pattern과는 다르기 때문에 유의하자
    
    ```java
    class Number {
        private $value;
    
        public function __construct($value) {
            $this->value = $value;
        }
    
        public function next() {
            return new Number ($this->value + 1);
        }
    }
    ```
    
3. Static creation (or factory) method
    - static으로 선언된 creation method
        - 즉, 생성을 위해서 객체가 필요하지 않은 경우임
    - static factory method라고 부르지 않게 유의하자 ⇒ factory method는 상속을 사용하는 디자인 패턴이기 때문. 즉 subclassing 할 수 없음
    - 다음 같은 경우에 유용함
        - 여러가지 다른 목적을 위한 여러가지 생성자가 존재해야 하는 경우
        - 새로 생성하는 것이 아니라 기존에 존재하는 객체들을 제사용하고 싶은 경우
    
    ```java
    class User {
        private $id, $name, $email, $phone;
    
        public function __construct($id, $name, $email, $phone) {
            $this->id = $id;
            $this->name = $name;
            $this->email = $email;
            $this->phone = $phone;
        }
    
        public static function load($id) {
            list($id, $name, $email, $phone) = DB::load_data('users', 'id', 'name', 'email', 'phone');
            $user = new User($id, $name, $email, $phone);
            return $user;
        }
    }
    ```
    
4. Simple factory pattern
    - 파라미터를 이용한 분기로 생성을 다르게 하는 생성 메소드를 가지고 있는 클래스를 의미함
    - 주로 일반 factory와 혼동하거나, factory 디자인 패턴들 중 하나와 혼동함
        - simple factory는 factory method의 도입 전 중간 과정이라고 생각하는 것을 권장
    - 단일 클래스의 단일 메소드로 표현되다가, 너무 커질 우려가 있어서 subclass로 나눈 경우로 볼 수 있음 ⇒ 몇번 반복하면 factory method pattern이 됨
    
    ```java
    class UserFactory {
        public static function create($type) {
            switch ($type) {
                case 'user': return new User();
                case 'customer': return new Customer();
                case 'admin': return new Admin();
                default:
                    throw new Exception('Wrong user type passed.');
            }
        }
    }
    ```
    
5. Factory Method pattern
    - 객체 생성을 위한 인터페이스를 제공하지만 생성될 객체의 유형을 하위 클래스가 변경할 수 있도록 하는 생성 디자인 패턴
    
    ```java
    abstract class Department {
        public abstract function createEmployee($id);
    
        public function fire($id) {
            $employee = $this->createEmployee($id);
            $employee->paySalary();
            $employee->dismiss();
        }
    }
    
    class ITDepartment extends Department {
        public function createEmployee($id) {
            return new Programmer($id);
        }
    }
    
    class AccountingDepartment extends Department {
        public function createEmployee($id) {
            return new Accountant($id);
        }
    }
    ```
    
6. Abstract Factory pattern
    - 구체적인 클래스를 지정하지 않고 관련 또는 종속 개체의 패밀리를 생성할 수 있는 생성 디자인 패턴

## 12. Command(=Action=Transaction)

- Behavioral pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2032.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2033.png)

- = Action = Transaction
- 요청을 객체로 캡슐화하며, 매개변수를 써서 여러 가지 다른 요구 사항을 집어넣을 수도 있는 패턴
    - 요청 내역을 큐에 저장하거나 로그로 기록할 수 도 있으며, 작업 취소 기능도 지원 가능
    - client는 command가 어떻게 생성되는지, 어떻게 수행되는지 전혀 신경 안써도 됨 ⇒ decoupling!
- 기능을 실행하고, 수행 스케쥴을 만들고, 먼 곳에서 사용할 때 유용함
- command는 간단한 클래스 이므로, 이것을 직렬화하고, 저장(database or text file)하고, 나중에 initial command로 복원하여 사용할 수도 있음 ⇒ 특정한 시간이나 특정한 상황에 command를 수행할 수 있게 만들기 유용함
- 복원되어야 하는 커맨드에 적용하는 것이 가장 유명함(ex. undo) ⇒ 이러한 경우 수행된 기능의 history를 stack으로 가지고 있어야 함
- 재사용가능하고 깔끔한 코드를 만드는 것이 가능하게 만들어줌! ⇒ SRP, OCP in SOLID
- 주로 UI와 business logic을 연결하는 역할을 함
- request 를 보내는 곳(UI)인 “Sender”에서 실제 완성되어야 할 로직을 갖고 있는 “Receiver”에 request를 바로 보내는 대신 “Command”를 내려줌 ⇒ Command가 UI와 logic layers의 coupling을 줄여주는 중간 layer 역할을 하게 됨
- 구성

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2034.png)

1. Command : 작업을 수행하기 위한 interface 선언
2. Concrete Command : receiver에 상응하는 작업을 실행하는 requests 선언
3. Invoker(=Sender) : request를 직접 Receiver에게 보내는 대신 command를 발동 시킴. 명령의 리스트를 저장하고 이 리스트에 맞춰서 동시 수행, 이전 수행 취소 등을 함
4. Receiver : request를 수행과 관련된 작업을 어떻게 수행하는지 아는 클래스. 어떠한 클래스도 receiver 역할 가능
5. Client: Concrete Command object를 선언하고 Receiver를 묶음
- 적용성
    - 작업으로 객체를 매개변수화하려는 경우 사용
    - 작업을 대기열에 넣거나 실행을 예약하거나 원격으로 실행하려는 경우 사용
    - 되돌릴 지도 모르는 작업을 구현하려는 경우 사용 ⇒ Memento 와 함께 사용됨
- 장점
    - 연산을 유발하는 클래스와 연산을 수행하는 클래스를 분리할 수 있음 ⇒ Single Responsibility Principle
    - 새 command를 코드 수정없이 추가할 수 있음 ⇒ Open/Closed Principle
    - undo/redo 기능을 추가할 수 있음
    - 지연 작업 실행을 구현할 수 있음
    - 여러 개 간단한 command를 조합해 하나의 복잡한 command를 만들 수 있음
- 단점
    - sender와 receiver 사이에 새로운 layer를 추가하는 것이기 때문에 코드가 다소 복잡해질 수 있음
- 다른 패턴과의 관계
    - Chain of Responsibility, Mediator, Observer, Command
        - sender와 receiver를 연결하는 여러가지 방법을 보여줌
            - Chain of Responsibility
                - 잠재적 receiver 중 하나가 처리할 때까지 잠재적 receiver의 동적 사슬을 따라 순차적으로 요청을 전달하는 구조
            - Command
                - receiver와 sender 간 단방향 연결
            - Mediator
                - receiver와 sender 간의 직접 연결을 제거하여 mediator 개체를 통해 간접적으로 통신하도록 하는 구조
            - Observer
                - receiver가 수신 요청을 동적으로 구독 및 구독 취소할 수 있음
    - Chain of Responsibility
        - Chain of Responsibility의 핸들러를 Command 패턴을 이용해서 구현할 수 있음
            - 요청으로 표시되는 동일한 컨텍스트 개체에 대해 다양한 작업을 실행할 수 있음
            - 또 다른 접근 방식: 요청 자체가 Command 개체
                - 체인에 연결된 일련의 서로 다른 컨텍스트에서 동일한 작업을 실행할 수 있음
    - Memento
        - undo 기능을 적용하기 위해서 Command 패턴과 같이 사용할 수 있음
            - Command는 다양한 연산을 목표 객체에 적용하는 것에만 신경 쓰면 되고, Memento는 Command가 수행되기 전 객체의 상태만 기억하는 것에만 신경 쓰면 됨
    - Strategy
        - 둘다 객체를 파라미터로 갖기 때문에 비슷해보일 수 있음
        - 하지만, 다른 의도로 사용됨
            - Command: 연산을 객체로 바꾸려는 의도 ⇒ 작업 실행을 연기하고, 대기열에 추가하고, 명령 기록을 저장하고, 원격 서비스에 명령을 보내는 등의 작업을 수행할 수 있음
            - Strategy:  같은 일을 하는 다른 알고리즘을 자유롭게 교체해서 사용하기 위한 의도
    - Prototype
        - Prototype은 Command 사본을 기록에 저장해야 할 때 도움이 될 수 있음
    - Visitor
        - Visitor를 Command의 강력한 버전이라고 생각해도 무방함
            - 다른 클래스의 다양한 객체에 대해 작업을 실행할 수 있음

## 13. Memento(=Token)

- Behavioral Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2035.png)

- = Token
- 캡슐화를 위반하지 않고, 객체의 상태를 외부에 snapshot으로 저장하고, 필요에 의하여 원하는 시점의 데이터를 복원할 수 있는 패턴
- 다음 예시 상황을 참고
    - 텍스트 에디터 앱을 만들 때 실행 취소 기능을 만들 것임
        - 직관적인 방법
            - 모든 행위를 수행하기 전에 앱의 모든 객체의 상태를 기록하고, 장치에 저장
            - 이후에 유저가 해당 행위를 되돌리기 원할 때, 앱은 저장한 이력에서 마지막 스냅샷을 꺼내와서 모든 객체의 상태를 복구
        - 문제
            1. 객체의 모든필드들을 조회해서 값을 복사한 후 저장소로 옮겨야함
                - 객체가 외부에 대해 자신의 접근제한을 많이 오픈해야 제대로 동작함 → 은닉화를 풀어야하는 상황
            2. 은닉화를 풀게 되면, 에디터 클래스들을 다시 손보거나 필드들을 일부 추가 및 삭제하면 영향 받는 객체들의 상태 역시 변경해야 함
            3. 필드 전체를 복사하니 스냅샷의 데이터가 엄청나게 많을 것임
            
            ⇒ 클래스의 세부사항을 노출시키거나, 상태의 접근 제한해서 스냅샷을 생산하는게 불가능해짐
            
- 메멘토 패턴의 원리
    - 스냅샷 상태를 만드는 일을 실제 주인인 originator 객체에 위임
        - 다른 객체들이 외부에서 에디터의 상태를 복사하지 않고, 접근권한을 모두 갖고 있는 데이터 클래스 자신이 스냅샷을 만들 수 있음
    - 객체의 상태를 복사해서 “memento”라고 불리는 특별한 객체에 저장
        - 내부는 해당 내용을 생성한 객체 외에 다른 객체들은 접근할 수 없음
        - 원본이 아닌 다른 객체들은 제한된 인터페이스로 스냅샷에 포함된 원본 객체의 상태가 아니라 스냅샷의 메타데이터(생성시간, 수행된 행위명)만 갖고 올 수 있음
    - 이런 제한된 정책을 구현하기 위해서는 “caretaker” 라고 하는 다른 객체안에 메멘토를 저장해야 함
        - 제한된 인터페이스로만 메멘토와 협업하기 때문에, 메멘토 안에 저장된 상태를 함부로 변경할 수 없음
        - 동시에 originator는 메멘토내의 모든 필드에 접근할 수 있기 때문에 이전 상태를 복구할 수 있게 됨
- 구성

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2036.png)

1. Memento
    - concrete memento의 fields에 접근을 제한하는 인터페이스
    - 오직 memento의 메타데이터, caretaker 에 의해 사용되는 메소드를 정의함
2. Concrete Memento
    - originator의 내부 상태 스냅샷 역할을 하는 값(Value Object)
    - concrete memento를 생성한 originator를 제외한 다른 객체의 접근을 막음
3. Caretaker
    - memento 보관을 책임지는 보관자
    - memento의 내용을 검토하거나 그 내용을 건드리지 않음
    - memento 스택을 저장함으로써 originator의 히스토리 추적
    - originator가 이전 상태를 알아야 할 때, 스택으로부터 최상위 원소를 가져와서 originator 복구 메소드로 전달함
4. Originator
    - 원본 객체를 의미
    - 상태를 저장함
    - 필요할 때 스냅샷으로 부터 해당 상태를 복구할뿐만 아니라, 자기 자신 상태의 스냅샷을 생산하기도 함

- 객체의 fields/getters/setters에 직접 접근이 캡슐화 원칙을 위배할 때, 보안의 이유로도 사용될 수 있음
    - 다른 object가 snapshot을 읽지 못하게 만들어 original object의 state를 안전하고 보안이 강화되게 만듬
- Command vs Memento
    - command 패턴은 redo/undo를 지원할 수 있지만 요청을 단일객체로 만들 수 있음
    - memento 패턴은 cache/restore 개념으로 객체의 내부 상태를 저장하고 있다는 것이 핵심
    - command 패턴은 상태를 사용하는 부분에 따로 보관해야했지만, memento 패턴은 state를 originator에 보관하게 되어 상태가 안전할 수 있다
    - 둘 중 하나만 사용해야 하는 개념은 아님
        - memento 패턴을 이용하여 객체의 내부 상태를 저장하고 있어야 할 때, 되돌리기 기능 제공시 명령 패턴을 함께 사용할 수 있기 때문
- 적용성
    - 객체의 이전 상태를 복원할 수 있도록 객체 상태의 스냅샷을 생성하려는 경우 사용
    - 객체의 field/getter/setter에 대한 직접 액세스가 캡슐화를 위반할 때 사용
- 장점
    - 캡슐화를 위반하지 않고 객체 상태의 스냅샷을 생성할 수 있음
    - Caretaker가 Originator의 상태 기록을 유지하도록 하여 발신자의 코드를 단순화할 수 있음
- 단점
    - Memento를 너무 자주 만들게 되면 메모리 사용이 많아짐
    - Caretaker는 오래된 Memento를 파괴할 수 있도록 Originator의 수명 주기를 추적해야 함
    - PHP, Python 및 JavaScript와 같은 대부분의 동적 프로그래밍 언어는 Memento 내의 상태가 그대로 유지된다고 보장할 수 없음
    - 상태를 저장하고 복구하는 데 시간이 오래 걸릴수 있음
        - 직렬화 해서 저장하는 것이 좋음
- 다른 패턴과의 관계
    - Command
        - undo 기능을 적용하기 위해서 Command 패턴과 같이 사용할 수 있음
            - Command는 다양한 연산을 목표 객체에 적용하는 것에만 신경 쓰면 되고, Memento는 Command가 수행되기 전 객체의 상태만 기억하는 것에만 신경 쓰면 됨
    - Iterator
        - Memento와 Iterator를 함께 사용하여, 현재 상태를 알고, 또 필요한 경우 되돌릴 수 있음
    - Prototype
        - Prototype이 Memento의 간단한 대안이 될 수도 있음
            - 히스토리에 저장하려는 상태인 객체가 간단하고 외부 리소스에 대한 링크가 없거나 링크가 재설정하기 쉬운 경우 대안으로 채택할 수 있음

## 14. Prototype

- Creational Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2037.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2038.png)

- 원형이 되는 인스턴스를 사용하여 생성할 객체의 종류를 명시하고, 이렇게 만든 견본 인스턴스를 복사하여 새로운 객체를 생성하는 패턴
- 클래스에 의존하지 않고, 객체를 복사할 수 있음
- 상황
    - 프레임워크에 추상화된 Graphic 클래스가 정의되어 있음
    - Graphic 객체의 인스턴스를 생성해서 문서에 추가하는 도구에 대한 GraphicTool 서브클래스 정의되어 있음
    - GraphicTool 클래스가 응용프로그램에만 국한된 게 아니고 범용 프레임워크임
        - GraphicTool 클래스가 어떻게 Graphic의 서브클래스들을 생성해야 하는지 알 수 없음
        - 이렇게 되면 각 Graphic 객체마다 서브클래스들을 만들어야 함
    - 이러한 문제를 해결하기 위해서는 GraphicTool 클래스가 Graphic 서브클래스의 인스턴스들을 복제하여 새로운 Graphic 인스턴스를 생성해야 하며, Graphic 서브 클래스의 인스턴스가 프로토타입이 됨
- 세부사항은 알 필요 없이, 복잡한 상태의 개체를 복사하려는 경우 유용함
    - 새 개체를 초기화하는 것만으로는 충분하지 않고, 유효한 복사본이어야 할 때
- 새로운 객체를 생성하기 위해 다른 Prototype 객체로 클래스를 구성할 수 있기 때문에 런타임 유연성을 가능하게 함
- Prototype 객체는 런타임에 동적으로 추가 및 제거될 수 있음
- 분석

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2039.png)

1. Prototype
    - 스스로를 복제하는 interface 선언
    - 주로 clone 이라는 이름의 메소드를 가지지만, declared/defined 라는 메소드를 가질 수도 있음
2. ConcretePrototype
    - 스스로 복제하는 기능 구현
    - 원본 복사하는 것 외에도, 연결된 객체 복제, 재귀 종속성 풀기 등과 관련된 복제 프로세스의 일부 극단적인 경우를 처리할 수도 있음
3. SubclassPrototype
    - ConcretePrototype과 같은 목적을 가지지만, 때로는 행위 같은 인자를 정의하여 base class를 확장할 수 있음
- 사용성
    - 복제해야 하는 구체 클래스에 코드가 종속되지 않게 하기 위해 사용
    - 오직 초기화 하는 방법만 다른 각각의 subclass를 줄이기 위해 사용
- 장점
    - 구체 클래스에 의존하지 않고 객체를 복제하는 것이 가능
    - 반복되는 초기화 코드를 없앨 수 있음
    - 복잡한 객체를 편하게 만들 수 있음
    - 복잡한 객체의 초기구성을 만들 때, 상속 대신 다른 방법을 제공
- 단점
    - 의존성이 순환하는 복잡한 객체를 복제할 때 까다로움
- 다른 패턴과의 관계
    - Factory Method
        - Factory Method에서 조금씩 발전하여 Abstract Factory, Prototype, Builder 패턴으로 발전하였음
    - Abstract Factory
        - 보통 Abstract Factory는 Factory Method의 세트로 구성되지만, Prototype의 세트로 구성할 수도 있음
    - Command
        - command 복제본을 저장해야 할 때 Prototype이 도움을 줄 수 있음
    - Composite, Decorator
        - Composite과 Decorator를 많이 사용하는 디자인에서는 Prototype을 사용하며 이점을 얻을 수 있음
            - 패턴을 적용하면 처음부터 다시 구성하는 대신 복잡한 구조를 복제할 수 있음
    - Factory Method
        - Prototype은 복제된 객체의 복잡한 초기화가 필요하지만, 상속으로 인한 단점이 없음
        - Factory Method는 상속을 기반으로 하지만 초기화 단계가 필요하지 않음
    - Memento
        - Prototype이 Memento의 간단한 대안이 될 수도 있음
            - 히스토리에 저장하려는 상태 객체가 간단하고 외부 리소스에 대한 링크가 없거나 링크가 재설정하기 쉬운 경우
    - Singleton
        - Prototype은 Singleton 로 구현될 수 있음

## 15. Proxy(=Surrogate)

- Structural Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2040.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2041.png)

- 다른 객체에 대한 접근을 제어하기 위한 역할
- 문제 상황
    - 많은 시스템의 리소스를 사용하는 객체가 있으나 언제나 필요한건 아님
    - Lazy Loading으로 구현이 가능하지만, 필요 시점에만 객체를 생성하고, 후에 모든 클라이언트는 해당 객체를 초기화 하는 방법은 코드 중복이 너무 많이 발생하게 됨
    - 해당 객체에 직접 주입하는 방법도 있지만, 3rd-party 라이브러리 라면 이 방법 역시 불가능
- 해결책
    - 프록시 패턴이 원본 서비스를 제공하는 객체와 동일한 인터페이스를 구현하는 새로운 프록시 클래스를 생성하여 이 문제를 해결함
    - 클라이언트가 요청을 보내면, 프록시 클래스는 실제 서비스 객체를 만들고, 요청을 위임
    - 이렇게 하면 좋은 점?
        - 원본 서비스 클래스의 변경없이 전처리나 후처리 기능을 제공할 수 있음
        - 원본 서비스 객체의 인터페이스를 동일하게 구현하기 때문에 클라이언트 입장에서는 원본 서비스를 사용하는 것과 다를바가 없음
- 실제 예시
    - 신용카드는 은행 계좌를 위한 프록시이며, 은행 계좌는 현금을 위한 프록시임
    - 둘 다 결제행위를 할 수 있는 같은 인터페이스를 구현하고 있음
    - 소비자는 돈을 직접 들고 다니지 않아도 되기 때문에 상당히 편리함
    - 가게 주인 역시 보증금을 잃어버릴 위험요소를 감수하지 않아도 되기 때문에 편리함
- 구조
    
    ![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2042.png)
    
    1. ServiceInterface
        - Service와 Proxy를 위한 인터페이스 정의
    2. Service
        - 비즈니스 로직을 포함하고 있는 사용해야할 실제 객체 정의
    3. Proxy
        - 실제 서비스와 동일한 인터페이스를 구현
        - 접근을 제어하는 service 객체를 가리키는 참조도 포함해야함
        - 실제 객체를 생성, 삭제 하는데 책임이 있을 수 있음
    4. Client
        - 같은 인터페이스를 이용해 Service, Proxy 모두 소통함
        - service 객체를 요구하는 어떤 코드에 proxy를 할당할 수 있음
- 프록시 패턴 종류
    1. Virtual Proxy (lazy initialization)
        - Lazy Loading 개념으로, 요청이 필요한 때만 고비용 객체를 생성함
        - 초기 비용이 많이 드는 연산이 포함된 객체의 경우 가상 프록시를 사용했을 때 효과를 볼 수 있음
    2. Protection Proxy (access control)
        - 원격 객체에 대한 실제 접근을 제어함
        - 객체 별로 접근 권한이 다를 때 유용하게 사용 가능
    3. Remote Proxy (local executaion of remote service)
        - 서로 다른 주소공간에 존재하는 객체를 가리키는 대표 객체
        - 로컬 환경에 위치함
    4. Logging Proxy (logging request)
        - 원본 서비스에 접근하는 요청에 대한 기록을 남길 수 있음
    5. Caching Proxy (caching request results)
        - 캐시를 보관하는 프록시
- Decorator vs Proxy
    - 공통점
        - (Proxy 패턴에서 원본에 해당하는) ConcreteComponent는 (Proxy 패턴에서 프록시에 해당하는) 데코레이터를 통해 호출되는 몇 가지 동작을 구현
        - 공통 기본 클래스(common base class)로부터 상속
    - 차이점
        - 의도에서 차이가 남
            - 데코레이터는 기능을 추가하거나, (좀 더 일반적으로는) ConcreteComponent의 핵심 기능에 추가 기능을 동적으로 선택할 수 있는 옵션을 제공
            - 프록시는 세부적으로 정의된 하우스키핑 코드(housekeeping code)를 원본으로부터 분리하는 역할
- 사용성
    - 초기화 지연(Lazy Initialization)가 필요할 때 사용
    - 접근 제한(Access Control)이 필요할 때 사용
    - 원격 서비스 실행(Remote Service Execution)이 필요할 때 사용
    - 요청 정보를 캐시에 보관(Caching request result)할 필요가 있을 때 사용
    - 원본 서비스 접근 기록(Logging Request)이 필요할 때 사용
    - 무거운 객체를 사용 하지 않을 때 자동으로 메모리에서 제거하는 스마트 레퍼런스를 위해 사용
- 장점
    - 서비스 개체를 알고 있는 클라이언트 없이 서비스 개체를 제어할 수 있음
    - 클라이언트가 신경 쓰지 않아도 서비스 개체의 수명 주기를 관리할 수 있음
    - 서비스 개체가 준비되지 않았거나 사용할 수 없는 경우에도 사용할 수 있음
    - 새로운 Proxy를 기존 코드 수정 없이 추가할 수 있음 ⇒ Open/Closed Principle
- 단점
    - 새로운 클래스를 생성해야 하므로 코드가 복잡해질 수 있음
    - 서비스 객체로부터 응답이 늦을 수 있음
- 다른 패턴과의 관계
    - Adapter, Decorator
        - Adapter는 감싸진 객체에 다른 인터페이스를 제공
        - Proxy는 감싸진 객체에 같은 인터페이스를 제공
        - Decorator는 감싸진 객체에 증강된 인터페이스를 제공
    - Facade
        - 둘 다 복잡한 엔티티를 버퍼링하고 자체적으로 초기화함
        - Proxy는 서비스 객체와 동일한 인터페이스를 가지고 있어 상호 교환이 가능함
    - Decorator
        - 공통점
            - 두 패턴 모두 한 개체가 일부 작업을 다른 개체에 위임해야 하는 구성 원칙을 기반으로 함
            - (Proxy 패턴에서 원본에 해당하는) ConcreteComponent는 (Proxy 패턴에서 Proxy에 해당하는) Decorator를 통해 호출되는 몇 가지 동작을 구현
            - 공통 기본 클래스(common base class)로부터 상속
        - 차이점
            - 의도에서 차이가 남
                - 데코레이터는 기능을 추가하거나, (좀 더 일반적으로는) ConcreteComponent의 핵심 기능에 추가 기능을 동적으로 선택할 수 있는 옵션을 제공
                - 프록시는 세부적으로 정의된 하우스키핑 코드(housekeeping code)를 원본으로부터 분리하는 역할
            - Proxy는 일반적으로 자체적으로 서비스 개체의 수명 주기를 관리
            - Decorator의 구성은 항상 클라이언트에 의해 제어됨

## 16. Decorator(=Wrapper)

- Structural Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2043.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2044.png)

- 객체에 동적으로 새로운 책임을 추가할 수 있게 해주는 패턴
- 시나리오
    - GUI 툴킷이 있다고 가정. 모든 사용자 UI 요소에는 필요 없지만, 어떤 특정 사용자 UI 요소에만 스크롤링이나 테두리 같은 속성을 추가할 필요가 있음.
    - Text 를 출력하는 서비스를 제공하는 TextView 클래스가 있다고 가정하자. 이 TextView에 스크롤 기능이나 두꺼운 테두리가 필요하다면 어떻게 해결해야 할까
        - 직관적인 해결책은 상속
        - 이미 존재하는 클래스를 상속받고, 또 다른 클래스에서 테두리 속성을 상속받으면 이 서브 클래스 인스턴스는 테두리라는 속성을 갖는다
    - 하지만 언제 어떻게 테두리를 장식해야할 지 제어해야한다면 난감한 상황이 펼쳐짐
    - 모든 TextView가 아니라 특정 TextView 에만 스크롤이나 테두리 기능이 필요하다면, 상속보다는 장식자(Decorator) 패턴을 사용하는것이 좋음
        - 테두리를 추가해야하는 객체를 한번 더 감싸는 것
- decorator는 각각 서로 독립적이므로  다양한 동작을 구현하기 위해 추가하고 합쳐질 수 있음
- 상속을 이용한 확장이 실용적이지 못할 때 유용한 패턴
- 코드 복잡성을 증가시킬수 있으므로 사용에 주의 해야함
- 분석

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2045.png)

1. Component
    - 객체를 위한 인터페이스 제공
2. Concrete Component
    - 기본적인 동작 선언
    - decorator에 의해서 기본 동작은 변경될 수 있음
3. Base Decorator
    - component 인터페이스로 선언된 객체를 감싼 객체를 참조하는 필드를 가짐
    - concrete components와 decorators를 모두 가질 수 있음
4. Concrete Decorators
    - component에 동적으로 추가할 수 있는 행동 선언
5. Client
    - concrete componet를 선언하고 여러 층의 decorator로 감싸 사용
- 구현할 때 고려할 점들
    - Component는 장식을 추가할 베이스가 되는 역할이므로 작고 가볍게 정의
        - 가급적 인터페이스만 정의
        - 무언가 저장하는 변수를 정의하지 않음
        - 저장할 것이 있으면 서브클래스에서 하자
    - 상속 구조를 통해 Decorator와 Component가 같은 구조를 갖게 하자
        - 투과적 인터페이스: Decorator로 계속해서 감싸도 Component 메소드는 계속 사용할 수 있음
    - 코드를 수정하지 않고도 준비된 Decorator를 조합해 기능을 추가할 수 있도록 생각해서 구현
    - 비슷한 성질의 작은 클래스가 많아질 수 있다는 단점을 고려
    - 구현하려는 내용이 객체의 겉을 변경하려는 것인지 속을 변경하려는 것인지 생각해보자
        - 속을 변경하는 것이라면 전략 패턴을 선택하는 것이 더 적절할 수 있음
    - 데코레이터 패턴으로 구현한 다음, 사용이 까다롭게 느껴지거나 자주 쓰는 조합이 있다면 다음 패턴을 사용하는 것을 고려해보자
        - Builder pattern
        - Factory pattern
        - Static factory method
    - Decorator가 다른 Decorator에 대해 알아야 할 필요가 있다면, Decorator 패턴의 사용 의도와 어긋나는 작업일 수 있음
    - 재귀적으로 기능을 갖게하는 방법 외에도, Decorator를 추가할 때 마다 얻은 아이템을 List로 관리하는 방법도 있음
- 주의사항
    - 데코레이터가 여러 개 있다면 순서에 주의
    - 코드가 여러 클래스로 흩어져 디버깅이 까다로워지고, 이해하기 어려울 수 있음
    - public 메소드가 많다면 Decorator을 적용하는 것이 바람직하지 않을 수 있음
- 사용성
    - 런타임 중 어떤 객체를 사용하는 코드들을 망치지 않고 해당 객체에 행동을 추가하고 싶을 때 사용
    - 상속을 이용해서 객체의 행동을 확장하는 것이 불가능하거나 어색할 때 사용
- 장점
    - 서브클래스를 만들지 않고 객체를 확장할 수 있음
    - 런타임에 특정 객체로 부터의 책임을 추가하거나 제거할 수 있음
    - 여러개의 Decorator들로 객체를 합쳐 행동 조합을 합칠수 있음
    - 여러개의 행위를 하던 monolithic한 클래스를 여러개의 작은 클래스로 나눌수 있게 됨 ⇒ Single Responsibility Principle
- 단점
    - wrapper 스택으로 부터 특정 wrapper를 제거하는 것이 어려움
    - 동작이 Decorator 스택의 순서에 의존하지 않는 방식으로 Decorator를 구현하는 것은 어려움
    - 초기 계층 설정에 관한 코드가 깔끔하지 못함
- 다른 패턴과의 관계
    - Adapter, Proxy
        - Adapter는 다른 인터페이스를 제공
        - Proxy는 같은 인터페이스를 제공
        - Decorator는 증강된 인터페이스를 제공
    - Adapter
        - Adapter는 인터페이스를 변환하지만 Decorator는 인터페이스의 변환없이 객체를 감싼다
    - Chain of Responsibility
        - 매우 비슷한 클래스 구조(recursive composition)를 가짐
        - 차이점
            - Chain of Responsibility handler 는 서로 독립적으로 임의의 작업을 실행할 수 있음. 또한 언제든지 요청을 더 이상 전달하지 않을 수 있음
            - 데코레이터는 기본 인터페이스와 일관성을 유지하면서 객체의 동작을 확장할 수 있음. 또한 데코레이터는 요청의 흐름을 중단할 수 없음
    - Composite
        - 비슷한 구조 다이어그램을 가짐. 두 패턴 모두 다 재귀 형태를 갖는다
            - Decorator는 자식이 1개, Composite 패턴은 자식이 1~n개 가능
            - Decorator는 감싸진 객체에 추가적인 책임을 더하는 반면, Composite은 단지 자식들의 결과를 합산하는 역할만 함
            - 하지만 두개의 패턴을 합칠 수 있음
                - Decorator를 사용하여 Composite tree에서 특정 개체의 동작을 확장할 수 있음
    - Composite, Prototype
        - Composite과 Decorator를 많이 사용하는 디자인에서는 Prototype을 이용하여 이점을 얻을 수 있음
            - Prototype을 처음부터 다시 구성하는 대신 복잡한 구조를 복제할 수 있음
    - Strategy
        - Decorator는 외부를 바꾸고, Strategy는 속을 바꾸는 역할을 함
    - Proxy
        - 공통점
            - 두 패턴 모두 한 개체가 일부 작업을 다른 개체에 위임해야 하는 구성 원칙을 기반으로 함
            - (Proxy 패턴에서 원본에 해당하는) ConcreteComponent는 (Proxy 패턴에서 Proxy에 해당하는) Decorator를 통해 호출되는 몇 가지 동작을 구현
            - 공통 기본 클래스(common base class)로부터 상속
        - 차이점
            - 의도에서 차이가 남
                - 데코레이터는 기능을 추가하거나, (좀 더 일반적으로는) ConcreteComponent의 핵심 기능에 추가 기능을 동적으로 선택할 수 있는 옵션을 제공
                - 프록시는 세부적으로 정의된 하우스키핑 코드(housekeeping code)를 원본으로부터 분리하는 역할
            - Proxy는 일반적으로 자체적으로 서비스 개체의 수명 주기를 관리
            - Decorator의 구성은 항상 클라이언트에 의해 제어됨

## 17. Bridge(=handle/body)

- Structural Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2046.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2047.png)

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

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2048.png)

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

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2049.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2050.png)

- construction과 representation을 분리하여, 같은 construction process가 여러가지 representation을 만들 수 있게 하는 패턴
- 주 목적: 생성 과정(logic)이 복잡한 객체(data)를 분리하려는 목적
    - 복잡한 객체(complex object): (특정한 기준은 없지만) constructor를 부르는 것만으로 끝나지 않는 객체(=추가적인 params나 method를 불러야 함)
- 객체 생성을 추상화 하여, 여러가지 다른 representation을 제공할 수 있도록, 생성 과정을 조정할 수 있게 함
- 객체 생성코드를 본래의 클래스로부터 builder 라는 것을 분리할 수 있게 만드는 패턴
    - builder: 같은 interface를 따르고 분리된 생성 과정을 채택한 것
    - 객체의 다른 representation을 만들고 싶다면, 다른 builder class를 만들고, 생성 과정을 추가하면 됨
- director라는 layer를 추가하여 객체 생성의 세부사항을 숨길 수 있음
    - builder interface와 생성 순서를 알고 있음
    - 필수로 필요한 것은 아님
- 구조

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2051.png)

1. Builder
    - Product의 부분들을 만들기 위한 모든 종류의 Builder의 interface를 가지고  있는 추상 인터페이스
2. Concrete Builder
    - 상세한 제조 과정을 정의. 각 Concrete Builder가 Product를 정의하고 상태를 추적함
3. Director
    - Builder interface를 사용하여 객체를 생성하고, 생성 순서를 정의하여 외부에서 사용할 수 있게 함
4. Product
    - 복잡하게 생성되는 객체를 의미하고, 각 파트들을 최종 결과로 만드는 interface/methods 를 외부에서 사용할 수 있게 만듬
5. Client
    - 특정 Builder 객체를 Director와 연결함. Product 객체는 Director class 인스턴스를 호출하여 생성
- 적용 가능성
    - "망원경 생성자" 를 제거하기 위해 사용
    - 코드가 일부 제품(예: 석조 및 목조 주택)의 다른 표현을 생성할 수 있도록 하기 위해 사용
    - Composite Tree 또는 기타 복잡한 개체를 구성하기 위해 사용
    - 서로를 참조하는 동일한 생성자 클래스를 다수 가지고 있다면 사용
        - 다수의 optional parameters를 가지고 있는 상황, default 값을 가지는 몇가지 짧은 버전의 constructor를 가지고 있을 때
        - 생성 과정은 비슷하지만, 세부사항이 다를 때
    - 복잡한 객체를 생성하는 알고리즘이 객체를 이루고 있는 파트와 독립적일 때 사용
- 장점
    - 개체를 단계별로 구성하거나 구성 단계를 연기하거나 재귀적으로 단계를 실행할 수 있음
    - 제품의 다양한 표현을 작성할 때 동일한 구성 코드를 재사용할 수 있음
    - 복잡한 객체 생성 코드를 비즈니스 로직과 분리할 수 있음 ⇒ Single Responsibility Principle
- 단점
    - 여러 개의 새로운 클래스를 생성해야 하기 때문에 코드를 복잡하게 만듬
- 다른 패턴과의 관계
    - Factory Method
        - Builder는 Factory Method로부터 시작하여 발달한 패턴
    - Abstract Factory
        - Builder는 복잡한 객체를 단계별로 구성하는데 중점을 둠
        - Abstract Factory는 관련 객체의 패밀리 생성에 중점을 둠
        - Abstract Factory는 객체를 즉시 반환하지만 Builder를 사용하면 객체를 가져오기 전에 몇 가지 추가 구성 단계를 실행할 수 있음
    - Composite
        - Composite tree를 구성할 때 Builder 패턴을 사용할 수 있음
            - 재귀적으로 작동하도록 생성 step을 프로그래밍 할 수 있기 때문
    - Bridge
        - Builder 패턴과 Bridge 패턴을 합쳐서 사용할 수 있음
            - Director 클래스는 Abstraction 역할을 하는 반면 다른 Builder 는 Implementation 역할을 함
    - Singleton
        - Builder 패턴은 Singleton으로 구현 될 수 있음

## 19. Flyweight

- Structural Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2052.png)

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

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2053.png)

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

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2054.png)

- 일련의 핸들러를 따라 요청을 전달할 수 있는 패턴
- 요청을 받으면 각 핸들러는 요청을 처리할지 아니면 체인의 다음 핸들러로 전달할지 결정
- 문제 상황
    - 온라인 주문 시스템을 구축한다고 가정해보자. 많은 기능들이 필요하겠지만 유저에 대한 인증이나, Admin 권한을 가진 사용자의 경우 모든 주문을 조회한다던지 하는 기능들이 필요할것이다.
    
    시스템이 비대해져가면서 비밀번호 brute force 어택을 막기 위한 기능, 요청에 대한 validation, 같은 요청에 대해 cache를 반환하는 기능이 필요할수도 있다.
    
    이 상태에서 또 다른 기능을 추가하면 로직은 복잡해진다. 하나를 변경할 때 다른 기능에 영향을 줄 수도 있고, 만약 이 기능들중 일부분의 기능이 다른 기능구현에 필요하다면 중복코드가 발생한다. 이렇게 되면 시스템을 관리하며 유지보수하기가 매우 힘들어진다
    
    ![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2055.png)
    
- 해결책
    - 다른 행동 패턴들과 유사하게 책임 연쇄 패턴도 핸들러라는 단일 객체를 사용한다. 위의 문제점과 같은 상황에서는 각 단계별 행동들이 단일 메소드를 가지는 클래스가 되고, 요청은 단일 메소드의 인자가 된다.
    - 책임 연쇄 패턴은 핸들러들을 연결하여 체인 형태로 구성한다. 체인에서 각 핸들러들은 다음 핸들러를 참조하는 필드를 가지고 있으며, 요청을 처리하고 넘긴다.
    - 또 하나의 특징이 있는데 마치 알고리즘에서 더 탐색할 필요가 없는 그래프 경로를 탐색하지 않는 가지치기 처럼, 각 핸들러는 요청을 다음 핸들러에 넘길지 말지 결정할 수 있다.

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2056.png)

- 패턴 사용시 여러 핸들러를 하나의 체인으로 연결하고 클라이언트가 해당 체인을 따라 요청을 전달할 수 있음 ⇒ **각 핸들러는 요청을 수신하고 처리 및/또는 추가로 전달**
- 요청 추가/제거/재정렬/처리순서 변경 할 수 있음
- 여러 종류의 요청을 다양한 방식으로 처리할 것이 예상되지만, 요청이나 처리 순서가 컴파일 타임에 정해지지 않는 경우 사용 해야함
- 주의해야 할 점
    - 요청 수행이 보장되지 않음
    - 발신자와 수신자 사이에 느슨한 결합을 도입하고 요청이 체인의 모든 핸들러에 의해 처리될 수 있기 때문에 실제로 처리된다는 보장이 없음
- 분석

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2057.png)

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

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2058.png)

- 알고리즘을 알고리즘을 실행하는 객체로 부터 분리하는 패턴
- 개체 구조의 요소에 대해 수행할 작업을 나타냄
- 작동하는 요소의 클래스를 변경하지 않고 새 작업을 정의할 수 있음
- tree나 collection의 복잡한 데이터 구조가 있고, 각 데이터 요소 클래스를 변경하지 않고 기능을 변경하고 싶을 때 사용
- 핵심 아이디어
    - 각각의 특정 복합 객체 클래스에 대해 double-dispatch 작업을 정의하는 것
    - Visitor 패턴의 맥락에서 이를 accept라고 함
    - client가 개체 구조를 탐색할 때, 각 요소의 accept 메서드가 호출되어 요청을 특정 방문자 개체에 위임하고 이 개체는 매개변수로 메서드에 전달. 그런 다음, Visitor 개체의 특정 메서드가 호출되어 실제 요청을 수행
- 분석

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2059.png)

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

## 22. Mediator

- Behavioral Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2060.png)

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2061.png)

- Intermediary/Controller 라고 불리기도 함
- 상호작용 로직을 객체로부터 분리하고, Mediator라는 컨트롤러에 이동시켜, 상호 교류하는 객체들간의 의존성을 줄여주는 패턴
- 객체 묶음이 어떻게 상호작용 하는지를 묶은 객체를 정의
- 객체끼리 서로 선언되는 것을 막아 loose coupling을 장려함
- 상호작용을 다양하게 만들어 줌
- colleagues: 서로 상호작용하는 객체들
    - colleagues는 서로에 대한 정보가 없고, 오직 mediator만 알고 있음 ⇒ colleagues들은 loosely coupled
- 객체끼리 상호작용 하는것을 간단화, 추상화 함
    - 기존의 N:M의 객체간 상호작용을, Mediator를 통해 1:N의 상호작용으로 만들어줌 ⇒ 이해하고 유지하기 쉬움
    - colleagues들은 communication act는 알아야 하지만, 디테일은 전혀 알 필요가 없음 ⇒ colleagues들을 바꾸지 않고 Mediator를 추가하는 것이 가능해짐
- 구조

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2062.png)

1. Mediator
    - 컴포넌트들과 상호작용하기 위한 인터페이스 정의
2. Concrete Mediator
    - 컴포넌트를 정의하여 컴포넌트간의 관계를 묶음
3. (Optional) Abstract Component or Component Interface
    - 유사하게 상호작용하는 컴포넌트가 상속할 수 있는 클래스
4. Concrete component or Colleague
    - Mediator가 참고하는 요소
    - 각각의 colleague는 다른 colleague와 소통하기 위해 Mediator와 소통함
    - Component들은 서로를 알고 있어서는 안됨 ⇒ 무조건 Mediator를 거쳐서 소통해야 함
    
- 적용
    - 다른 클래스와 밀접하게 coupled 되어 있기 때문에 일부 클래스를 변경하기 어려울 때 사용
    - 컴포넌트가 다른 컴포넌트에 너무 의존적이어서 다른 프로그램에서 컴포넌트를 재사용할 수 없을 때 사용
    - 다양한 컨텍스트에서 몇 가지 기본 동작을 재사용하기 위해 수많은 구성 요소 하위 클래스를 만들어야 한 경우 대신 사용
    - 구동중에 컴포넌트를 추가할 필요가 있을 때 사용
    
    💣 모든 communication logic을 추가하면 God Object가 될 가능성이 존재함
    
    - Mediator는 오직 communication만 책임진다는 것을 유의하고 사용해야 함
    - 연산, 데이터 변환 등 관계 없는 기능이 Mediator에 없도록 잘 작성해야 함
- 장점
    - 여러개의 컴포넌트 간 상호작용을 하나로 묶을 수 있다 ⇒ Single Responsibility Principle
    - 기존 코드 수정 없이 새로운 Merdiator를 추가할 수 있음 ⇒ Open/Closed Principle
    - 각각의 컴포넌트를 쉽게 재사용할 수 있다
- 단점
    - Mediator가 God Object가 될 수도 있음
- 다른 패턴과의 관계
    - Chain of Responsibility, Command, Observer
        - 요청의 sender와 receiver을 연결하는 다양한 방법 제시
            - CoR : 잠재적 수신자 중 하나가 처리할 때까지 잠재적 수신자의 동적 사슬을 따라 순차적으로 요청을 전달
            - Command : 발신자와 수신자 간의 단방향 연결을 설정
            - Mediator : 송신자와 수신자 간의 직접 연결을 제거하여 중재자 개체를 통해 간접적으로 통신하도록 함
            - Observer : 수신자가 수신 요청을 동적으로 구독 및 구독 취소할 수 있음
    - Facade
        - 밀접하게 coupled된 클래스 사이의 상호작용을 정리해준다는 비슷한 역할을 함
        - Facade: 간단한 subsystem 인터페이스를 제공하지만, 새로운 기능을 추가하진 않음. subsystem은 facade를 모르고 subsystem 객체들은 서로서로 소통함
        - Mediator: system의 컴포넌트간의 상호작용을 중재함. 각각의 컴포넌트는 mediator만 알고 다른 컴포넌트는 아예 모름
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

## 23. Observer

- Behavioral Pattern

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2063.png)

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

![Untitled](OOP%20Design%20Pattern%209afd8ac1e48a41bf81e9c143a8b3eb6a/Untitled%2064.png)

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