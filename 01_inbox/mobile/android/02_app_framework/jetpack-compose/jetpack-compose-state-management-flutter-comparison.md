# Jetpack Compose 상태 관리 & Flutter 비교 가이드

이 문서는 Jetpack Compose에서 상태를 어떻게 관리하는지 Flutter 경험 기준으로 비교해서 정리합니다.

핵심은 단순합니다.

```text
Compose UI는 상태를 읽는다.
상태가 바뀌면, 그 상태를 읽은 Composable이 다시 실행될 수 있다.
```

Flutter에서 `build()`가 다시 호출되는 것처럼, Compose에서는 `@Composable` 함수가 다시 실행되는 것을 **recomposition**이라고 부릅니다.

관련 공식 문서:

- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving)
- [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
- [Side effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)

Compose Runtime이 상태 읽기와 쓰기를 어떻게 추적하는지에 집중해서 보고 싶다면
[[jetpack-compose-automatic-state-observation-for-flutter-developers|compose_automatic_state_observation_flutter_guide.md]]를 먼저 봅니다.

---

## 1. Flutter와 Compose의 큰 차이

| 관점           | Flutter                                  | Jetpack Compose                             |
|:-------------|:-----------------------------------------|:--------------------------------------------|
| UI 선언        | `Widget build(BuildContext context)`     | `@Composable fun Screen()`                  |
| 로컬 상태        | `StatefulWidget` + `State`               | `remember { mutableStateOf(...) }`          |
| 상태 변경        | `setState { ... }`                       | `state.value = ...` 또는 `var value by state` |
| 다시 그리기       | `build()` 재실행                            | recomposition                               |
| 화면 단위 상태     | Provider, Riverpod, Bloc, Cubit 등        | ViewModel + StateFlow/Flow                  |
| 암묵적 의존성 전달   | InheritedWidget, Provider context lookup | CompositionLocal                            |
| 복원 가능한 UI 상태 | RestorationMixin, PageStorage 등          | `rememberSaveable`, `SavedStateHandle`      |

Compose는 Flutter처럼 선언형 UI입니다. 하지만 Flutter의 `StatefulWidget`처럼 클래스를 나누지 않고, 함수 안에서 `remember`로
Composition에 값을 저장합니다.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }

    Button(onClick = { count += 1 }) {
        Text(text = "$count")
    }
}
```

위 코드는 Flutter로 치면 `StatefulWidget` 안의 `int count`와 `setState`에 가까운 로컬 UI 상태입니다.

---

## 2. Compose에서 상태란 무엇인가?

Compose에서 상태는 시간이 지나며 바뀔 수 있고, UI 결과에 영향을 주는 값입니다.

```text
입력창의 text
선택된 tab
체크박스 checked 여부
로그인 세션 상태
운동 기록 목록
로딩/성공/실패 상태
```

다만 모든 상태를 같은 곳에 두면 안 됩니다.

| 상태 종류                                    | 권장 위치                  |
|:-----------------------------------------|:-----------------------|
| 버튼 눌림, 임시 expanded 여부                    | `remember`             |
| 입력값, 선택 tab처럼 회전 후에도 유지할 작은 UI 상태        | `rememberSaveable`     |
| 화면 전체의 로딩/성공/실패, form validation, API 결과 | ViewModel              |
| 로그인 세션, 앱 설정                             | Repository + DataStore |
| 운동 기록, 측정 이력처럼 쌓이는 구조화 데이터               | Repository + Room      |

`remember`는 UI 함수 내부의 메모리입니다. 앱 데이터 저장소가 아닙니다.

---

## 3. `mutableStateOf`

`mutableStateOf`는 Compose가 관찰할 수 있는 상태 객체를 만듭니다.

```kotlin
val countState = remember { mutableStateOf(0) }

Text(text = "${countState.value}")

