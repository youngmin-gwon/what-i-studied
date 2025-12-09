---
title: Singleton Pattern
tags: [creational-pattern, design-pattern, gof, oop]
aliases: []
date modified: 2025-12-09 11:57:48 +09:00
date created: 2024-12-12 14:53:18 +09:00
---

## Description

하나의 인스턴스만을 만들어 사용하기 위한 패턴.

커넥션 풀, 스레드 풀, 디바이스 설정 객체 등의 경우 인스턴스를 여러 개 만들게 되면 자원을 낭비하게 되거나 버그를 발생시킬 수 있으므로 오직 하나만 생성하고 그 인스턴스를 사용하도록 하는 것이 이 패턴의 목적.

class 의 instance 를 만드는 것이 비용이 클 때 사용할 수 있음. ex. 클래스를 인스턴스화 할 때 외부 데이터를 가져오는 시간이 많이 드는 경우

같은 객체를 반복해서 사용해야될 때 사용할 수 있음

하나의 인스턴스만을 사용하게 하도록 하기 위해 인스턴스 생성에 특별한 제약을 걸어둬야 함 → 생성자에 private 접근 제어자를 지정하고, 유일한 단일 객체를 반환할 수 있도록 정적 메소드를 지원해야 함. 또한 유일한 단일 객체를 참조할 정적 참고변수가 필요함.

## Consideration

- 필요할 때만 사용하기 위해서 lazy construction 을 고려해야함.
- 대부분의 경우 singleton class 를 생성하기 위해 parameters 가 필요하지 않아야 함 ⇒ parameter 를 받는 다는 것은 조건에 따라 다른 객체가 생성된다는 의미이고 이것은 더이상 singleton 이라고 할 수 없음
- multi-threaded 환경에서 safe 하게 사용할 수 있도록 해야함 (만약, singleton 이 mutable data 를 가지고 있다면 예상하지 못한 결과를 만들어낼 수 있음)
- 때로는, singleton 은 anti-pattern 이라는 것을 숙지해야함 (OOP [[../../../solid/SOLID]] principle 에서 [[../../../solid/SRP(Single Responsibility Principle)]] 을 위배함)
- 타입으로 제공되는 인터페이스가 있지 않다면 singleton 을 복제하는 것이 불가능하기 때문에 unit test 를 어렵게 함
