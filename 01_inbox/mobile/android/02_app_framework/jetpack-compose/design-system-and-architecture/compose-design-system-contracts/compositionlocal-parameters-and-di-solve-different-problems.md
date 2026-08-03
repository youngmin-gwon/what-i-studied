---
title: CompositionLocal 매개변수와 DI는 다른 문제를 해결한다
tags: [android, jetpack-compose, compose/design-system]
aliases: [CompositionLocal vs DI]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# CompositionLocal 매개변수와 DI는 다른 문제를 해결한다

파라미터 전달은 Composable의 명시적 계약이다. 호출자가 값과 event를 제어해야 하거나 특정 component에만 필요한 값이면 파라미터가 우선이다.

CompositionLocal은 하위 UI tree 전체에 적용되는 UI 환경 값을 숨은 context처럼 제공한다. theme, density, layout policy처럼 많은 node가 읽지만 중간 layer가 의미를 몰라도 되는 값에 맞다.

DI는 객체 graph의 생성, lifetime, 구현 binding을 다룬다. Repository, use case, database, network client를 Local에 숨기는 것은 dependency visibility와 testability를 낮출 수 있다.

관련 노트: [CompositionLocal은 트리 범위의 UI 환경 값을 암묵적으로 전달한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system-contracts/compositionlocal-passes-tree-scoped-ui-environment-implicitly.md), [Android dependency injection](01_inbox/mobile/android/02_app_framework/dependency-injection/android-dependency-injection-map.md)

출처: [Locally scoped data with CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal), [Dependency injection on Android](https://developer.android.com/training/dependency-injection)
