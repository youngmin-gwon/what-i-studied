# Flow, StateFlow, SharedFlow, Channel 구분

Compose 상태 관리에서 자주 헷갈리는 지점은 "상태"와 "이벤트"를 같은 통로로 다루는 것입니다.

| 도구              | Compose에서의 주된 역할          | Flutter 감각으로 보면                    | 주의점                                  |
|:----------------|:--------------------------|:-----------------------------------|:-------------------------------------|
| `Flow<T>`       | 시간이 지나며 여러 값이 나오는 비동기 스트림 | `Stream<T>`                        | 자체로 현재값을 보장하지 않음                     |
| `StateFlow<T>`  | 화면이 그릴 최신 UI 상태           | `ValueNotifier<T>` + `Stream`에 가까움 | 반드시 초기값이 있고 최신값을 즉시 받을 수 있음          |
| `SharedFlow<T>` | 여러 collector에게 일회성 이벤트 발행 | broadcast stream                   | Snackbar/Toast/Navigation 같은 이벤트에 적합 |
| `Channel<T>`    | 한 소비자에게 순서대로 전달되는 큐       | single-subscription queue          | 여러 화면이 동시에 받을 이벤트에는 부적합              |

기준은 다음처럼 잡으면 됩니다.

```text
화면이 지금 무엇을 그려야 하는가?
-> StateFlow

DB, DataStore, callback API에서 값이 계속 흘러오는가?
-> Flow

한 번만 처리할 UI 이벤트인가?
-> SharedFlow 또는 Channel
```

```kotlin
data class LoginUiState(
    val email: String = "",
    val isLoading: Boolean = false,
)

sealed interface LoginEvent {
    data class ShowSnackbar(val message: String) : LoginEvent
    data object NavigateHome : LoginEvent
}

class LoginViewModel(
    private val loginService: LoginService,
) : ViewModel() {
    private val _uiState = MutableStateFlow(LoginUiState())
    val uiState: StateFlow<LoginUiState> = _uiState.asStateFlow()

    private val _events = MutableSharedFlow<LoginEvent>()
    val events: SharedFlow<LoginEvent> = _events.asSharedFlow()

    fun login() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true) }
            runCatching {
                loginService.login(_uiState.value.email)
            }.onSuccess {
                _events.emit(LoginEvent.NavigateHome)
            }.onFailure {
                _events.emit(LoginEvent.ShowSnackbar("로그인에 실패했습니다."))
            }
            _uiState.update { it.copy(isLoading = false) }
        }
    }
}
```

Composable에서는 상태와 이벤트를 분리해서 받습니다.

```kotlin
@Composable
fun LoginRoute(
    viewModel: LoginViewModel,
    onNavigateHome: () -> Unit,
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    LaunchedEffect(viewModel) {
        viewModel.events.collect { event ->
            when (event) {
                is LoginEvent.ShowSnackbar -> {
                    // snackbarHostState.showSnackbar(event.message)
                }
                LoginEvent.NavigateHome -> onNavigateHome()
            }
        }
    }

    LoginScreen(
        uiState = uiState,
        onLoginClick = viewModel::login,
    )
}
```
