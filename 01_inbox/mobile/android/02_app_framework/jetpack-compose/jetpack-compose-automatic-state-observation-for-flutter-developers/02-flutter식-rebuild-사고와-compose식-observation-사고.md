# Flutter식 rebuild 사고와 Compose식 observation 사고

상위 노트: [[jetpack-compose-automatic-state-observation-for-flutter-developers]]

| 관점       | Flutter                                              | Compose                                                          |
|:---------|:-----------------------------------------------------|:-----------------------------------------------------------------|
| 갱신 시작점   | `setState()`, `notifyListeners()`, provider emission | `MutableState.value` 변경, `StateFlow` emission을 Compose State로 수집 |
| 갱신 범위 판단 | 개발자가 `StatefulWidget`, `Consumer`, `Selector` 경계로 조절 | Runtime이 State read 정보를 기반으로 invalidation scope 결정               |
| 상태 보관 위치 | `State`, Provider/Riverpod/Bloc, controller          | `remember`, state holder, ViewModel, Flow/StateFlow              |
| UI 함수    | `build()`                                            | `@Composable` 함수                                                 |
| 중요한 질문   | 어디를 rebuild할까?                                       | 이 Composable이 어떤 State를 읽는가?                                     |

Flutter의 `ref.watch(counterProvider)`나 `ValueListenableBuilder`는 "이 UI가 이 값을 보고 있다"는 구독 관계를 명시합니다.
Compose는 `state.value`를 읽는 행위 자체를 Runtime이 추적합니다.

---
