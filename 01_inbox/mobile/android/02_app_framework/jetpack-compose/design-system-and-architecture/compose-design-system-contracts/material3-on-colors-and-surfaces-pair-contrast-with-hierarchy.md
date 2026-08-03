---
title: Material 3 On 색상과 Surface는 대비와 계층을 연결한다
tags: [android, jetpack-compose, compose/design-system]
aliases: [on color, surface container]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# Material 3 On 색상과 Surface는 대비와 계층을 연결한다

`onPrimary`, `onPrimaryContainer`, `onSurface` 같은 `on*` role은 대응하는 배경 role 위에 놓이는 text/icon color다. 임의 배경에 임의 `on*` color를 섞으면 contrast 의도가 깨진다.

Surface와 surface container 계열은 배경, card, navigation area, pane 같은 표면 계층을 표현한다. Material 3에서는 depth를 그림자만이 아니라 surface tone과 tonal elevation으로도 표현한다.

`on*` pairing은 출발점이지 모든 실제 조합의 contrast 보장을 대신하지 않는다. typography, disabled state, alpha, custom color가 섞이면 실제 렌더링 contrast를 검증해야 한다.

관련 노트: [Material 3 color role은 고정 색상값이 아니라 의미를 표현한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system-contracts/material3-color-roles-express-semantic-intent-not-fixed-colors.md), [접근성 품질은 서비스, 검사기, Semantics 테스트로 검증한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/accessibility-quality-requires-service-scanner-and-semantics-verification.md)

출처: [Material Design color roles](https://m3.material.io/styles/color/roles), [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3)
