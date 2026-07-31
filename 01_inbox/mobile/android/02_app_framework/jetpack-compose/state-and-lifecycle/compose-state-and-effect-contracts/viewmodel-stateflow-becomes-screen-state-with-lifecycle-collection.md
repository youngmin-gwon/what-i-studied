# ViewModel의 StateFlow는 collectAsStateWithLifecycle로 화면 상태로 변환한다

상위 문서: [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)
관련 정본: [StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/stateflow-is-for-current-screen-state-flow-is-for-source-stream.md), [ViewModel은 mutable 상태를 숨기고 읽기 전용 상태만 노출한다](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel-exposes-read-only-state.md)


ViewModel이 노출한 `StateFlow<UiState>`는 Compose가 직접 그리는 값이 아니다.
Composable은 `collectAsStateWithLifecycle()`로 이를 lifecycle-aware Compose `State`로 변환한다.

```kotlin
@Composable
fun BenefitRoute(viewModel: BenefitViewModel) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    BenefitScreen(uiState = uiState, onAction = viewModel::onAction)
}
```

이 선택은 화면이 활성 lifecycle 상태에 있을 때만 수집하도록 만든다.
화면이 보이지 않는 동안 불필요한 수집과 UI 갱신을 줄이고, 다시 활성화되면 최신 상태를 읽는다.

## Compose API 선택 기준

- Android lifecycle을 사용하는 화면의 Flow는 `collectAsStateWithLifecycle`을 우선한다.
- lifecycle이 없는 순수 Compose 환경에서는 `collectAsState`가 맞을 수 있다.
- Flow를 수집하면서 snackbar나 navigation 같은 부수효과를 실행해야 하면 `LaunchedEffect`와 lifecycle-aware 수집을 조합한다.
- 단순히 화면을 그릴 값은 `State`로 변환해 Composable의 입력으로 전달한다.

`collectAsStateWithLifecycle`은 ViewModel을 대체하지 않는다.
ViewModel은 화면 상태의 owner이고, 이 API는 그 상태를 현재 UI 수명에 맞춰 읽는 adapter다.
Composable이 StateFlow를 직접 변환하더라도 source of truth는 ViewModel에 남는다.

## 화면 경계

Route Composable은 상태 수집과 event 연결을 맡는다.
하위 screen Composable은 이미 변환된 `UiState`와 명시적인 callback을 받는다.
하위 Composable이 ViewModel을 직접 찾아가면 수명과 테스트 경계가 흐려질 수 있다.

```kotlin
@Composable
fun BenefitRoute(viewModel: BenefitViewModel) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    BenefitContent(
        state = state,
        onRefresh = viewModel::refresh,
    )
}
```

수집 결과를 다시 ViewModel에 저장하지 않는다.
Flow를 Compose State로 바꾼 뒤 필요한 만큼만 읽고, UI는 그 값을 선언적으로 렌더링한다.
화면이 사라진 뒤에도 계속 실행되어야 하는 데이터 작업은 Compose 수집의 수명에 맡기지 않는다.

## 흔한 오류

- `collectAsState`만 사용해 Android lifecycle을 무시한다.
- Composable 본문에서 수동 `launch`로 Flow를 수집한다.
- 수집된 값을 또 다른 mutable 상태에 복사해 source of truth를 만든다.
- UI controller를 ViewModel에 넣고 effect 경계를 없앤다.

권장 기준은 [Lifecycle-aware collection](https://developer.android.com/develop/ui/compose/state#other-supported-types-of-state)과 [UI layer state holders](https://developer.android.com/topic/architecture/ui-layer/stateholders)를 함께 적용하는 것이다.
