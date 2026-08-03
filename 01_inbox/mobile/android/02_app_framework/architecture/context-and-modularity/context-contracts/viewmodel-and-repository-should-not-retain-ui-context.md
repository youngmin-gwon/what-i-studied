---
title: viewmodel-and-repository-should-not-retain-ui-context
tags: [android, android/architecture, android/context]
aliases: ["ViewModel과 Repository는 UI Context를 보관하지 않는다"]
date modified: 2026-08-03 17:27:27 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## ViewModel 과 Repository 는 UI Context 를 보관하지 않는다

ViewModel 은 screen state 와 외부 작업을 조율하는 owner 이지 Activity, View, Fragment, UI Context 의 저장소가 아니다. Repository 는 data policy 와 source of truth 를 담당하지 UI 화면 인스턴스를 보관하지 않는다.

플랫폼 API 때문에 Context 가 필요하다면 먼저 그 API 가 어느 layer 의 책임인지 묻는다. UI permission, navigation, toast, resource formatting 은 UI layer 에 남기는 편이 맞고, database/file/system service 처럼 process-scoped dependency 는 application context 나 좁은 interface 를 data boundary 에 주입할 수 있다.

예외가 필요하면 수명과 테스트 경계를 명시한다. "어디서든 Context 가 필요해서 ViewModel 에 넣었다"는 설계 근거가 아니다.

관련 노트: [ViewModel 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [ViewModel은 UI controller/context를 보관하지 않는다](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel-does-not-retain-ui-controller-or-context.md), [Android Dependency Injection Map](01_inbox/mobile/android/02_app_framework/dependency-injection/android-dependency-injection-map.md).

공식 문서: [Guide to app architecture](https://developer.android.com/topic/architecture)
