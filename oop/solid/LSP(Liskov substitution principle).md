# LSP(Liskov substitution principle)

- 프로그램의 정확성을 깨지 않으면서 하위 타입의 인스턴스로 바꿀수 있어야한다

- 하위 타입은 언제나 기반 타입과 호환될 수 있어야 함. 즉 **서브 타입은 기반 타입과 약속한 규약**(public interface, method exception)**을 지켜야 함**

- 상위 타입 클래스 자리에 하위 타입 인스턴스로 바꾸더라도 문제가 생기지 않아야 한다

- **다형성**을 지원하기 위한 원칙

- 인터페이스를 구현한 구현체는 믿고 사용하려면 LSP가 필요하다

- 상속에 관한 중요한 이야기
  - 상속은 구현상속(extends) 이든 인터페이스 상속(implements) 이든 궁극적으로는 다형성을 통한 확장성 획득을 목표로 함
  - LSP원리도 역시 서브 클래스가 확장에 대한 인터페이스를 준수해야 함을 의미
  - 다형성과 확장성을 극대화 하려면 하위 클래스를 사용하는 것보다는 상위 클래스(인터페이스)를 사용하는 것이 좋음
  - 일반적으로 선언은 기반 클래스로 생성은 구체 클래스로 대입하는 방법을 사용
  - 생성 시점에서 구체 클래스를 노출시키기 꺼려지는 경우 생성 부분을 Abstract Factory 등의 패턴을 사용하여 유연성을 높일 수 있음
  - 상속을 통한 재사용은 기반 클래스와 서브 클래스 사이에 IS-A 관계가 있을 경우로만 제한 되어야 함
    - 그 외의 경우에는 합성(composition)을 이용한 재사용을 해야함

- 상속은 다형성과 따로 생각할 수 없음
  - 다형성으로 인한 확장효과를 얻기 위해서는 서브 클래스가 기반 클래스와 클라이언트 간의 규약(인터페이스)을 어겨서는 안됨
  - 결국 이 구조는 다형성을 통한 확장 원리인 OCP를 제공하게 됨
  - 따라서, LSP는 OCP를 구성하는 구조가 됨
  - 객체지향 설계 원리는 이렇게 서로가 서로를 이용하기도 하고 포함하기도 하는 특징을 가짐