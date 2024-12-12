# Factory Method(=Virtual Constructor)

#design-pattern, #creational-pattern

## Description

![Untitled](Untitled%2027.png)

- = Virtual Constructor
- 객체를 만드는 인터페이스를 제공하지만, 서브클래스에서 어떤 클래스를 초기화 할지 정하는 패턴

## Structure

![Untitled](Untitled%2028.png)

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

## Examples

- Logistic에 관련된 앱을 만들었다. 처음에는 Truck만 신경쓰면 되어서 Truck을 코드 전체에 작성했다
- Logistic이 잘 되어서 Ship도 추가하고 싶다. 허나 Ship을 추가하기 위해 코드 베이스 전체를 수정해야 할 것이다
- Transport 인터페이스를 만들고 Factory Method 패턴을 사용해서 하위 클래스에서 Truck인지, Ship인지 정하게 만든다

## Adaptability

- 목적: 실제로 product를 사용하는 곳과 product를 생성하는 곳을 분리하기 위함
  - 새 concrete product를 추가해야되는 경우, 오직 factory method를 오버라이드하는 새로운 ConcreteCreator도 생성되야 한다는 것을 인지
- 새로운 인스턴스를 계속 생성할 필요가 없는 경우 적용할 수 있음
  - 이미 생성된 객체를 추적하는 cache layer나 저장소를 둬서 반환할 수 있도록 설정하는 방식으로 가능
- 추후에 어떠한 타입의 객체를 사용해야 하는지 모를 때 사용

## Pros

- product를 생성하는 곳을 한 곳으로 이동시킬 수 있음 ⇒ Single Responsibility Principle
- 코드 수정 없이 새로운 product를 추가할 수 있음 ⇒ Open/Closed Principle
- Creator와 ConcreteProduct간의 결합도를 줄일 수 있음
- 객체를 사용할 클래스에서 직접 객체를 만들게 되는 문제를 해결할 수 있음
- sub-classing 함으로 compile-time 유연성을 가질 수 있음
- 코드에서 application에 특정된 클래스의 직접 바인딩을 제거할 수 있다. 덕분에 코드는 인터페이스만 신경쓰면 된다

## Cons

- 패턴을 구현하기 위해 많은 새 하위 클래스를 도입해야 하므로 코드가 더 복잡해질 수 있음
  - 가장 좋은 시나리오는 생성자 클래스의 기존 계층 구조에 패턴을 도입하는 경우

## Relationship with other patterns

### [[Abstract Factory Pattern]], [[Prototype Pattern]], [[Builder Pattern]]

- 모두 Factory Method를 기반으로 발전 됨
- Factory Method보다 자유롭지만, 복잡함

### [[Abstract Factory Pattern]]

- Abstract Factory는 Factory Method의 세트를 기반으로 만들어짐

### [[Iterator Pattern]]

- Factory Method와 Iterator를 함께 사용하여, 컬렉션 하위 클래스가 컬렉션과 호환되는 다양한 유형의 반복자를 반환하도록 할 수 있음

### [[Prototype Pattern]]

- Prototype은 상속을 기반으로 하지 않지만  복제된 객체의 복잡한 초기화가 필요
- Factory Method는 상속을 기반으로 하지만 초기화 단계가 필요하지 않음

### [[Template Method Pattern]]

- Factory Method는 Template Method를 구체화 한것. 동시에 Factory Method는 큰 Template Method의 한 단계 역할을 할 수 있음
