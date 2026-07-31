# Jetpack Compose 상태 관리 & Flutter 비교 가이드

이 문서는 Jetpack Compose에서 상태를 어떻게 관리하는지 Flutter 경험 기준으로 비교해서 정리합니다.

핵심은 단순합니다.

```text
Compose UI는 상태를 읽는다.
상태가 바뀌면, 그 상태를 읽은 Composable이 다시 실행될 수 있다.
```

Flutter에서 `build()`가 다시 호출되는 것처럼, Compose에서는 `@Composable` 함수가 다시 실행되는 것을 **recomposition**이라고 부릅니다.

관련 공식 문서:

- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving)
- [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
- [Side effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)

Compose Runtime이 상태 읽기와 쓰기를 어떻게 추적하는지에 집중해서 보고 싶다면
[[jetpack-compose-automatic-state-observation-for-flutter-developers]]를 먼저 봅니다.

---

## 원자 노트

- [[flutter-compose-state-model-differences|Flutter와 Compose의 큰 차이]]
- [[what-is-state-in-compose|Compose에서 상태란 무엇인가?]]
- [[mutable-state-of|`mutableStateOf`]]
- [[remember-in-compose|`remember`]]
- [[kotlin-by-delegated-property-in-compose|Kotlin `by` 키워드]]
- [[remember-saveable|`rememberSaveable`]]
- [[state-hoisting|State hoisting]]
- [[viewmodel-flow-stateflow-in-compose|ViewModel, Flow, StateFlow와의 관계]]
- [[common-remember-apis|자주 쓰는 `remember~` 계열]]
- [[compose-state-related-apis|`remember`는 아니지만 같이 알아야 하는 API]]
- [[compose-state-project-guidelines|이 프로젝트 기준]]
- [[compose-state-common-mistakes|실수하기 쉬운 지점]]
- [[compose-state-selection-rules|판단 규칙]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, 각 H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
