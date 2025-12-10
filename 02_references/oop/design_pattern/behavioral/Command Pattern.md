---
title: Command Pattern
tags: [behavioral-pattern, design-pattern, gof, oop]
aliases: []
date modified: 2025-12-10 14:26:21 +09:00
date created: 2024-12-12 15:47:04 +09:00
---

## Description

![Untitled](../../../../../_assets/oop/command_overview.png)

![Untitled](../../../../../_assets/oop/command_example.png)

## Description

![Untitled](../../../../../_assets/oop/command_overview.png)

![Untitled](../../../../../_assets/oop/command_example.png)

**Command Pattern**은 **요청(Request)을 객체로 캡슐화**하여, 사용자가 보낸 요청을 나중에 이용할 수 있도록 매개변수화하거나, 요청을 큐(Queue)에 저장/로깅하고, 실행된 작업을 취소(Undo)할 수 있게 해주는 패턴입니다.

- **핵심**: "실행하고 싶은 동작"을 객체로 감싸서(Command), "동작을 요청하는 쪽(Sender)"과 "동작을 수행하는 쪽(Receiver)"을 분리(Decoupling)합니다.
- **활용**:
  - 버튼 클릭 등의 UI 이벤트 처리.
  - 작업 예약(Scheduling), 매크로(Macro) 기록.
  - 트랜잭션(Transaction) 관리 및 롤백(Undo) 기능 구현.
- **장점**: Sender는 Receiver가 누구인지, 어떻게 동작하는지 알 필요 없이 그저 "Command를 실행해라"라고 명령만 내리면 됩니다.

## Structure

![Untitled](../../../../../_assets/oop/command_structure.png)

1. **Command** : 작업을 수행하기 위한 interface 선언.
2. **Concrete Command** : receiver 에 상응하는 작업을 실행하는 requests 선언.
3. **Invoker(=Sender)** : request 를 직접 Receiver 에게 보내는 대신 command 를 발동 시킴. 명령의 리스트를 저장하고 이 리스트에 맞춰서 동시 수행, 이전 수행 취소 등을 함.
4. **Receiver** : request 를 수행과 관련된 작업을 어떻게 수행하는지 아는 클래스. 어떠한 클래스도 receiver 역할 가능.
5. **Client**: Concrete Command object 를 선언하고 Receiver 를 묶음.

## Adaptability

- 작업으로 객체를 매개변수화하려는 경우 사용.
- 작업을 대기열에 넣거나 실행을 예약하거나 원격으로 실행하려는 경우 사용.
- 되돌릴 지도 모르는 작업을 구현하려는 경우 사용 ⇒ [Memento Pattern](Memento%20Pattern.md) 와 함께 사용됨.

## Pros

- 연산을 유발하는 클래스와 연산을 수행하는 클래스를 분리할 수 있음 ⇒ [SRP(Single Responsibility Principle)](../../solid/SRP(Single%20Responsibility%20Principle).md)
- 새 command 를 코드 수정없이 추가할 수 있음 ⇒ [OCP(Open Closed Principle)](../../solid/OCP(Open%20Closed%20Principle).md)
- undo/redo 기능을 추가할 수 있음.
- 지연 작업 실행을 구현할 수 있음.
- 여러 개 간단한 command 를 조합해 하나의 복잡한 command 를 만들 수 있음.

## Cons

- sender 와 receiver 사이에 새로운 layer 를 추가하는 것이기 때문에 코드가 다소 복잡해질 수 있음.

## Relationship with other patterns

### [Chain of Responsibility Pattern](Chain%20of%20Responsibility%20Pattern.md), [Mediator Pattern](Mediator%20Pattern.md), [Observer Pattern](Observer%20Pattern.md)

- sender 와 receiver 를 연결하는 여러가지 방법을 보여줌.
  - **[Chain of Responsibility Pattern](Chain%20of%20Responsibility%20Pattern.md)**
    - 잠재적 receiver 중 하나가 처리할 때까지 잠재적 receiver 의 동적 사슬을 따라 순차적으로 요청을 전달하는 구조.
  - **[Command Pattern](Command%20Pattern.md)**
    - receiver 와 sender 간 단방향 연결.
  - **[Mediator Pattern](Mediator%20Pattern.md)**
    - receiver 와 sender 간의 직접 연결을 제거하여 mediator 개체를 통해 간접적으로 통신하도록 하는 구조.
  - **[Observer Pattern](Observer%20Pattern.md)**
    - receiver 가 수신 요청을 동적으로 구독 및 구독 취소할 수 있음.

### [Chain of Responsibility Pattern](Chain%20of%20Responsibility%20Pattern.md)

- Chain of Responsibility 의 핸들러를 Command 패턴을 이용해서 구현할 수 있음.
  - 요청으로 표시되는 동일한 컨텍스트 개체에 대해 다양한 작업을 실행할 수 있음.
  - 또 다른 접근 방식: 요청 자체가 Command 개체.
    - 체인에 연결된 일련의 서로 다른 컨텍스트에서 동일한 작업을 실행할 수 있음.

### [Memento Pattern](Memento%20Pattern.md)

- undo 기능을 적용하기 위해서 Command 패턴과 같이 사용할 수 있음.
  - Command 는 다양한 연산을 목표 객체에 적용하는 것에만 신경 쓰면 되고, Memento 는 Command 가 수행되기 전 객체의 상태만 기억하는 것에만 신경 쓰면 됨.

### [Strategy Pattern](Strategy%20Pattern.md)

- 둘 다 객체를 파라미터로 갖기 때문에 비슷해 보일 수 있음.
- 하지만, 다른 의도로 사용됨.
  - **Command**: 연산을 객체로 바꾸려는 의도 ⇒ 작업 실행을 연기하고, 대기열에 추가하고, 명령 기록을 저장하고, 원격 서비스에 명령을 보내는 등의 작업을 수행할 수 있음.
  - **Strategy**: 같은 일을 하는 다른 알고리즘을 자유롭게 교체해서 사용하기 위한 의도.

### [Prototype Pattern](../creational/Prototype%20Pattern.md)

- Prototype 은 Command 사본을 기록에 저장해야 할 때 도움이 될 수 있음.

### [Visitor Pattern](Visitor%20Pattern.md)

- Visitor 를 Command 의 강력한 버전이라고 생각해도 무방함.
  - 다른 클래스의 다양한 객체에 대해 작업을 실행할 수 있음.
