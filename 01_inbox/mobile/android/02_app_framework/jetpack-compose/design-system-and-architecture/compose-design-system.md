---
title: compose-design-system
tags: [android, compose/design-system, jetpack-compose]
aliases: [Compose design system, CompositionLocal, Material 3 Compose]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Compose Design System 은 Material Theme 과 프로젝트 토큰을 통합한다

Compose design system 정본은 Compose layering, module boundary, **CompositionLocal**(UI 트리 상위에서 하위로 매개변수 전달 없이 암시적으로 데이터를 전파하는 스코프 메커니즘), Material 3 color role, 프로젝트별 design-system provider 를 분리한다. UI layout 과 accessibility 는 [Compose layout, animation, accessibility](../layout-and-ui/compose-layout-animation-accessibility.md) 로 보낸다.

정본 묶음: [Compose design system contracts](./compose-design-system/compose-design-system.md)

### 읽는 순서

- [Compose는 상위 컴포넌트가 맞지 않을 때 낮은 계층으로 내려갈 수 있게 설계됐다](./compose-design-system/compose-layers-let-you-drop-down-when-higher-level-components-do-not-fit.md)
- [Compose 모듈 경계는 의존성 범위와 교체 비용을 드러낸다](./compose-design-system/compose-module-boundaries-expose-dependency-scope-and-replacement-cost.md)
- [CompositionLocal은 트리 범위의 UI 환경 값을 암묵적으로 전달한다](./compose-design-system/compositionlocal-passes-tree-scoped-ui-environment-implicitly.md)
- [CompositionLocal, 파라미터, DI는 서로 다른 문제를 푼다](./compose-design-system/compositionlocal-parameters-and-di-solve-different-problems.md)
- [Design system provider는 Material theme과 프로젝트 Local을 함께 제공한다](./compose-design-system/design-system-provider-composes-material-theme-and-project-locals.md)
- [Material 3 color role은 고정 색상값이 아니라 의미를 표현한다](./compose-design-system/material3-color-roles-express-semantic-intent-not-fixed-colors.md)
- [Material 3 on-color와 surface 계열은 대비와 계층을 함께 만든다](./compose-design-system/material3-on-colors-and-surfaces-pair-contrast-with-hierarchy.md)
- [Dynamic color는 Material color scheme에 들어오는 플랫폼 입력이다](./compose-design-system/dynamic-color-is-platform-input-to-a-material-color-scheme.md)
- [프로젝트 Adaptive Local은 Android 표준이 아닌 설계 결정이다](./compose-design-system/project-adaptive-locals-are-design-system-decisions-not-android-canon.md)
