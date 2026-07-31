# MVI Intent는 Controller가 아니다

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

아래 질문은 아키텍처를 공부하다 보면 자연스럽게 나옵니다.

```text
MVC의 Controller, MVI의 Intent, MVVM의 ViewModel은 이름만 바뀐 것 아닌가?
```

문제의식은 맞습니다. 하지만 정확히는 이렇게 고쳐야 합니다.

```text
Controller, Presenter, ViewModel, Bloc, Store는 비교할 수 있다.
하지만 MVI의 Intent는 Controller나 ViewModel과 같은 위치가 아니다.
Intent는 중재자가 아니라 사용자 입력/행동을 표현한 값이다.
```

즉, `MVC의 C`, `MVP의 P`, `MVVM의 VM`, `Bloc`, `Store`는 모두 "사용자 입력을 받아 화면 상태를 만들거나 Model과 연결하는 중간 객체"라는
공통점을 가집니다. 그러나 `MVI의 I(Intent)`는 그 중간 객체 자체가 아니라 중간 객체에 들어가는 입력값입니다.

더 정확한 비교는 다음과 같습니다.

| 패턴   | 입력/행동           | 중재자/상태 생산자                                 | 화면이 읽는 것                            |
|:-----|:----------------|:-------------------------------------------|:------------------------------------|
| MVC  | user event      | Controller                                 | View 직접 변경 또는 Model                 |
| MVP  | user event      | Presenter                                  | View interface 호출                   |
| MVVM | user action     | ViewModel                                  | Observable state / binding property |
| MVI  | Intent / Action | Store, Reducer, Processor, Bloc, 또는 MVI 스타일 ViewModel | 단일 State                            |

Data flow로 보면 차이가 더 선명합니다.
