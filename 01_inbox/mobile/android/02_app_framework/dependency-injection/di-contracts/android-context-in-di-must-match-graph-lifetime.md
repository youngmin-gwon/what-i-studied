---
title: android-context-in-di-must-match-graph-lifetime
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:19 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## DI graph 에 넣는 Android Context 는 graph lifetime 과 맞아야 한다

`Context` 는 단순 dependency 가 아니라 resource, service, permission, theme, lifecycle 과 연결된 platform capability 다. Application graph 에는 `applicationContext` 처럼 app lifetime 과 맞는 Context 만 넣어야 한다.

Activity 나 Fragment Context 를 app-wide graph 에 넣으면 화면이 사라진 뒤에도 UI owner 가 붙잡힐 수 있다. 반대로 theme, window, UI-bound service 가 필요한 작업에는 Application Context 가 충분하지 않을 수 있으므로 더 짧은 owner boundary 에서 받아야 한다.

관련 노트: [Context boundaries](../../architecture/context-and-modularity/android-context-boundaries.md).

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
