# CoroutineScope: Coroutine의 작업장

Coroutine은 아무 데서나 막 띄우면 안 됩니다. 어디에 소속된 작업인지가 중요합니다.

이 소속 범위를 `CoroutineScope`라고 합니다.

| Scope                      | 수명                               | 대표 사용처                        |
|:---------------------------|:---------------------------------|:------------------------------|
| `viewModelScope`           | ViewModel이 사라질 때까지               | 화면 상태 로딩, 유저 액션 처리            |
| `lifecycleScope`           | Activity/Fragment Lifecycle까지    | 생명주기와 직접 연결된 작업               |
| `rememberCoroutineScope()` | Composable이 Composition에 남아있는 동안 | Snackbar, Drawer 열기 같은 UI 이벤트 |
| WorkManager 내부 Scope       | Worker 실행 중                      | 앱이 꺼져도 보장되어야 하는 백그라운드 작업      |

가장 많이 쓰는 것은 `viewModelScope`입니다.

```kotlin
class BenefitViewModel(
    private val repository: BenefitRepository,
) : ViewModel() {
    fun refresh() {
        viewModelScope.launch {
            repository.refreshBenefits()
        }
    }
}
```

ViewModel이 제거되면 `viewModelScope` 안에서 실행 중인 Coroutine도 함께 취소됩니다.
