---
aliases: []
date created: 2024-12-12 14:38:36 +09:00
date modified: 2024-12-16 12:20:29 +09:00
tags: [design-pattern, gof, oop, structural-pattern]
title: Structural Pattern
---

## Description

클래스나 객체를 조합해 더 큰 구조를 만드는 패턴

- 서로 독립적으로 개발한 클래스 라이브러리를 마치 하나인 것처럼 사용할 수 있음
- 여러 인터페이스를 합성하여 서로 다른 인터페이스들의 통일된 추상을 제공
- 인터페이스나 구현을 복합하는 것이 아니라 객체를 합성하는 방법을 제공

## Type

1. 어댑터 패턴 ([[patterns/Adapter Pattern]]) : 인터페이스가 호환되지 않는 클래스들을 함께 사용할 수 있도록, 타 클래스의 인터페이스를 기존 인터페이스에 덧씌운다
2. 브리지 패턴 ([[patterns/Bridge Pattern]]) : 추상화와 구현을 분리해 둘을 각각 따로 발전시킬 수 있다
3. 합성 패턴 ([[patterns/Composite Pattern]]) : 0 개, 1 개 혹은 그 이상의 객체를 묶어 하나의 객체로 사용할 수 있다
4. 데코레이터 패턴 ([[patterns/Decorator Pattern]]) : 기존 객체의 메서드에 새로운 행동을 추가하거나 오버라이드 할 수 있다
5. 퍼사드 패턴 ([[patterns/Facade Pattern]]) : 많은 분량의 코드에 접근할 수 있는 단순한 인터페이스를 제공한다
6. 플라이웨이트 패턴 ([[patterns/Flyweight Pattern]]) : 다수의 유사한 객체를 생성, 조작하는 비용을 절감할 수 있다
7. 프록시 패턴 ([[patterns/Proxy Pattern]]) : 접근 조절, 비용 절감, 복잡도 감소를 위해 접근이 힘든 객체에 대한 대역을 제공한다
