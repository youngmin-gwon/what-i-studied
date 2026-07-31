# Android 상태 관리 정본 지도

이 폴더는 Android 화면 상태 관리의 정본 노트를 모은다. 기존의 긴 설명형 노트는 이곳의 의미 단위 노트로 흡수하고, 기존 경로는 가능한 한 짧은 경유 노트로 남긴다.

## 읽는 순서

1. [ViewModel은 화면 단위 상태와 외부 작업을 조율한다](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel-orchestrates-screen-state-and-external-work.md)
2. [UI는 상태를 아래로 받고 사용자 행동을 위로 전달한다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-receives-state-and-sends-actions-up.md)
3. [UiState는 새 collector가 받아도 안전한 현재 화면의 표현이다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/uistate-represents-current-screen-for-new-collectors.md)
4. [StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/stateflow-is-for-current-screen-state-flow-is-for-source-stream.md)
5. [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/launched-effect-owns-composable-cancellable-work.md)

## 하위 지도

- [Android ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md)
- [Android UI State](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-state.md)
- [Android Reducer](01_inbox/mobile/android/02_app_framework/architecture/state-management/reducer/reducer.md)
- [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)
- [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)
