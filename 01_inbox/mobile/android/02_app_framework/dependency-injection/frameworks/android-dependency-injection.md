---
title: android-dependency-injection
tags: []
aliases: []
date modified: 2026-04-05 17:43:03 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-dependency-injection](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection.md)

### Dependency Injection: Hilt, Dagger & Koin

안드로이드 앱의 확장성과 테스트 가능성을 극대화하는 **의존성 주입(Dependency Injection)** 패턴과 주요 프레임워크들을 분석합니다.

단순히 라이브러리를 설정하고 사용하는 법을 넘어, **Hilt**와 **Dagger**가 어떻게 컴파일 타임에 의존성 그래프를 검증하고 객체의 생명주기를 관리하는지 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [💡 Context: 왜 DI 가 필수인가?](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection/01-context-%EC%99%9C-di-%EA%B0%80-%ED%95%84%EC%88%98%EC%9D%B8%EA%B0%80.md)
- [의존성 주입이란](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection/02-%EC%9D%98%EC%A1%B4%EC%84%B1-%EC%A3%BC%EC%9E%85%EC%9D%B4%EB%9E%80.md)
- [Hilt (권장)](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection/03-hilt-%EA%B6%8C%EC%9E%A5.md)
- [Dagger (Legacy - 수동 설정)](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection/04-dagger-legacy-%EC%88%98%EB%8F%99-%EC%84%A4%EC%A0%95.md)
- [Koin (경량 DI)](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection/05-koin-%EA%B2%BD%EB%9F%89-di.md)
- [테스트](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection/06-%ED%85%8C%EC%8A%A4%ED%8A%B8.md)
- [비교](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection/07-%EB%B9%84%EA%B5%90.md)
- [더 보기](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/android-dependency-injection/08-%EB%8D%94-%EB%B3%B4%EA%B8%B0.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
