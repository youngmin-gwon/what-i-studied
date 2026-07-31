---
title: Design system provider composes Material theme and project locals
tags: [android, jetpack-compose, compose/design-system]
aliases: [DesignSystemProvider, MaterialTheme]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# Design system provider composes Material theme and project locals

Design system provider는 앱 root나 feature boundary에서 `MaterialTheme`과 프로젝트 전용 CompositionLocal을 함께 제공하는 경계다. 하위 UI는 같은 color, typography, shape, adaptive policy를 일관되게 읽는다.

Provider는 UI 환경 값의 계산과 범위를 모으는 곳이지 화면 상태나 business dependency를 숨기는 장소가 아니다. 화면마다 바뀌는 state는 parameter/state holder로 전달하고, repository나 service는 DI가 소유한다.

`compositionLocalOf`와 `staticCompositionLocalOf` 선택은 값 변경 시 관찰과 recomposition 범위에 영향을 준다. 값이 실제로 바뀌는지, 얼마나 자주 읽히는지, 누락 시 실패 전략이 무엇인지가 선택 기준이다.

관련 노트: [CompositionLocal은 트리 범위의 UI 환경 값을 암묵적으로 전달한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system-contracts/compositionlocal-passes-tree-scoped-ui-environment-implicitly.md), [Material 3 color role은 고정 색상값이 아니라 의미를 표현한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system-contracts/material3-color-roles-express-semantic-intent-not-fixed-colors.md)

출처: [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Locally scoped data with CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal)
