---
title: dynamic-color-is-platform-input-to-a-material-color-scheme
tags: [android, compose/design-system, jetpack-compose]
aliases: [Dynamic color, Material You]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Dynamic Color 는 Material Color Scheme 에 대한 플랫폼 입력이다

Dynamic color 는 Android 12 이상에서 시스템이 제공하는 색상 입력을 Material color scheme 으로 연결하는 테마 경계다. 앱은 dynamic color 사용 여부, brand scheme fallback, API level 별 동작을 theme boundary 에서 결정한다.

Composable 은 wallpaper 색을 직접 다루지 않고 `ColorScheme` 의 semantic role 을 읽는다. 그래야 dynamic color 를 끄거나 브랜드 고정 scheme 으로 바꿔도 component 의미가 유지된다.

전형적인 구현은 `Build.VERSION.SDK_INT >= Build.VERSION_CODES.S` 조건에서 `dynamicLightColorScheme(context)` 또는 `dynamicDarkColorScheme(context)` 로 `ColorScheme` 을 만들고, 조건을 만족하지 않으면 앱이 정의한 고정 brand `ColorScheme` 으로 fallback 하는 방식이다.

Dynamic color 가 모든 surface 에서 동일하게 동작한다고 가정하지 않는다. 일반 Compose screen, app widget/Glance, notification, remote surface 는 각각 렌더링 경계와 지원 정책이 다를 수 있다.

관련 노트: [Material 3 color role은 고정 색상값이 아니라 의미를 표현한다](./material3-color-roles-express-semantic-intent-not-fixed-colors.md), [Glance는 Compose UI가 아니라 RemoteViews 위젯 경계로 렌더링한다](../../../app-widgets/app-widget-contracts/glance-renders-app-widgets-through-remoteviews-not-compose-ui.md)

출처: [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Dynamic color](https://m3.material.io/styles/color/dynamic-color/overview)
