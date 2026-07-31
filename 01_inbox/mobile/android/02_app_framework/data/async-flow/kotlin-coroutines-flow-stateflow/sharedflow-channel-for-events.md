# SharedFlow와 Channel: 상태가 아니라 이벤트를 다루는 도구

상위 노트: [[kotlin-coroutines-flow-stateflow]]

### 6-1. 상태와 이벤트는 다르다

UI에서 가장 많이 헷갈리는 부분입니다.

| 구분         | 예시                                   | 적합한 도구               |
|:-----------|:-------------------------------------|:---------------------|
| 상태(State)  | 로딩 중, 목록 데이터, 선택된 탭, 에러 문구           | StateFlow            |
| 이벤트(Event) | Snackbar 한 번 보여주기, 뒤로 가기, 토스트, 네비게이션 | SharedFlow / Channel |

상태는 "지금 화면이 무엇을 그려야 하는가"입니다. 이벤트는 "지금 한 번 발생하고 사라지는 신호"입니다.

### 6-2. Snackbar 이벤트 예시

```kotlin
sealed interface ProfileEvent {
    data class ShowSnackbar(val message: String) : ProfileEvent
}

class ProfileViewModel(
    private val repository: ProfileRepository,
) : ViewModel() {
    private val _events = MutableSharedFlow<ProfileEvent>()
    val events: SharedFlow<ProfileEvent> = _events.asSharedFlow()

    fun save() {
        viewModelScope.launch {
            runCatching {
                repository.saveProfile()
            }.onSuccess {
                _events.emit(ProfileEvent.ShowSnackbar("저장했습니다."))
            }.onFailure {
                _events.emit(ProfileEvent.ShowSnackbar("저장에 실패했습니다."))
            }
        }
    }
}
```

```kotlin
@Composable
fun ProfileRoute(
    viewModel: ProfileViewModel = viewModel(),
    snackbarHostState: SnackbarHostState = remember { SnackbarHostState() },
) {
    LaunchedEffect(viewModel) {
        viewModel.events.collect { event ->
            when (event) {
                is ProfileEvent.ShowSnackbar -> {
                    snackbarHostState.showSnackbar(event.message)
                }
            }
        }
    }

    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    ProfileScreen(uiState = uiState)
}
```

화면에 그릴 상태는 `collectAsStateWithLifecycle()`, 한 번 처리할 이벤트는 `LaunchedEffect`에서 `collect`하는 식으로 나눕니다.

> [!TIP]
> "새 구독자가 들어왔을 때 이전 값을 다시 받아야 하는가?"라고 물어보면 상태와 이벤트를 구분하기 쉽습니다. 다시 받아야 하면 StateFlow, 다시 받으면 안 되면
> SharedFlow/Channel입니다.

---
