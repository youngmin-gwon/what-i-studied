---
title: app-widget-contracts
tags: [android, android/app-widgets]
aliases: ["App Widget 계약"]
date modified: 2026-08-05 13:14:59 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## App Widget 계약

App Widget 은 Activity, Service 와는 다른 계약을 가진 컴포넌트다. 화면을 소유하지도, 오래 실행되는 프로세스를 갖지도 않고, launcher(host)가 broadcast 를 보낼 때만 짧게 깨어나 `RemoteViews` 를 채워 넘긴다. 이 클러스터는 그 계약을 lifecycle, layout 제약, 설정, 갱신 주기 네 축으로 나눠서 다룬다.

### 정본 노트

- [AppWidgetProvider lifecycle은 지속 프로세스가 아니라 broadcast로 갱신된다](./appwidgetprovider-lifecycle-runs-through-broadcasts-not-a-persistent-process.md) - `onUpdate`/`onEnabled`/`onDisabled`/`onDeleted` 콜백이 Activity/Service 수명과 다른 이유.
- [RemoteViews는 위젯 layout을 고정된 View 부분집합으로 제한한다](./remoteviews-restricts-widget-layouts-to-a-fixed-view-subset.md) - host 프로세스가 앱의 커스텀 View 를 모르기 때문에 생기는 제약.
- [위젯 설정 Activity는 pin 시점에 실행되는 계약을 가진다](./widget-configuration-activity-runs-once-at-pin-time.md) - `ACTION_APPWIDGET_CONFIGURE` 와 `setResult` 계약.
- [updatePeriodMillis는 최소 간격만 보장하는 best-effort 스케줄이다](./updateperiodmillis-is-a-best-effort-minimum-interval-not-a-guarantee.md) - 30 분 하한과 `WorkManager` 로 보완하는 패턴.
- [Glance는 Compose UI가 아니라 RemoteViews 위젯 경계로 렌더링한다](./glance-renders-app-widgets-through-remoteviews-not-compose-ui.md) - Compose 문법으로 위 계약을 감싸는 API.

### 읽는 기준

위젯이 왜 화면처럼 계속 살아있지 않은지 궁금하면 lifecycle 노트로 간다. layout 이 왜 일반 Compose/View 마음대로 안 되는지 궁금하면 RemoteViews 노트로 간다. 처음 배치할 때 뜨는 설정 화면의 계약은 설정 Activity 노트에서, "왜 15 분마다 갱신이 안 되는가"는 updatePeriodMillis 노트에서 확인한다. Compose 로 위젯을 작성하고 싶다면 Glance 노트에서 시작하되, 그 밑에 이 네 계약이 그대로 깔려 있다는 점을 먼저 이해해야 한다.

### 다루지 않는 범위

Wear OS tile, 알림(notification)에 쓰이는 `RemoteViews` custom layout, Quick Settings tile 은 각각 별도 계약이며 이 클러스터에서 다루지 않는다.

상위 문서: [Android 앱 아키텍처는 UI 패턴보다 수명과 OS 진입점을 나누는 문제다](../../architecture/android-app-architecture.md)
