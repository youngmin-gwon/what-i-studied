# StateFlow: 현재 상태를 들고 있는 Flow

상위 노트: [[kotlin-coroutines-flow-stateflow]]

### 5-1. StateFlow란?

`StateFlow`는 **항상 현재값을 하나 가지고 있는 Flow**입니다.

일반 Flow가 "흘러오는 데이터"라면, StateFlow는 "현재 상태가 적힌 전광판"에 가깝습니다.

| 구분       | Flow                      | StateFlow     |
|:---------|:--------------------------|:--------------|
| 현재값 보관   | 없음                        | 있음            |
| 초기값 필요   | 필요 없음                     | 반드시 필요        |
| 새 구독자 동작 | collect 시점부터 받음           | 즉시 최신값 1개를 받음 |
| 대표 용도    | DB 관찰, 이벤트 스트림, 비동기 파이프라인 | 화면 UI 상태      |
| 성격       | 보통 Cold                   | Hot           |

`StateFlow`는 UI 상태에 특히 잘 맞습니다. 화면은 언제든 "지금 무엇을 그려야 하는지"를 알아야 하기 때문입니다.

```kotlin
data class ProfileUiState(
    val isLoading: Boolean = false,
    val userName: String = "",
    val errorMessage: String? = null,
)
```

```kotlin
class ProfileViewModel(
    private val repository: ProfileRepository,
) : ViewModel() {
    private val _uiState = MutableStateFlow(ProfileUiState(isLoading = true))
    val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()

    fun load() {
        viewModelScope.launch {
            runCatching {
                repository.fetchProfile()
            }.onSuccess { profile ->
                _uiState.value = ProfileUiState(userName = profile.name)
            }.onFailure {
                _uiState.value = ProfileUiState(errorMessage = "프로필을 불러오지 못했습니다.")
            }
        }
    }
}
```

### 5-2. `MutableStateFlow`는 ViewModel 안에 숨긴다

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

### 5-3. Compose에서 StateFlow 구독하기

Compose에서는 `collectAsStateWithLifecycle()`을 사용해 StateFlow를 구독합니다.

```kotlin
@Composable
fun ProfileRoute(
    viewModel: ProfileViewModel = viewModel(),
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    ProfileScreen(
        uiState = uiState,
        onRetryClick = viewModel::load,
    )
}
```

`collectAsStateWithLifecycle()`은 화면 생명주기를 고려해, 화면이 보이는 동안에만 안전하게 Flow를 수집합니다.

> [!IMPORTANT]
> Compose에서 Flow를 직접 `collect`하려고 `LaunchedEffect`를 남발하지 마세요. 화면에 그릴 상태라면 대부분
`collectAsStateWithLifecycle()`이 맞습니다.

### 5-4. `stateIn`: Flow를 StateFlow로 바꾸는 표준 패턴

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
