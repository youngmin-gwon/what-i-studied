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

- **클래스는 변경해야 할 이유가 단 하나여야 한다.**- 여기서 '변경의 이유'란**'해당 기능을 사용하는 사용자(Actor)나 이해관계자 집단'** 을 의미함.
- 클래스가 여러 책임(역할)을 떠안게 되면, 서로 다른 이유로 변경이 발생할 때 서로에게 영향을 줄 수 있음. (God Object 방지)

## 상세 내용

### 책임(Responsibility)과 변경의 축

- SRP에서 말하는 '책임'은 단순히 '해야 할 일'을 넘어서 **'변경을 요청하는 집단'** 으로 해석해야 명확함.
- 예를 들어, `Employee` 클래스가 `calculatePay()`(회계팀 담당)와 `saveToDB()`(DB관리팀 담당)를 모두 가진다면, 회계 로직 변경 시 DB 로직도 같은 파일에 있어 실수로 영향을 줄 위험이 생김.
- 따라서 **서로 다른 액터(Actor)가 담당하는 로직은 서로 다른 클래스로 분리** 해야 함.

### 효과

-**유지보수성 향상**: 기능이 명확히 분리되어 있어 수정할 위치를 찾기 쉬움.
-**파급 효과(Side Effect) 감소**: 한 클래스의 변경이 다른 클래스에 주는 영향을 최소화함.
-**의존성 순환 방지**: 책임이 분리되면 의존성 관계가 단순해져 Circular Dependency 문제를 피하기 쉬움.
