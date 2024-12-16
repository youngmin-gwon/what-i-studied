---
aliases: []
date created: 2024-12-13 00:02:00 +09:00
date modified: 2024-12-16 12:20:17 +09:00
tags: [design-pattern, general-pattern, oop]
title: Collecting Parameter Pattern
---

## Description

Collecting Parameter Pattern 은 여러 데이터를 함수로 전달해야 할 때, 단일 객체를 통해 이 데이터를 수집하고 전달하는 패턴입니다.

이는 인수 목록이 길어지거나 복잡한 경우 코드를 간결하고 가독성 있게 만들기 위해 사용됩니다.

## Structure

```dart
class ParameterObject {
  // 여러 매개변수를 속성으로 포함
}

void someMethod(ParameterObject params) {
  // params 속성을 사용해 작업 수행
}```

1. Parameter Object: 여러 매개변수를 포함하는 객체.
2. Method: 이 객체를 받아 필요한 처리를 수행하는 함수.

## Example

### Before

```dart
void processUser(String name, int age, String email, bool isActive) {
  print("Name: $name, Age: $age, Email: $email, Active: $isActive");
}```

### After

```dart
class UserParams {
  String name;
  int age;
  String email;
  bool isActive;

  UserParams({
    required this.name,
    required this.age,
    required this.email,
    required this.isActive,
  });
}

void processUser(UserParams params) {
  print("Name: ${params.name}, Age: ${params.age}, Email: ${params.email}, Active: ${params.isActive}");
}

void main() {
  UserParams userParams = UserParams(
    name: "John Doe",
    age: 25,
    email: "john.doe@example.com",
    isActive: true,
  );

  processUser(userParams);
}
```

## Adaptability

1. 많은 파라미터를 전달해야 할 때: 인수 목록이 너무 길어지거나 이해하기 어렵다면 사용.
2. 관련 데이터가 그룹화될 때: 연관된 데이터를 묶어 객체로 만들면 코드 가독성이 향상됨.
3. 매개변수 확장 가능성이 높을 때: 매개변수가 추가될 여지가 있으면 객체로 관리하기 쉬움.
4. 테스트 및 재사용성을 고려할 때: 데이터를 별도의 객체로 관리하면 테스트와 재사용이 용이.

## Pros

1. 가독성 향상: 함수 정의와 호출이 간단해지고, 코드를 이해하기 쉬워짐.
2. 확장성: 매개변수가 늘어나더라도 객체에 필드를 추가하는 방식으로 유연하게 대처 가능.
3. 중복 제거: 관련 데이터를 묶음으로 처리하여 중복 코드를 줄임.
4. 재사용성: Parameter Object 를 다른 함수나 모듈에서도 재사용 가능. → SRP

## Cons

1. 객체 생성 비용: Parameter Object 를 추가로 생성해야 하는 비용이 발생.
2. 과도한 추상화 가능성: 단순한 함수에도 패턴을 적용하면 불필요하게 복잡해질 수 있음.
3. 추적 어려움: 데이터가 하나의 객체에 담기면서 어느 데이터가 어느 시점에 변경되었는지 추적하기 어려워질 수 있음.

## Relationship with other patterns

### [[../../creational/patterns/Builder Pattern]]

- 두 패턴 모두 복잡한 데이터 구성을 단순화하고 가독성을 높이는 데 중점을 둠.
- Collecting Parameter Pattern 은 데이터를 한 객체에 묶는 데 집중하고, Builder Pattern 은 객체 생성을 단계적으로 처리함.
- 차이점
  - Collecting Parameter Pattern 은 단순히 데이터를 전달하기 위한 패턴인 반면, Builder Pattern 은 복잡한 객체를 생성하는 과정에 대한 패턴.
  - Collecting Parameter Pattern 은 함수 호출 시에만 주로 사용되는 반면, Builder Pattern 은 객체 초기화 과정 전체에서 사용됨.

### [[../../structural/patterns/Composite Pattern]]

- Collecting Parameter Pattern 에서 Parameter Object 는 Composite Pattern 처럼 여러 속성을 포함하여 복잡한 구조를 나타낼 수도 있음.

### Data Transfer Object Pattern

- Collecting Parameter Pattern 의 Parameter Object 는 DTO 와 유사한 역할을 수행하지만, 주로 함수 호출을 간소화하는 데 초점이 맞춰짐.
