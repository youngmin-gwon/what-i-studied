---
title: "Context는 Android 환경 capability이지 일반 DI container가 아니다"
tags: [android, android/architecture, android/context]
aliases: ["Context는 Android 환경 capability이지 일반 DI container가 아니다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Context는 Android 환경 capability이지 일반 DI container가 아니다

`Context`는 resource, system service, file, database, component start, permission check처럼 Android 환경이 필요한 작업을 수행하는 framework handle이다.

그러나 Context는 모든 의존성을 꺼내 쓰는 service locator가 아니다. 어떤 Context를 전달할지는 API 호출이 필요한 환경과 그 값을 보관하는 객체의 수명에 의해 결정된다.

긴 수명의 객체가 Activity context를 들고 있으면 화면 인스턴스를 해제하지 못할 수 있다. 반대로 Activity theme/window가 필요한 UI 작업에 application context를 쓰면 동작은 하더라도 의미가 틀어질 수 있다.

관련 노트: [Application Context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/application-context-fits-process-lifetime-work-not-themed-ui.md), [Activity Context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/activity-context-carries-window-theme-and-short-lifetime.md), [Android Dependency Injection Map](01_inbox/mobile/android/02_app_framework/dependency-injection/android-dependency-injection-map.md).

공식 문서: [Context reference](https://developer.android.com/reference/android/content/Context)
