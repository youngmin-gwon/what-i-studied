---
title: android-compose-internals
tags: [android, android/compose, android/jetpack, android/ui]
aliases: []
date modified: 2026-07-31 15:18:35 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Jetpack Compose Internals android android/compose android/ui

Jetpack Compose 의 내부 동작과 성능 최적화. 기본은 [android-jetpack-architecture](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture.md) 참고.

---

## 원자 노트

- [Compose 기본 개념](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/01-compose-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90.md)
- [재구성 (Recomposition)](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/02-%EC%9E%AC%EA%B5%AC%EC%84%B1-recomposition.md)
- [상태 관리](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/03-%EC%83%81%ED%83%9C-%EA%B4%80%EB%A6%AC.md)
- [Side Effects](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/04-side-effects.md)
- [성능 최적화](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/05-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94.md)
- [LazyColumn/LazyRow 최적화](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/06-lazycolumn-lazyrow-%EC%B5%9C%EC%A0%81%ED%99%94.md)
- [Modifier 최적화](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/07-modifier-%EC%B5%9C%EC%A0%81%ED%99%94.md)
- [CompositionLocal](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/08-compositionlocal.md)
- [ViewModel 통합](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/09-viewmodel-%ED%86%B5%ED%95%A9.md)
- [Navigation Compose](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/10-navigation-compose.md)
- [Navigation Compose (Type-Safe Routing)](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/11-navigation-compose-type-safe-routing.md)
- [테스팅](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/android-compose-internals-12-%ED%85%8C%EC%8A%A4%ED%8C%85.md)
- [디버깅](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/android-compose-internals-13-%EB%94%94%EB%B2%84%EA%B9%85.md)
- [Kotlin 2.0+ Compose 컴파일러 분리](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/14-kotlin-2-0-compose-%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC-%EB%B6%84%EB%A6%AC.md)
- [Strong Skipping Mode (Compose 1.6+)](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/15-strong-skipping-mode-compose-1-6.md)
- [더 보기](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals/16-%EB%8D%94-%EB%B3%B4%EA%B8%B0.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H3 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