Button(onClick = { countState.value += 1 }) {
    Text("Increase")
}
```

`countState.value`를 읽은 Composable은 그 값이 바뀌면 recomposition 대상이 됩니다.

일반 Kotlin 변수는 Compose가 관찰하지 못합니다.

```kotlin
@Composable
fun WrongCounter() {
    var count = 0

    Button(onClick = { count += 1 }) {
        Text(text = "$count")
    }
}
```

이 코드는 클릭해도 UI가 기대대로 갱신되지 않습니다. 값 변경을 Compose runtime이 알 수 없고, recomposition이 일어나면 `count`가 다시 `0`으로
만들어질 수 있습니다.

---

## 4. `remember`

`remember`는 Composable이 recomposition되더라도 값을 유지하게 해줍니다.

```kotlin
@Composable
fun SearchBox() {
    var query by remember { mutableStateOf("") }

    TextField(
        value = query,
        onValueChange = { query = it },
    )
}
```

`remember`의 수명은 **Composition에 남아 있는 동안**입니다.

```text
recomposition: 유지됨
화면 회전으로 Activity 재생성: 기본적으로 사라짐
프로세스 종료 후 복원: 사라짐
해당 Composable이 화면에서 제거됨: 사라짐
```

### key가 있는 `remember`

`remember`는 key를 받을 수 있습니다.

```kotlin
val formatter = remember(locale) {
    DateTimeFormatter.ofPattern("yyyy.MM.dd", locale)
}
```

`locale`이 같으면 기존 값을 재사용하고, `locale`이 바뀌면 block을 다시 실행해 새 값을 만듭니다.

이 패턴은 "이 값은 특정 입력이 바뀔 때만 다시 계산되어야 한다"는 뜻을 코드에 남깁니다.

---

## 5. Kotlin `by` 키워드

`by`는 Compose 전용 문법이 아니라 Kotlin의 **delegated property** 문법입니다.

Compose에서는 `MutableState<T>`를 더 자연스럽게 읽고 쓰기 위해 자주 사용합니다.

아래 두 코드는 의미가 같습니다.

```kotlin
val countState = remember { mutableStateOf(0) }

Text(text = "${countState.value}")
Button(onClick = { countState.value += 1 }) {
    Text("Increase")
}
```

```kotlin
var count by remember { mutableStateOf(0) }

Text(text = "$count")
Button(onClick = { count += 1 }) {
    Text("Increase")
}
```

`by`를 쓰려면 보통 다음 import가 필요합니다.

```kotlin
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
```

읽기 전용이면 `getValue`만 필요합니다.

```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

여기서 `by`는 `uiState.value`를 매번 쓰지 않게 해주는 Kotlin 문법입니다. 상태 관리 도구 자체가 아닙니다.

---

## 6. `rememberSaveable`

`rememberSaveable`은 `remember`처럼 recomposition 사이에 값을 유지하고, 추가로 Activity 재생성이나 프로세스 복원 상황에서도 저장 가능한
값을 복원합니다.

```kotlin
@Composable
fun LoginForm() {
    var email by rememberSaveable { mutableStateOf("") }

    TextField(
        value = email,
        onValueChange = { email = it },
    )
}
```

`rememberSaveable`이 적합한 상태:

```text
입력창 text
선택된 tab key
현재 열려 있는 page id
간단한 filter 값
작은 enum/string/int/boolean 상태
```

`rememberSaveable`이 부적합한 상태:

```text
Repository
HTTP client
암호화 key
큰 list
bitmap
DB entity 전체 목록
서버에서 다시 받아야 하는 screen data 전체
```

저장 가능한 기본 타입이 아니면 `Saver`를 정의할 수 있습니다.

```kotlin
data class DraftMessage(
    val title: String,
    val body: String,
)

val DraftMessageSaver = listSaver<DraftMessage, String>(
    save = { listOf(it.title, it.body) },
    restore = { DraftMessage(title = it[0], body = it[1]) },
)

@Composable
fun MessageEditor() {
    var draft by rememberSaveable(stateSaver = DraftMessageSaver) {
        mutableStateOf(DraftMessage(title = "", body = ""))
    }
}
```

다만 `Saver`를 만들 수 있다고 해서 아무 데이터나 저장해도 되는 것은 아닙니다. `rememberSaveable`은 작은 UI 복원 상태에만 쓰는 편이 안전합니다.

---

## 7. State hoisting

Compose에서는 상태를 가능하면 필요한 곳까지 끌어올립니다. 이를 **state hoisting**이라고 합니다.

상태를 가진 Composable:

```kotlin
@Composable
fun SearchBox() {
    var query by rememberSaveable { mutableStateOf("") }

    TextField(
        value = query,
        onValueChange = { query = it },
    )
}
```

상태를 밖으로 올린 Composable:

```kotlin
@Composable
fun SearchBox(
    query: String,
    onQueryChange: (String) -> Unit,
) {
    TextField(
        value = query,
        onValueChange = onQueryChange,
    )
}
```

두 번째 형태가 더 재사용하기 쉽고 테스트하기 쉽습니다.

Compose의 기본 흐름은 다음과 같습니다.

```text
state down
events up
```

즉 부모는 상태를 내려주고, 자식은 이벤트를 올립니다.

Flutter의 `value` + `onChanged` 패턴과 거의 같습니다.

---

## 8. ViewModel, Flow, StateFlow와의 관계

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
기준은 [[viewmodel-ui-state-reducer|viewmodel_ui_state_reducer_guide.md]]를 따릅니다. 이 문서는
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

