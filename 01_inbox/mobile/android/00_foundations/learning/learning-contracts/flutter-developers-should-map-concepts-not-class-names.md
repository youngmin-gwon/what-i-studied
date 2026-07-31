---
title: flutter-developers-should-map-concepts-not-class-names
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-01 01:08:14 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Flutter 개발자는 class 이름보다 개념 경계를 대응시켜야 한다

Flutter 경험이 있는 개발자는 Widget 과 Composable, BuildContext 와 Android Context, Provider/Riverpod 과 Compose state observation 을 이름으로 바로 대응시키기 쉽다. 하지만 실제 boundary 는 다르다.

Compose 의 Composable 은 state 를 UI 로 계산하는 함수에 가깝고, Android Context 는 UI tree 위치가 아니라 platform capability 다. ViewModel 은 StatefulWidget 의 State 가 아니라 screen state holder 와 external work coordinator 에 가깝다.

이 매핑은 Compose/state 문서와 Context 문서로 연결하고, learning resource 문서 안에서 반복 설명하지 않는다.

관련 노트: [Compose runtime/state](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Context boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md), [ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md).

### 판단 기준

Foundation 노트는 세부 구현을 반복하지 않고 Android 지식이 어느 계층의 문제인지 찾아가는 입구로 사용한다.

### 경계

학습 순서나 역사 설명은 API 목록을 외우는 방향이 아니라 runtime, framework, service, security, tooling boundary 를 구분하는 방향으로 유지한다.
