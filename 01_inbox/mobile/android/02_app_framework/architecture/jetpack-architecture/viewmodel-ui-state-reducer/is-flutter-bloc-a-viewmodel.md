# Flutter Bloc은 ViewModel인가

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

이 질문도 강하게 표현하면 이렇게 정리할 수 있습니다.

```text
Flutter Bloc은 Android ViewModel과 비교할 수 있다.
하지만 패턴 기준으로는 MVVM보다 MVI/Redux 계열에 더 가깝다.
```

Flutter Bloc은 보통 아래 흐름을 가집니다.

```text
View
 -> add(Event)
Bloc
 -> emit(State)
View
```

Android ViewModel은 보통 아래 흐름을 가집니다.

```text
Compose UI
 -> ViewModel function
ViewModel
 -> StateFlow<UiState>
Compose UI
```

역할만 보면 둘 다 View와 data/domain layer 사이에서 user action을 받고 UI state를 만들어 View에 노출합니다. 그래서 실무 대화에서
"Android에서는 ViewModel이 하던 일을 Flutter에서는 Bloc이 한다"고 느낄 수 있습니다.

하지만 이것을 "Bloc은 MVVM의 ViewModel이다"라고 정리하면 부정확합니다. Bloc은 `Event -> Bloc -> State -> View` 흐름을 명시적으로
강제하므로, 패턴 기준으로는 MVVM보다 **MVI/Redux 계열의 state container/event processor**에 더 가깝습니다. Flutter 자체가 MVI라는 뜻은
아닙니다. Flutter는 선언형 UI 프레임워크이고, Bloc을 선택했을 때 그 상태 관리 구조가 MVI/Redux 쪽에 가까운 것입니다.

하지만 차이도 분명합니다.

| 관점        | Flutter Bloc                         | Android ViewModel                    |
|:----------|:-------------------------------------|:-------------------------------------|
| 기본 성격     | event-driven state machine/store     | lifecycle-aware screen state holder  |
| 입력        | `Event`                              | 함수 호출 또는 `UiAction`                  |
| 출력        | `State` stream                       | `StateFlow<UiState>` 등               |
| async 위치  | Bloc 내부가 일반적                         | ViewModel 내부가 일반적                    |
| lifecycle | Flutter widget tree/BlocProvider가 관리 | Android Lifecycle/ViewModelStore가 관리 |
| 상태 전이 강제성 | `Event -> State` 구조가 강함              | 함수, Flow, update 등으로 더 느슨함           |

그래서 문서에서 비교할 때는 이렇게 말하는 편이 가장 덜 헷갈립니다.

```text
Flutter Bloc은 Android ViewModel과 동일한 것은 아니다.
Bloc은 패턴 기준으로 MVI/Redux 계열에 가깝다.
Android ViewModel은 MVVM/MVI 중 하나를 강제하지 않는 lifecycle-aware screen state holder다.
```

이 관점으로 보면 이름에 덜 끌려갑니다. 중요한 것은 클래스 이름이 아니라, 그 객체가 화면 상태의 source of truth인지, user action을 받는지, 외부 작업
결과를 UI state로 바꾸는지입니다.

---
