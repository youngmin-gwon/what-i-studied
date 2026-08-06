---
title: flutter-developers-should-map-concepts-not-class-names
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 17:20:53 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Flutter 개발자는 class 이름보다 개념 경계를 대응시켜야 한다

Flutter 경험이 있는 개발자는 Widget 과 Composable, BuildContext 와 Android Context, Provider/Riverpod 과 Compose state observation 을 이름으로 바로 대응시키기 쉽다. 하지만 실제 boundary 는 다르다.

Compose 의 Composable 은 state 를 UI 로 계산하는 함수에 가깝고, Android Context 는 UI tree 위치가 아니라 platform capability 다. [viewmodel](../../../02_app_framework/viewmodel.md) 은 StatefulWidget 의 State 가 아니라 screen state holder 와 external work coordinator 에 가깝다.

이 매핑은 Compose/state 문서와 Context 문서로 연결하고, learning resource 문서 안에서 반복 설명하지 않는다.

관련 노트: [Compose runtime/state](../../../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Context boundaries](../../../02_app_framework/architecture/context-and-modularity/android-context-boundaries.md), [ViewModel](../../../02_app_framework/architecture/state-management/viewmodel/viewmodel.md).

### 판단 기준

두 framework 의 개념을 비교할 때는 이름보다 state owner, UI tree 위치, platform capability, lifecycle, disposal 책임이 같은지 확인한다. 하나라도 다르면 일대일 대응으로 외우지 않는다.

### 경계

이 노트는 오해하기 쉬운 개념 경계만 교정한다. Flutter 와 Compose API 의 전체 대응표나 migration recipe 는 소유하지 않는다.
