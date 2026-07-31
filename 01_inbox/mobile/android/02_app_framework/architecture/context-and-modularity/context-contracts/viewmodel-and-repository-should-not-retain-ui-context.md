---
title: "ViewModel과 Repository는 UI Context를 보관하지 않는다"
tags: [android, android/architecture, android/context]
aliases: ["ViewModel과 Repository는 UI Context를 보관하지 않는다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# ViewModel과 Repository는 UI Context를 보관하지 않는다

ViewModel은 screen state와 외부 작업을 조율하는 owner이지 Activity, View, Fragment, UI Context의 저장소가 아니다. Repository는 data policy와 source of truth를 담당하지 UI 화면 인스턴스를 보관하지 않는다.

플랫폼 API 때문에 Context가 필요하다면 먼저 그 API가 어느 layer의 책임인지 묻는다. UI permission, navigation, toast, resource formatting은 UI layer에 남기는 편이 맞고, database/file/system service처럼 process-scoped dependency는 application context나 좁은 interface를 data boundary에 주입할 수 있다.

예외가 필요하면 수명과 테스트 경계를 명시한다. "어디서든 Context가 필요해서 ViewModel에 넣었다"는 설계 근거가 아니다.

관련 노트: [ViewModel 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [ViewModel은 UI controller/context를 보관하지 않는다](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel-does-not-retain-ui-controller-or-context.md), [Android Dependency Injection Map](01_inbox/mobile/android/02_app_framework/dependency-injection/android-dependency-injection-map.md).

공식 문서: [Guide to app architecture](https://developer.android.com/topic/architecture)