## 9. 자주 쓰는 `remember~` 계열

Compose와 Jetpack 라이브러리에는 `remember`로 시작하는 API가 많습니다. 공통점은 "Composition 수명에 맞춰 어떤 객체를 기억한다"는 것입니다.

상태나 작업이 어떤 수명에 묶여야 하는지부터 판단해야 할
때는 [[jetpack-compose-state-lifetime-api-selection|compose_state_lifetime_api_guide.md]]를 먼저 봅니다.

| API                                 | 역할                                  | 주의점                                              |
|:------------------------------------|:------------------------------------|:-------------------------------------------------|
| `remember`                          | recomposition 사이에 값 유지              | 화면에서 제거되면 사라짐                                    |
| `rememberSaveable`                  | 저장 가능한 UI 상태 복원                     | 큰 데이터나 dependency 저장 금지                          |
| `rememberCoroutineScope`            | Composable 수명에 묶인 CoroutineScope 제공 | 화면 이벤트용. 장기 비즈니스 작업은 ViewModel이 더 적합             |
| `rememberUpdatedState`              | effect를 재시작하지 않고 최신 값/lambda 참조     | `LaunchedEffect(Unit)` 안에서 최신 callback이 필요할 때 유용 |
| `rememberScrollState`               | 일반 scroll 상태                        | 단순 scroll container용                             |
| `rememberLazyListState`             | `LazyColumn`, `LazyRow` scroll 상태   | list position 제어/관찰에 사용                          |
| `rememberPagerState`                | pager page 상태                       | foundation pager 사용 시                            |
| `rememberSaveableStateHolder`       | key별 saveable state 보관              | navigation, tab, custom back stack에서 유용          |
| `rememberLauncherForActivityResult` | Activity Result launcher 등록         | 권한 요청, 이미지 선택 등 platform result 처리               |
| `rememberModalBottomSheetState`     | Material3 bottom sheet 상태           | sheet 표시/숨김은 coroutine과 함께 다루는 경우가 많음            |
| `rememberDrawerState`               | Material drawer 상태                  | navigation drawer open/close 상태                  |
| `rememberDatePickerState`           | Material3 date picker 상태            | picker 내부 선택 상태                                  |
| `rememberTimePickerState`           | Material3 time picker 상태            | picker 내부 선택 상태                                  |
| `rememberInfiniteTransition`        | 무한 animation transition             | 화면에 있을 때만 의미 있음                                  |
| `rememberTransition`                | animation transition 상태             | state 기반 animation에 사용                           |

Navigation 3를 쓰는 경우에도 같은 원리입니다. back stack, entry decorator, saveable state holder 등은 Composition
안에서 기억해야 할 UI navigation state입니다.

---

## 10. `remember`는 아니지만 같이 알아야 하는 API

### `derivedStateOf`

`derivedStateOf`는 다른 상태에서 계산되는 파생 상태를 만들 때 사용합니다.

```kotlin
val listState = rememberLazyListState()
val showScrollToTop by remember {
    derivedStateOf {
        listState.firstVisibleItemIndex > 0
    }
}
```

스크롤처럼 자주 바뀌는 값에서 실제 UI 갱신은 특정 조건이 바뀔 때만 필요할 수 있습니다. 이때 `derivedStateOf`가 도움이 됩니다.

다만 단순 문자열 조합이나 가벼운 계산에 무조건 쓰는 것은 과합니다.

### `LaunchedEffect`

Composable이 Composition에 들어왔을 때 coroutine 작업을 시작합니다.

```kotlin
LaunchedEffect(userId) {
    viewModel.load(userId)
}
```

key가 바뀌면 기존 작업이 취소되고 다시 시작됩니다.

### `DisposableEffect`

등록과 해제가 쌍으로 필요한 작업에 씁니다.

```kotlin
DisposableEffect(lifecycleOwner) {
    val observer = LifecycleEventObserver { _, _ -> }
    lifecycleOwner.lifecycle.addObserver(observer)

    onDispose {
        lifecycleOwner.lifecycle.removeObserver(observer)
    }
}
```

### `produceState`

외부 async source를 Compose `State<T>`로 변환합니다.

```kotlin
val image by produceState<Image?>(initialValue = null, url) {
    value = imageRepository.load(url)
}
```

앱 아키텍처에서는 ViewModel/Repository로 빼는 편이 더 명확한 경우가 많습니다.

### `snapshotFlow`

Compose State 읽기를 Flow로 변환합니다.

```kotlin
LaunchedEffect(listState) {
    snapshotFlow { listState.firstVisibleItemIndex }
        .collect { index ->
            analytics.trackScroll(index)
        }
}
```

UI state 변화를 Flow operator와 연결해야 할 때 사용합니다.

