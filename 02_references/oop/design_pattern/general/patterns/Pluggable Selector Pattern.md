---
title: Pluggable Selector Pattern
tags: [design-pattern, general-pattern, oop]
aliases: []
date modified: 2025-12-10 14:25:15 +09:00
date created: 2024-12-12 23:55:33 +09:00
---

## Description

## Description

**Pluggable Selector Pattern**은 호출할 메서드를 하드코딩하지 않고, 실행 시점(Runtime)에 메서드의 이름이나 식별자(Selector)를 동적으로 결정하여 실행하는 디자인 패턴입니다.

- **핵심**: 인터페이스를 구현한 여러 클래스를 만드는 대신(Strategy), 하나의 클래스 안에서 Reflection이나 동적 호출 기능을 이용해 메서드 이름만 바꿔서 다른 로직을 수행합니다.
- **주 사용처**: 리플렉션(Reflection)을 지원하는 언어(Smalltalk, Java, Ruby 등)에서, 비슷한 서명(Signature)을 가진 메서드들 중 하나를 동적으로 골라 실행할 때 사용합니다.

## Structure

1. **Client**: 실행하고 싶은 메서드의 이름(Selecter)을 결정하고 전달함.
2. **Invoker**: 전달받은 Selector를 이용해 실제 메서드를 찾아 실행(Invoke)함.

## Example

### Before (Switch/Case or Strategy)

비슷한 로직을 수행하는 메서드가 많을 때, 이를 분기문으로 처리하거나 각각 클래스로 만들면 코드가 길어집니다.

```dart
String calculate(String type, int a, int b) {
  if (type == "add") return add(a, b);
  else if (type == "sub") return sub(a, b);
  // ... 계속 늘어남
}
```

### After (Pluggable Selector)

Dart는 Reflection(Mirrors)을 지원하지만, 여기서는 개념적인 설명을 위해 `Function` 맵을 사용하는 방식(또는 리플렉션과 유사한 방식)으로 예시를 듭니다. (동적 언어에서는 메서드 이름을 문자열로 받아 실행합니다).

```dart
class Calculator {
  // 실제 로직들
  int add(int a, int b) => a + b;
  int sub(int a, int b) => a - b;
  int mul(int a, int b) => a * b;

  // Pluggable Selector Execution
  int execute(String selectorName, int a, int b) {
    // Reflection을 사용한 동적 호출 (개념적 예시)
    // 실제 Dart 환경(Flutter 등)에서는 Mirror 사용이 제한될 수 있으므로
    // Map<String, Function> 등으로 구현하는 경우가 많음.
    
    // instance.invoke(selectorName, [a, b]);
    // 여기서는 개념적으로 "이름으로 함수를 찾는다"는 것이 중요함.
    throw UnimplementedError("Use Reflection or Map to find method by name: $selectorName");
  }
}
```

## Adaptability

1. **Strategy 패턴의 클래스 폭발 방지**: 아주 간단한 로직 차이 때문에 수많은 Strategy 클래스를 만드는 것을 피하고 싶을 때.
2. **동적 메서드 매핑**: 외부 설정 파일이나 사용자 입력 문자열에 따라 실행할 메서드가 결정도야 할 때.

## Pros

1. **클래스 수 감소**: 비슷비슷한 작은 클래스들을 만들지 않아도 됨.
2. **유연성**: 문자열(Selector)만 바꾸면 실행 로직이 바뀜.

## Cons

1. **타입 안정성 감소**: 컴파일 타임에 메서드 존재 여부를 확인하기 어려움 (오타 나면 런타임 에러).
2. **리팩토링 어려움**: IDE가 메서드 사용처를 추적하기 어려워짐 (이름이 문자열로 관리되므로).
3. **보안 이슈**: 의도치 않은 내부 메서드가 호출될 수 있음.

## Relationship with other patterns

### [Strategy Pattern](../../behavioral/Strategy%20Pattern.md)

- **Strategy**: 인터페이스를 구현한 **객체(Object)**를 교체하여 로직을 변경. (더 안전함, 권장됨)
- **Pluggable Selector**: 호출할 **메서드 이름(String)**을 교체하여 로직을 변경. (더 가벼움, 위험함)

### [Command Pattern](../../behavioral/Command%20Pattern.md)

- Command 패턴은 요청 자체를 객체로 캡슐화하는 것이고, Pluggable Selector는 단순히 어떤 메서드를 때릴지 고르는 방법론에 가까움.
