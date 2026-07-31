# `MutableStateFlow`는 ViewModel 안에 숨긴다

외부에서 상태를 마음대로 바꾸면 안 됩니다. 그래서 보통 아래 패턴을 사용합니다.

```kotlin
private val _uiState = MutableStateFlow(HomeUiState())
val uiState: StateFlow<HomeUiState> = _uiState.asStateFlow()
```

| 변수         | 접근 범위                | 역할        |
|:-----------|:---------------------|:----------|
| `_uiState` | ViewModel 내부 private | 상태 변경 가능  |
| `uiState`  | 외부 공개                | 읽기/구독만 가능 |

이 패턴은 "상태의 소유자는 ViewModel이고, UI는 상태를 읽기만 한다"는 구조를 강제합니다.

ViewModel이 어떤 책임을 맡고, 상태 계산이 커졌을 때 Reducer로 어떻게
분리할지는 [[viewmodel-ui-state-reducer]]를 참조하세요. 이 문서는
Flow/StateFlow 자체의 의미와 사용 패턴에 집중합니다.
