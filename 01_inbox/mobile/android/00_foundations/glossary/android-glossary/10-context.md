---
title: 10-context
tags: ["android", "android/glossary"]
aliases: ["Android Context"]
date modified: 2026-08-03 17:21:37 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Context 는 애플리케이션 환경 정보와 시스템 서비스에 접근하는 전역 인터페이스다

정의: Context 는 resource, system service, package identity, storage, theme 같은 Android environment capability 에 접근하는 framework handle 이다.

혼동 방지: Context 는 dependency container 가 아니다. Activity Context, Application Context, component Context 는 lifetime 과 UI capability 가 다르므로 오래 보관할 때 leak boundary 를 먼저 판단해야 한다.

정본 링크:

- [Context capability contract](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-is-android-environment-capability-not-dependency-container.md)
- [Context leak boundary](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-leaks-happen-when-reference-outlives-component-lifetime.md)
