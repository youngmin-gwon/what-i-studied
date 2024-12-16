---
aliases: []
date created: 2024-12-12 23:58:38 +09:00
date modified: 2024-12-16 12:20:32 +09:00
tags: [design-pattern, oop, testing-pattern]
title: Self Shunt Pattern
---

## Description

**Self Shunt Pattern**은 시스템에서 특정 객체가 자신을 일시적으로 다른 방식으로 변경하여, 그 객체의 동작을 잠시 우회하거나 다른 방법으로 처리하도록 하는 패턴

이 패턴은 객체가 외부에서의 호출이나 동작을 변경하지 않고, 자신 내부에서 자신의 동작 방식을 일시적으로 전환하여 상황에 맞는 동작을 하게 하는 방식

## Structure

1. **Self-Referencing Object**:
   - 자신을 참조하는 객체. 해당 객체가 특정 상황에 따라 자신의 동작을 변경할 수 있도록 함
2. **Shunt Logic**:
   - 객체가 일시적으로 동작을 우회할 수 있는 로직. 특정 조건이나 상황에 따라 이 로직을 활성화하여, 객체가 다른 방식으로 동작
3. **Original Behavior**:
   - 기본적으로 객체가 수행해야 하는 동작. 하지만 특정 상황에서 이 동작을 변경하여 새로운 동작을 실행

### Details

- 객체는 일반적인 동작을 수행하지만, 특정 조건이 맞으면 자신을 다른 동작으로 전환
- 이후 조건이 풀리면 다시 원래의 동작으로 돌아옴

## Example

예시: 상황에 따라 다른 동작을 수행하는 객체

```dart
class Worker {
  String _currentState = "working";

  void doWork() {
    if (_currentState == "working") {
      print("Performing work...");
    } else {
      print("Paused, not working.");
    }
  }

  void pauseWork() {
    _currentState = "paused";
    print("Work paused.");
  }

  void resumeWork() {
    _currentState = "working";
    print("Resumed work.");
  }

  void shunt() {
    // Self Shunt Logic: Temporarily change the behavior
    _currentState = "paused";  // Change state temporarily to pause work
    print("Temporarily stopped work.");
  }
}

void main() {
  var worker = Worker();
  worker.doWork();  // Output: Performing work...

  worker.shunt();  // Output: Temporarily stopped work.
  worker.doWork();  // Output: Paused, not working.

  worker.resumeWork();  // Output: Resumed work.
  worker.doWork();  // Output: Performing work...
}
```

- Worker 클래스는 작업을 진행하는 객체입니다. doWork() 메서드를 통해 작업을 수행하고, pauseWork() 와 resumeWork() 메서드를 통해 작업을 일시 중지하거나 재개할 수 있음
- shunt() 메서드는 Self Shunt Pattern 을 구현한 예시로, 객체가 일시적으로 자신을 "paused" 상태로 변경하여 doWork() 메서드의 동작을 우회하도록 함
- 이렇게 하면 객체는 외부에서 호출되는 동작을 변경하지 않고도 자신 내부에서 잠시 다른 방식으로 동작할 수 있음

## Adaptability

1. 동작의 일시적인 변경이 필요한 경우
    - 객체가 외부에서의 호출 없이, 특정 조건에 따라 동작을 잠시 변경할 필요가 있을 때 유용
2. 동작 우회가 필요한 상황
    - 오류 처리나 예외 상황에서 기본 동작을 우회할 수 있도록 해야 할 때
3. 동작을 유연하게 처리해야 하는 경우
    - 특정 상태에서 객체가 다른 방식으로 동작해야 할 때, 이를 객체 내부에서 처리할 수 있음
4. 상태 기반 로직 처리
    - 객체가 여러 상태에 따라 동작을 달리해야 하는 경우, 상태 변화에 따라 동작을 유연하게 변경하고 싶은 상황에서 사용할 수 있음

## Pros

1. 유연성
    - 객체가 외부 개입 없이 내부에서 동작을 전환할 수 있어 매우 유연
2. 동작 변경의 간편성
    - 동작을 일시적으로 변경하고, 변경된 동작을 빠르게 복원할 수 있음
3. 효율성
    - 외부에서의 호출 없이 객체 내부에서만 동작을 변경하므로 코드 복잡도를 줄일 수 있음
4. 상태 관리
    - 객체가 상태에 따라 다른 동작을 수행하도록 하여, 상태 관리가 용이해짐

## Cons

1. 추가적인 상태 관리 필요
    - 객체가 상태에 따라 동작을 변경하므로, 상태 관리가 복잡해질 수 있음
2. 디버깅 어려움
    - 동작을 임의로 변경하는 부분이 많아 디버깅 시 문제를 추적하기 어려울 수 있음
3. 복잡성 증가
    - 객체가 다양한 동작을 처리해야 할 때 코드가 지나치게 복잡해질 수 있음
4. 의도치 않은 동작 변경
    - 동작을 일시적으로 변경하는 로직이 의도치 않게 부작용을 일으킬 가능성이 있음

## Relationship with other patterns

### Similarity

#### [[../../behavioral/patterns/State Pattern]]

State Pattern 과 유사하게 객체가 상태에 따라 동작을 변경

그러나 Self Shunt Pattern 은 상태를 바꿀 때마다 반드시 동작을 우회하는 특징이 있음

#### [[../../behavioral/patterns/Strategy Pattern]]

Strategy Pattern 은 객체가 동작을 변경할 수 있도록 인터페이스를 사용하여 외부에서 동작을 주입하는 방식인데, Self Shunt Pattern 은 내부에서 동작을 직접 변경

### Difference

#### [[../../behavioral/patterns/Command Pattern]]

Command Pattern 은 명령 객체를 사용하여 동작을 캡슐화하고, 외부에서 동작을 실행하는 반면, Self Shunt Pattern 은 객체가 자신의 동작을 일시적으로 변경하여 실행

#### [[../../structural/patterns/Decorator Pattern]]

Decorator Pattern 은 객체의 기능을 동적으로 추가하는 데 사용되며, Self Shunt Pattern 은 객체의 동작을 일시적으로 변경하는 데 초점
