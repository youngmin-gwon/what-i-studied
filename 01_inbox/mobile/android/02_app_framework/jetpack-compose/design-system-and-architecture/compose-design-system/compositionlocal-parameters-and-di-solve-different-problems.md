---
title: compositionlocal-parameters-and-di-solve-different-problems
tags: [android, compose/design-system, jetpack-compose]
aliases: [CompositionLocal vs DI]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## CompositionLocal 매개변수와 DI 는 다른 문제를 해결한다

파라미터 전달은 Composable 의 명시적 계약이다. 호출자가 값과 event 를 제어해야 하거나 특정 component 에만 필요한 값이면 파라미터가 우선이다.

**CompositionLocal**(UI 트리 상위에서 하위로 매개변수 전달 없이 암시적으로 데이터를 전파하는 스코프 메커니즘) 은 하위 UI tree 전체에 적용되는 UI 환경 값을 숨은 context 처럼 제공한다. theme, density, layout policy 처럼 많은 node 가 읽지만 중간 layer 가 의미를 몰라도 되는 값에 맞다.

DI 는 객체 graph 의 생성, lifetime, 구현 binding 을 다룬다. Repository, use case, database, network client 를 Local 에 숨기는 것은 dependency visibility 와 testability 를 낮출 수 있다.

예를 들어 `spacing: Dp` 를 함수 인자로 받으면 파라미터, `val LocalSpacing = compositionLocalOf { 16.dp }` 를 선언해 하위 tree 가 `LocalSpacing.current` 로 읽으면 CompositionLocal, `class OrderRepository @Inject constructor(...)` 처럼 **Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리)/Dagger 가 생성과 lifetime 을 관리하면 DI 다.

관련 노트: [CompositionLocal은 트리 범위의 UI 환경 값을 암묵적으로 전달한다](./compositionlocal-passes-tree-scoped-ui-environment-implicitly.md), [Android dependency injection](../../../dependency-injection/android-dependency-injection-map.md)

출처: [Locally scoped data with CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal), [Dependency injection on Android](https://developer.android.com/training/dependency-injection)
