---
title: OCP(Open Closed Principle)
tags: [ocp, oop, solid]
aliases: []
date modified: 2025-10-17 18:42:48 +09:00
date created: 2024-12-12 15:19:39 +09:00
---

## 개요

> "Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification."
> Bertrand Meyer

- **Open for Extension (확장에 열려 있다)**: 새로운 변경사항이 발생했을 때 유연하게 코드를 추가할 수 있어야 한다.
- **Closed for Modification (변경에 닫혀 있다)**: 기존 코드를 직접 수정하지 않고도 새로운 기능을 추가할 수 있어야 한다.

## 상세 내용

- **높은 응집도와 낮은 결합도**를 유지하는 핵심 원리
  - **높은 응집도 (High Cohesion)**
    - 하나의 모듈, 클래스가 하나의 책임 또는 관심사에만 집중되어 있다.
    - 같은 책임, 관심사를 기반으로 하나의 객체로 설계하기 때문에 객체에 변경이 발생하더라도 다른 곳에 미치는 영향이 제한적이다.
  - **낮은 결합도 (Low Coupling)**
    - 결합도: 하나의 오브젝트가 변경이 일어날 때 관계를 맺고 있는 다른 오브젝트에게 변화를 요구하는 정도.
    - 하나의 변경이 발생할 때 다른 모듈과 객체로 **변경에 대한 요구가 전파되지 않는 상태**.
    - 책임과 관심사가 다른 객체 또는 모듈과는 낮은 결합도를 유지해야 함.
    - (유지보수 관점에서) 높은 응집도 보다 더 중요한 원칙일 수 있음.

## Implementation

- **추상화(Abstraction)와 다형성(Polymorphism)** 이 OCP를 가능하게 하는 핵심 메커니즘.
  - 인터페이스를 통해 의존성을 역전시키면 구현체가 바뀌어도 클라이언트 코드는 변경되지 않음.
- 전역 변수를 사용하는 것은 OCP를 위배하기 쉬우므로 자제해야 함.
