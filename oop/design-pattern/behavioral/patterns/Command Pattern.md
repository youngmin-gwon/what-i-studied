# Command(=Action=Transaction)

#BehavioralPattern

## Description

![Untitled](command_overview.png)

![Untitled](command_example.png)

- 요청을 객체로 캡슐화하며, 매개변수를 써서 여러 가지 다른 요구 사항을 집어넣을 수도 있는 패턴
  - 요청 내역을 큐에 저장하거나 로그로 기록할 수 도 있으며, 작업 취소 기능도 지원 가능
  - client는 command가 어떻게 생성되는지, 어떻게 수행되는지 전혀 신경 안써도 됨 ⇒ decoupling!
- 기능을 실행하고, 수행 스케쥴을 만들고, 먼 곳에서 사용할 때 유용함
- command는 간단한 클래스 이므로, 이것을 직렬화하고, 저장(database or text file)하고, 나중에 initial command로 복원하여 사용할 수도 있음 ⇒ 특정한 시간이나 특정한 상황에 command를 수행할 수 있게 만들기 유용함
- 복원되어야 하는 커맨드에 적용하는 것이 가장 유명함(ex. undo) ⇒ 이러한 경우 수행된 기능의 history를 stack으로 가지고 있어야 함
- 재사용가능하고 깔끔한 코드를 만드는 것이 가능하게 만들어줌! ⇒ SRP, OCP in SOLID
- 주로 UI와 business logic을 연결하는 역할을 함
- request 를 보내는 곳(UI)인 “Sender”에서 실제 완성되어야 할 로직을 갖고 있는 “Receiver”에 request를 바로 보내는 대신 “Command”를 내려줌 ⇒ Command가 UI와 logic layers의 coupling을 줄여주는 중간 layer 역할을 하게 됨

## Structure

![Untitled](command_structure.png)

1. Command : 작업을 수행하기 위한 interface 선언
2. Concrete Command : receiver에 상응하는 작업을 실행하는 requests 선언
3. Invoker(=Sender) : request를 직접 Receiver에게 보내는 대신 command를 발동 시킴. 명령의 리스트를 저장하고 이 리스트에 맞춰서 동시 수행, 이전 수행 취소 등을 함
4. Receiver : request를 수행과 관련된 작업을 어떻게 수행하는지 아는 클래스. 어떠한 클래스도 receiver 역할 가능
5. Client: Concrete Command object를 선언하고 Receiver를 묶음

## Adaptability

- 작업으로 객체를 매개변수화하려는 경우 사용
- 작업을 대기열에 넣거나 실행을 예약하거나 원격으로 실행하려는 경우 사용
- 되돌릴 지도 모르는 작업을 구현하려는 경우 사용 ⇒ [[Memento Pattern]] 와 함께 사용됨

## Pros

- 연산을 유발하는 클래스와 연산을 수행하는 클래스를 분리할 수 있음 ⇒ [[SRP(Single Responsibility Principle)]]
- 새 command를 코드 수정없이 추가할 수 있음 ⇒ [[OCP(Open Closed Principle)]]
- undo/redo 기능을 추가할 수 있음
- 지연 작업 실행을 구현할 수 있음
- 여러 개 간단한 command를 조합해 하나의 복잡한 command를 만들 수 있음

## Cons

- sender와 receiver 사이에 새로운 layer를 추가하는 것이기 때문에 코드가 다소 복잡해질 수 있음

- 다른 패턴과의 관계

### [[Chain of Responsibility Pattern]], [[Mediator Pattern]], [[Observer Pattern]]

- sender와 receiver를 연결하는 여러가지 방법을 보여줌
  - [[Chain of Responsibility Pattern]]
    - 잠재적 receiver 중 하나가 처리할 때까지 잠재적 receiver의 동적 사슬을 따라 순차적으로 요청을 전달하는 구조
  - [[Command Pattern]]
    - receiver와 sender 간 단방향 연결
  - [[Mediator Pattern]]
    - receiver와 sender 간의 직접 연결을 제거하여 mediator 개체를 통해 간접적으로 통신하도록 하는 구조
  - [[Observer Pattern]]
    - receiver가 수신 요청을 동적으로 구독 및 구독 취소할 수 있음

### [[Chain of Responsibility Pattern]]

- Chain of Responsibility의 핸들러를 Command 패턴을 이용해서 구현할 수 있음
  - 요청으로 표시되는 동일한 컨텍스트 개체에 대해 다양한 작업을 실행할 수 있음
  - 또 다른 접근 방식: 요청 자체가 Command 개체
    - 체인에 연결된 일련의 서로 다른 컨텍스트에서 동일한 작업을 실행할 수 있음

### [[Memento Pattern]]

- undo 기능을 적용하기 위해서 Command 패턴과 같이 사용할 수 있음
  - Command는 다양한 연산을 목표 객체에 적용하는 것에만 신경 쓰면 되고, Memento는 Command가 수행되기 전 객체의 상태만 기억하는 것에만 신경 쓰면 됨

### [[Strategy Pattern]]

- 둘다 객체를 파라미터로 갖기 때문에 비슷해보일 수 있음
- 하지만, 다른 의도로 사용됨
  - Command: 연산을 객체로 바꾸려는 의도 ⇒ 작업 실행을 연기하고, 대기열에 추가하고, 명령 기록을 저장하고, 원격 서비스에 명령을 보내는 등의 작업을 수행할 수 있음
  - Strategy:  같은 일을 하는 다른 알고리즘을 자유롭게 교체해서 사용하기 위한 의도

### [[Prototype Pattern]]

- Prototype은 Command 사본을 기록에 저장해야 할 때 도움이 될 수 있음

### [[Visitor Pattern]]

- Visitor를 Command의 강력한 버전이라고 생각해도 무방함
  - 다른 클래스의 다양한 객체에 대해 작업을 실행할 수 있음
