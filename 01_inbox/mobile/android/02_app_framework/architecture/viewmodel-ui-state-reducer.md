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

- [[viewmodel-as-screen-state-holder|ViewModel은 화면 단위 State Holder다]]
- [[why-viewmodel-name-is-confusing|ViewModel이라는 이름이 헷갈리는 이유]]
- [[is-flutter-bloc-a-viewmodel|Flutter Bloc은 ViewModel인가]]
- [[mvc-mvp-mvvm-mvi-real-differences|MVC, MVP, MVVM, MVI에서 진짜 달라진 것]]
- [[state-down-action-up|기본 구조: State Down, Action Up]]
- [[uistate-user-action-event-naming|UiState, User Action, Event 이름 구분]]
- [[separating-fetch-state-and-interaction-state|Fetch 상태와 Interaction 상태를 꼭 합쳐야 하나]]
- [[compose-state-holder-in-viewmodel|Compose State Holder를 ViewModel에 둬도 되는가]]
- [[state-vs-one-off-event|상태와 일회성 이벤트를 구분한다]]
- [[too-many-copy-calls-in-viewmodel|ViewModel 안의 `copy()`가 많아질 때]]
- [[what-is-a-reducer|Reducer란 무엇인가]]
- [[what-reducer-should-not-do|Reducer가 하지 말아야 할 일]]
- [[when-to-introduce-reducer|Reducer 도입 기준]]
- [[flutter-bloc-as-reducer|Flutter Bloc을 Reducer 관점에서 다시 보면]]
- [[viewmodel-reducer-testing-strategy|테스트 전략]]
- [[viewmodel-reducer-project-guidelines|현재 프로젝트 기준]]
- [[viewmodel-reducer-checklist|체크리스트]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, 각 H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
