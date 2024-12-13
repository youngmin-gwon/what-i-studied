# Strategy(=Policy)

#oop, #design-pattern, #behavioral-pattern

## Description

![Untitled](../../../../_assets/oop/Untitled%2014.png)

![Untitled](../../../../_assets/oop/Untitled%2015.png)

- 알고리즘 집단을 만들고, 각각을 캡슐화 한 후, 집단의 각각을 교환가능하게 만드는 것이 목적
- 가장 실용적인 디자인 패턴 중 하나
- 객체 내부에서 다른 계산로직을 사용하거나 알고리즘을 run-time 중 동적으로 바꾸고 싶을 때 사용
- 새로운 알고리즘을 추가함으로 로직을 바꿀 필요가 없으므로 [[SOLID]] 중 [[OCP(Open Closed Principle)]] (O in SOLID) 를 성립하게 만들어줌
- 예시
  - Sorting algorithms: 각각의 정렬 알고리즘을 추출하여 각각의 클래스로 만들고 sort() 할 수 있는 interface를 만들어 사용
  - Payment strategies : 각각의 결제 방법을 클래스로 만들고 사용자의 선택에 따라 알고리즘 수행
  - Damage calculation in RPG : 각기 다른 동작에 따라 데미지를 계산하는 알고리즘이 있고 각 공격의 문맥에 따라 다른 데미지를 계산하는 알고리즘을 적용

![Untitled](../../../../_assets/oop/Untitled%2016.png)

## Structure

- Strategy: Concrete Strategies에서 공통적으로 사용되는 interface를 정의. 어떤 strategy를 사용할지는 context에서 정해질 것임
- Concrete Strategies: Strategy interface에 맞춰 알고리즘 정의
- Context: Strategy 객체를 가지고 있음. 어떤 알고리즘이 사용될지에 대해서는 독립적 ⇒ 동적으로 바뀔 수 있음
- Client: Concrete Strategies 중 특정한 알고리즘을 선택하고 Context로 넘김

## Adaptability

- 다양한 알고리즘을 사용하고 런타임 중에 한 알고리즘에서 다른 알고리즘으로 전환할 수 있도록 하려는 경우
- 일부 동작을 실행하는 방식만 다른 유사한 클래스가 많이 있는 경우 사용
- 사용자에게 중요하지 않을 수 있는 알고리즘의 구현 세부 정보에서 클래스의 비즈니스 논리를 분리하기 위해 사용
- 알고리즘의  전환 사이 대규모 조건문이 있는 경우 사용

## Pros

- 연관 있는 알고리즘들을 각각의 추출된 class 에 정의한 후 공통 interface 를 정의 ⇒ compile-time flexibility 를 줌
  - run-time 중 추출된 클래스를 동적으로 교환할 수 있음
- 코드, 내부 데이터, 다양한 알고리즘의 dependencies 를 isolate할 수 있음
- 간단한 interface를 사용하여 동적으로 알고리즘 수행 혹은 알고리즘 교체를 할 수 있음
- 새로운 ConcreteStrategy를 코드 수정없이 추가할 수 있음 ⇒ Open/Closed Principle

## Cons

- 사용하는 곳에서 반드시 각 ConcreteStrategy의 차이를 알고 적절하게 사용해야 함
- 알고리즘이 거의 바뀌지 않는다면, 복잡하게 Stategy패턴을 사용할 이유가 없음
- 대부분의 언어에서 Functional type support를 하기 때문에 굳이 코드베이스를 크게 만들이유가 없다

## Relationship with other patterns

### [[Bridge Pattern]], [[State Pattern]], (일부분 [[Adapter Pattern]])

- 구조가 비슷함(다른 객체에 실제 작업을 위임하는 구조)
- 모두 다른 문제를 풀기 위한 방법
  - 패턴은 특정 방식으로 코드를 구조화하기 위한 단순한 레시피가 아님
  - **해결해야하는 문제를 다른 개발자와 소통하기 위한 방법으로 패턴을 사용해야 함**

### [[Decorator Pattern]]

- Decorator는 객체의 겉을 바꾸는 역할, Strategy는 객체의 속을 바꾸는 역할

### [[Command Pattern]]

- 둘다 객체를 파라미터로 갖기 때문에 비슷해보일 수 있음
- 하지만, 다른 의도로 사용됨
  - Command: 연산을 객체로 바꾸려는 의도 ⇒ 작업 실행을 연기하고, 대기열에 추가하고, 명령 기록을 저장하고, 원격 서비스에 명령을 보내는 등의 작업을 수행할 수 있음
  - Strategy:  같은 일을 하는 다른 알고리즘을 자유롭게 교체해서 사용하기 위한 의도

### [[Template Method Pattern]]

- Template Method 패턴은 상속 기반. subclass에서 수정이 필요한 알고리즘 일부분을 확장하는 방법
- Strategy 패턴은 구성 기반. 다르게 동작하는 전략을 제공해서 객체의 행위를 변경하는 방법
- Template Method는 class level에서 동작하고, Strategy는 object level에서 동작함 ⇒ Template Method는 static 하기 때문에 compile-time-safe, Strategy는 runtime-safe 함
- Template Method 패턴은 공통된 기능을 공유하도록 설계되어 있지만, Strategy 패턴은 모든 implementation이 독립적이고 공유되는 코드가 없다

### [[State Pattern]]

- State는 Strategy를 확장한 패턴으로 간주됨
  - 둘 모두 구성 기반
  - helper 객체가 context를 변경하는 것을 도와 줌
- Strategy는 상속을 대체하려는 목적
- State는 코드내의 조건문들을 대체하려는 목적
