# `stateIn`: Flow를 StateFlow로 바꾸는 표준 패턴

Repository에서 받은 Flow를 ViewModel에서 StateFlow로 바꿀 때 `stateIn`을 사용합니다.

```kotlin
val uiState: StateFlow<HomeUiState> =
    repository.observeHome()
        .map { home ->
            HomeUiState.Ready(home)
        }
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5_000),
            initialValue = HomeUiState.Loading,
        )
```

각 파라미터의 의미는 다음과 같습니다.

| 파라미터           | 의미                             |
|:---------------|:-------------------------------|
| `scope`        | StateFlow가 살아있을 CoroutineScope |
| `started`      | 언제 upstream Flow를 수집할지         |
| `initialValue` | 첫 화면에 보여줄 초기 상태                |

`SharingStarted.WhileSubscribed(5_000)`은 Android ViewModel에서 자주 쓰는 설정입니다.

뜻은:

* UI가 구독 중이면 upstream Flow를 수집한다.
* UI가 잠깐 사라져도 5초 동안은 수집을 유지한다.
* 화면 회전처럼 짧은 재구성에서 불필요한 재시작을 줄인다.

---
