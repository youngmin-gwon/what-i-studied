# ViewModel, Flow, StateFlow와의 관계

상위 노트: [[jetpack-compose-state-management-flutter-comparison]]

`remember`는 Composable 내부의 상태입니다. 화면 단위 정책이나 API 호출 결과를 오래 들고 있기에는 약합니다.

화면 단위 상태는 보통 ViewModel에 둡니다.

```kotlin
class LoginViewModel(
    private val loginService: LoginService,
) : ViewModel() {
    private val _uiState = MutableStateFlow(LoginUiState())
    val uiState: StateFlow<LoginUiState> = _uiState.asStateFlow()

    fun emailChanged(email: String) {
        _uiState.update { it.copy(email = email) }
    }
}
```

Composable에서는 lifecycle-aware 방식으로 구독합니다.

```kotlin
@Composable
fun LoginRoute(
    viewModel: LoginViewModel,
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    LoginScreen(
        uiState = uiState,
        onEmailChange = viewModel::emailChanged,
    )
}
```

Flutter로 느슨하게 비교하면 다음에 가깝습니다.

| Flutter                  | Compose/Android                   |
|:-------------------------|:----------------------------------|
| Riverpod Notifier, Cubit | ViewModel에 가까운 state holder       |
| Bloc                     | MVI/Redux 계열 state container에 가까움 |
| Stream, ValueNotifier    | Flow, StateFlow                   |
| Consumer, BlocBuilder    | `collectAsStateWithLifecycle()`   |
| Repository               | Repository                        |

주의할 점은 Flutter 자체가 MVVM이나 MVI를 강제하지 않는다는 것입니다. Flutter는 선언형 UI 프레임워크이고, Provider/Riverpod/Bloc 같은 상태
관리 선택지에 따라 구조가 달라집니다. 특히 Bloc은 `Event -> Bloc -> State -> View` 흐름을 강하게 갖기 때문에 MVVM보다 MVI/Redux 계열에
더 가깝습니다.

`StateFlow`는 ViewModel 전용 개념이 아닙니다. Kotlin Coroutines의 observable state holder입니다. 다만 UI가 구독하는 화면
상태에는 ViewModel과 함께 쓰는 경우가 많습니다.

Repository에서 `Flow`나 `StateFlow`를 노출할 수도 있습니다. 예를 들어 session 상태처럼 앱 전체에서 관찰해야 하는 값은
repository/observer가 `Flow<SessionState>`를 제공하고, root ViewModel이 그것을 화면 상태로 변환할 수 있습니다.

ViewModel 자체의 책임, user action 이름, 일회성 이벤트, Reducer 도입
기준은 [[viewmodel-ui-state-reducer]]를 따릅니다. 이 문서는
Compose 관점의 상태 위치 판단에 집중하고, ViewModel 내부 구조는 별도 문서에서 다룹니다.

### 8-1. Flow, StateFlow, SharedFlow, Channel 구분

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

### 8-2. Flow는 앱 간 데이터 전달 API가 아니다

`Flow`는 Kotlin 객체가 같은 앱 프로세스 안에서 값을 주고받는 방식입니다.

```text
Room -> Flow -> Repository -> ViewModel -> Compose
DataStore -> Flow -> SessionRepository -> RootViewModel
callback API -> callbackFlow -> ViewModel
```

다른 앱으로 데이터를 공개하거나 전달하려면 Flow가 아니라 Android 플랫폼 경계를 사용해야 합니다.

| 목적                          | 사용하는 도구                       |
|:----------------------------|:------------------------------|
| 다른 앱이 내 구조화 데이터를 조회         | `ContentProvider`             |
| 다른 앱에 파일 공유                 | `FileProvider`                |
| 다른 앱/시스템에 한 번의 작업 요청        | `Intent` / `PendingIntent`    |
| 웹 링크로 앱 진입                  | App Link / Deep Link          |
| 시스템/AI agent가 앱 기능을 검색하고 실행 | App Functions                 |
| 낮은 수준의 프로세스 간 바인딩           | Bound Service / Binder / AIDL |

> [!IMPORTANT]
> Flow는 "앱 안의 상태 흐름"이고, ContentProvider/Intent/FileProvider/App Functions는 "앱 밖과 만나는 통로"입니다. 이 둘을 섞어
> 생각하면 아키텍처 경계가 흐려집니다.

---
