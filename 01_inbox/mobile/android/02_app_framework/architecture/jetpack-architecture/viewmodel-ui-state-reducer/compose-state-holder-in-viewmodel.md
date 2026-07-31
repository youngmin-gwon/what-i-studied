# Compose State Holder를 ViewModel에 둬도 되는가

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

일반적인 UDF 설명만 보면 text field도 아래처럼 immutable `UiState`와 callback으로 다루고 싶어집니다.

```kotlin
data class LoginUiState(
    val id: String = "",
    val password: String = "",
)

TextField(
    value = uiState.id,
    onValueChange = viewModel::onIdChanged,
)
```

이 방식은 이해하기 쉽고 UDF 모양도 선명합니다. 하지만 Compose의 state-based text field는 `value/onValueChange` 대신 `TextFieldState`를
사용합니다.

```kotlin
class SignInViewModel : ViewModel() {
    val idState = TextFieldState()
    val passwordState = TextFieldState()
}

TextField(state = viewModel.idState)
SecureTextField(state = viewModel.passwordState)
```

이 구조는 strict한 `Immutable UiState -> UI -> callback -> ViewModel` 형태는 아닙니다. `TextFieldState` 자체가 mutable state holder이고,
text field가 그 객체를 직접 수정합니다. 하지만 이것이 곧 UDF를 깨는 구조라는 뜻은 아닙니다.

더 정확히는 다음처럼 봅니다.

```text
UDF의 예외
-> 아님

immutable UiState 모델의 예외
-> 맞음
```

ViewModel이 상태를 소유하고, UI가 그 상태를 읽어 렌더링하며, 사용자 입력이 그 상태를 갱신한다는 점에서는 여전히 단방향 데이터 흐름으로 이해할 수 있습니다.
다만 매 입력마다 `UiState(id = "...")` 같은 새 immutable 객체를 만드는 대신, `TextFieldState` 내부의 Compose Snapshot 상태가 변경됩니다.

Compose state-based text field에서 `TextFieldState`는 다음 성격을 가집니다.

- Composable 함수나 UI widget이 아니라 text input 전용 state holder입니다.
- text, selection, composition을 함께 관리합니다.
- keyboard/input pipeline과 동기화 문제를 줄이기 위해 만들어졌습니다.
- Compose snapshot state를 사용하므로 ViewModel이 Compose runtime 쪽 타입을 알게 됩니다.
- ViewModel에서 만들면 `rememberTextFieldState()`의 save/restore는 자동으로 받지 못하므로 필요한 경우 `SavedStateHandle` 등으로 복원을 직접 설계해야 합니다.

따라서 선택 기준은 다음입니다.

| 선택 | 적합한 경우 | 주의점 |
|:---|:---|:---|
| `UiState`에 `String`을 두고 value-based `TextField` 사용 | 단순 입력, strict UDF를 우선할 때 | 최신 state-based text field의 input 동기화 장점을 덜 활용 |
| `TextFieldState`를 Composable/route에 두고 ViewModel에 변경 통지 | text input state를 UI 수명에 묶고 싶을 때 | ViewModel의 state가 text field의 source of truth는 아님 |
| `TextFieldState`를 ViewModel에 둠 | text input state까지 screen ViewModel이 소유해야 할 때, `SecureTextField`/state-based API를 적극 사용할 때 | Compose snapshot 타입이 ViewModel에 들어오고, 저장/복원 설계를 별도로 고려 |

현재 `SignInViewModel`처럼 `TextFieldState`를 ViewModel에 두는 구조는 Compose state-based text field 관점에서는 허용 가능한 선택입니다. 다만
프로젝트 문서에서 말하는 일반 원칙, 즉 "`NavController`, `SnackbarHostState`, `FocusRequester` 같은 UI controller/effect runner는 ViewModel에
두지 않는다"와는 구분해야 합니다.

이 구조를 쓴다면 다음 규칙을 지킵니다.

- `TextFieldState`는 text input state holder로만 사용합니다.
- Repository, domain model, api module로 `TextFieldState`를 넘기지 않습니다.
- domain validation에는 `textFieldState.text.toString()`처럼 primitive 값만 넘깁니다.
- 화면 복원이 중요하면 `SavedStateHandle`이나 route-level `rememberTextFieldState()` 중 어디가 source of truth인지 명확히 정합니다.
- 팀이 strict immutable `UiState` UDF를 우선한다면 value-based `TextField` 또는 route-local `TextFieldState` + ViewModel callback 구조를 선택합니다.

Compose state holder라고 해서 모두 ViewModel에 넣어도 되는 것은 아닙니다. 기준은 그 객체가 **지속적인 UI state holder**인지, 아니면 **UI
controller/effect runner**인지입니다.

| 객체 | ViewModel 보관 | 이유 |
|:---|:---|:---|
| `TextFieldState` | 가능 | 지속되는 text input 상태입니다. text, selection, IME composition을 함께 관리합니다. |
| custom plain state holder | 가능 | 화면 정책을 표현하는 순수 state holder라면 ViewModel 또는 Composition 중 적절한 수명에 둘 수 있습니다. |
| `LazyListState` | 보통 UI layer | 대부분 스크롤 위치/제어 상태입니다. 마지막 읽은 위치처럼 제품 상태가 되면 별도 값으로 ViewModel에 올립니다. |
| `PagerState` | 경우에 따라 UI layer | pager 제어 상태에 가깝습니다. 현재 탭이 화면 정책이면 selected tab 값만 ViewModel에 둘 수 있습니다. |
| `SnackbarHostState` | 보통 두지 않음 | transient UI effect 실행기입니다. ViewModel은 snackbar message/event만 보내고 UI가 `showSnackbar()`를 실행합니다. |
| `SheetState`, `DrawerState` | 보통 두지 않음 | bottom sheet/drawer 표시와 animation을 제어하는 UI interaction controller입니다. |
| `FocusRequester` | 두지 않음 | focus 이동을 실행하는 UI controller입니다. |
| `NavController` | 두지 않음 | navigation 실행기입니다. ViewModel은 navigation 목적을 state/event로 표현하고 route/app layer가 처리합니다. |

예를 들어 snackbar는 ViewModel이 `SnackbarHostState`를 직접 들고 `showSnackbar()`를 호출하기보다, 일회성 event를 내보내고 Composable이 처리합니다.

```kotlin
sealed interface SaveEvent {
    data class ShowSnackbar(val message: String) : SaveEvent
}

LaunchedEffect(viewModel) {
    viewModel.events.collect { event ->
        when (event) {
            is SaveEvent.ShowSnackbar -> snackbarHostState.showSnackbar(event.message)
        }
    }
}
```

반대로 `TextFieldState`는 snackbar처럼 "한 번 실행하고 사라지는 effect"가 아니라 현재 입력 필드의 지속적인 상태입니다. 이 차이 때문에
`TextFieldState`는 ViewModel 보관이 가능하고, `SnackbarHostState`는 보통 UI layer에 두는 편이 맞습니다.

---
