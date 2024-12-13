# Key

#flutter, #concept, #key

Widget이 Widget Tree를 이동할 때 State를 보존하게 도와주는 역할

Scroll 위치나 Collection을 수정할 때 State를 유지하도록 사용할 수 있음

## 언제?

대부분의 경우는 필요하지 않음

`State`를 포함하는 같은 타입의 widget Collection을 추가하거나, 제거하거나, 정렬할 때 사용할 수 있음

collection의 전체 subtree가 stateless이면 key는 필요하지 않음. 즉, stateful 일 때만 Key가 필요함

- widget tree는 element tree를 만든다
- element tree는 widget의 type에 대한 정보를 가지고, 자식 element들에 대한 reference를 가짐
- element를 skeleton이라고 생각하자
  - App의 Structure를 보여주지만, 추가적인 정보는 reference를 이용하여 widget을 바라보면 됨
- 만약 collection(ex. Row Widget)의 순서를 바꾼다면 어떻게 되나?
  - Flutter가 element tree를 collection부터 자식까지 돌면서 구조가 같은지 확인한다
  - element tree에 new widget이 이전과 같은 타입인지, Key가 같은지 확인하고, 맞다면 새 widget으로 교체한다
- Stateless, Stateful은 다르게 동작하게 된다
  - Stateless의 경우, key가 없다면 Type만 확인하기 때문에 Type이 같으면 새 widget으로 교체된다 ⇒ 문제 없음
  - Stateful의 경우, Element는 State까지 따로 가지고 있다
  - key가 없는 Stateful을 교환하려고 하면, type 체크만 한 이후, 맞다면 Widget reference만 교체한다 ⇒ 문제가 됨
    - State는 바뀌지 않음
    - 이 경우에 Key가 필요하게 됨
    - Key가 있으면, type 비교는 통과했지만 Key가 일치하지 않기 때문에 Flutter는 Element tree가 다르다는 것을 깨닫고 원래 Element들을 deactivate함
    - Widget Reference들을 가져와서 원래 Element tree와 비교하기 시작함
    - Flutter가 key가 맞지 않는 element들에게 reference를 뒤져서 맞는 것을 찾아서 연결해줌

## 어디에 사용해야하는가

> 보존해야하는 sub widget tree 최상단에 넣어줘라

첫번째 stateful widget에 넣어주는 것 아님 ⇒ 만약 Stateless Widget으로 감싼 Stateful Widget을 실험해본다면 매우 이상한 현상을 볼 수 있을 것임

- Flutter의 element-to-widget matching 알고리즘은 한번에 한 위젯 단계 밖에 체크하지 못한다
- LocalKey를 사용한다면, 아래 단계 key 값이 달라서 비교했는데 맞는 값이 없다면 전혀 예상하지 못한 새로운 값을 만들어내게 된다

## 어떤 키를 사용해야하나

### 1. ValueKey

> 하나의 값으로 유효함을 증명할 수 있을 때

eg. (중복 아이템이 등록되지 않았다는 상황에서) Todo-List item의 task

### 2. ObjectKey

> 하나의 값은 안되지만 여러 값의 조합으로 유효함을 증명할 수 있을 때

eg. 전화번호부의 사용자 정보

### 3. UniqueKey

> build method 전에 비교할만한 값이 없을 때 사용

하지만 사용에 주의해야함

- UniqueKey를 build method 안에서 사용하면 매번 build가 수행될 때마다 Key값이 바뀌어서 사용하는 의미가 없어짐

또한, random number를 key로 사용하지 않게 주의해야 함

- 역시 UniqueKey와 같은 이유로, build 마다 값이 바뀌는 경우를 조심

### 4. PageStorageKey

> Scroll location을 담고 있는 특별한 키, 여러개의 Scroll이 있는 경우 사용하면 좋을 듯

### 5. GlobalKey

> Widget tree에서 widget의 위치가 완전히 바뀌지만, RenderObject를 사용하고 싶다면 사용할 수 있는 key

performance optimization!

간단한 화면에서는 매우 유용하게 사용할 수 있음

GlobalKey는 ValueKey보다 비싸다는 것을 명심하자

KeyedSubtree랑 같이 사용하면 RenderObject를 그대로 사용하고 싶은 Widget을 const로 유지할 수 있게 도와줌, 대신 Widget의 Key는 없애는 방식으로 사용해야 함
