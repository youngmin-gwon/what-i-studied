# Pluggable Object

## Description

**Pluggable Object Pattern**은 객체의 동작이나 기능을 실행 시간에 동적으로 변경할 수 있도록 설계된 패턴

이 패턴은 플러그인처럼 객체 간의 결합도를 낮추고, 특정 작업을 필요에 따라 유연하게 대체하거나 확장할 수 있게 함

## Structure

1. **Interface or Abstract Class**: 공통 동작(메서드)을 정의.
2. **Concrete Implementations**: 구체적인 동작을 구현하는 클래스.
3. **Pluggable Host Object**: 동작을 실행 시간에 주입받아 사용하는 객체.

## Example

### Before

기존 방식: 고정된 동작

```dart
class Printer {
  void printMessage() {
    print("Default Printing...");
  }
}

void main() {
  Printer printer = Printer();
  printer.printMessage(); // Output: Default Printing...
}
```

### After

```dart
// Abstract Interface
abstract class PrinterBehavior {
  void printMessage();
}

// Concrete Implementations
class DefaultPrinter implements PrinterBehavior {
  @override
  void printMessage() => print("Default Printing...");
}

class FancyPrinter implements PrinterBehavior {
  @override
  void printMessage() => print("✨ Fancy Printing ✨");
}

// Pluggable Host Object
class Printer {
  PrinterBehavior _behavior;

  Printer(this._behavior);

  void setBehavior(PrinterBehavior behavior) {
    _behavior = behavior;
  }

  void printMessage() {
    _behavior.printMessage();
  }
}

void main() {
  // Initial setup with default behavior
  Printer printer = Printer(DefaultPrinter());
  printer.printMessage(); // Output: Default Printing...

  // Dynamically change behavior at runtime
  printer.setBehavior(FancyPrinter());
  printer.printMessage(); // Output: ✨ Fancy Printing ✨
}
```

## What?

Store a reference to an object which implements a known interface and make references to it throughout the rest of the object.

## Why?

We would like to reduce the amount of conditional logic in the following code, which controls movement for a person who is either driving or walking. It's messy as it is, and if we add a third mode of transport, we're really going to be suffering.

```ruby
class Driver
  def start
    @driving = driving?

    if @driving
      press_accelerator
    else
      pedal
    end
  end

  def steer
    if @driving
      turn_wheel
    else
      turn_handlebars
    end
  end

  def stop
    if @driving
      release_accelerator
    else
      stop_pedaling
    end
  end
end
```

## How?

```ruby
class Driver
  def start
    @mode = if driving?
              DrivingMode.new
            else
              CyclingMode.new
            end

    @mode.start
  end

  def steer
    @mode.steer
  end

  def stop
    @mode.stop
  end
end
```
