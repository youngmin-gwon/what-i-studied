# Iterator

#oop, #design-pattern, #behavioral-pattern

## Description

![Untitled](../../../../_assets/oop/Untitled%2024.png)

- 컬렉션 구현 방법을 노출시키지 않으면서도 그 집합체안에 들어있는 모든 항목을 순회 접근할 수 있게 해 주는 방법을 제공해 주는 패턴
  - 무언가 많이 모여 있는 것을 하나씩 지정해서 순서대로 처리하는 패턴
- Iterator 패턴을 사용하면 집합체 내에서 어떤 식으로 일이 처리되는지 몰라도 그 안에 들어있는 항목들에 대해서 반복작업을 수행 할 수 있다

## Examples

![Untitled](../../../../_assets/oop/Untitled%2025.png)

- 며칠 동안 로마를 방문하여 주요 명소와 명소를 모두 방문할 계획입니다. 그러나 일단 거기에 가면 콜로세움조차 찾을 수 없는 원을 그리며 걷는 데 많은 시간을 낭비할 수 있습니다.
- 반면에 스마트폰용 가상 가이드 앱을 구입하여 내비게이션에 사용할 수 있습니다. 그것은 똑똑하고 저렴하며 원하는만큼 흥미로운 장소에 머물 수 있습니다.
- 세 번째 대안은 여행 예산의 일부를 지출하고 그의 손등처럼 도시를 아는 현지 가이드를 고용할 수 있다는 것입니다. 가이드는 귀하의 취향에 맞게 여행을 조정하고 모든 명소를 보여주고 흥미 진진한 이야기를 많이 들려줄 수 있습니다. 그것은 훨씬 더 재미있을 것입니다. 그러나 슬프게도 더 비쌉니다.
- 머리 속에서 태어난 임의의 방향, 스마트폰 내비게이터 또는 인간 가이드와 같은 이 모든 옵션은 로마에 있는 방대한 명소와 명소 컬렉션을 반복하는 역할을 합니다.

## Structure

![Untitled](../../../../_assets/oop/Untitled%2026.png)

1. IterableCollection
   - Iterator를 생성하기 위한 인터페이스
   - 컬렉션과 호환되는 Iterator를 얻기 위한 하나 이상의 메서드를 선언
     - ConcreteCollection이 다양한 종류의 Iterator를 반환할 수 있도록 메서드의 반환 유형은 Iterator 인터페이스로 선언
2. ConcreteCollection
   - 특정 ConcreteIterator의 새 인스턴스를 반환하기 위해 Iterator 생성을 구현
     - 클라이언트가 요청할 때마다 특정 ConcreteIterator 클래스의 새 인스턴스를 반환
3. Iterator
   - Collection에 접근하고 순차 순회 하기 위한 인터페이스
   - 컬렉션 순회에 필요한 작업(다음 요소 가져오기, 현재 위치 검색, 반복 다시 시작 등)을 선언
4. ConcreteIterator
   - iterator 인터페이스를 구현
   - 컬렉션을 순회하기 위한 특정 알고리즘을 구현
   - 자체적으로 순회 진행을 추적해야 함
     - 이를 통해 여러 Iterator가 서로 독립적으로 동일한 컬렉션을 순회할 수 있음

## Adaptability

- collection 데이터 타입이 내부적으로 복잡하고, 복잡성을 client에 보여주고 싶지 않을 때 이 패턴을 사용하라
- 순회 코드의 중복을 줄이기 위해 이 패턴을 사용하라
- 구조의 타입이 알려져 있지 않거나, 서로 다른 데이터 구조를 순회하고 싶을 때 사용하라
- 일일이 접근하는 작업을 컬렉션 객체가 아닌 반복자 객체에서 맡게 됨
  - 집합체 인터페이스 구현이 간단해짐
  - 집합체에서는 반복작업에 손을 떼고 원래 자신이 할일에만 전념할 수 있음
    - [[SRP(Single Responsibility Principle)]], DRY 준수하게 됨
  - 같은 collection을 다른 규칙으로 순회하는 방법이 필요할 때, 하나의 인터페이스를 부풀리는 것이 아니라 iterator 클래스를 하나 더 구현하기만 하면 되기 때문에 유용하게 사용할 수 있음
  - 데이터 구조 구현을 확정할 수 없지만, 순회하는 방법이 필요할때 유용함

## Pros

- 장황한 순회 알고리즘을 별도의 클래스로 추출하여 클라이언트 코드와 컬렉션을 정리할 수 있음 ⇒ [[SRP(Single Responsibility Principle)]]
- 기존 코드 수정 없이 새로운 유형의 컬렉션 및 반복자를 추가할 수 있음 ⇒ [[OCP(Open Closed Principle)]]
- 각 iterator 객체에는 고유한 반복 상태가 포함되어 있으므로 동일한 collection을 병렬로 순회 할 수 있음
- 원할 때 순회를 중단/재개 할 수 있음

## Cons

- 간단한 Collection만 사용한다면 과한 패턴
- 일부 특수 컬렉션의 요소를 직접 살펴보는 것보다 덜 효율적일 수 있음

## Relationship with other patterns

### [[Composite Pattern]]

- Composite와 Iterator를 함께 사용하여, Composite tree를 순회 하게 할 수 있음

### [[Factory Method Pattern]]

- Factory Method와 Iterator를 함께 사용하여, 컬렉션 하위 클래스가 컬렉션과 호환되는 다양한 유형의 반복자를 반환하도록 할 수 있음

### [[Memento Pattern]]

- Memento와 Iterator를 함께 사용하여, 현재 상태를 알고, 또 필요한 경우 되돌릴 수 있음

### [[Visitor Pattern]]

- Visitor와 Iterator를 함께 사용하여, 모두 다른 클래스이더라도, 복잡한 데이터 구조를 순회하고 요소에 대해 일부 작업을 실행할 수 있음
