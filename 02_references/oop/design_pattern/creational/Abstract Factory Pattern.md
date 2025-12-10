---
title: Abstract Factory Pattern
tags: [creational-pattern, design-pattern, gof, oop]
aliases: []
date modified: 2025-12-09 17:37:27 +09:00
date created: 2024-12-12 15:51:24 +09:00
---

## Description

**Abstract Factory Pattern**은 구체적인 클래스(Concrete Class)에 의존하지 않고, 서로 연관되거나 의존적인 객체들의 **제품군(Family)을 생성하는 인터페이스**를 제공하는 패턴입니다.

- **핵심**: "관련된 객체들을 한 번에 모아서 만든다."
- **목적**: 객체 생성 로직을 클라이언트로부터 분리(캡슐화)하여, 제품군을 쉽게 교체할 수 있도록 함.

## Examples

- **UI 테마**: `Light Theme` vs `Dark Theme`. 버튼, 텍스트박스, 체크박스 등 모든 UI 요소가 테마에 맞춰 세트로 생성되어야 함.
- **OS 호환**: `Windows` vs `Mac`. 각 OS에 맞는 버튼, 창, 마우스 커서 객체들이 세트로 생성되어야 함.

## [Factory Method](Factory%20Method%20Pattern.md)와의 차이점

| 구분 | Factory Method | Abstract Factory |
| :--- | :--- | :--- |
| **목적** | **단일 객체** 생성의 처리를 서브클래스에 위임 | **관련된 객체 제품군(Family)** 생성의 인터페이스 제공 |
| **유연성** | 상속(Inheritance)을 통해 객체 생성 로직 변경 | 구성(Composition)을 통해 객체 생성 팩토리 자체를 교체 |
| **관점** | "어떤 객체 하나를 만들까?" | "어떤 스타일의 객체 세트를 만들까?" |

## Structure

![Untitled](../../../../../_assets/oop/Untitled%2031.png)

1. **Abstract Factory**
    - abstract product 를 생성하는 interface 선언.
2. **Concrete Factory**
    - concrete product 객체들을 생성하는 operations 를 적용.
    - **각각의 Concrete Factory 는 오직 하나의 variant 와 일치한다**.
3. **Product**
    - product 객체의 interface 선언.
4. **Concrete Product**
    - 상응하는 Concrete Factory 에 의해 만들어지는 product 채택.
5. **Client**
    - Abstract factory 만 사용하여 product 사용.

## Adaptability

- 코드가 관련 제품의 다양한 제품군과 함께 작동해야 하지만 해당 제품의 구체적인 클래스에 의존하고 싶지 않을 때 사용해야 함.
  - 미리 정의되지 않았거나 단순히 미래의 확장성을 허용하기 위해.
- 객체가 생성되거나 구성, 표현되는 방식과 무관하게 시스템을 독립적으로 만들고자 할 때.
- 여러 제품군 중 하나를 선택해서 시스템을 설정해야 하고 한번 구성한 제품을 다른 것으로 대체할 수 있을 때.
- 관련된 제품 객체들이 함께 사용되도록 설계되었고, 이 부분에 대한 제약이 외부에도 지켜지도록 하고 싶을 때.
- 제품에 대한 클래스 라이브러리를 제공하고, 그들의 구현이 아닌 인터페이스를 노출시키고 싶을 때.

## Pros

- product 를 생성하는 곳을 한 곳으로 이동시킬 수 있음 ⇒ **[SRP(Single Responsibility Principle)](../../solid/SRP(Single%20Responsibility%20Principle).md)**.
- 코드 수정 없이 새로운 product 를 추가할 수 있음 ⇒ **[OCP(Open Closed Principle)](../../solid/OCP(Open%20Closed%20Principle).md)**.
- Creator 와 ConcreteProduct 간의 결합도를 줄일 수 있음.

## Cons

- 새로운 종류의 Product 를 제공하기 어려울 수 있다.

## Relationship with other patterns

### [Prototype Pattern](Prototype%20Pattern.md), [Builder Pattern](Builder%20Pattern.md)

- 모두 Factory Method 를 기반으로 발전 됨.
- Factory Method 보다 자유롭지만, 복잡함.

### [Builder Pattern](Builder%20Pattern.md)

- Builder 는 복잡한 객체를 단계별로 생성하는 패턴.
- Abstract Factory 는 관계있는 객체의 family 를 만드는 패턴.
- Abstract Factory 는 객체를 바로 생성하지만, Builder 는 객체 생성까지 추가적인 시간이 필요함.

### [Factory Method Pattern](Factory%20Method%20Pattern.md)

- Abstract Factory 는 Factory Method 의 세트를 기반으로 만들어짐.

### [Facade Pattern](../structural/Facade%20Pattern.md)

- 클라이언트 코드에서 서브시스템 객체가 생성되는 방식을 숨기고 싶을 때 Facade 의 대안으로 사용할 수 있음.

