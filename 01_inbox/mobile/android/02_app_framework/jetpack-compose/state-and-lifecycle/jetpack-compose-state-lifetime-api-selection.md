# Jetpack Compose 상태 수명과 API 선택

이 문서는 Compose 상태 수명 판단의 진입점이다. API별 장문 설명은 의미 단위 정본 노트로 흡수했다.

## 정본

- [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)
- [Compose 상태 API는 필요한 수명에 맞춰 선택한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-api-selection-by-lifetime.md)
- [Composable 수명보다 오래 필요한 작은 복원 상태에만 rememberSaveable을 사용한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/remember-saveable-is-for-small-restorable-ui-state.md)
- [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/launched-effect-owns-composable-cancellable-work.md)
- [등록과 해제가 쌍인 작업은 DisposableEffect로 관리한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/disposable-effect-pairs-registration-and-cleanup.md)
- [ViewModel의 StateFlow는 lifecycle-aware collection으로 화면 상태가 된다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/viewmodel-stateflow-becomes-screen-state-with-lifecycle-collection.md)
