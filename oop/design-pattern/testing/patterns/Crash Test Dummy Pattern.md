# Crash Test Dummy

## Description

**Crash Test Dummy Pattern**은 시스템에서 특정 코드나 구성 요소가 예상대로 작동하는지 확인하기 위해, 의도적으로 잘못된 입력이나 예외적인 상황을 주입하여 시스템의 반응을 테스트하는 디자인 패턴

이 패턴은 시스템이 예상치 못한 상황에서 어떻게 동작하는지, 그리고 예외 처리 로직이 제대로 작동하는지를 검증하는 데 사용됩니다. 일반적으로 실제 프로덕션 환경에서 발생할 수 있는 이상 상황을 시뮬레이션하는 데 유용

## Structure

1. **Dummy Object**:
   - 의도적으로 잘못된 값을 제공하는 객체. 실제 로직을 실행하는 데 사용되는 것이 아니라 테스트나 예외 처리 용도로만 사용
2. **System Under Test (SUT)**:
   - Dummy Object가 주입되어 테스트되는 시스템. 시스템은 정상적인 객체가 아닌 Dummy Object를 처리하도록 설계
3. **Test Handler**:
   - Crash Test Dummy가 주입된 후 시스템이 어떻게 반응하는지, 예외 처리가 어떻게 이루어지는지를 처리하고 검증하는 역할

### Details

- Crash Test Dummy가 시스템에 주입
- 시스템은 정상적으로 작동해야 하지만, Dummy Object로 인해 예외적인 상황이나 오류가 발생할 수 있음
- 시스템이 이러한 오류를 어떻게 처리하는지, 그리고 테스트가 성공적으로 완료되었는지를 확인

## 3. Example

```dart
class UserInput {
  String username;

  UserInput(this.username);

  bool validate() {
    // 이름이 비어있거나 null이면 잘못된 입력으로 처리
    return username.isNotEmpty;
  }
}

class CrashTestDummy {
  String username = "";

  bool simulateInvalidInput() {
    return username.isEmpty; // 항상 잘못된 입력을 시뮬레이션
  }
}

class SystemUnderTest {
  void handleUserInput(UserInput input) {
    if (input.validate()) {
      print("Input is valid.");
    } else {
      print("Invalid input.");
    }
  }
}

void main() {
  // 정상적인 사용자 입력
  var validInput = UserInput("valid_username");
  var sut = SystemUnderTest();
  sut.handleUserInput(validInput); // Output: Input is valid.

  // Crash Test Dummy를 사용한 잘못된 입력 시뮬레이션
  var crashDummy = CrashTestDummy();
  var invalidInput = UserInput(crashDummy.username);
  sut.handleUserInput(invalidInput); // Output: Invalid input.
}
```

- UserInput 클래스는 사용자가 입력한 이름을 검증
- CrashTestDummy 클래스는 의도적으로 잘못된 입력을 제공하여 시스템이 어떻게 반응하는지를 테스트
- SystemUnderTest 클래스는 입력을 처리하고 검증
- CrashTestDummy는 의도적인 잘못된 데이터를 주입하여 시스템의 예외 처리 로직을 테스트

## What?

A Crash Test Dummy is an object that we have created to fail in a specific — and spectacular — way.

## Why?

We're our own error handling code around a third party API, file system, or similar with well defined but difficult to reproduce failure modes. How do you force someone elses' API to return a given error code, for example, or test that your application gracefully handles a full hard disk without filling the hard disk with trash data?

## How?

We can make a crash test dummy by mocking or stubbing the object that does the actual system interaction and forcing it to raise a certain exception. This allows us to test the error handling in our code without performing extreme acts.

```ruby
require 'net/http'

# Our API client. It performs HTTP interactions, it (usually) works, but it
# doesn't do any error handling of its own.
class MyApiClient
  def read_from_endpoint
    :some_good_stuff_returned_from_the_api
  end
end

# The class under test. This class consumes data from the API using the
# API client, and we want to ensure that our rescue block behaves as
# expected.
class ApiConsumer
  def pull_data
    response = MyApiClient.new.read_from_endpoint
  rescue Net::ReadTimeout
    response = :read_timeout_failure
  ensure
    response
  end
end

RSpec.describe ApiConsumer do
  it 'handles read timeouts from the api' do
    # We're using a stubbed method to implement our crash test dummy.
    expect_any_instance_of(MyApiClient).to receive(:read_from_endpoint)
                                             .and_raise(Net::ReadTimeout)

    consumer = ApiConsumer.new
    expect(consumer.pull_data).to eq(:read_timeout_failure)
  end
end
```
