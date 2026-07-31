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
[jetpack-compose-automatic-state-observation-for-flutter-developers](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers.md)를 먼저 봅니다.

---

## 원자 노트

- [Flutter와 Compose의 큰 차이](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/flutter-compose-state-model-differences.md)
- [Compose에서 상태란 무엇인가?](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/what-is-state-in-compose.md)
- [`mutableStateOf`](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/mutable-state-of.md)
- [`remember`](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/remember-in-compose.md)
- [Kotlin `by` 키워드](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/kotlin-by-delegated-property-in-compose.md)
- [`rememberSaveable`](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/remember-saveable.md)
- [State hoisting](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/state-hoisting.md)
- [ViewModel, Flow, StateFlow와의 관계](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/viewmodel-flow-stateflow-in-compose.md)
- [자주 쓰는 `remember~` 계열](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/common-remember-apis.md)
- [`remember`는 아니지만 같이 알아야 하는 API](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/compose-state-related-apis.md)
- [이 프로젝트 기준](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/compose-state-project-guidelines.md)
- [실수하기 쉬운 지점](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/compose-state-common-mistakes.md)
- [판단 규칙](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison/compose-state-selection-rules.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, 각 H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
