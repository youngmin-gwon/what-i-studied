---
title: flutter key
tags: [concept, flutter, key]
aliases: []
date modified: 2025-12-16 15:43:09 +09:00
date created: 2024-12-14 11:17:03 +09:00
---

Widget 이 Widget Tree 를 이동할 때 State 를 보존하게 도와주는 역할

Scroll 위치나 Collection 을 수정할 때 State 를 유지하도록 사용할 수 있음

## 언제?

대부분의 경우는 필요하지 않음

`State` 를 포함하는 같은 타입의 widget Collection 을 추가하거나, 제거하거나, 정렬할 때 사용할 수 있음

collection 의 전체 subtree 가 stateless 이면 key 는 필요하지 않음. 즉, stateful 일 때만 Key 가 필요함

- widget tree 는 element tree 를 만든다
- element tree 는 widget 의 type 에 대한 정보를 가지고, 자식 element 들에 대한 reference 를 가짐
- element 를 skeleton 이라고 생각하자
  - App 의 Structure 를 보여주지만, 추가적인 정보는 reference 를 이용하여 widget 을 바라보면 됨
- 만약 collection(ex. Row Widget) 의 순서를 바꾼다면 어떻게 되나?
  - Flutter 가 element tree 를 collection 부터 자식까지 돌면서 구조가 같은지 확인한다
  - element tree 에 new widget 이 이전과 같은 타입인지, Key 가 같은지 확인하고, 맞다면 새 widget 으로 교체한다
- Stateless, Stateful 은 다르게 동작하게 된다
  - Stateless 의 경우, key 가 없다면 Type 만 확인하기 때문에 Type 이 같으면 새 widget 으로 교체된다 ⇒ 문제 없음
  - Stateful 의 경우, Element 는 State 까지 따로 가지고 있다
  - key 가 없는 Stateful 을 교환하려고 하면, type 체크만 한 이후, 맞다면 Widget reference 만 교체한다 ⇒ 문제가 됨
    - State 는 바뀌지 않음
    - 이 경우에 Key 가 필요하게 됨
    - Key 가 있으면, type 비교는 통과했지만 Key 가 일치하지 않기 때문에 Flutter 는 Element tree 가 다르다는 것을 깨닫고 원래 Element 들을 deactivate 함
    - Widget Reference 들을 가져와서 원래 Element tree 와 비교하기 시작함
    - Flutter 가 key 가 맞지 않는 element 들에게 reference 를 뒤져서 맞는 것을 찾아서 연결해줌

## 어디에 사용해야하는가

>보존해야하는 sub widget tree 최상단에 넣어줘라

첫번째 stateful widget 에 넣어주는 것 아님 ⇒ 만약 Stateless Widget 으로 감싼 Stateful Widget 을 실험해본다면 매우 이상한 현상을 볼 수 있을 것임

- Flutter 의 element-to-widget matching 알고리즘은 한번에 한 위젯 단계 밖에 체크하지 못한다
- LocalKey 를 사용한다면, 아래 단계 key 값이 달라서 비교했는데 맞는 값이 없다면 전혀 예상하지 못한 새로운 값을 만들어내게 된다

## 어떤 키를 사용해야하나

### 1. ValueKey

>하나의 값으로 유효함을 증명할 수 있을 때

eg. (중복 아이템이 등록되지 않았다는 상황에서) Todo-List item 의 task

### 2. ObjectKey

>하나의 값은 안되지만 여러 값의 조합으로 유효함을 증명할 수 있을 때

eg. 전화번호부의 사용자 정보

### 3. UniqueKey

>build method 전에 비교할만한 값이 없을 때 사용

하지만 사용에 주의해야함

- UniqueKey 를 build method 안에서 사용하면 매번 build 가 수행될 때마다 Key 값이 바뀌어서 사용하는 의미가 없어짐

또한, random number 를 key 로 사용하지 않게 주의해야 함

- 역시 UniqueKey 와 같은 이유로, build 마다 값이 바뀌는 경우를 조심

### 4. PageStorageKey

>Scroll location 을 담고 있는 특별한 키, 여러개의 Scroll 이 있는 경우 사용하면 좋을 듯

### 5. GlobalKey

>Widget tree 에서 widget 의 위치가 완전히 바뀌지만, RenderObject 를 사용하고 싶다면 사용할 수 있는 key

performance optimization!

간단한 화면에서는 매우 유용하게 사용할 수 있음

GlobalKey 는 ValueKey 보다 비싸다는 것을 명심하자

KeyedSubtree 랑 같이 사용하면 RenderObject 를 그대로 사용하고 싶은 Widget 을 const 로 유지할 수 있게 도와줌, 대신 Widget 의 Key 는 없애는 방식으로 사용해야 함
