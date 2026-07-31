---
title: Glance renders app widgets through RemoteViews not Compose UI
tags: [android, jetpack-compose, compose/ui]
aliases: [Glance, RemoteViews, App widgets]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# Glance renders app widgets through RemoteViews not Compose UI

Glance는 Kotlin과 Compose Runtime 기반의 API로 app widget을 선언하지만, 일반 Compose UI를 launcher에서 직접 실행하는 기술이 아니다. Glance content는 host가 소비할 수 있는 `RemoteViews` 경계로 변환된다.

그래서 일반 Compose `Modifier`, Material component, screen state holder를 그대로 섞어 쓰는 모델이 아니다. Glance에는 `GlanceModifier`, Glance 전용 component와 action/update 제약이 있다.

App widget은 host process와 update lifecycle의 제약을 받는다. 앱 화면의 in-memory state가 widget에 그대로 살아 있다고 가정하지 말고, 필요한 persistent state와 update trigger를 별도로 설계한다.

관련 노트: [Compose layout, animation, accessibility](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md), [Background work contracts](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)

출처: [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance), [Manage and update GlanceAppWidget](https://developer.android.com/develop/ui/compose/glance/glance-app-widget), [App widgets overview](https://developer.android.com/develop/ui/views/appwidgets/overview)
