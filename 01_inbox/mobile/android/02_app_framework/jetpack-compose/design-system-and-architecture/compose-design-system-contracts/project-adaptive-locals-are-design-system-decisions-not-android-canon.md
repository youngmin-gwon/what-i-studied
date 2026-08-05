---
title: project-adaptive-locals-are-design-system-decisions-not-android-canon
tags: [android, compose/design-system, jetpack-compose]
aliases: [project adaptive locals, custom CompositionLocal]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## 프로젝트 Adaptive Local 은 Android 표준이 아닌 설계 결정이다

`LocalWindowSizeClass`, `LocalAdaptiveInfo` 같은 Jetpack 제공 Local 외에, 프로젝트가 자체적으로 정의한 `**CompositionLocal**(UI 트리 상위에서 하위로 매개변수 전달 없이 암시적으로 데이터를 전파하는 스코프 메커니즘)` 값(예: 화면 크기 구간, 레이아웃 모드, 브랜드 토큰)은 Android SDK 나 Compose 표준 API 가 아니라 프로젝트의 design-system 결정이다.

이런 값은 다른 프로젝트에서 동일한 이름이나 분할 방식을 가정하지 않는다. 정본 노트에는 API 규칙이 아니라 "이 프로젝트가 왜 이 값을 Local 로 제공하는가"와 함께 type, default, provider 위치, consumer, recomposition 비용을 실제 구현과 맞춰 기록한다.

이름만 보고 Android 일반 규칙으로 승격하지 않는다. 일반 Compose 학습 문서와 분리해서 관리해야 한다.

관련 노트: [Design system provider 는 Material theme 과 프로젝트 Local 을 함께 제공한다](./design-system-provider-composes-material-theme-and-project-locals.md), [CompositionLocal 은 tree-scoped UI 환경을 암묵적으로 전달한다](./compositionlocal-passes-tree-scoped-ui-environment-implicitly.md)
