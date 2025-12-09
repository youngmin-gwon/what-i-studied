---
title: Template Method Pattern
tags: [behavioral-pattern, design-pattern, gof, oop]
aliases: []
date modified: 2025-12-09 17:08:22 +09:00
date created: 2024-12-12 15:35:58 +09:00
---

## Description

![Untitled](../../../../../_assets/oop/Untitled%205.png)

- 알고리즘의 구조를 바꾸지 않고 하위 클래스들이 알고리즘의 몇몇 단계를 재정의하게 함.
- 불변하는 알고리즘의 전체 틀을 기준으로 세부사항을 다양하게 만들고자 할 때 사용하게 됨.
- 코드 재사용을 위한 핵심적인 기술 → **DRY Principle (Don't Repeat Yourself)**.
  - 여러 단계로 구성된 알고리즘 (데이터 가져오기 → 처리 → 계산 결과 제공) 이 있을 때 어떤 경우 요구사항은 "3rd-party API 로 데이터 가져오기 → 데이터 처리 → 콘솔창에 계산 결과 제공 " 일 수 있고, 또 다른 경우 " 내장 파일로 데이터 가져오기 → 데이터 처리 → 이메일로 계산 결과 제공 " 일 수 있음.
  - **세부정보는 다르지만 전체 알고리즘 구조는 같다**: " 데이터 가져오기 → 처리 → 계산결과 제공 ".
  - 이러한 경우 template method 는 유용함 : 각 단계 세부 정보는 변경 할 수 있지만 전체 구조는 지켜야 함.
- **변하지 않는 기능은 슈퍼 클래스에 만들어 두고** **자주 변경하며 확장할 기능은 서브 클래스에 만드는 방식**으로 구동.

## Structure

![Untitled](../../../../../_assets/oop/Untitled%206.png)

- **AbstractClass**: 알고리즘의 뼈대를 설명하는 templateMethod 포함. primitive operations 나 AbstractClass 혹은 다른 객체들에 정의된 operations 을 호출함.
- **ConcreteClass**: 변하지 않는 알고리즘 단계를 구현하기 위해 AbstractClass 에 의존.
- Template Method 기능 타입들
  - **primitive operations** : 하위 클래스에서 반드시 구현되어야 하는 추상 함수. default implementation 을 제공하고 필요한 경우 하위 클래스에서 재정의 될 수 있는 concrete operations.
  - **final operations**: 하위 클래스에 의해 override 될 수 없는 concrete operations.
  - **hook operations**: 필요한 경우 하위 클래스가 확장할 수 있는 default behavior 을 제공하는 concrete operations. 대부분의 경우 default 가 아무것도 안 하는 것임.
  - **template method itself**: final 로 정의 될 수 있기 때문에 하위 클래스에 의해 override 될 수 없음.
- template method 는 operations 중 어떤 것이 hook operation 인지 abstract operations 인지 알려줄 필요가 있음 ⇒ override 되어야 하는 경우 접두사로 "Do-" 를 붙여 hook 인지 알려줄 수 있음.
- `Hollywood Principle`

> Don't call us, we will call you

![Untitled](../../../../../_assets/oop/Untitled%207.png)

- Template method 는 high-level component 로 간주됨 → clients 나 알고리즘의 concrete operations 가 template method 에 의해 호출된다는 의미.
  - abstraction 은 details 에 의존하면 안 되고, details 가 abstractions 에 의존해야 함 ⇒ **[DIP(Dependency Inversion Principle)](../../../solid/DIP(Dependency%20Inversion%20Principle).md)**.

## Example

![template_method.png](../../../../../_assets/oop/template_method.png)

## Adaptability

- 알고리즘의 특정 단계만 확장하고 전체 알고리즘이나 해당 구조는 확장하지 않도록 할 때 사용.
- 전체적으로 같지만, 약간의 차이만 있는 알고리즘을 적용할 때 사용.

## Pros

1. 중복 코드를 줄일 수 있다 (=DRY).
2. 자식 클래스의 역할을 줄여 핵심 로직의 관리가 용이하다.
3. 좀 더 코드를 객체지향적으로 구성할 수 있다.
4. 클라이언트가 큰 알고리즘의 특정 부분만 재정의하도록 하여 알고리즘의 다른 부분에 발생하는 변경 사항의 영향을 덜 받도록 할 수 있음.

## Cons

1. 추상 메소드가 많아지면 클래스 관리가 복잡해진다.
2. Subclass 에서 default 구현을 무시하여 **[LSP(Liskov substitution principle)](../../../solid/LSP(Liskov%20substitution%20principle).md)** 을 위반할 수도 있음.
3. 클래스 간의 관계와 코드가 꼬여버릴 염려가 있다.
4. 일부 클라이언트는 알고리즘이 제공한 skeleton 에 의해 제한될 수 있음.

## Relationship with other patterns

### [Factory Method Pattern](../../creational/Factory%20Method%20Pattern.md)

- Factory Method 는 Template Method 를 구체화 한 것. 동시에 Factory Method 는 큰 Template Method 의 한 단계 역할을 할 수 있음.

### [Strategy Pattern](Strategy%20Pattern.md)

- Template Method 는 상속을 기반으로 함 ⇒ 이 메서드를 사용하면 하위 클래스에서 해당 부분을 확장하여 알고리즘의 일부를 변경할 수 있음.
- Strategy 은 구성을 기반으로 함 ⇒ 해당 동작에 해당하는 다른 전략을 제공하여 개체 동작의 일부를 변경할 수 있음.
- Concrete Algorithm 이 선택될 때 차이가 있음.
  - Template Method 는 template 을 상속하기 때문에 컴파일 타임에 정해짐.
  - Strategy 는 런타임에 정해지기 때문에 동적으로 알고리즘 할당 가능.
- Template Method 는 공통된 기능을 공유하도록 설계되어 있지만, Strategy 패턴은 모든 implementation 이 독립적이고 공유되는 코드가 없다.
