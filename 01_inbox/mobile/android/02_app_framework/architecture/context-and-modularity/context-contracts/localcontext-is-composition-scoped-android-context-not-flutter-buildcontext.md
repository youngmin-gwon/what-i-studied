---
title: localcontext-is-composition-scoped-android-context-not-flutter-buildcontext
tags: [android, android/architecture, android/context]
aliases: ["LocalContext는 Composition에서 읽는 Android Context이지 Flutter BuildContext가 아니다"]
date modified: 2026-08-04 13:20:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## LocalContext 는 Composition 에서 읽는 Android Context 이지 Flutter BuildContext 가 아니다

`LocalContext.current` 는 Compose tree 를 통해 전달되는 현재 Android `Context` 다. resource formatting, toast, activity start 같은 UI event 근처의 Android API 호출에 사용할 수 있다.

이 값은 Flutter 의 `BuildContext` 와 같지 않다. Flutter `BuildContext` 는 widget 이 element tree 에서 어디에 있는지를 나타내는 handle 이고, Android `Context` 는 platform environment capability 다. 둘 다 유효 수명 밖에서 쓰면 문제가 되지만, 소유 모델과 실패 방식은 다르다.

`LocalContext` 를 ViewModel 이나 repository 에 넘겨 장기 보관하면 Compose 의 explicit state/data flow 가 흐려진다. 필요한 값이나 action 을 좁게 만들어 전달하고, long-lived dependency 에는 application context 나 abstraction 을 사용한다.

`LocalContext.current` 를 람다나 콜백에 캡처해 Composition 밖(예: 별도 object, ViewModel)에 저장하면, 그 Composable 이 화면에서 사라진 뒤에도 Activity context 가 참조 체인에 남아 LeakCanary 나 Memory Profiler 의 heap dump 에서 retained Activity 로 나타날 수 있다.

관련 노트: [Context 기본 경계](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-is-android-environment-capability-not-dependency-container.md), [Compose runtime 정본](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [ViewModel/Repository Context 경계](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/viewmodel-and-repository-should-not-retain-ui-context.md).

공식 문서: [CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal)
