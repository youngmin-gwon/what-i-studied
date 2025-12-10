---
title: ISP(Interface Segregation Principle)
tags: [isp, oop, solid]
aliases: []
date modified: 2024-12-16 15:31:18 +09:00
date created: 2024-12-12 15:24:28 +09:00
---

## 개요

> "Clients should not be forced to depend upon interfaces that they do not use."
> Robert C. Martin

- **자신이 사용하지 않는 인터페이스는 구현하지 말아야 한다.**- 어떤 클래스가 다른 클래스에 종속될 때에는 가능한 최소한의 인터페이스만을 사용해야 함.
-**"하나의 일반적인 범용 인터페이스 보다는, 여러 개의 구체적인 인터페이스가 낫다."**

## 상세 내용

- [SRP(Single Responsibility Principle)](SRP(Single%20Responsibility%20Principle).md) 가 클래스의 단일책임을 강조한다면, ISP 는 **인터페이스의 단일책임** 을 강조함.
- 인터페이스를 잘게 쪼개어 클라이언트가 꼭 필요한 기능만 구현하거나 의존하게 해야 함.

## 대전제
- 핵심이 되는**Root Interface** 는 한번 정해지면 바뀌지 않아야 한다.
- 인터페이스가 변경되면 이를 구현한 수많은 클래스와 사용하는 코드들이 모두 영향을 받기 때문.

## 적용 방법 (How)
- 하나의 거대한 인터페이스를 여러 클라이언트가 서로 다른 목적으로 사용할 때:
  - 각 클라이언트의 목적에 맞게 **인터페이스를 분리(Segregation)** 해서 제공하자.
  - 예: `SmartPhone` 인터페이스 하나에 `call()`, `sms()`, `app()`, `charge()` 가 다 있는 것보다, `Phone`, `AppDevice`, `Chargable` 로 나누는 것.
