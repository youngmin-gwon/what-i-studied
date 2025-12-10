---
title: SRP(Single Responsibility Principle)
tags: [oop, solid, srp]
aliases: []
date modified: 2025-12-10 14:22:26 +09:00
date created: 2024-12-12 15:16:57 +09:00
---

## 개요

>"A class should have one, and only one, reason to change."
>Robert C. Martin

- **클래스는 하나의 책임만 가져야 한다.**
- 클래스 하나에 이것저것 다 넣지 말아라. (God Object 방지)
- 어떤 변화에 의해 클래스 변경을 하는 이유는 **단 하나** 뿐 이어야 한다.

## 상세 내용

- 기능으로 분리해도 되고, 목적으로 분리해도 되니, **유지보수성을 최대한 높일 수 있는 방식**으로 코드를 작성해야 함
- SRP 를 적용함으로써, 책임 영역이 확실해지기 때문에 **책임의 변경에서 다른 책임의 변경으로의 연쇄작용**에서 자유로울 수 있음
  - 연쇄작용에 매우 주의 해야함
  - 설계에서 절대 있어서는 안되는 일 ⇒ **의존성 순환 (Circular Dependency)**
  - A 를 수정하니 B 를 수정해야되고 B 를 수정하니 C 를 수정해야하고 C 를 수정하니 A 를 또 수정해야하는 경우 ⇒ 절대 발생해서는 안됨
- 변경사항이 있을 때, 애플리케이션의 **파급 효과 (Side Effect)** 가 적으면 SRP 원칙을 잘 따른 것으로 볼 수 있음
- 다른 객체지향원칙을 적용하는 기초가 됨
