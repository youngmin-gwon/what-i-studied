---
title: Pluggable Selector Pattern
tags: [design-pattern, general-pattern, oop]
aliases: []
date modified: 2025-12-10 14:25:15 +09:00
date created: 2024-12-12 23:55:33 +09:00
---

## Description

**Pluggable Selector Pattern**은 실행 시점에서 데이터를 선택하거나 작업의 흐름을 결정하는 로직을 동적으로 설정할 수 있도록 설계된 패턴

이 패턴은 다양한 선택 기준 (Selector) 을 캡슐화하여 조건문과 분기 로직을 대체하고, 더 유연하고 확장 가능한 코드를 작성할 수 있게 함

## Structure

1. **Selector Interface**:
   - 선택 로직을 정의하는 공통 인터페이스.
2. **Concrete Selector**:
   - 특정 조건에 따라 선택 로직을 구현한 클래스.
3. **Selector Host**:
   - Selector 객체를 주입받아 선택 로직을 실행하는 클래스.

### Details

`Selector Host` 는 선택 작업을 외부에서 주입된 `Selector` 객체에 위임

선택 기준이 변경되면 새로운 `Selector` 를 주입하여 동작을 유연하게 변경 가능

## Example

### Before

```dart
String selectCategory(String itemType) {
  if (itemType == "fruit") {
    return "Fruits Section";
  } else if (itemType == "vegetable") {
    return "Vegetables Section";
  } else {
    return "Miscellaneous Section";
  }
}

void main() {
  print(selectCategory("fruit"));      // Output: Fruits Section
  print(selectCategory("vegetable")); // Output: Vegetables Section
}
```

### After

```dart
// Selector Interface
abstract class Selector {
  String select(String itemType);
}

// Concrete Selectors
class FruitSelector implements Selector {
  @override
  String select(String itemType) {
    return "Fruits Section";
  }
}

class VegetableSelector implements Selector {
  @override
  String select(String itemType) {
    return "Vegetables Section";
  }
}

class DefaultSelector implements Selector {
  @override
  String select(String itemType) {
    return "Miscellaneous Section";
  }
}

// Selector Host
class CategorySelector {
  Selector _selector;

  CategorySelector(this._selector);

  void setSelector(Selector selector) {
    _selector = selector;
  }

  String execute(String itemType) {
    return _selector.select(itemType);
  }
}

void main() {
  // Initial setup with FruitSelector
  CategorySelector categorySelector = CategorySelector(FruitSelector());
  print(categorySelector.execute("fruit")); // Output: Fruits Section

  // Dynamically switch to VegetableSelector
  categorySelector.setSelector(VegetableSelector());
  print(categorySelector.execute("vegetable")); // Output: Vegetables Section

  // Switch to DefaultSelector
  categorySelector.setSelector(DefaultSelector());
  print(categorySelector.execute("other")); // Output: Miscellaneous Section
}
```

## Adaptability

1. 조건문 및 분기 로직을 줄이고 싶을 때
   - 복잡한 조건문이 많아지는 경우 이를 각 Selector 로 캡슐화하여 가독성을 높일 수 있음.
2. 동적으로 선택 로직을 변경해야 할 때
   - 실행 중에 다른 선택 기준으로 교체해야 하는 시스템.
3. 다양한 선택 기준이 추가될 가능성이 있는 경우
   - 새로운 선택 기준이 필요할 때 기존 코드에 영향을 주지 않고 새로운 Selector 만 추가.
4. 테스트 가능한 코드가 필요할 때
   - 각 선택 로직을 별도의 클래스로 캡슐화하면 단위 테스트 작성이 쉬워짐.

## Pros

1. 가독성과 유지보수성 향상
   - 조건문과 분기를 없애고 로직을 캡슐화하여 코드의 명확성을 높임.
2. 확장성
   - 새로운 선택 기준을 추가해도 기존 코드를 수정할 필요 없음 (Open/Closed Principle 준수).
3. 동적 변경 가능
   - 실행 중에도 선택 로직을 자유롭게 교체 가능.
4. 테스트 용이성
   - 각 Selector 를 독립적으로 테스트할 수 있어 테스트가 쉬움.

## Cons

1. 추가 클래스 증가:
   - 각 선택 기준마다 새로운 Selector 클래스를 만들어야 하므로 클래스 수가 많아질 수 있음.
2. 복잡성 증가:
   - 간단한 선택 작업에 적용할 경우 오히려 코드가 복잡해질 수 있음.
3. 초기 설계 비용:
   - 패턴을 도입하고 구조를 잡는 데 추가적인 시간과 노력이 필요.

## Relationship with other patterns

### Similarity

#### [Strategy Pattern](../../behavioral/Strategy%20Pattern.md)

둘 다 객체의 동작을 캡슐화하여 변경 가능하게 설계하지만, Pluggable Selector Pattern 은 선택 로직에 초점을 맞춤.

#### [State Pattern](../../behavioral/State%20Pattern.md)

State Pattern 은 상태에 따라 객체의 동작을 변경하며, Pluggable Selector Pattern 은 선택 기준에 따라 데이터를 처리.

### Difference

#### Factory Pattern

Factory Pattern 은 객체 생성에 초점, Pluggable Selector Pattern 은 동적으로 선택 로직을 변경하는 데 초점.

#### [Decorator Pattern](../../structural/Decorator%20Pattern.md)

Decorator Pattern 은 기존 객체에 추가 기능을 덧붙이는 데 사용되지만, Pluggable Selector Pattern 은 로직의 " 선택 " 부분을 교체.
