---
title: Null Object Pattern
tags: [design-pattern, general-pattern, oop]
aliases: []
date modified: 2025-12-10 14:23:35 +09:00
date created: 2024-12-13 00:00:26 +09:00
---

## Description

`null` 값을 사용하는 대신 특정 작업을 수행하지 않는 객체를 제공하는 디자인 패턴

이 패턴은 `null` 체크를 줄이고, 코드의 복잡성을 감소시키며, 기본 동작을 정의할 수 있게 함.

## Structure

1. **Abstract Interface**: 공통 작업 (메서드) 을 정의하는 인터페이스나 추상 클래스.
2. **Concrete Implementation**: 실제 동작을 수행하는 클래스.
3. **Null Object**: 아무 동작도 하지 않거나 기본 동작을 제공하는 클래스.

## Example

### Before

기존 방식으로 null check

```dart
abstract class Animal {
  void makeSound();
}

class Dog implements Animal {
  @override
  void makeSound() => print("Woof!");
}

void playWithAnimal(Animal? animal) {
  if (animal != null) {
    animal.makeSound();
  } else {
    print("No animal to play with.");
  }
}

void main() {
  Animal? dog = Dog();
  Animal? nullAnimal = null;

  playWithAnimal(dog);
  playWithAnimal(nullAnimal);
}
```

### After

null check 하지 않음

```dart
abstract class Animal {
  void makeSound();
}

class Dog implements Animal {
  @override
  void makeSound() => print("Woof!");
}

// Null Object
class NullAnimal implements Animal {
  @override
  void makeSound() {
    // No operation or default behavior
    print("Silence...");
  }
}

void playWithAnimal(Animal animal) {
  animal.makeSound();
}

void main() {
  Animal dog = Dog();
  Animal nullAnimal = NullAnimal();

  playWithAnimal(dog);         // Output: Woof!
  playWithAnimal(nullAnimal);  // Output: Silence...
}
```

## Adaptability

1. null 체크를 피하고 싶을 때:
    - 메서드나 클래스가 항상 유효한 객체를 기대할 때.
2. 기본 동작을 정의해야 할 때:
    - 비어 있거나 기본값으로 동작해야 하는 경우.
3. 코드의 복잡도를 줄이고 싶을 때:
    - 여러 if-else 또는 null 체크가 반복적으로 사용되는 경우.
4. 다형성을 유지하려는 경우:
    - null 대신 특정 인터페이스의 구현체를 사용하여 객체의 행위를 일관되게 유지.

## Pros

1. 가독성 향상:
    - null 체크를 제거하여 더 간결하고 읽기 쉬운 코드를 작성할 수 있음.
2. 기본 동작 제공:
    - null 대신 명확한 기본 동작을 정의함으로써 예외 발생 가능성을 줄임.
3. 다형성 활용:
    - null 대신 인터페이스 구현체를 사용하여 다형성을 유지.
4. 버그 감소:
    - null 로 인해 발생할 수 있는 런타임 오류 (NullPointerException 등) 를 방지.

## Cons

1. 추가 클래스 생성:
    - Null Object 를 구현하기 위해 추가 클래스가 필요, 코드 복잡도가 증가할 수 있음.
2. 의도 파악 어려움:
    - Null Object 의 동작이 명확하지 않으면 실제 객체와의 차이를 이해하기 어려울 수 있음.
3. 메모리 오버헤드:
    - null 을 사용하는 것보다 객체를 생성하고 유지하는 데 추가 메모리가 필요.

## Relationship with other patterns

### Similarity

#### [Strategy Pattern](../behavioral/patterns/Strategy%20Pattern.md)

둘 다 인터페이스를 사용하여 다양한 동작을 캡슐화하지만, Null Object Pattern 은 비활성 동작을 제공하는 데 초점이 있음.

#### [Decorator Pattern](../structural/patterns/Decorator%20Pattern.md)

Decorator 는 동작을 추가하거나 변경하지만, Null Object 는 비활성 또는 기본 동작을 제공함.

### Difference

#### Factory Pattern

Factory Pattern 은 객체 생성을 책임지고, Null Object Pattern 은 비활성 객체를 제공하여 null 을 대체.

#### [Null Object Pattern](Null%20Object%20Pattern.md)

State Pattern 은 객체 상태에 따라 동작이 변하지만, Null Object Pattern 은 null 을 처리하기 위한 고정된 동작을 제공.
