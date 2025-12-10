---
title: Collecting Parameter Pattern
tags: [design-pattern, general-pattern, oop]
aliases: []
date modified: 2025-12-10 14:28:00 +09:00
date created: 2024-12-13 00:02:00 +09:00
---

## Description

## Description

**Collecting Parameter Pattern** 은 메서드가 결과를 반환(Return)하는 대신, 결과를 수집할 객체(컬렉션 등)를 파라미터로 전달받아 그 객체에 결과를 추가(Accumulate)하는 디자인 패턴입니다.

- **목적**: 여러 메서드나 복잡한 객체 구조(예: Composite)를 순회하며 결과를 하나의 객체에 모으고 싶을 때 사용합니다.
- **방식**: `void method(Collector collector)` 형태를 가집니다.

## Structure

1. **Collector**: 결과를 수집할 컨테이너 역할을 하는 객체 (List, StringBuffer, Map, 또는 사용자 정의 클래스).
2. **Client**: Collector를 생성하고, 메서드에 전달한 뒤, 최종 결과를 Collector에서 가져옴.
3.**Methods**: Collector를 인자로 받아, 자신의 결과값을 Collector에 추가함.

## Example

### Before (String Concatenation with Return)

재귀 호출에서 문자열을 계속 반환하고 합치면 메모리 비효율이 발생하고 코드가 복잡해질 수 있습니다.

```dart
class Node {
  String name;
  List<Node> children = [];

  Node(this.name);

  String toStringHelper() {
    String result = name;
    for (var child in children) {
      result += ", " + child.toStringHelper();
    }
    return result;
  }
}
```

### After (Collecting Parameter)

`StringBuffer`를 Collecting Parameter로 사용하여 결과를 누적합니다.

```dart
class Node {
  String name;
  List<Node> children = [];

  Node(this.name);

  // Collecting Parameter (buffer)
  void writeTo(StringBuffer buffer) {
    if (buffer.isNotEmpty) {
      buffer.write(", ");
    }
    buffer.write(name);
    
    for (var child in children) {
      child.writeTo(buffer);
    }
  }
}

void main() {
  var root = Node("Root");
  root.children.add(Node("Child1"));
  root.children.add(Node("Child2"));

  var buffer = StringBuffer();
  root.writeTo(buffer); // Pass collecting parameter
  
  print(buffer.toString()); // Output: Root, Child1, Child2
}
```

## Adaptability

1. **Composite 패턴과 함께 사용**: 트리 구조의 노드들로부터 정보를 수집할 때 매우 유용합니다.
2.**메서드 시그니처가 복잡해질 때**: 리턴 타입이 복잡하거나 여러 종류의 정보를 모아야 할 때 객체 하나만 넘기면 됨.
3.**성능 최적화**: 거대한 문자열이나 리스트를 매번 생성하여 반환하는 비용을 줄이고자 할 때.

## Pros

1.**성능 이점**: 중간 객체 생성을 줄일 수 있음 (예: String Concatenation 방지).
2. **코드 단순화**: 복잡한 반환값 전달 로직을 제거할 수 있음.

## Cons

1.**Side Effect**: 파라미터로 넘어온 객체가 수정되므로, 함수형 프로그래밍(불변성) 원칙에는 위배될 수 있음.
2. **가독성**: 메서드의 반환값이 `void`라, 무엇을 하는지 명확하지 않을 수 있음 (이름을 `collectTo`, `writeTo` 등으로 잘 지어야 함).

## Relationship with other patterns

### [Composite Pattern](../../structural/Composite%20Pattern.md)

- Collecting Parameter는 Composite 구조를 순회하면서 정보를 모을 때 가장 많이 사용되는 패턴 중 하나입니다.

### [Visitor Pattern](../../behavioral/Visitor%20Pattern.md)

- Visitor 패턴에서도 Visitor 객체 내부에 상태를 저장하여 Collecting Parameter와 유사한 효과를 낼 수 있습니다. Visitor 자체가 Collecting Parameter 역할을 하기도 합니다.

### Parameter Object (Different Pattern)

- 많은 사람들이 **Parameter Object Pattern** (여러 인자를 하나의 객체로 묶는 리팩토링 기법) 과 혼동하지만 다릅니다.
  - Parameter Object: 인자 전달을 편하게 하기 위함 (Input).
  - Collecting Parameter: 결과를 모으기 위함 (Output).

