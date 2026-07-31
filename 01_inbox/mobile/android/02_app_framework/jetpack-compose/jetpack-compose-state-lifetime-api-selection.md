# Compose State Lifetime & API 선택 가이드

이 문서는 Compose에서 상태나 작업을 **얼마나 오래 살릴지**에 따라 어떤 owner와 API를 선택해야 하는지 정리합니다.

핵심은 다음입니다.

```text
상태를 오래 살리고 싶다
-> 더 높은 owner로 hoist한다

상태를 같이 죽이고 싶다
-> 그 composable 안에서 remember/effect로 소유한다

navigation destination 수명에 묶고 싶다
-> entry-scoped ViewModel을 쓴다

앱/세션 수명에 묶고 싶다
-> root ViewModel, repository, DataStore/Room로 올린다
```

관련 공식 문서:

- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
- [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)
- [Lifecycle in Jetpack Compose](https://developer.android.com/topic/libraries/architecture/lifecycle)
- [Use Kotlin coroutines with lifecycle-aware components](https://developer.android.com/topic/libraries/architecture/coroutines)

---

## 1. 먼저 수명을 정한다

상태 관리 API를 고르기 전에 이 질문을 먼저 합니다.

```text
이 상태나 작업은 무엇과 같이 태어나고, 무엇과 같이 사라져야 하는가?
```

| 원하는 수명                            | 대표 owner/API                                                               | 예시                                        |
|:----------------------------------|:---------------------------------------------------------------------------|:------------------------------------------|
| recomposition 사이에만 유지             | `remember`                                                                 | password visible, expanded 여부             |
| composable이 composition에 있는 동안 유지 | `remember`, `LaunchedEffect`, `DisposableEffect`, `rememberCoroutineScope` | animation trigger, listener 등록, drawer 열기 |
| Activity 재생성/프로세스 복원까지 작은 값 유지    | `rememberSaveable`                                                         | 입력 draft, 선택 tab key, filter key          |
| navigation entry와 같이 유지           | entry-scoped `ViewModel`, `rememberSaveableStateHolderNavEntryDecorator()` | detail 화면 상태, 화면별 form state              |
| 여러 composable이 공유                 | 공통 parent로 state hoisting                                                  | parent layout이 관리하는 selected item         |
| 여러 destination/flow가 공유           | parent/root ViewModel, 명시적 shared ViewModel scope                          | auth flow state, main tab state           |
| 앱/세션 전체에서 유지                      | root ViewModel, Repository, DataStore, Room                                | session, app settings, cached entities    |
| 화면이 보이는 동안만 Flow 수집               | `collectAsStateWithLifecycle()`                                            | `StateFlow<UiState>` 구독                   |
| START/STOP에 맞춰 리소스 시작/정리          | `LifecycleStartEffect`, `repeatOnLifecycle`                                | 위치 업데이트, 센서, stream                       |
| RESUME/PAUSE에 맞춰 리소스 시작/정리        | `LifecycleResumeEffect`                                                    | camera preview, video playback            |

수명은 "어느 화면에 보이는가"보다 중요합니다. 같은 화면에 표시되어도 session 상태와 입력 form 상태의 owner는 다를 수 있습니다.

---

## 2. 하나의 Composable과 같이 사라져야 하는 상태

해당 composable 내부에서만 쓰고, composable이 제거되면 같이 사라져도 되는 상태는 `remember`가 가장 단순합니다.

```kotlin
@Composable
fun PasswordField() {
    var passwordVisible by remember {
        mutableStateOf(false)
    }

    IconButton(
        onClick = { passwordVisible = !passwordVisible }
    ) {
        // icon
    }
}
```

적합한 상태:

- tooltip expanded 여부
- password visibility
- 임시 pressed/selected UI 상태
- 화면 밖으로 나가면 의미 없는 animation toggle

주의할 점:

- `remember`는 process death 복원을 보장하지 않습니다.
- composable이 조건부 렌더링에서 빠지면 상태도 사라집니다.
- 여러 sibling이 함께 읽어야 하면 더 높은 parent로 올립니다.

---

## 3. Composable보다 오래 살아야 하는 작은 UI 복원 상태

화면 회전, Activity 재생성, process death 후에도 작은 UI 값이 복원되어야 하면 `rememberSaveable`을 씁니다.

```kotlin
@Composable
fun SearchHeader() {
    var query by rememberSaveable {
        mutableStateOf("")
    }

    TextField(
        value = query,
        onValueChange = { query = it },
    )
}
```

적합한 상태:

- 입력 draft
- 선택된 tab key
- filter enum/string
- 간단한 page id
- 작은 boolean/int/string 상태

부적합한 상태:

- repository, client, database
- bitmap, 큰 list, entity 전체 목록
- auth token, session key 같은 영구 보관 데이터
- 서버에서 다시 받아야 하는 큰 screen data

`rememberSaveable`은 저장소가 아니라 UI 복원 장치입니다. 앱을 껐다 켜도 의미 있게 남아야 하는 데이터는 DataStore/Room으로 내려야 합니다.

---

## 4. 비동기 작업이 Composable과 같이 취소되어야 할 때

composition 진입 시 시작하고, key가 바뀌거나 composable이 사라지면 취소되어야 하는 coroutine은 `LaunchedEffect`를 씁니다.

```kotlin
@Composable
fun ProductRoute(
    productId: String,
    viewModel: ProductViewModel,
) {
    LaunchedEffect(productId) {
        viewModel.load(productId)
    }
}
```

적합한 작업:

- 특정 key가 바뀔 때 ViewModel에 load 요청
- 일회성 event 수집 후 snackbar/navigation 처리
- animation 시작
- UI-local async 작업

주의할 점:

- Composable body에서 직접 `repository.load()`를 호출하지 않습니다.
- `LaunchedEffect(Unit)`은 해당 composition 생명 동안 한 번만 실행됩니다. 내부에서 쓰는 값이 바뀌어야 하면 key에 넣거나
  `rememberUpdatedState`를 씁니다.
- 화면 비즈니스 작업은 가능하면 ViewModel의 `viewModelScope`에서 처리하고, `LaunchedEffect`는 UI와 lifecycle에 묶인 트리거로 둡니다.

---

## 5. 이벤트 handler에서 coroutine이 필요할 때

버튼 클릭, drawer 열기, scroll animation처럼 event handler 내부에서 coroutine을 시작해야 하면`rememberCoroutineScope()`
를 씁니다.

```kotlin
@Composable
fun ScrollToTopButton(
    listState: LazyListState,
) {
    val scope = rememberCoroutineScope()

    Button(
        onClick = {
            scope.launch {
                listState.animateScrollToItem(0)
            }
        }
    ) {
        Text("Top")
    }
}
```

이 scope는 composable이 composition에서 제거되면 취소됩니다.

적합한 작업:

- `SnackbarHostState.showSnackbar()`
- `DrawerState.open()`
- `LazyListState.animateScrollToItem()`
- bottom sheet show/hide

장기 비즈니스 작업이나 저장 작업은 ViewModel로 올리는 편이 좋습니다.

---

## 6. 등록과 해제가 쌍이면 DisposableEffect

listener, observer, callback 등록처럼 반드시 정리해야 하는 작업은 `DisposableEffect`를 씁니다.

```kotlin
@Composable
fun LifecycleLogger(
    lifecycleOwner: LifecycleOwner,
) {
    DisposableEffect(lifecycleOwner) {
        val observer = LifecycleEventObserver { _, event ->
            // log event
        }

        lifecycleOwner.lifecycle.addObserver(observer)

        onDispose {
            lifecycleOwner.lifecycle.removeObserver(observer)
        }
    }
}
```

적합한 작업:

- listener 등록/해제
- sensor callback 등록/해제
- 외부 SDK attach/detach
- lifecycle observer 등록/해제

정리 작업이 필요 없다면 `LaunchedEffect`나 `SideEffect`가 더 맞을 수 있습니다.

---

## 7. 화면에 그릴 Flow는 collectAsStateWithLifecycle

Compose에서 `StateFlow<UiState>`를 화면에 그릴 상태로 읽을 때는 `collectAsStateWithLifecycle()`을 우선 사용합니다.

```kotlin
@Composable
fun ProfileRoute(
    viewModel: ProfileViewModel,
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    ProfileScreen(uiState = uiState)
}
```

이 API는 Flow를 lifecycle-aware하게 수집하고, 최신 값을 Compose `State`로 변환합니다. 화면이 보이지 않을 때 불필요한 수집을 줄이는 데 도움이
됩니다.

Compose에서 화면 상태를 읽기 위해 아래처럼 직접 수집하는 패턴은 대부분 피합니다.

```kotlin
LaunchedEffect(viewModel) {
    viewModel.uiState.collect { uiState ->
        // 화면 상태를 수동으로 반영
    }
}
```

화면에 그릴 상태라면 `collectAsStateWithLifecycle()`이 기본입니다. `LaunchedEffect`에서 collect하는 것은 snackbar,
navigation 같은 일회성 event를 처리할 때 더 적합합니다.

---

## 8. View system에서는 repeatOnLifecycle

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

## 9. START/STOP 또는 RESUME/PAUSE에 맞춘 작업

데이터를 화면에 그리기 위한 Flow 수집이 아니라, lifecycle 상태에 맞춰 외부 리소스를 시작/정리해야 하면 lifecycle-aware effect를 씁니다.

START/STOP에 맞춘 작업:

```kotlin
@Composable
fun LocationUpdates(
    locationClient: LocationClient,
) {
    LifecycleStartEffect(locationClient) {
        locationClient.start()

        onStopOrDispose {
            locationClient.stop()
        }
    }
}
```

RESUME/PAUSE에 맞춘 작업:

```kotlin
@Composable
fun CameraPreview(
    camera: CameraController,
) {
    LifecycleResumeEffect(camera) {
        camera.resume()

        onPauseOrDispose {
            camera.pause()
        }
    }
}
```

선택 기준:

- 화면이 보이는 동안만 필요하면 START/STOP
- 사용자가 실제로 상호작용 가능한 foreground 상태에서만 필요하면 RESUME/PAUSE
- 단순 화면 state Flow 수집이면 `collectAsStateWithLifecycle()`

---

## 10. Navigation entry 수명에 묶고 싶을 때

Navigation 3에서는 화면 destination 단위 수명에 `ViewModel`과 saveable state를 묶을 수 있습니다.

```kotlin
NavDisplay(
    backStack = backStack,
    entryDecorators = listOf(
        rememberSaveableStateHolderNavEntryDecorator(),
        rememberViewModelStoreNavEntryDecorator(),
    ),
    entryProvider = entryProvider {
        entry<TrainingDetailRoute> { route ->
            val viewModel = viewModel<TrainingDetailViewModel>()
            TrainingDetailScreen(
                trainingId = route.id,
                uiState = viewModel.uiState,
            )
        }
    },
)
```

의미:

- entry가 back stack에 남아 있으면 해당 entry의 ViewModel도 유지됩니다.
- entry가 back stack에서 제거되면 해당 ViewModel도 정리됩니다.
- `rememberSaveableStateHolderNavEntryDecorator()`는 entry별 saveable state를 보존합니다.
- `rememberViewModelStoreNavEntryDecorator()`는 entry별 `ViewModelStoreOwner`를 제공합니다.

이 구조는 detail 화면, form 화면, wizard 단계처럼 navigation destination 단위로 살아야 하는 상태에 적합합니다.

---

## 11. 하나의 Composable보다 오래, 앱 전체보다는 짧게

상태가 child composable보다 오래 살아야 하면 더 높은 owner로 올립니다.

```text
child composable 내부에서만 필요
-> child remember

screen 전체에서 필요
-> route/screen rememberSaveable 또는 screen ViewModel

navigation destination 동안 필요
-> entry-scoped ViewModel

tab/flow 전체에서 공유
-> parent composable state 또는 parent ViewModel

앱/세션 전체에서 공유
-> root ViewModel, repository, DataStore
```

예를 들어 sign-in 화면 안에서 password visibility는 field composable의 `remember`로 충분합니다. 반면 auth flow 전체에서 "
회원가입 중 선택한 약관/단계"를 공유해야 한다면 auth flow parent state나 shared ViewModel이 더 적합합니다.

---

## 12. 앱/세션 수명 상태

앱 전체나 세션 전체에서 의미 있는 상태는 특정 composable이나 screen ViewModel에 가두지 않습니다.

대표 예:

- 로그인 session
- app settings
- feature flag
- cached database entity
- user preference

권장 owner:

- Repository
- DataStore
- Room
- root ViewModel
- app/session observer

예를 들어 session 상태는 screen별 ViewModel이 각각 fetch하기보다 `SessionRepository` 또는 `SessionStateObserver`가
Flow를 제공하고, root/app ViewModel이 이를 `StateFlow`로 노출하는 편이 자연스럽습니다.

---

## 13. 선택 규칙

새 상태나 작업을 추가할 때 아래 순서로 판단합니다.

```text
1. recomposition 동안만 유지되면 충분한가?
   -> remember

2. composable이 사라지면 같이 취소/정리되어야 하나?
   -> LaunchedEffect / DisposableEffect / rememberCoroutineScope

3. Activity 재생성이나 process death 후 작은 UI 값이 복원되어야 하나?
   -> rememberSaveable

4. 화면에 그릴 Flow 상태인가?
   -> collectAsStateWithLifecycle

5. View system에서 Flow를 collect해 view를 직접 갱신하는가?
   -> lifecycleScope + repeatOnLifecycle

6. navigation destination과 같이 살아야 하나?
   -> entry-scoped ViewModel

7. 여러 composable/destination이 공유해야 하나?
   -> parent state holder 또는 shared ViewModel scope

8. 앱 재시작 후에도 남아야 하나?
   -> DataStore / Room / Repository
```

---

## 14. 흔한 실수

### Composable body에서 직접 side effect 실행

```kotlin
@Composable
fun BadScreen(repository: ProductRepository) {
    repository.refresh()
}
```

Composable body는 recomposition 때마다 다시 실행될 수 있습니다. side effect는 `LaunchedEffect`, ViewModel,
lifecycle-aware effect 중 적절한 owner로 옮깁니다.

### 화면 상태 Flow를 LaunchedEffect에서 수동 collect

```kotlin
LaunchedEffect(viewModel) {
    viewModel.uiState.collect {
        // 화면 state를 수동으로 반영
    }
}
```

Compose에서 화면에 그릴 state라면 `collectAsStateWithLifecycle()`을 씁니다.

### ViewModel에 UI controller 보관

```kotlin
class BadViewModel : ViewModel() {
    lateinit var snackbarHostState: SnackbarHostState
}
```

`SnackbarHostState`, `NavController`, `DrawerState`, `SheetState`, `FocusRequester` 같은 객체는 UI
controller/effect runner에 가깝습니다. ViewModel은 event나 state만 내보내고, 실행은 composable layer가 맡습니다.

### 모든 상태를 ViewModel로 올리기

password visibility, tooltip expanded처럼 composable 내부에서만 의미 있는 상태까지 ViewModel로 올리면 화면 구조가 불필요하게
무거워집니다.

```text
가장 낮은 공통 owner에 둔다.
필요할 때만 더 위로 올린다.
```

---

## 15. 관련 문서

- [[jetpack-compose-automatic-state-observation-for-flutter-developers|compose_automatic_state_observation_flutter_guide.md]]
- [[jetpack-compose-state-management-flutter-comparison|compose_state_management_flutter_comparison.md]]
- [[jetpack-compose-side-effects-and-lifecycle|compose_side_effects_and_lifecycle.md]]
- [[viewmodel-ui-state-reducer|viewmodel_ui_state_reducer_guide.md]]
- [[jetpack-navigation-3-guide|navigation_guide.md]]
- [[kotlin-coroutines-flow-stateflow|kotlin_coroutines_flow_stateflow.md]]
