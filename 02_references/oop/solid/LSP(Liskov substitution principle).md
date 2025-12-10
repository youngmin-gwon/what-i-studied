---
title: LSP(Liskov substitution principle)
tags: [lsp, oop, solid]
aliases: []
date modified: 2024-12-16 15:31:20 +09:00
date created: 2024-12-12 15:22:01 +09:00
---

## 개요

> "Subtypes must be substitutable for their base types."
> Barbara Liskov

- 프로그램의 정확성을 깨지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다.
- **하위 타입은 언제나 기반 타입과 호환될 수 있어야 함**.
- 즉,**서브 타입은 기반 타입과 약속한 규약 (public interface, method exception) 을 반드시 지켜야 함**.

## 상세 내용

- 상위 타입 클래스 자리에 하위 타입 인스턴스로 바꾸더라도 논리적 오류가 생기지 않아야 한다.
-**다형성** 을 올바르게 지원하기 위한 원칙.
- 인터페이스를 구현한 구현체(Component)를 믿고 사용하려면 LSP 가 필수적이다.

## 상속과 LSP

- 상속은 구현 상속(`extends`)이든 인터페이스 상속(`implements`)이든 궁극적으로는 **다형성을 통한 확장성 획득** 을 목표로 함.
- LSP 원리도 역시 서브 클래스가 확장에 대한 인터페이스를 준수해야 함을 의미.
-**IS-A 관계** 가 성립할 때만 상속을 사용해야 함.
    - 그 외의 경우에는**합성 (Composition)** 을 이용한 재사용을 권장.

## OCP와의 관계

- LSP 는 다형성을 통한 확장 원리인**OCP 를 지원하는 핵심 구조** 가 됨.
- 다형성으로 인한 확장 효과를 얻기 위해서는 서브 클래스가 기반 클래스와 클라이언트 간의 규약(인터페이스)을 어겨서는 안 되기 때문.
- 따라서, LSP 위반은 곧 OCP 위반으로 조만간 이어짐.