### [Bridge Pattern](../structural/Bridge%20Pattern.md)

- Abstract Factory 와 Bridge 패턴을 함께 사용할 수 있음.
- Bridge 에서 정의한 일부 추상화가 특정 구현에서만 작동할 수 있을 때 유용함.
- Abstract Factory 는 관계를 캡슐화하고 클라이언트 코드에서 복잡성을 숨길 수 있음.

### [Singleton Pattern](Singleton%20Pattern.md)

- Abstract Factory 는 Singleton 패턴으로 적용될 수 있음.

## Difference in "factory" keyword

### 1. Factory

- 무언가를 생성하는 function, method, class 를 의미하는 모호한 용어.
- 대부분의 경우, factory 는 객체를 생성하지만, 때때로 file, 데이터베이스의 record 를 생성하기도 함.
- 주로 사용하는 상황 예시.
  - 프로그램의 GUI 를 생성하는 function 혹은 method.
  - User 를 생성하는 클래스.
  - 특정 방식으로 클래스 생성자를 호출하는 정적 메서드.
  - Creational 디자인 패턴 중 하나.

### 2. Creation method

- 객체를 생성하는 메소드.
  - 팩토리 메소드 패턴의 모든 결과가 " 생성 메소드 " 이지만 반드시 그 반대는 아님을 의미.
- 동일 의미
  - **Martin Fowler**가 *Refactoring*에서 언급했던 factory method.
  - **Joshua Bloch**가 *Effective Java*에서 언급했던 static factory method.
- 실제로 생성 메서드는 생성자 호출을 둘러싼 래퍼일 뿐임.
  - 하지만, 생성자 변경 사항에서 코드를 분리하는 데 도움이 될 수 있음.
  - 또한, 새로 만드는 대신 기존 개체를 반환하는 특정 논리를 포함할 수도 있음.
- 많은 사람이 factory method 라고 부름 ⇒ 새로운 객체를 만드는 메소드 이기 때문.
- factory method pattern 과는 다르기 때문에 유의하자.

```java
class Number {
    private $value;

    public function __construct($value) {
        $this->value = $value;
    }

    public function next() {
        return new Number ($this->value + 1);
    }
}
```

### 3. Static creation (or factory) method

- static 으로 선언된 creation method.
  - 즉, 생성을 위해서 객체가 필요하지 않은 경우임.
- static factory method 라고 부르지 않게 유의하자 ⇒ factory method 는 상속을 사용하는 디자인 패턴이기 때문. 즉 sub-classing 할 수 없음.
- 다음 같은 경우에 유용함.
  - 여러 가지 다른 목적을 위한 여러 가지 생성자가 존재해야 하는 경우.
  - 새로 생성하는 것이 아니라 기존에 존재하는 객체들을 재사용하고 싶은 경우.

```java
class User {
    private $id, $name, $email, $phone;

    public function __construct($id, $name, $email, $phone) {
        $this->id = $id;
        $this->name = $name;
        $this->email = $email;
        $this->phone = $phone;
    }

    public static function load($id) {
        list($id, $name, $email, $phone) = DB::load_data('users', 'id', 'name', 'email', 'phone');
        $user = new User($id, $name, $email, $phone);
        return $user;
    }
}
```

### 4. Simple factory pattern

- 파라미터를 이용한 분기로 생성을 다르게 하는 생성 메소드를 가지고 있는 클래스를 의미함.
- 주로 일반 factory 와 혼동하거나, factory 디자인 패턴들 중 하나와 혼동함.
  - simple factory 는 factory method 의 도입 전 중간 과정이라고 생각하는 것을 권장.
- 단일 클래스의 단일 메소드로 표현되다가, 너무 커질 우려가 있어서 subclass 로 나눈 경우로 볼 수 있음 ⇒ 몇 번 반복하면 factory method pattern 이 됨.

```java
class UserFactory {
    public static function create($type) {
        switch ($type) {
            case 'user': return new User();
            case 'customer': return new Customer();
            case 'admin': return new Admin();
            default:
                throw new Exception('Wrong user type passed.');
        }
    }
}
```

### 5. Factory Method pattern

- 객체 생성을 위한 인터페이스를 제공하지만 생성될 객체의 유형을 하위 클래스가 변경할 수 있도록 하는 생성 디자인 패턴.

```java
abstract class Department {
    public abstract function createEmployee($id);

    public function fire($id) {
        $employee = $this->createEmployee($id);
        $employee->paySalary();
        $employee->dismiss();
    }
}

class ITDepartment extends Department {
    public function createEmployee($id) {
        return new Programmer($id);
    }
}

class AccountingDepartment extends Department {
    public function createEmployee($id) {
        return new Accountant($id);
    }
}
```

### 6. Abstract Factory pattern

- 구체적인 클래스를 지정하지 않고 관련 또는 종속 개체의 패밀리를 생성할 수 있는 생성 디자인 패턴.
