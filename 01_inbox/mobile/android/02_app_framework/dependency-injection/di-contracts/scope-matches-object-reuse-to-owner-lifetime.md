---
title: scope-matches-object-reuse-to-owner-lifetime
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:47 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Scope 는 singleton 장식이 아니라 owner lifetime 에 맞춘 재사용 계약이다

Scope 는 "한 번만 만든다"는 느낌보다 "어떤 graph/component instance 안에서 재사용되는가"를 정의한다. Application scope, Activity scope, ViewModel scope 는 서로 다른 owner lifetime 을 가진다.

짧은 lifetime 객체를 긴 graph 에 넣으면 leak 이 생기고, 긴 lifetime 객체를 짧은 graph 마다 새로 만들면 cache, connection, observer 정책이 흔들린다. scope 를 붙이기 전에는 객체가 누구의 상태를 들고 누구와 함께 사라져야 하는지 먼저 정한다.

관련 노트: [Context lifetime in DI](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/android-context-in-di-must-match-graph-lifetime.md), [ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md).

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
