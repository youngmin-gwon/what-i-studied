# Flutter 개발자를 위한 Compose 상태 모델

이 문서는 Flutter 개발자가 Compose 상태 모델로 넘어갈 때의 진입점이다. Flutter 비교 자체보다 정본 판단 규칙을 먼저 읽는다.

## 먼저 읽을 정본

- [Compose 상태 API는 필요한 수명에 맞춰 선택한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-api-selection-by-lifetime.md)
- [UI는 상태를 아래로 받고 사용자 행동을 위로 전달한다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-receives-state-and-sends-actions-up.md)
- [ViewModel의 StateFlow는 lifecycle-aware collection으로 화면 상태가 된다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/viewmodel-stateflow-becomes-screen-state-with-lifecycle-collection.md)
- [StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/stateflow-is-for-current-screen-state-flow-is-for-source-stream.md)

## Flutter 관점의 핵심

Flutter의 `build()`가 자주 호출되어도 괜찮듯이 Compose의 Composable도 recomposition으로 자주 다시 실행될 수 있다. 차이는 Compose Runtime이 snapshot state 읽기를 관찰해 다시 실행할 범위를 더 세밀하게 정한다는 점이다.

따라서 Compose에서는 `Widget` 계층을 설계한다기보다, 현재 state를 받아 UI를 계산하는 함수를 설계한다고 보는 편이 낫다.
