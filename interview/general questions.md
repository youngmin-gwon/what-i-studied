---
date created: Monday, December 9th 2024, 12:31:10 pm
date modified: Monday, December 16th 2024, 2:45:08 am
title: general questions
---

## Programming-related Question

### 추상 클래스와 인터페이스의 차이?

#### 1. Abstract Class

- 인스턴스화 되도록 디자인 되지 않음
- implementation 이 없을 수도, 몇개만 있을 수도, 모두 있을 수도 있음
- 하위클래스들이 공통적인 implementation 을 공유하도록 디자인 되었음
- IS - A "~이다 "

#### 2. Interface

- (키워드) implementation 이 없는 abstract class
- Java 같은 언어는 다중 상속을 지원하지 않지만, 다중 인터페이스는 지원함
  - 다중 상속으로 발생하는 문제 ([Deadly Diamond of Death Problem](http://en.wikipedia.org/wiki/Diamond_problem#The_diamond_problem)) 를 해결하기 위한 방법
- HAS - A "~을 할 수 있는 "

#### 공통점

- 추상 클래스와 인터페이스는 상속받는 클래스 혹은 구현하는 인터페이스 안에 있는 추상 메소드를 구현하도록 강제함

#### 차이점

1. 사용 의도의 차이
    - 추상 클래스
      - 클래스를 상속받아 기능을 이용하고, 확장시키기 위해서 사용
    - 인터페이스
      - 함수 정의만 놓고, 이를 하위 클래스에서 구현하도록 강제하여 같은 동작을 보장하기 위해서 사용
    - 이렇게 구분하는 이유는 다중 상속의 가능 여부에 따라 용도가 다르기 때문
      - 다중 상속이 되지 않는 언어에서는 **해당 클래스 구분을 추상클래스 상속을 통해 해결**하고, **할 수 있는 기능들을 인터페이스로 구현**
2. 공통된 기능 사용 여부
    - 민약 모든 클래스가 인터페이스를 사용해서 기본 틀을 구성한다면, 공통으로 필요한 기능들도 모든 클래스에서 오버라이딩 하여 재정의 해야하는 번거로움이 있음
    - 이러한 경우 추상클래스를 이용해 일반 메서드를 작성하여 자식 클래스에서 사용할 수 있도록 처리
    - 만약 추상클래스를 상속하는데 공통된 기능이 필요하다면?
      - 인터페이스로 작성해서 구현

#### 정리

- 추상 클래스 사용 시기: 상속 관계를 쭉 타고 올라갔을 때 같은 조상클래스를 상속하는데 기능까지 완벽히 똑같은 기능이 필요한 경우
- 인터페이스 사용 시기: 상속 관계를 쭉 타고 올라갔을 때 다른 조상클래스를 상속하는데 같은 기능이 필요할 경우

### Mixin 은 무엇인가?

- 같은 클래스 계층에 있지 않은 클래스들로 부터 코드를 재 사용하는 방법
- 클래스 계층에 제한 받지 않고 코드를 재사용할 수 있음
- 상속으로 오는 문제를 해결하기 위한 방법

```dart
abstract class Creature {}

abstract class FlyingAnimal extends Creature {
  void flutter() {
    print("flutter!");
  }
}

abstract class Insect extends FlyingAnimal {}

abstract class Bird extends FlyingAnimal {
  void chirp() {
    print("chirp");
  }
}

class Mosquito extends Insect {}

class Dash extends Bird {}

class Parrot extends Bird {}

abstract class Writable {
  void write();
}

// Interface를 이용하면 매번 같은 행위를 하는 함수를 적어줘야하는 문제가 생김
class QuickBird extends Bird implements Writable {
  @override
  void write() {
    print("writing");
  }
}

class Human extends Creature implements Writable {
  @override
  void write() {
    print("writing");
  }
}
```

- class 를 mixin 으로 사용할 수도, mixin 예약어를 사용한 것 역시 mixin 으로 사용할 수 있음
  - on 키워드를 사용하기 위해서는 mixin 키워드를 이용해서 정의해야함
- mixin 은 polymorphic 하다
  - 상속한 class 와 is 비교했을 때, true 가 되고, mixin 역시 true 이다

```dart
void main(List<String> args) {
  String result = '';

  AB ab = AB();

  print(ab is P); // true
  print(ab is A); // true
  print(ab is B); // true

  BA ba = BA();

  print(ba is P); // true
  print(ba is A); // true
  print(ba is B); // true
}
```

- mixin 내부 원리
  - mixin 은 mixin 을 위에 쌓아서 새로운 클래스를 생성하는 원리로 작동함
- mixin 및 상속의 순서 중요
  - 가장 오른쪽에 있는 것이 우선권을 가지기 때문에 만약 같은 메소드, 필드가 있다면 왼쪽 mixin 이나 class 들의 것들은 가장 오른쪽 것에 overridden 된다

```dart
// mixin 원본
class AB extends P with A, B {}

class BA extends P with B, A {}
```

```dart
// 내부적 의미
class PA = P with A;
class PAB = PA with B;

class AB extends PAB {}

class PB = P with B;
class PBA = PB with A;

class BA extends PBA {}
```

- Mixin 하여 사용할 때, 가장 오른쪽에 있는 Mixin 혹은 상속이 사용된다는 것 명심하기
  - 다중상속이 없음 ⇒ mixin 은 다중상속을 얻는 방법이 아니라 동작을 추상화하고 재사용하기위한 방법이기 때문
- 주의해야할 점
  - 다중 Mixin 을 사용하면 안됨
    - SRP 원칙을 위반하게 됨
    - 사용자를 매우 헷갈리게 할 수 있음
- Mixin 은 상속을 대체하는 것이 아니라 확장한 것임을 명심
