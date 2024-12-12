# Crash Test Dummy

#design-pattern, #test-pattern

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

예시: 사용자 입력 검증

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

## Adaptability

1. 예외 처리 로직 테스트
   - 시스템에서 예상치 못한 예외나 오류를 처리하는 능력을 검증하고 싶을 때.
2. 강건한 시스템 구축
   - 시스템이 다양한 비정상적인 입력이나 상황에서도 안정적으로 동작하는지 확인하고 싶을 때.
3. 시스템의 내구성 검증
   - 시스템의 오류 복구 기능이나 내구성을 테스트하여, 다양한 상황에서의 안정성을 평가하고자 할 때.
4. 개발 초기 단계
   - 코드가 완전히 안정화되지 않은 상태에서 예외 상황을 미리 시뮬레이션하여 시스템이 예상대로 동작하는지 확인하고 싶을 때.

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
   - 실제 시스템 코드와 별개로 테스트용 더미 객체를 많이 만들어야 하므로, 테스트 코드가 복잡해질 수 있음
2. 불필요한 오류 발생
   - 시스템이 오류를 처리하는 로직을 검증하기 위해 의도적으로 오류를 발생시키기 때문에, 실제 시스템에서는 필요하지 않은 오류 상황을 만들게 됨
3. 시뮬레이션의 한계
   - 실제 환경에서는 더 복잡한 오류나 상황이 발생할 수 있는데, 테스트 환경에서 완벽하게 재현하기 어려울 수 있음
4. 유지보수 비용
   - 테스트 목적의 더미 객체를 지속적으로 관리하고 업데이트해야 하므로 유지보수 비용이 추가될 수 있음

## Relationship with other patterns

### Similarity

#### [[Strategy Pattern]]

Crash Test Dummy Pattern은 시스템의 동작을 변경할 수 있도록 주입하는 방식으로 Strategy Pattern과 유사하게 동작을 교체하지만, 주로 오류나 예외 처리를 위한 테스트 용도로 사용됨

#### [[Observer Pattern]]

Observer Pattern은 상태 변화에 대한 반응을 캡슐화하지만, Crash Test Dummy Pattern은 시스템이 예외 상황에 어떻게 반응하는지 확인하는 데 초점을 맞추고 있음

### Difference

#### [[State Pattern]]

State Pattern은 객체의 상태에 따라 동작을 변경하는 패턴으로, 시스템의 상태에 맞춰 동작을 정의하지만, Crash Test Dummy Pattern은 의도적으로 비정상적인 입력을 주어 시스템의 반응을 테스트하는 데 사용됨

#### [[Prototype Pattern]]

Prototype Pattern은 객체의 복제에 중점을 둡니다. 반면 Crash Test Dummy는 객체가 특정 동작을 어떻게 처리하는지, 특히 예외적인 상황을 시뮬레이션하는 데 중점을 둡니다.
