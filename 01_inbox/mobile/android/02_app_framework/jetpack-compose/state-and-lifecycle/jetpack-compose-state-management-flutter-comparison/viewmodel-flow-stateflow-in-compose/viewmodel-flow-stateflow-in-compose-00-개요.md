# ViewModel, Flow, StateFlow와의 관계 개요

상위 노트: [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)

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
기준은 [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)를 따릅니다. 이 문서는
Compose 관점의 상태 위치 판단에 집중하고, ViewModel 내부 구조는 별도 문서에서 다룹니다.
