---
aliases: []
date created: 2024-12-12 14:42:07 +09:00
date modified: 2024-12-16 12:20:01 +09:00
tags: [behavioral-pattern, design-pattern, gof, oop]
title: Behavioral Pattern
---

## Description

객체나 클래스 사이의 알고리즘이나 책임 분배에 관련된 패턴

- 객체가 수행할 수 없는 작업을 여러 개의 객체로 어떻게 분배 하며 객체 사이의 결합도 최소화에 중점을 둠
- 주로 클래스에 적용 하는지 아니면 객체에 적용 하는지에 따라 구분되는 패턴

## Type

1. 책임연쇄 패턴 ([[patterns/Chain of Responsibility Pattern]]) : 책임들이 연결되어 있어 내가 책임을 못 질 것 같으면 다음 책임자에게 자동으로 넘기는 구조
2. 커맨드 패턴 ([[patterns/Command Pattern]]) : 명령어를 각각 구현하는 것 보다는 하나의 추상 클래스에 메서드를 만들고 각 명령이 들어오면 그에 맞는 서브 클래스가 선택되어 실행
3. 인터프리터 패턴 ([[patterns/Interpreter Pattern]]) : 문법 규칙을 클래스화한 구조를 갖는 SQL 언어나 통신 프로토콜 같은 것을 개발할 때 사용
4. 이터레이터 패턴 ([[patterns/Iterator Pattern]]) : 반복이 필요한 자료구조를 모두 동일한 인터페이스를 통해 접근할 수 있도록 메서드를 이용해 자료구조를 활용할 수 있도록 해줌
5. 옵저버 패턴 ([[patterns/Observer Pattern]]) : 어떤 클래스에 변화가 일어났을 때, 이를 감지하여 다른 클래스에 통보해 줌
6. 전략 패턴 ([[patterns/Strategy Pattern]]) : 알고리즘 군을 정의하고 각각의 클래스로 캡슐화한 다음, 필요할 때 서로 교환해서 사용할 수 있게 해줌
7. 템플릿 메서드 패턴 ([[patterns/Template Method Pattern]]) : 상위 클래스에서는 추상적으로 표현하고 그 구체적인 내용은 하위 클래스에서 결정됨
8. 방문자 패턴 ([[patterns/Visitor Pattern]]) : 각 클래스의 데이터 구조로부터 처리 기능을 분리하여 별도의 visitor 클래스로 만들어 놓고 해당 클래스의 메서드가 각 클래스를 돌아다니며 특정 작업을 수행
9. 중재자 패턴 ([[patterns/Mediator Pattern]]) : 클래스간의 복잡한 상호작용을 캡슐화하여 한 클래스에 위임해서 처리함
10. 상태 패턴 ([[patterns/State Pattern]]) : 동일한 동작을 객체의 상태에 따라 다르게 처리해야 할 때 사용
11. 기념품 패턴 ([[patterns/Memento Pattern]]) : ctrl + z 같은 undo 기능 개발할 때 유용한 디자인 패턴. 클래스 설계 관점에서 객체의 정보를 저장
