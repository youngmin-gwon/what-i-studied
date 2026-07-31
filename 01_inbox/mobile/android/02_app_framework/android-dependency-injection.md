---
title: android-dependency-injection
tags: []
aliases: []
date modified: 2026-04-05 17:43:03 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-dependency-injection]]

### Dependency Injection: Hilt, Dagger & Koin

안드로이드 앱의 확장성과 테스트 가능성을 극대화하는 **의존성 주입(Dependency Injection)** 패턴과 주요 프레임워크들을 분석합니다.

단순히 라이브러리를 설정하고 사용하는 법을 넘어, **Hilt**와 **Dagger**가 어떻게 컴파일 타임에 의존성 그래프를 검증하고 객체의 생명주기를 관리하는지 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [[01-context-왜-di-가-필수인가|💡 Context: 왜 DI 가 필수인가?]]
- [[02-의존성-주입이란|의존성 주입이란]]
- [[03-hilt-권장|Hilt (권장)]]
- [[04-dagger-legacy-수동-설정|Dagger (Legacy - 수동 설정)]]
- [[05-koin-경량-di|Koin (경량 DI)]]
- [[06-테스트|테스트]]
- [[07-비교|비교]]
- [[08-더-보기|더 보기]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
