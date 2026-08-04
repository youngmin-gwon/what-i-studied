---
title: mybenefit-adaptive-locals-are-project-reference-not-android-canon
tags: [android, compose/design-system, jetpack-compose]
aliases: [MyBenefit adaptive locals]
date modified: 2026-08-03 18:09:43 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## MyBenefit Adaptive Local 은 Android 표준이 아닌 프로젝트 참조값이다

`LocalMyBenefit*` 같은 adaptive Local 은 Android SDK 나 Jetpack Compose 표준 API 가 아니라 이 프로젝트의 design-system decision 이다. 일반 정본에는 API 규칙이 아니라 "프로젝트가 왜 이 값을 Local 로 제공하는가"를 기록한다.

프로젝트 reference 노트는 type, default, provider 위치, consumer, recomposition 비용을 실제 구현과 맞춰 확인해야 한다. 이름만 보고 Android 일반 규칙으로 승격하지 않는다.

이 문서는 MyBenefit 의 adaptive 값 흐름을 보존하되, 일반 Compose 학습 문서와 분리한다. 다른 프로젝트에서는 같은 이름이나 분할 방식을 전제하지 않는다.

관련 노트: [Design system provider는 Material theme과 프로젝트 Local을 함께 제공한다](./design-system-provider-composes-material-theme-and-project-locals.md), [Large screen contracts](../../../../07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)
