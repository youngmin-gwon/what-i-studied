---
title: application-context-fits-process-lifetime-work-not-themed-ui
tags: [android, android/architecture, android/context]
aliases: ["Application Context는 프로세스 수명 작업에 맞고 themed UI에는 맞지 않는다"]
date modified: 2026-08-04 13:20:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Application Context 는 프로세스 수명 작업에 맞고 themed UI 에는 맞지 않는다

Application context 는 앱 프로세스 전체에 연결된 Context 다. repository, database, DataStore, file directory, system service 접근처럼 화면 인스턴스와 무관하게 오래 살아야 하는 작업에 적합하다.

Application context 가 Activity context 의 안전한 범용 대체물은 아니다. Dialog, window, themed resource, activity result, UI navigation 처럼 화면과 window token 이 필요한 작업에는 Activity 나 UI layer 가 owner 여야 한다.

DI graph 에서 Context 가 필요할 때도 lifetime 을 명확히 해야 한다. singleton graph 에는 application context 나 좁은 platform abstraction 만 넣고, Activity context 는 Activity-scoped object 나 UI event 경계에서만 사용한다.

application context 로 dialog 를 직접 띄우면 `WindowManager.BadTokenException`("Unable to add window — token null is not for an application") 이 발생한다. 이 예외 자체가 "window token 이 필요한 작업에 window 가 없는 Context 를 썼다"는 관찰 가능한 신호다.

관련 노트: [Context leak 경계](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-leaks-happen-when-reference-outlives-component-lifetime.md), [Android Dependency Injection Map](01_inbox/mobile/android/02_app_framework/dependency-injection/android-dependency-injection-map.md), [persistence 정본](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md).

공식 문서: [Context reference](https://developer.android.com/reference/android/content/Context)
