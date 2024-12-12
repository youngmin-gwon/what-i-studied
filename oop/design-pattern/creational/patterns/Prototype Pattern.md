# Prototype

## Description

[[Creational Pattern]]

![Untitled](Untitled%2037.png)

![Untitled](Untitled%2038.png)

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

## Structure

![Untitled](Untitled%2039.png)

1. Prototype
   - 스스로를 복제하는 interface 선언
   - 주로 clone 이라는 이름의 메소드를 가지지만, declared/defined 라는 메소드를 가질 수도 있음
2. ConcretePrototype
   - 스스로 복제하는 기능 구현
   - 원본 복사하는 것 외에도, 연결된 객체 복제, 재귀 종속성 풀기 등과 관련된 복제 프로세스의 일부 극단적인 경우를 처리할 수도 있음
3. SubclassPrototype
   - ConcretePrototype과 같은 목적을 가지지만, 때로는 행위 같은 인자를 정의하여 base class를 확장할 수 있음

## Adaptability

- 복제해야 하는 구체 클래스에 코드가 종속되지 않게 하기 위해 사용
- 오직 초기화 하는 방법만 다른 각각의 subclass를 줄이기 위해 사용

## Pros

- 구체 클래스에 의존하지 않고 객체를 복제하는 것이 가능
- 반복되는 초기화 코드를 없앨 수 있음
- 복잡한 객체를 편하게 만들 수 있음
- 복잡한 객체의 초기구성을 만들 때, 상속 대신 다른 방법을 제공

## Cons

- 의존성이 순환하는 복잡한 객체를 복제할 때 까다로움

## Relationship with other patterns

### [[Factory Method Pattern]]

- Factory Method에서 조금씩 발전하여 Abstract Factory, Prototype, Builder 패턴으로 발전하였음
- Prototype은 복제된 객체의 복잡한 초기화가 필요하지만, 상속으로 인한 단점이 없음
- Factory Method는 상속을 기반으로 하지만 초기화 단계가 필요하지 않음

### [[Abstract Factory Pattern]]

- 보통 Abstract Factory는 Factory Method의 세트로 구성되지만, Prototype의 세트로 구성할 수도 있음

### [[Command Pattern]]

- command 복제본을 저장해야 할 때 Prototype이 도움을 줄 수 있음

### [[Composite Pattern]], [[Decorator Pattern]]

- Composite과 Decorator를 많이 사용하는 디자인에서는 Prototype을 사용하며 이점을 얻을 수 있음
- 패턴을 적용하면 처음부터 다시 구성하는 대신 복잡한 구조를 복제할 수 있음

### [[Memento Pattern]]

- Prototype이 Memento의 간단한 대안이 될 수도 있음
- 히스토리에 저장하려는 상태 객체가 간단하고 외부 리소스에 대한 링크가 없거나 링크가 재설정하기 쉬운 경우

### [Singleton Pattern]

- Prototype은 Singleton 로 구현될 수 있음
