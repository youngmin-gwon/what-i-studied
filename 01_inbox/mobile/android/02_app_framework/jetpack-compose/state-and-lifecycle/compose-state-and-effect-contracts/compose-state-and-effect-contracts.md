# Compose 상태와 Effect 계약

Compose 상태 API는 값의 수명과 작업의 owner를 기준으로 고른다. `remember`, `rememberSaveable`, ViewModel, effect API를 편의성 기준으로 섞지 않는다.

## 정본 노트

- [Compose 상태 API는 필요한 수명에 맞춰 선택한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-api-selection-by-lifetime.md)
- [Composable 수명보다 오래 필요한 작은 복원 상태에만 rememberSaveable을 사용한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/remember-saveable-is-for-small-restorable-ui-state.md)
- [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/launched-effect-owns-composable-cancellable-work.md)
- [등록과 해제가 쌍인 작업은 DisposableEffect로 관리한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/disposable-effect-pairs-registration-and-cleanup.md)
- [UI 컨트롤러와 Effect 실행기는 UI 수명에 둔다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/ui-controllers-and-effect-runners-live-with-ui-lifetime.md)
- [ViewModel의 StateFlow는 lifecycle-aware collection으로 화면 상태가 된다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/viewmodel-stateflow-becomes-screen-state-with-lifecycle-collection.md)

관련 지도: [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)
