# Self Shunt Pattern

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

- 객체는 일반적인 동작을 수행하지만, 특정 조건이 맞으면 자신을 다른 동작으로 전환합니다.
- 이후 조건이 풀리면 다시 원래의 동작으로 돌아옵니다.

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

- UserInput 클래스는 사용자가 입력한 이름을 검증합니다.
- CrashTestDummy 클래스는 의도적으로 잘못된 입력을 제공하여 시스템이 어떻게 반응하는지를 테스트합니다.
- SystemUnderTest 클래스는 입력을 처리하고 검증합니다.
- CrashTestDummy는 의도적인 잘못된 데이터를 주입하여 시스템의 예외 처리 로직을 테스트합니다.

## Adaptability

1. 예외 처리 로직 테스트
    • 시스템에서 예상치 못한 예외나 오류를 처리하는 능력을 검증하고 싶을 때.
2. 강건한 시스템 구축
    • 시스템이 다양한 비정상적인 입력이나 상황에서도 안정적으로 동작하는지 확인하고 싶을 때.
3. 시스템의 내구성 검증
    • 시스템의 오류 복구 기능이나 내구성을 테스트하여, 다양한 상황에서의 안정성을 평가하고자 할 때.
4. 개발 초기 단계
    • 코드가 완전히 안정화되지 않은 상태에서 예외 상황을 미리 시뮬레이션하여 시스템이 예상대로 동작하는지 확인하고 싶을 때.

## Pros

1. 시스템의 강건성 검증
    - 예외나 오류 상황에서도 시스템이 적절하게 반응하는지 확인할 수 있음.
2. 예기치 않은 상황에 대한 대비
    - 현실적인 예외 상황을 시뮬레이션함으로써 시스템이 실제 운영 환경에서도 안전하게 동작하도록 만듦.
3. 예외 처리 로직 개선
    - Crash Test Dummy를 사용하여 예외 처리 코드가 제대로 작동하는지 검증하고 개선할 수 있음.
4. 테스트 커버리지 확대
    - 다양한 비정상적인 상황을 테스트하여 시스템의 신뢰성을 높일 수 있음.

## Cons

1. 테스트 코드의 과도한 의존성
    - 실제 시스템 코드와 별개로 테스트용 더미 객체를 많이 만들어야 하므로, 테스트 코드가 복잡해질 수 있음.
2. 불필요한 오류 발생
    - 시스템이 오류를 처리하는 로직을 검증하기 위해 의도적으로 오류를 발생시키기 때문에, 실제 시스템에서는 필요하지 않은 오류 상황을 만들게 됨.
3. 시뮬레이션의 한계
    - 실제 환경에서는 더 복잡한 오류나 상황이 발생할 수 있는데, 테스트 환경에서 완벽하게 재현하기 어려울 수 있음.
4. 유지보수 비용
    - 테스트 목적의 더미 객체를 지속적으로 관리하고 업데이트해야 하므로 유지보수 비용이 추가될 수 있음.

## Why?

If we are testing object A and want to ensure that it performs the appropriate actions on object B, we might construct a mock B to pass to A.

We can reduce the complexity of our test and the number of objects required by ensuring that our test itself implements the interface we would expect of B, and then pass self to A.

## How?

```ruby
# The class that we're trying to test. We want to ensure that when passed an
# object which adheres to the loggable interface, the `write_to_log` method
# adds a log line to the logger object.
class SomeClass
  def write_to_log(logger, log_line)
    logger.add(log_line)
  end
end

# This defines the behaviour of the logger object, extracted to a module for
# convenience. In a real example, we might not be so lucky to have everything
# wrapped into a little bundle for us, but hey.
module Loggable
  attr_reader :lines

  def add(log_line)
    @lines ||= []
    @lines << log_line
  end
end

class Logger
  include Loggable
end


RSpec.describe SomeClass do
  include Loggable

  it 'uses the self shunt pattern to make an object under test interact directly with the test class' do
    object_under_test = SomeClass.new
    object_under_test.write_to_log(self, 'this_is_a_test')
    expect(lines.include?('this_is_a_test')).to be true 
  end
end
```
