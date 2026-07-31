# 현재 프로젝트 기준

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

현재 프로젝트의 `SignInViewModel`, `SignUpOtpVerificationViewModel`, `AppSessionViewModel` 정도는 아직 별도
Reducer가 필수인 복잡도는 아닙니다.

권장 기준:

- 현재처럼 작은 auth 화면은 `_uiState.update { it.copy(...) }`로 유지합니다.
- 실제 auth API 연동 후 입력 필드, 검증 상태, 약관 동의, 단계 이동이 크게 늘어나면 `SignUpStateReducer` 분리를 검토합니다.
- Reducer를 만들더라도 `Repository`, `Channel`, `Flow`, coroutine은 ViewModel에 남깁니다.
- Android 플랫폼 `Intent`와 혼동되지 않도록 화면 action 타입 이름은 `UiAction`을 우선 사용합니다.
- 화면 복원에 필요한 route id와 navigation scope는 [jetpack-navigation-3-guide](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide.md)를 따릅니다.
- 상태와 작업의 수명별 owner/API 선택은 [jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)를 따릅니다.
- Flow, StateFlow, SharedFlow, Channel 자체의
  의미는 [kotlin-coroutines-flow-stateflow](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow.md)를 따릅니다.
- Compose의 `remember`, `rememberSaveable`, state hoisting
  기준은 [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)
  를 따릅니다.

---
