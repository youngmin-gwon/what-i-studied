---
title: Flyweight
created at: 2024-12-12
tags:
  - gof
  - oop
  - design-pattern
  - structural-pattern
aliases:
---

## Description

![Untitled](../../../../_assets/oop/Untitled%2052.png)

- 각 객체의 모든 데이터를 보관하는 대신 여러 개체 간에 공통된 state를 공유하여 RAM을 적개 사용하는 패턴
  - 성능 최적화를 위한 패턴
  - RAM 차지로 인한 성능 문제가 있을 때만 적용
  - 다른 의미 있는 방법이 없을 때 사용
- 슈팅 게임을 만든다고 생각했을 때 총알, 미사일 등을 모두 각각의 객체로 만들어서 사용하게 되면 어마어마한 램 공간을 사용하게 된다 ⇒ 이럴 때 Flyweight 패턴을 적용해 볼 수 있다
- 몇가지를 제외하고 비슷하게 여러 개 사용되는 객체에 적용
- 객체를 두가지로 나눠서 사용
  - Intrinsic state: 변하지 않는 데이터 ⇒ Flyweight 에 저장
  - Extrinsic state: 각 인스턴스마다 변하는 데이터 ⇒ Context 에 저장
- Flyweight는 객체 내부에 Extrinsic state 저장을 중단할는 대신, 이 상태를 의존하는 특정 메소드에 Extrinsic state를 전달하는 방법 제시

## Structure

![Untitled](../../../../_assets/oop/Untitled%2053.png)

1. ***Flyweight***
    - Intrinsic state를 포함하는 곳
    - 변하지 않으니 Intrinsic state는 immutable 해야함
    - method로 extrinsic state가 전달 됨
    - 이 객체는 많은 다른 context에서 공유가 가능해야함
2. ***FlyweightFactory***
    - Flyweight 객체를 만들고 관리하는 곳
    - Client가 Factory를 호출할 때 특정 Flyweight 객체가 존재하는지 확인
      - 존재하지 않으면 새 인스턴스 생성한 다음 반환
3. ***Context***
    - Extrinsic state를 포함하는 곳
      - Extrinsic state는 유일 값
4. ***Client***
    - Flyweight의 Extrinsic state를 저장, 계산, 유지하는 역할

## Adaptability

- 프로그램이 사용 가능한 RAM에 거의 맞지 않는 엄청난 수의 객체를 지원해야 하는 경우에만 사용

## Pros

- 비슷한 객체를 많이 사용할 때, RAM을 아낄 수 있음

## Cons

- flyweight 메서드를 호출할 때마다 컨텍스트 데이터 중 일부를 다시 계산해야 하는 경우 CPU와 RAM의 trade-off 가 있음
- 코드가 복잡해짐
