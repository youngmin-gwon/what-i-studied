---
title: glance-renders-app-widgets-through-remoteviews-not-compose-ui
tags: [android, compose/ui, jetpack-compose]
aliases: [App widgets, Glance, RemoteViews]
date modified: 2026-08-03 18:10:31 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Glance renders app widgets through RemoteViews not Compose UI

Glance 는 Kotlin 과 Compose Runtime 기반의 API 로 app widget 을 선언하지만, 일반 Compose UI 를 launcher 에서 직접 실행하는 기술이 아니다. Glance content 는 host 가 소비할 수 있는 `RemoteViews` 경계로 변환된다.

그래서 일반 Compose `Modifier`, Material component, screen state holder 를 그대로 섞어 쓰는 모델이 아니다. Glance 에는 `GlanceModifier`, Glance 전용 component 와 action/update 제약이 있다.

App widget 은 host process 와 update lifecycle 의 제약을 받는다. 앱 화면의 in-memory state 가 widget 에 그대로 살아 있다고 가정하지 말고, 필요한 persistent state 와 update trigger 를 별도로 설계한다.

관련 노트: [Compose layout, animation, accessibility](../compose-layout-animation-accessibility.md), [Background work contracts](../../../../04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)

출처: [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance), [Manage and update GlanceAppWidget](https://developer.android.com/develop/ui/compose/glance/glance-app-widget), [App widgets overview](https://developer.android.com/develop/ui/views/appwidgets/overview)
