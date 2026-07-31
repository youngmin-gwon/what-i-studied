---
title: Composable compiler output enables restart and skip control
tags: [android, jetpack-compose, compose/runtime]
aliases: [Compose compiler, skippable, restartable]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

`@Composable`은 단순한 marker가 아니라 Compose compiler가 Runtime과 협력할 호출 문맥을 만들도록 한다. Compiler는 Composable call graph, restart 가능성, skip 가능성, remember 위치 같은 정보를 Runtime이 다룰 수 있는 형태로 바꾼다.

`Composer` parameter, restart group, slot operation 같은 세부는 버전별 compiler/runtime 구현 detail이다. 정본 노트에서는 “컴파일러가 재구성 제어 정보를 만든다”까지만 앱 개발자가 의존할 mental model로 둔다.

Skippability는 compiler가 판단하는 안정성 정보와 Runtime의 parameter comparison이 함께 만든다. Kotlin 2.0.20 이후 strong skipping 기본값 같은 버전 조건은 성능 정본에서 따로 다룬다.

관련 노트: [Compose 안정성과 strong skipping은 skippability에 영향을 준다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-stability-and-strong-skipping-affect-skippability.md), [Composition은 호출 위치 identity로 remember 값을 보존한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composition-uses-callsite-identity-to-preserve-remembered-values.md)

출처: [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping)
