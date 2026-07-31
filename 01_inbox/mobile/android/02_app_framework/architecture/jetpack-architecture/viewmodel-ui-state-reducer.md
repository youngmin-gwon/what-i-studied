# ViewModel, UI State, Reducer 가이드

이 문서는 Compose 화면에서 `ViewModel`이 무엇을 책임지고, `UiState`, user action, 일회성 이벤트를 어떻게 나누며, 화면 상태 전이가 복잡해졌을
때 Reducer를 언제 도입할지 정리합니다.

핵심은 다음입니다.

```text
UI는 상태를 읽는다.
UI는 사용자 행동을 ViewModel에 전달한다.
ViewModel은 화면 단위 상태를 만들고 외부 작업을 조율한다.
같은 화면에 보이는 상태라도 수명과 소유자가 다르면 분리할 수 있다.
상태 계산이 커질 때만 Reducer로 순수 상태 전이를 분리한다.
```

관련 공식 문서:

- [ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel)
- [UI layer](https://developer.android.com/topic/architecture/ui-layer)
- [State holders and UI state](https://developer.android.com/topic/architecture/ui-layer/stateholders)
- [UI events](https://developer.android.com/topic/architecture/ui-layer/events)
- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)

---

## 원자 노트

- [ViewModel은 화면 단위 State Holder다](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/viewmodel-as-screen-state-holder.md)
- [ViewModel이라는 이름이 헷갈리는 이유](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/why-viewmodel-name-is-confusing.md)
- [Flutter Bloc은 ViewModel인가](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/is-flutter-bloc-a-viewmodel.md)
- [MVC, MVP, MVVM, MVI에서 진짜 달라진 것](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/mvc-mvp-mvvm-mvi-real-differences.md)
- [기본 구조: State Down, Action Up](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/state-down-action-up.md)
- [UiState, User Action, Event 이름 구분](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/uistate-user-action-event-naming.md)
- [Fetch 상태와 Interaction 상태를 꼭 합쳐야 하나](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/separating-fetch-state-and-interaction-state.md)
- [Compose State Holder를 ViewModel에 둬도 되는가](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/compose-state-holder-in-viewmodel.md)
- [상태와 일회성 이벤트를 구분한다](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/state-vs-one-off-event.md)
- [ViewModel 안의 `copy()`가 많아질 때](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/too-many-copy-calls-in-viewmodel.md)
- [Reducer란 무엇인가](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/what-is-a-reducer.md)
- [Reducer가 하지 말아야 할 일](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/what-reducer-should-not-do.md)
- [Reducer 도입 기준](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/when-to-introduce-reducer.md)
- [Flutter Bloc을 Reducer 관점에서 다시 보면](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/flutter-bloc-as-reducer.md)
- [테스트 전략](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/viewmodel-reducer-testing-strategy.md)
- [현재 프로젝트 기준](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/viewmodel-reducer-project-guidelines.md)
- [체크리스트](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer/viewmodel-reducer-checklist.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, 각 H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
