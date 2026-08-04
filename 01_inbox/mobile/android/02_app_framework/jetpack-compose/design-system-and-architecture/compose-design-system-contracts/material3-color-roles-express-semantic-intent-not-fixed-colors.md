---
title: material3-color-roles-express-semantic-intent-not-fixed-colors
tags: [android, compose/design-system, jetpack-compose]
aliases: [ColorScheme, Material 3 color roles]
date modified: 2026-08-03 18:10:04 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Material 3 색상 역할은 고정된 색상이 아닌 의미적 의도를 표현한다

Material 3 color role 은 `#6200EE` 같은 고정 색상값이 아니라 UI 에서의 의미를 표현한다. `primary`, `secondary`, `tertiary`, `error`, `surface` 는 색상 이름이 아니라 emphasis, state, surface 역할이다.

컴포넌트가 raw color 대신 `MaterialTheme.colorScheme` 의 semantic role 을 읽으면 light/dark theme, dynamic color, brand scheme 변경에도 의도가 유지된다.

정본 문서에는 token 표 전체를 복제하지 않는다. 중요한 것은 어떤 컴포넌트가 어떤 역할을 써야 하는지, container 와 content color 를 어떻게 짝지어야 하는지다.

관련 노트: [Material 3 on-color와 surface 계열은 대비와 계층을 함께 만든다](./material3-on-colors-and-surfaces-pair-contrast-with-hierarchy.md), [Dynamic color는 Material color scheme에 들어오는 플랫폼 입력이다](./dynamic-color-is-platform-input-to-a-material-color-scheme.md)

출처: [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Material Design color roles](https://m3.material.io/styles/color/roles)
