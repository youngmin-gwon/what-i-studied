---
title: "Context"
tags: ["android", "android/glossary"]
aliases: ["Android Context"]
---

# Context

정의: Context는 resource, system service, package identity, storage, theme 같은 Android environment capability에 접근하는 framework handle이다.

혼동 방지: Context는 dependency container가 아니다. Activity Context, Application Context, component Context는 lifetime과 UI capability가 다르므로 오래 보관할 때 leak boundary를 먼저 판단해야 한다.

정본 링크:
- [Context capability contract](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-is-android-environment-capability-not-dependency-container.md)
- [Context leak boundary](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-leaks-happen-when-reference-outlives-component-lifetime.md)
