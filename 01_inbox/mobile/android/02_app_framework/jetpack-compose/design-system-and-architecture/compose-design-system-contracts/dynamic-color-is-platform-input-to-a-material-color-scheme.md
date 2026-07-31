---
title: Dynamic color is platform input to a Material color scheme
tags: [android, jetpack-compose, compose/design-system]
aliases: [Dynamic color, Material You]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# Dynamic color is platform input to a Material color scheme

Dynamic color는 Android 12 이상에서 시스템이 제공하는 색상 입력을 Material color scheme으로 연결하는 테마 경계다. 앱은 dynamic color 사용 여부, brand scheme fallback, API level별 동작을 theme boundary에서 결정한다.

Composable은 wallpaper 색을 직접 다루지 않고 `ColorScheme`의 semantic role을 읽는다. 그래야 dynamic color를 끄거나 브랜드 고정 scheme으로 바꿔도 component 의미가 유지된다.

Dynamic color가 모든 surface에서 동일하게 동작한다고 가정하지 않는다. 일반 Compose screen, app widget/Glance, notification, remote surface는 각각 렌더링 경계와 지원 정책이 다를 수 있다.

관련 노트: [Material 3 color role은 고정 색상값이 아니라 의미를 표현한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system-contracts/material3-color-roles-express-semantic-intent-not-fixed-colors.md), [Glance는 Compose UI가 아니라 RemoteViews 위젯 경계로 렌더링한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/glance-renders-app-widgets-through-remoteviews-not-compose-ui.md)

출처: [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Dynamic color](https://m3.material.io/styles/color/dynamic-color/overview)
