---
title: Self Shunt Pattern
tags: [design-pattern, oop, testing-pattern]
aliases: []
date modified: 2025-12-10 14:02:40 +09:00
date created: 2024-12-12 23:58:38 +09:00
---

## Description

## Description

**Self Shunt Pattern**은 테스트 케이스(Test Case)가 테스트 대상 객체의 협력자(Collaborator) 인터페이스를 직접 구현하여, 별도의 Mock/Stub 클래스를 만들지 않고도 상호작용을 검증하는 테스트 디자인 패턴입니다.

- **목적**: 테스트를 위해 별도의 Mock 클래스를 정의하는 번거로움을 줄이고, 테스트 메서드 내부에서 상호작용을 바로 확인할 수 있게 합니다.
- **핵심**: 테스트 대상 객체에 `this`(테스트 클래스 자신)를 전달합니다.

## Structure

1. **Target Object (SUT)**: 테스트 대상. 협력자(Collaborator)를 주입받아 사용함.
2. **Collaborator Interface**: 대상 객체가 의존하는 인터페이스.
3. **Test Case (Self Shunt)**: 테스트 클래스 자체가 Collaborator Interface를 구현(Implement). SUT에게 자기 자신(`this`)을 의존성으로 주입.

## Example

### Before (별도의 Mock 클래스 생성)

```dart
class MockDisplay implements Display {
  String lastMessages = "";
  void show(String message) {
    lastMessage = message;
  }
}

void testDisplay() {
  var mock = MockDisplay();
  var user = User(mock);
  user.sayHello();
  assert(mock.lastMessage == "Hello");
}
```

### After (Self Shunt 적용)

테스트 클래스가 직접 인터페이스를 구현합니다.

```dart
class UserTest implements Display { // 1. 인터페이스 구현
  String _lastMessage = "";

  // 2. 협력자 메서드 오버라이드 (자신에게 결과 기록)
  @override
  void show(String message) {
    _lastMessage = message;
  }

  void testSayHello() {
    var user = User(this); // 3. 자기 자신(this)을 주입
    user.sayHello();
    
    assert(_lastMessage == "Hello"); // 4. 상태 검증
  }
}
```

## Adaptability

1. **Mock 클래스 생성이 번거로울 때**
    - 간단한 인터페이스를 검증해야 하는데 별도 파일을 만들기 귀찮을 때.
2. **상호작용 검증이 필요할 때**
    - 메서드가 호출되었는지, 어떤 값이 전달되었는지 확인해야 할 때.

## Pros

1. **테스트 가독성 향상**: 검증 로직이 테스트 클래스 내부에 모여 있어 이해하기 쉬움.
2. **불필요한 클래스 감소**: 1회성 Mock 클래스를 만들지 않아도 됨.

## Cons

1. **인터페이스가 복잡하면 부적합**: 구현해야 할 메서드가 50개라면 테스트 클래스가 너무 지저분해짐 (이럴 땐 Mock Framework 사용 권장).
2. **테스트 클래스의 역할 혼재**: 테스트 로직과 Mock 로직이 섞일 수 있음.

## Relationship with other patterns

### [Crash Test Dummy Pattern](Crash%20Test%20Dummy%20Pattern.md)

- **Self Shunt**는 정상적인 상호작용 검증에 주로 쓰이고, **Crash Test Dummy**는 에러/예외 상황 시뮬레이션에 주로 쓰임.

### Mock Object

- Self Shunt는 Mock Object 패턴을 구현하는 하나의 기법(Manual Mocking)으로 볼 수 있음.