---

## 11. 이 프로젝트 기준

현재 프로젝트에서는 다음 기준으로 나누는 편이 좋습니다.

| 대상                        | 위치                                                       |
|:--------------------------|:---------------------------------------------------------|
| Root session 판정           | `AppSessionViewModel` 또는 root ViewModel                  |
| session 저장                | `feature:session:impl`의 repository/DataStore             |
| session 상태 contract       | `feature:session:api`                                    |
| 로그인 form 입력값              | 처음에는 `rememberSaveable`, 검증/로그인 로직이 커지면 `AuthViewModel`  |
| 복잡한 form 상태 전이            | 처음에는 ViewModel의 `_uiState.update`, 반복이 커지면 선택적으로 Reducer |
| Auth flow back stack      | auth shell/flow Composable 내부의 navigation state          |
| Main tab 선택               | `rememberSaveable` 또는 Navigation 3 back stack            |
| Main tab별 화면 상태           | 각 feature impl의 route/ViewModel                          |
| foldable/tablet layout 선택 | window size/posture state를 읽고 shell에서 adaptive UI 결정     |
| deep link 처리              | app/root navigation layer에서 route key로 변환                |

중요한 기준은 다음입니다.

```text
UI만 알면 되는 상태인가?
-> remember / rememberSaveable

화면 정책, 로딩, API 결과, validation이 섞이는가?
-> ViewModel

앱을 껐다 켜도 남아야 하는가?
-> DataStore / Room

여러 feature가 공유해야 하는 contract인가?
-> api module

실제 Android 저장소, 네트워크, 암호화 구현인가?
-> impl module
```

---

## 12. 실수하기 쉬운 지점

### Composable body에서 직접 API 호출하지 않기

```kotlin
@Composable
fun BadScreen() {
    repository.load()
}
```

Composable은 recomposition될 수 있으므로 body에 직접 side effect를 두면 호출이 반복될 수 있습니다. ViewModel 또는
`LaunchedEffect`로 옮겨야 합니다.

### `remember`에 repository/client 저장하지 않기

```kotlin
val repository = remember { SessionRepository(...) }
```

DI로 조립할 객체를 UI 기억 장치에 넣으면 수명과 테스트 경계가 흐려집니다. Repository, HTTP client, DataStore, cipher 같은
dependency는 DI에서 만들고 주입하는 편이 맞습니다.

### `rememberSaveable`을 영구 저장소처럼 쓰지 않기

`rememberSaveable`은 UI 복원 장치입니다. sessionKey, auth token, 운동 기록, 측정 이력 같은 데이터는 DataStore나 Room에 저장해야
합니다.

### `by`를 상태 관리 도구로 오해하지 않기

`by`는 Kotlin 문법입니다. 상태를 관찰 가능하게 만드는 것은 `mutableStateOf`, `StateFlow`, `collectAsStateWithLifecycle`
같은 API입니다.

### Flutter BuildContext와 Android Context를 같은 것으로 보지 않기

Flutter의 `BuildContext`는 widget tree 안의 위치에 가깝고, Android의 `Context`는 앱/컴포넌트가 OS 리소스와 시스템 서비스에 접근하는
환경 핸들입니다.

Compose에서 Android `Context`가 필요하면 `LocalContext.current`를 사용하지만, Repository나 ViewModel에 오래 보관할 객체로
넘기는 것은 피하는 편이 좋습니다. 자세한
내용은 [[android-context|android_context.md]]를
참조하세요.

---

## 13. 판단 규칙

Compose 상태 위치는 다음 순서로 판단하면 됩니다.

```text
1. recomposition 동안만 유지되면 충분한가?
   -> remember

2. 화면 회전이나 프로세스 복원 후에도 작은 UI 값이 살아야 하는가?
   -> rememberSaveable

3. API 호출, validation, loading/error, screen policy가 있는가?
   -> ViewModel

4. 앱 재시작 후에도 남아야 하는 데이터인가?
   -> DataStore 또는 Room

5. 여러 feature가 알아야 하는 contract인가?
   -> api module에 interface/model

6. Android 저장소/네트워크/암호화 같은 실제 구현인가?
   -> impl module
```

Flutter식으로 요약하면 다음과 같습니다.

```text
setState로 충분한 로컬 UI 상태
-> remember / rememberSaveable

Riverpod/Cubit이 필요할 정도의 화면 상태
-> ViewModel + StateFlow

Bloc처럼 Event -> State 전이 규칙이 많아진 화면
-> ViewModel + 선택적 Reducer로 MVI에 가까운 구조 구성

SharedPreferences/secure storage/database에 넣을 데이터
-> DataStore / Room / Repository
```
