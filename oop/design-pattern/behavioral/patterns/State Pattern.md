# State

#oop, #design-pattern, #behavioral-pattern

## Description

![Untitled](../../../../_assets/oop/Untitled%2017.png)

- 객체의 내부 상태가 바뀌었을 때 행동을 바꿀 수 있게 해주는 패턴
- 상태 전이를 위한 조건 로직이 지나치게 복잡한 경우 이를 해소하기 위한 방법
- Finite-state machine을 이해해야 아이디어를 이해할 수 있음

![Untitled](../../../../_assets/oop/Untitled%2018.png)

- Jira 예시
- task가 들어갈 수 있는 유한한 상태가 있음
- 모든 상태는 유일하고, 다르게 행동함
- 이러한 상태는 다른 상태로 언제든지 변할 수 있음
  - 하지만, 현재 상태에서 변할 수 있게 정해진 상태로만 변경할 수 있음
- 조건문을 이용해서 구현할 수 있겠지만, 이런 경우 새로운 상태를 추가하는 것이 매우 어려워 짐
  - state pattern을 이용하면 새 상태를 추가하는 것이 매우 쉬워지고, 상태 변경도 명백해진다

## Structure

![Untitled](../../../../_assets/oop/Untitled%2019.png)

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

## Adaptability

- 상태가 많고, 자주 변경되며, 상태에 따라서 다르게 동작하는 경우 사용되야 함
- 유사한 상태 및 전환에 걸쳐 중복 코드가 많은 경우 사용
- 상태에 따른 조건이 까다로울 때 사용

## Example

- e-commerce application에서 주문 상태 관리
- 현재 상태에 적절한 신호등 색 보여주기
- Medium 기사 상태(draft, submitted, published…)

## Pros

- 특정 상태에 관련된 코드를 분리된 클래스로 만들어줌 ⇒ Single Responsibility Principle
- 새 상태를 코드 수정없이 추가할 수 있음 ⇒ Open/Closed Principle
- 조건문을 없애 코드를 더욱 간단하게 만들 수 있음

## Cons

- 상태가 많이 바뀌지 않고, 상태가 많이 없을 때는 패턴 적용하는 것이 과함

## Relationship with other patterns

### [[Strategy Pattern]] (일부분 [[Adapter Pattern]])

- 구조가 비슷함(다른 객체에 실제 작업을 위임하는 구조)
- 모두 다른 문제를 풀기 위한 방법
  - 패턴은 특정 방식으로 코드를 구조화하기 위한 단순한 레시피가 아님
  - **해결해야하는 문제를 다른 개발자와 소통하기 위한 방법으로 패턴을 사용해야 함**

### [[Strategy Pattern]]

- State는 Strategy를 확장한 패턴으로 간주됨
  - 둘 모두 구성 기반
  - helper 객체가 context를 변경하는 것을 도와 줌
  - Strategy는 Strategy는 상속을 대체하려는 목적
  - State는 코드내의 조건문들을 대체하려는 목적
