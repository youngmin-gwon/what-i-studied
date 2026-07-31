# View system에서는 repeatOnLifecycle

상위 노트: [[jetpack-compose-state-lifetime-api-selection]]

Activity/Fragment/XML View에서 Flow를 수집해 view를 직접 갱신할 때는 `repeatOnLifecycle`이 현대적인 기본 패턴입니다.

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { uiState ->
            // update views
        }
    }
}
```

`Flow`와 `StateFlow`는 `LiveData.observe()`처럼 UI가 `STOPPED`일 때 자동으로 수집을 멈추지 않습니다. 그래서 View system에서는
`repeatOnLifecycle(STARTED)`로 화면이 보일 때만 collect하고, `STOPPED`가 되면 collect block을 취소했다가 다시 시작합니다.

Compose에서는 이 패턴을 직접 쓰는 대신, 화면 상태 수집에는 보통 `collectAsStateWithLifecycle()`을 사용합니다.

```text
View system
-> lifecycleScope + repeatOnLifecycle

Compose
-> collectAsStateWithLifecycle
```

`repeatOnLifecycle`은 낡은 API가 아닙니다. Compose에서는 더 높은 수준의 Compose 전용 wrapper를 우선 쓸 뿐입니다.

---
