---
title: DIP(Dependency Inversion Principle)
tags: [dip, oop, solid]
aliases: []
date modified: 2024-12-16 15:31:16 +09:00
date created: 2024-12-12 15:29:14 +09:00
---

## 개요

> "Depend upon abstractions. Do not depend upon concretions."
> Robert C. Martin

- **구체화(Concretion)가 아니라 추상화(Abstraction)에 의존해야 한다.**
- 즉, **구현 클래스가 아니라 인터페이스에 의존해야 한다.**
- 고수준 모듈은 저수준 모듈의 구현에 의존해서는 안 되며, 저수준 모듈이 고수준 모듈에서 정의한 추상 타입에 의존해야 한다.

## 상세 내용

- **예시 (Analogy)**
  - 연극(고수준)은 특정 배우(저수준/구체화)를 염두에 두고 기획되기보다는 **배역(추상화)** 에 집중해서 기획되어야 한다.
  - 그래야 배우가 바뀌어도 연극은 계속될 수 있다.

- **Dependency Inversion (의존성 역전)**
  - 전통적인 절차 지향 프로그래밍에서는 상위 모듈이 하위 모듈을 가져다 썼다. (의존성 방향: 상위 -> 하위)
  - DIP를 적용하면 하위 모듈이 상위 모듈의 인터페이스를 구현한다. (의존성 방향: 하위 -> 상위 인터페이스)
  - 하위 레벨의 변경이 상위 레벨 모듈의 변경을 강제하는 위계관계를 끊어낸다.

## 핵심 키워드

1.  **IoC (Inversion of Control)**: 제어의 역전. 프레임워크가 객체의 생명주기를 관리.
2.  **Hook Method**: 템플릿 메소드 패턴 등에서 자식 클래스가 로직에 개입할 수 있는 지점.
3.  **확장성**: 결합도를 낮춤으로써 얻는 이점.
