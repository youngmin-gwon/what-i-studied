# Pluggable Selector

**Pluggable Selector Pattern**은 실행 시점에서 데이터를 선택하거나 작업의 흐름을 결정하는 로직을 동적으로 설정할 수 있도록 설계된 패턴

이 패턴은 다양한 선택 기준(Selector)을 캡슐화하여 조건문과 분기 로직을 대체하고, 더 유연하고 확장 가능한 코드를 작성할 수 있게 함

## Structure

1. **Selector Interface**:
   - 선택 로직을 정의하는 공통 인터페이스.
2. **Concrete Selector**:
   - 특정 조건에 따라 선택 로직을 구현한 클래스.
3. **Selector Host**:
   - Selector 객체를 주입받아 선택 로직을 실행하는 클래스.

### Details

`Selector Host`는 선택 작업을 외부에서 주입된 `Selector` 객체에 위임

선택 기준이 변경되면 새로운 `Selector`를 주입하여 동작을 유연하게 변경 가능

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

## What?

Replace subclasses with dynamically generated method calls.

## Why?

If we have a large number of subclasses that each implement a single method, the overhead involved in maintaining the code can outweigh the benefit of separating them.

```ruby
class Person
  def greeting
    raise NotImplementedError
  end
end

class EnglishSpeaker < Person
  def greeting
    'Hello!'
  end
end

class FrenchSpeaker < Person
  def greeting
    'Bonjour!'
  end
end
```

## How?

By dynamically constructing our method call based on the desired type, we limit the area in which our changes must take place and the system is easier to maintain and comprehend.

```ruby
class Person
  def greet(language)
    send "#{language}_greeting"
  end

  def english_greeting
    'Hello!'
  end

  def french_greeting
    'Bonjour!'
  end
end
```
