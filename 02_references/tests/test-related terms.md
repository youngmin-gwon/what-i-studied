---
title: test-related terms
tags: [concept, test]
aliases: []
date modified: 2025-12-10 00:29:18 +09:00
date created: 2024-12-18 11:49:39 +09:00
---

## 0.인수기준 (User Acceptance Criteria)

- 프로젝트가 반드시 달성해야 하는 사전에 설정된 기준과 요구사항
- 마치 장보기 할 때, 사야 할 물건을 정리한 리스트와 유사함
- [PM에게 유용한 '인수 기준' 작성법](https://brunch.co.kr/@yongjinjinipln/84)

## 1. 테스트 객체

- SUT(System Under Test): 주요 테스트 객체 (primary object)
- Collaborator: 부차적 객체 (secondary objects)
- Test Double: 테스팅 목적으로 진짜 객체 대신 사용되는 모든 종류의 위장 객체

## 2. 검증

### 상태 검증

- 메소드가 수행된 후 SUT 나 협력객체의 **상태** 를 살펴봄으로써 올바른 동작을 했는지 판단

```dart
SomeClass someClass = new SomeClass();
someClass.someMethod();

assertThat(someMethod.someStatus()).isEqualTo(true);
```

### 행위 검증

- 상태 검증과는 달리 SUT 가 협력객체의 특정 메서드가 호출되었는지 등의 **행위** 를 검사함으로써 올바른 동작을 했는지 판단

```dart
SomeClass someClass = new SomeClass();

verify(someClass).someMethod();
```

## 3. 테스트 더블

- [xUnit 테스트 패턴](http://www.acornpub.co.kr/book/xunit) 에서 소개한 테스트 관련 용어
- 테스트를 진행하기 어려운 경우 이를 대신해 테스트를 진행할 수 있도록 만들어주는 객체
  - 테스트 하려는 객체와 연관된 객체를 사용하기 어렵고 모호할 때 대신 해줄 수 있는 객체 (ex. DB 조회)
- 영화 촬영시 위험한 역할을 대신하는 스턴트 더블에서 비롯됨
- 종류는 [Dummy](#dummy), [Fake](#fake), [Stub](#stub), [Spy](#spy), [Mock](#mock) 로 나눔

### Dummy

- 가장 기본적인 테스트 더블
- 인스턴스화 된 객체가 필요하지만 기능은 필요하지 않은 경우에 사용
- Dummy 객체의 메서드가 호출되었을 때 정상 동작은 보장하지 않음
- 객체는 전달되지만 사용되지 않는 객체
- 동작하지 않아도 테스트에는 영향을 미치지 않는 객체를 Dummy 객체라고 함

```dart
abstract class PrintWarning {
  void print();
}

class PrintWarningDummy implements PrintWarning {
  @override
  void print() {
    // 아무런 동작하지 않음
  }
}
```

### Fake

- 복잡한 로직이나 객체 내부에서 필요로 하는 다른 외부 객체들의 동작을 단순화하여 구현한 객체
- 동작의 구현을 가지고 있지만 실제 프로덕션에는 적합하지 않은 객체
- 실제 사용되는 객체처럼 정교하게 동작하지 않는 객체임

```dart
class User {
  final int _id;
  final String _name;

  const User({
    required int id,
    required String name,
  })  : _id = id,
        _name = name;

  int get id => _id;

  String get name => _name;
}

abstract class UserRepository {
  void save(User user);
  User? findById(int id);
}

class FakeUserRepository implements UserRepository {
  final List<User> _users = <User>[];

  @override
  User? findById(int id) {
    for (final user in _users) {
      if (user.id == id) {
        return user;
      }
    }
    return null;
  }

  @override
  void save(User user) {
    if (findById(user.id) == null) {
      _users.add(user);
    }
  }
}
```

### Stub

- Dummy 객체가 실제로 동작하는 것처럼 보이게 만들어 놓은 객체
- 인터페이스 또는 기본 클래스가 최소한으로 구현된 상태
- 테스트에서 호출된 요청에 대해 미리 준비한 의도된 결과를 제공
- 테스트에 프로그램된 것 외에는 응답하지 않음
- 협력객체의 특정 부분이 테스트하기 힘들 경우 stub 을 사용하면 수월하게 테스트할 수 있음

```dart
class StubUserRepository implements UserRepository {
  @override
  User? findById(int id) {
    return User(id: id, name: "Test User");
  }

  @override
  void save(User user) {
  }
}
```

- 단점?
  - 테스트가 수정될 경우 Stub 객체도 함께 수정해야 함

### Spy

- Stub 의 역할을 가지면서 호출된 내용에 대해 약간의 정보를 기록함
- 테스트 더블로 구현된 객체에 자기 자신이 호출 되었을 때 확인이 필요한 부분을 기록하도록 구현
- 실제 객체처럼 동작시킬 수 있고, 필요한 부분에 대해서는 Stub 으로 만들어서 동작을 지정할 수도 있음

```dart
class Mail {}

class MailingService {
  int sendMailCount = 0;
  final _mails = <Mail>[];

  void sendMail(Mail mail) {
    sendMailCount++;
    _mails.add(mail);
  }

  int getSendMailCount() {
    return sendMailCount;
  }
}
```

### Mock

- 호출에 대한 기대를 명세하고 내용에 따라 동작하도록 프로그래밍 된 객체
- stub 과 헷갈리기 때문에 주의
- 다른 테스트 더블과는 달리 행위검증 사용을 추구함
- 혹자는 Fake 와 달리 아무런 state 를 가지지 않고 행동만 하는 것을 이야기 한다고 함
