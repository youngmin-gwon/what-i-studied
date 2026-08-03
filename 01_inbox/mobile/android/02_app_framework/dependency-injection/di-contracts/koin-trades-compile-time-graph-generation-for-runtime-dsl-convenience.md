---
title: koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:34 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Koin 은 런타임 DSL 편의와 정적 graph 검증의 트레이드오프를 가진다

Koin 은 Kotlin DSL 로 binding 을 선언하고 런타임에 dependency 를 resolve 하는 방식에 가깝다. 설정이 가볍고 읽기 쉬운 장점이 있지만, Dagger/Hilt 같은 정적 graph generation 과는 실패 시점과 검증 방식이 다르다.

따라서 Koin 을 선택할 때는 간단한 setup 만 보지 말고 startup cost, runtime resolution failure, module loading, test override, IDE/build integration 까지 같이 판단한다.

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
