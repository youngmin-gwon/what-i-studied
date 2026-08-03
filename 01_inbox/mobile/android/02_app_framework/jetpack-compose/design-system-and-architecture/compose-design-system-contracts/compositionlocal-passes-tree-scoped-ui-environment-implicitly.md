---
title: CompositionLocal은 트리 범위 UI 환경을 암묵적으로 전달한다
tags: [android, jetpack-compose, compose/design-system]
aliases: [CompositionLocal]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# CompositionLocal은 트리 범위 UI 환경을 암묵적으로 전달한다

CompositionLocal은 Composition tree의 특정 하위 범위에 값을 암묵적으로 제공하는 API다. 기본 데이터 흐름은 파라미터 전달이며, CompositionLocal은 theme, typography, layout direction, density처럼 넓게 쓰이는 UI 환경 값에 적합하다.

`CompositionLocalProvider`가 값을 제공하면 하위 Composable은 `LocalX.current`로 가장 가까운 provider의 값을 읽는다. 호출 그래프 중간 계층이 그 값을 알 필요가 없을 때 boilerplate를 줄일 수 있다.

암묵성은 비용이다. Local을 많이 쓰면 Composable의 입력 계약이 숨겨지고 테스트 setup이 어려워진다. 기본값, 제공 누락, 변경 빈도와 recomposition 범위를 설계해야 한다.

관련 노트: [CompositionLocal, 파라미터, DI는 서로 다른 문제를 푼다](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system-contracts/compositionlocal-parameters-and-di-solve-different-problems.md), [Design system provider는 Material theme과 프로젝트 Local을 함께 제공한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system-contracts/design-system-provider-composes-material-theme-and-project-locals.md)

출처: [Locally scoped data with CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal)
