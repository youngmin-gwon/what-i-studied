---
title: Pluggable Object Pattern
tags: [design-pattern, general-pattern, oop]
aliases: []
date modified: 2025-12-10 13:27:13 +09:00
date created: 2024-12-12 23:54:34 +09:00
---

## Description

**Pluggable Object Pattern**은 객체의 동작이나 기능을 실행 시간에 동적으로 변경할 수 있도록 설계된 패턴

이 패턴은 동작을 외부에서 주입 (plug-in) 받아 실행하므로, 조건문을 줄이고 객체 간의 결합도를 낮추는 데 유용함

**Pluggable Object Pattern**은 알려진 인터페이스를 구현한 객체에 대한 참조를 저장하고, 이를 통해 나머지 객체가 동작을 수행하도록 설계함

이렇게 하면 코드 전반에서 동작을 명시적으로 정의하지 않고, 참조된 객체를 통해 간접적으로 실행할 수 있음

이 패턴을 사용하는 이유는 조건문과 분기 로직을 줄여 코드의 가독성을 높이고 유지보수를 용이하게 하기 위함임

다음과 같은 상황을 고려

- 사람 (Person) 이 " 운전 중 " 이거나 " 걷는 중 " 일 때 움직임을 제어하는 코드가 있음.
- 조건문을 사용하면 코드가 복잡해지고, 새로운 이동 방식이 추가되면 복잡성이 더 심화됨.
- Pluggable Object Pattern 을 사용하면 이동 방식을 캡슐화하고, 동작을 외부에서 주입함으로써 조건문을 없앨 수 있음.

## Structure

1. **Interface or Abstract Class**: 공통 동작 (메서드) 을 정의.
2. **Concrete Implementations**: 구체적인 동작을 구현하는 클래스.
3. **Pluggable Host Object**: 동작을 실행 시간에 주입받아 사용하는 객체.

## Example

### Before

기존 방식: 고정된 동작, 조건문 사용

```dart
class Person {
  void move(String mode) {
    if (mode == "drive") {
      print("Driving...");
    } else if (mode == "walk") {
      print("Walking...");
    } else {
      print("Unknown mode of transport.");
    }
  }
}

void main() {
  Person person = Person();
  person.move("drive"); // Output: Driving...
  person.move("walk");  // Output: Walking...
}```

### After

```dart
// Movement Interface
abstract interface class Movement {
  void move();
}

// Concrete Implementations
class Drive implements Movement {
  @override
  void move() => print("Driving...");
}

class Walk implements Movement {
  @override
  void move() => print("Walking...");
}

// Host Object
class Person {
  Movement _movement;

  Person(this._movement);

  void setMovement(Movement movement) {
    _movement = movement;
  }

  void move() {
    _movement.move();
  }
}

void main() {
  // Initial setup with Drive
  Person person = Person(Drive());
  person.move(); // Output: Driving...

  // Dynamically switch to Walk
  person.setMovement(Walk());
  person.move(); // Output: Walking...
}
```

## Adaptability

1. 조건문과 분기 로직을 줄이고 싶을 때
   - 복잡한 조건문을 캡슐화하여 간결한 코드 작성.
2. 동적으로 동작을 변경해야 할 때
   - 실행 중에 다른 동작을 유연하게 교체.
3. 확장 가능성이 필요한 경우
   - 새로운 동작이 추가되어도 기존 코드를 수정하지 않음.
4. 다형성을 활용하고 싶을 때
   - 인터페이스를 통해 다양한 구현체를 교체 가능

## Pros

1. 유연성
   - 실행 중에 객체 동작을 쉽게 변경할 수 있음.
2. 확장성
   - 새로운 동작을 추가하더라도 기존 코드를 변경할 필요 없음 → [OCP(Open Closed Principle)](../../../solid/OCP(Open%20Closed%20Principle).md)
3. 결합도 감소
   - 조건문 대신 플러그인 객체에 위임하여 결합도를 낮춤
4. 가독성 향상
   - 조건문이 제거되어 코드가 더 간결해짐

## Cons

1. 추가 클래스 증가
   - 각 동작마다 새로운 클래스를 만들어야 하므로 클래스 수가 많아질 수 있음
2. 복잡성 증가:
   - 간단한 동작을 위한 설계로는 오히려 과도한 복잡성을 초래할 수 있음
3. 런타임 오류 가능성:
   - 잘못된 객체를 주입하면 예상치 못한 동작이나 오류가 발생할 수 있음

## Relationship with other patterns

### Similarity

#### [Strategy Pattern](../../behavioral/Strategy%20Pattern.md)

둘 다 인터페이스를 사용하여 동작을 캡슐화하고, 실행 시점에 교체 가능

Pluggable Object Pattern 은 주로 객체 동작을 교체하는 데 초점이 있음

#### [State Pattern](../../behavioral/State%20Pattern.md)

State Pattern 은 객체의 상태에 따라 동작을 변경, Pluggable Object Pattern 은 플러그인을 통해 동작을 교체

### Difference

#### [Decorator Pattern](../../structural/Decorator%20Pattern.md)

Decorator 는 기존 동작에 새로운 기능을 추가하지만, Pluggable Object Pattern 은 동작을 완전히 교체

#### Dependency Injection

Dependency Injection 은 객체 생성을 초기화 단계에서 결정, Pluggable Object Pattern 은 실행 중에도 동작을 교체 가능
