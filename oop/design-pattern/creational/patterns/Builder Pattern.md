# Builder

#design-pattern, #creational-pattern

## Description

![Untitled](Untitled%2049.png)

![Untitled](Untitled%2050.png)

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

## Structure

![Untitled](Untitled%2051.png)

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

## Adaptability

- "망원경 생성자" 를 제거하기 위해 사용
- 코드가 일부 제품(예: 석조 및 목조 주택)의 다른 표현을 생성할 수 있도록 하기 위해 사용
- Composite Tree 또는 기타 복잡한 개체를 구성하기 위해 사용
- 서로를 참조하는 동일한 생성자 클래스를 다수 가지고 있다면 사용
  - 다수의 optional parameters를 가지고 있는 상황, default 값을 가지는 몇가지 짧은 버전의 constructor를 가지고 있을 때
  - 생성 과정은 비슷하지만, 세부사항이 다를 때
- 복잡한 객체를 생성하는 알고리즘이 객체를 이루고 있는 파트와 독립적일 때 사용

## Pros

- 개체를 단계별로 구성하거나 구성 단계를 연기하거나 재귀적으로 단계를 실행할 수 있음
- 제품의 다양한 표현을 작성할 때 동일한 구성 코드를 재사용할 수 있음
- 복잡한 객체 생성 코드를 비즈니스 로직과 분리할 수 있음 ⇒ [[SRP(Single Responsibility Principle)]]

## Cons

- 여러 개의 새로운 클래스를 생성해야 하기 때문에 코드를 복잡하게 만듬

## Relationship with other patterns

### [[Factory Method Pattern]]

- Builder는 Factory Method로부터 시작하여 발달한 패턴

### [[Abstract Factory Pattern]]

- Builder는 복잡한 객체를 단계별로 구성하는데 중점을 둠
- Abstract Factory는 관련 객체의 패밀리 생성에 중점을 둠
- Abstract Factory는 객체를 즉시 반환하지만 Builder를 사용하면 객체를 가져오기 전에 몇 가지 추가 구성 단계를 실행할 수 있음

### [[Composite Pattern]]

- Composite tree를 구성할 때 Builder 패턴을 사용할 수 있음
  - 재귀적으로 작동하도록 생성 step을 프로그래밍 할 수 있기 때문

### [[Bridge Pattern]]

- Builder 패턴과 Bridge 패턴을 합쳐서 사용할 수 있음
  - Director 클래스는 Abstraction 역할을 하는 반면 다른 Builder 는 Implementation 역할을 함

### [[Singleton Pattern]]

- Builder 패턴은 Singleton으로 구현 될 수 있음
