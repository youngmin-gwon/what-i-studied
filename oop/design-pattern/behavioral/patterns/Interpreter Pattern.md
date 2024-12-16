---
aliases: []
date created: 2024-12-12 15:47:19 +09:00
date modified: 2024-12-16 12:20:04 +09:00
tags: [behavioral-pattern, design-pattern, gof, oop]
title: Interpreter Pattern
---

## Description

- 언어를 주고, 문법의 표현을 정의하여 해당 언어로 된 기술 문장을 해석하는 번역기를 함께 정의하는 패턴
- 규칙을 정의하고 이에 맞춰서 프로세스를 해석하는 패턴
- 규칙 관리가 쉬워짐
- 분석

## Structure

![Untitled](../../../../_assets/oop/Untitled%2023.png)

1. AbstractExpression
    - 추상 구문 트리에 속한 모든 노드에 해당하는 클래스들이 공통으로 가져야 할 `interpret()` 연산을 추상 연산으로 정의
2. TerminalExpression
    - 문법에 정의한 터미널 기호와 관련된 해석 방법을 구현
    - 문장을 구성하는 모든 터미널 기호에 대해서 해당 클래스를 만들어야 함
    - 사칙 연산에서 숫자의 역할
3. NonTerminalExpression
    - non-terminal 기호에 대한 `interpret()` 연산 구현
    - 사칙 연산에서 연산자 역할
4. Context
    - Expression 인스턴스에 공유되는 번역기에 대한 포괄적인 정보를 포함
5. Client
    - 언어로 정의한 특정 문장을 나타내는 추상 구문 트리
    - 추상 구문 트리는 NonTerminalExpression 과 TerminalExpression 클래스의 인스턴스로 구성
    - 이 인스턴스의 `interpret()` 연산을 호출

## [[Composite Pattern]] vs Interpreter

- Composite 패턴은 오직 static 한 시스템 특성을 정의하거나 구조를 정의하기 위해서 사용됨
- Interpreter 패턴은 언어를 상징하고, 행위를 정의하고, 트리 안의 구성 노드들의 해석 방법을 제시하고, 문맥을 공유하기 위해 사용됨
- Interpreter 패턴은 문장을 구성하기 위해서 Composite 패턴을 사용함

## Adaptability

- 비교적 간단한 언어 (e.g. RegEx, bar codes, 사칙 연산) 를 해석하기 위해서만 사용됨
- 성능이 중요한 고려사항이 아닐때만 사용해야함
- 어떤 언어의 문법을 10 개 이하의 클래스로 구현할 수 있다면, Interpreter 패턴을 사용하는 것이 좋다.
  - 검색 조건식을 통해 객체나 데이터베이스를 검색하는 것

## Examples

- Specification 과 Query Object 패턴은 Interpreter 패턴을 매우 적극적으로 사용하는 예다. 두 패턴은 모두 단순한 문법과 객체의 조합을 이용해 검색 조건식을 모델화하는 것으로, 검색 조건식과 그 표현을 분리하는 데 유용하게 쓰일 수 있다. 예를 들어, Query Object 패턴은 쿼리를 일반화해 모델로 만들기 때문에 데이터베이스에 실제로 쿼리할 때 사용되는 SQL 로 쉽게 변환할 수 있다.
- 인터프리터는 시스템 설정을 런타임에 변경하기 위해 사용되는 경우도 많다. 예를 들어, 시스템에서 사용자 인터페이스를 통해 사용자가 원하는 설정을 쿼리 형태로 입력받은 다음, 그 쿼리를 나타내는 해석 가능한 객체 구조를 동적으로 생성할 수 있다. 이런 식으로 인터프리터는 시스템 내의 모든 동작이 정적이어서, 동적으로 설정할 수 없는 경우에는 불가능한 훨씬 더 큰 강력함과 융통성을 제공할 수 있다.

## Consideration

- Interpreter 패턴은 단순한 언어를 해석할 때 유용한 패턴임
  - 문법을 클래스 몇 개로 모델화 할 수 있을 때, 그 언어는 단순하다고 말함
  - 단순한 언어의 문장이나 수식은 그 문법을 정의하는 클래스들의 인스턴스를 조합해 표현할 수 있음 ⇒ 이때는 보통, Composite 패턴을 이용
- Interpreter 패턴을 구현하는 것은 Composite 패턴보다 약간 더 복잡할 뿐이지만, 가장 어려운 점은 어떤 경우에 인터프리터가 필요한지를 아는 것임
- 언어가 복잡하거나 반대로 아주 단순한 경우에는 Interpreter 가 필요 없음 ⇒ 어떤 언어의 문법을 10 개 이하의 클래스로 구현할 수 있다면 선택해볼만 함
