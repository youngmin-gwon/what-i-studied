---
title: collect-flow-for-ui-with-lifecycle-aware-api
tags: [android, android/async, android/data, android/flow-state-contracts]
aliases: ["화면에 그릴 Flow는 lifecycle-aware API로 수집한다"]
date modified: 2026-08-03 18:07:31 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 화면에 그릴 Flow 는 lifecycle-aware API 로 수집한다

상위 문서: [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)

화면에 그릴 Flow 는 화면이 사용자에게 보이는 동안만 수집해야 한다.

View 시스템에서는 `repeatOnLifecycle`, Compose 에서는 `collectAsStateWithLifecycle` 를 사용한다.

이렇게 하면 화면이 중지된 동안 UI 갱신과 불필요한 작업을 줄일 수 있다.

### View 시스템

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state ->
            render(state)
        }
    }
}
```

`STARTED` 가 되면 수집을 시작하고, `STOPPED` 가 되면 블록을 취소한다.

다시 `STARTED` 가 되면 수집 블록을 새로 시작하므로 반복 수집에 안전하다.

### Compose

```kotlin
@Composable
fun BenefitRoute(viewModel: BenefitViewModel) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    BenefitScreen(state = uiState)
}
```

화면에 그릴 상태는 lifecycle-aware 상태 수집 API 를 사용한다.

Snackbar 와 Navigation 같은 일회성 이벤트는 상태로 변환하지 않고 별도 `LaunchedEffect` 에서 수집한다.

Flow 를 `launch` 로 무조건 수집해야 한다면 그 수집이 화면 수명과 함께 취소되는지 확인한다.

수집 위치를 화면 밖 전역 scope 로 올리면 중복 수집, 화면이 사라진 뒤의 렌더링, 자원 누수가 생길 수 있다.

ViewModel 은 화면 상태를 준비하고 UI 는 자신의 lifecycle 에 맞춰 이를 수집하는 경계를 지킨다.

상태 수집과 이벤트 수집을 같은 방식으로 처리하지 않는다.

상태는 재생 가능한 화면 모델로, 이벤트는 한 번 처리할 신호로 각 lifecycle 동작을 구분한다.

수집 중단과 재시작이 예상되는 화면에서는 중복 observer 가 생기지 않는지 확인한다.

렌더링 함수는 현재 상태를 받아 멱등적으로 화면을 갱신하도록 만든다.
