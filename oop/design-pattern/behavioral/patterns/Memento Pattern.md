# Memento(=Token)

#oop, #design-pattern, #behavioral-pattern

## Description

![Untitled](Untitled%2035.png)

- 캡슐화를 위반하지 않고, 객체의 상태를 외부에 snapshot으로 저장하고, 필요에 의하여 원하는 시점의 데이터를 복원할 수 있는 패턴
- 다음 예시 상황을 참고
  - 텍스트 에디터 앱을 만들 때 실행 취소 기능을 만들 것임
    - 직관적인 방법
      - 모든 행위를 수행하기 전에 앱의 모든 객체의 상태를 기록하고, 장치에 저장
      - 이후에 유저가 해당 행위를 되돌리기 원할 때, 앱은 저장한 이력에서 마지막 스냅샷을 꺼내와서 모든 객체의 상태를 복구
    - 문제
        1. 객체의 모든필드들을 조회해서 값을 복사한 후 저장소로 옮겨야함
           - 객체가 외부에 대해 자신의 접근제한을 많이 오픈해야 제대로 동작함 → 은닉화를 풀어야하는 상황
        2. 은닉화를 풀게 되면, 에디터 클래스들을 다시 손보거나 필드들을 일부 추가 및 삭제하면 영향 받는 객체들의 상태 역시 변경해야 함
        3. 필드 전체를 복사하니 스냅샷의 데이터가 엄청나게 많을 것임
            ⇒ 클래스의 세부사항을 노출시키거나, 상태의 접근 제한해서 스냅샷을 생산하는게 불가능해짐

## Principles

- 스냅샷 상태를 만드는 일을 실제 주인인 originator 객체에 위임
  - 다른 객체들이 외부에서 에디터의 상태를 복사하지 않고, 접근권한을 모두 갖고 있는 데이터 클래스 자신이 스냅샷을 만들 수 있음
- 객체의 상태를 복사해서 “memento”라고 불리는 특별한 객체에 저장
  - 내부는 해당 내용을 생성한 객체 외에 다른 객체들은 접근할 수 없음
  - 원본이 아닌 다른 객체들은 제한된 인터페이스로 스냅샷에 포함된 원본 객체의 상태가 아니라 스냅샷의 메타데이터(생성시간, 수행된 행위명)만 갖고 올 수 있음
- 이런 제한된 정책을 구현하기 위해서는 “caretaker” 라고 하는 다른 객체안에 메멘토를 저장해야 함
  - 제한된 인터페이스로만 메멘토와 협업하기 때문에, 메멘토 안에 저장된 상태를 함부로 변경할 수 없음
  - 동시에 originator는 메멘토내의 모든 필드에 접근할 수 있기 때문에 이전 상태를 복구할 수 있게 됨

## Structure

![Untitled](Untitled%2036.png)

1. Memento
   - concrete memento의 fields에 접근을 제한하는 인터페이스
   - 오직 memento의 메타데이터, caretaker 에 의해 사용되는 메소드를 정의함
2. Concrete Memento
   - originator의 내부 상태 스냅샷 역할을 하는 값(Value Object)
   - concrete memento를 생성한 originator를 제외한 다른 객체의 접근을 막음
3. Caretaker
   - memento 보관을 책임지는 보관자
   - memento의 내용을 검토하거나 그 내용을 건드리지 않음
   - memento 스택을 저장함으로써 originator의 히스토리 추적
   - originator가 이전 상태를 알아야 할 때, 스택으로부터 최상위 원소를 가져와서 originator 복구 메소드로 전달함
4. Originator
   - 원본 객체를 의미
   - 상태를 저장함
   - 필요할 때 스냅샷으로 부터 해당 상태를 복구할뿐만 아니라, 자기 자신 상태의 스냅샷을 생산하기도 함

- 객체의 fields/getters/setters에 직접 접근이 캡슐화 원칙을 위배할 때, 보안의 이유로도 사용될 수 있음
  - 다른 object가 snapshot을 읽지 못하게 만들어 original object의 state를 안전하고 보안이 강화되게 만듬

## Command vs Memento

- command 패턴은 redo/undo를 지원할 수 있지만 요청을 단일객체로 만들 수 있음
- memento 패턴은 cache/restore 개념으로 객체의 내부 상태를 저장하고 있다는 것이 핵심
- command 패턴은 상태를 사용하는 부분에 따로 보관해야했지만, memento 패턴은 state를 originator에 보관하게 되어 상태가 안전할 수 있다
- 둘 중 하나만 사용해야 하는 개념은 아님
  - memento 패턴을 이용하여 객체의 내부 상태를 저장하고 있어야 할 때, 되돌리기 기능 제공시 명령 패턴을 함께 사용할 수 있기 때문

## Adaptability

- 객체의 이전 상태를 복원할 수 있도록 객체 상태의 스냅샷을 생성하려는 경우 사용
- 객체의 field/getter/setter에 대한 직접 액세스가 캡슐화를 위반할 때 사용

## Pros

- 캡슐화를 위반하지 않고 객체 상태의 스냅샷을 생성할 수 있음
- Caretaker가 Originator의 상태 기록을 유지하도록 하여 발신자의 코드를 단순화할 수 있음

## Cons

- Memento를 너무 자주 만들게 되면 메모리 사용이 많아짐
- Caretaker는 오래된 Memento를 파괴할 수 있도록 Originator의 수명 주기를 추적해야 함
- PHP, Python 및 JavaScript와 같은 대부분의 동적 프로그래밍 언어는 Memento 내의 상태가 그대로 유지된다고 보장할 수 없음
- 상태를 저장하고 복구하는 데 시간이 오래 걸릴수 있음
  - 직렬화 해서 저장하는 것이 좋음

## Relationship with other patterns

### [[Command Pattern]]

- undo 기능을 적용하기 위해서 Command 패턴과 같이 사용할 수 있음
- Command는 다양한 연산을 목표 객체에 적용하는 것에만 신경 쓰면 되고, Memento는 Command가 수행되기 전 객체의 상태만 기억하는 것에만 신경 쓰면 됨

### [[Iterator Pattern]]

- Memento와 Iterator를 함께 사용하여, 현재 상태를 알고, 또 필요한 경우 되돌릴 수 있음

### [[Prototype Pattern]]

- Prototype이 Memento의 간단한 대안이 될 수도 있음
- 히스토리에 저장하려는 상태인 객체가 간단하고 외부 리소스에 대한 링크가 없거나 링크가 재설정하기 쉬운 경우 대안으로 채택할 수 있음
