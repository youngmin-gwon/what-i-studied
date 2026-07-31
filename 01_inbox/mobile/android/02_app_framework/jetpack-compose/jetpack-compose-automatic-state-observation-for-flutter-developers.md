# Compose Automatic State Observation: Flutter 개발자 관점

이 문서는 Android Developers 영상
[A Compose State of Mind - Using Jetpack Compose's Automatic State Observation](https://www.youtube.com/watch?v=rmv2ug-wW4U)
의
핵심을 Flutter 개발자 관점에서 정리합니다.

이 문서의 범위는 `remember`, `mutableStateOf`, ViewModel API 사용법 자체가 아니라, Compose Runtime이 상태를 어떻게 관찰하고
recomposition 범위를 어떻게 결정하는지 이해하는 것입니다. API 선택은
[[jetpack-compose-state-management-flutter-comparison|compose_state_management_flutter_comparison.md]]와
[[jetpack-compose-state-lifetime-api-selection|compose_state_lifetime_api_guide.md]]를 기준으로 봅니다.

관련 공식 문서:

- [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model)
- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
- [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)

---

## 1. 이 영상의 핵심

Flutter에서는 보통 다음 흐름으로 생각합니다.

```text
setState()
-> 이 StatefulWidget 아래를 dirty로 표시
-> build() 재실행
```

Compose의 핵심은 조금 다릅니다.

```text
State 값 변경
-> 그 State를 읽었던 composition scope가 invalidation됨
-> 필요한 Composable 함수가 다시 실행될 수 있음
```

즉 Compose에서는 "어디에서 `setState()`를 호출했는가"보다 "어떤 Composable이 어떤 State를 읽었는가"가 더 중요합니다.

```text
UI = f(state)
```

Composable은 상태를 입력으로 받아 UI를 계산하는 함수이고, Compose Runtime은 그 함수 실행 중 발생한 state read를 기록합니다.

---

## 2. Flutter식 rebuild 사고와 Compose식 observation 사고

| 관점       | Flutter                                              | Compose                                                          |
|:---------|:-----------------------------------------------------|:-----------------------------------------------------------------|
| 갱신 시작점   | `setState()`, `notifyListeners()`, provider emission | `MutableState.value` 변경, `StateFlow` emission을 Compose State로 수집 |
| 갱신 범위 판단 | 개발자가 `StatefulWidget`, `Consumer`, `Selector` 경계로 조절 | Runtime이 State read 정보를 기반으로 invalidation scope 결정               |
| 상태 보관 위치 | `State`, Provider/Riverpod/Bloc, controller          | `remember`, state holder, ViewModel, Flow/StateFlow              |
| UI 함수    | `build()`                                            | `@Composable` 함수                                                 |
| 중요한 질문   | 어디를 rebuild할까?                                       | 이 Composable이 어떤 State를 읽는가?                                     |

Flutter의 `ref.watch(counterProvider)`나 `ValueListenableBuilder`는 "이 UI가 이 값을 보고 있다"는 구독 관계를 명시합니다.
Compose는 `state.value`를 읽는 행위 자체를 Runtime이 추적합니다.

---

## 3. State changes need to be tracked by Compose

일반 Kotlin 변수는 Compose가 관찰하지 못합니다.

```kotlin
@Composable
fun BadCounter() {
    var count = 0

    Button(onClick = { count += 1 }) {
        Text("$count")
    }
}
```

`count += 1`은 Kotlin 변수만 바꿉니다. Compose Runtime 입장에서는 어떤 observable state가 바뀌었는지 알 수 없고, 다음
recomposition에서
`count`는 다시 `0`으로 초기화될 수도 있습니다.

Compose가 추적할 수 있는 상태로 만들어야 합니다.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }

    Button(onClick = { count += 1 }) {
        Text("$count")
    }
}
```

여기서 중요한 점은 두 가지입니다.

- `mutableStateOf(0)`은 Compose가 관찰할 수 있는 `MutableState<Int>`를 만듭니다.
- `remember`는 이 state holder가 recomposition마다 새로 만들어지지 않게 Composition 안에 보관합니다.

Flutter로 비유하면 `MutableState<T>`는 `ValueNotifier<T>`에 가깝고, `remember`는 `State` 객체 없이 Element tree 안에
값을 보존하는
느낌에 가깝습니다.

---

## 4. Automatic State Observation의 실제 의미

다음 코드에서 `Header`와 `Footer`는 `userNameState.value`를 읽지 않습니다.

```kotlin
@Composable
fun ProfileScreen(
    userNameState: State<String>,
    cartCount: Int,
) {
    Column {
        Header(cartCount)
        UserName(userNameState)
        Footer()
    }
}

@Composable
fun UserName(userNameState: State<String>) {
    Text(userNameState.value)
}
```

`userNameState.value`를 `UserName` 내부에서만 읽는다면, Compose는 그 읽기 정보를 기반으로 다시 실행해야 할 범위를 좁힐 수 있습니다.

```text
Header
-> userNameState.value를 읽지 않음

UserName
-> userNameState.value를 읽음

Footer
-> userNameState.value를 읽지 않음
```

그래서 Compose에서 성능을 생각할 때는 "Composable이 자주 호출되면 안 된다"가 아니라 "상태 읽기를 어디에서 하는가"를 먼저 봐야 합니다.

다만 public reusable Composable에는 보통 `State<T>` 자체보다 plain value와 event callback을 넘기는 편이 좋습니다. 부모에서
`val userName by state`처럼 값을 이미 읽었다면 부모가 invalidation scope가 되고, 그 이후에는 안정적인 파라미터와 skipping 규칙이 실제
재실행 범위를 줄입니다.

---

## 5. `remember`는 캐시보다 Composition 저장공간에 가깝다

Flutter 개발자는 `remember`를 단순 memoization으로 이해하기 쉽습니다. 하지만 Compose에서 더 중요한 관점은
**Composition에 귀속된 저장공간**입니다.

```kotlin
@Composable
fun SearchBar() {
    var query by remember { mutableStateOf("") }

    TextField(
        value = query,
        onValueChange = { query = it },
    )
}
```

이 값은 `SearchBar`가 Composition에 남아 있는 동안 유지됩니다.

```text
recomposition
-> 유지

SearchBar가 composition에서 제거됨
-> 사라짐

Activity recreation/process death 복원
-> 기본 remember만으로는 보장하지 않음
```

화면 회전이나 process death 후에도 작은 UI 값을 복원해야 하면 `rememberSaveable`을 선택합니다. 화면 정책, API 결과, validation처럼
Composable보다 오래 살아야 하는 상태는 ViewModel이나 repository로 올립니다.

---

## 6. State Down, Events Up

Automatic state observation은 "상태를 아무 데나 둬도 된다"는 뜻이 아닙니다. Compose 코드는 여전히 단방향 데이터 흐름으로 설계해야 합니다.

```kotlin
@Composable
fun SearchBar(
    query: String,
    onQueryChange: (String) -> Unit,
) {
    TextField(
        value = query,
        onValueChange = onQueryChange,
    )
}
```

흐름은 다음처럼 잡습니다.

```text
State Down
-> 부모 또는 state holder가 현재 값을 내려준다

Events Up
-> 자식은 사용자의 의도를 callback으로 올린다
```

Flutter의 `TextField(controller: ...)`보다 Compose의 `value` + `onValueChange`는 상태 소유자를 더 명시적으로 드러냅니다.
Riverpod으로
비유하면 `Provider -> Widget -> Callback -> Notifier` 흐름과 가깝습니다.

---

## 7. State는 가장 낮은 공통 owner에 둔다

상태를 무조건 ViewModel로 올리는 것은 Flutter에서 모든 값을 전역 Provider로 만드는 것과 비슷한 안티패턴입니다.

```text
SearchBar 안에서만 쓰는 expanded/query
-> SearchBar 내부 remember 또는 rememberSaveable

SearchBar와 ResultList가 함께 알아야 하는 query
-> 둘의 가장 낮은 공통 parent로 hoist

검색 정책, debounce, API 호출, loading/error
-> ViewModel

앱 재시작 후에도 남아야 하는 검색 이력
-> Repository + DataStore/Room
```

Compose의 state hoisting은 "가능한 한 위로 올린다"가 아니라 "읽고 쓰는 범위의 가장 낮은 공통 owner로 올린다"에 가깝습니다.

---

## 8. ViewModel은 Composition보다 오래 사는 state holder다

Flutter 개발자가 ViewModel을 `StatefulWidget.State`처럼 이해하면 수명이 꼬입니다.

ViewModel은 Composition 밖에 있고, configuration change 후에도 유지됩니다. Flutter로 비유하면 화면 단위 Riverpod Notifier나
Bloc에
더 가깝습니다.

```kotlin
@Composable
fun ProfileRoute(
    viewModel: ProfileViewModel,
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    ProfileScreen(
        uiState = uiState,
        onRefresh = viewModel::refresh,
    )
}
```

이 구조에서 책임은 나뉩니다.

| 계층              | 책임                                        |
|:----------------|:------------------------------------------|
| `ProfileScreen` | 상태를 읽어 UI를 그림, 이벤트 callback 호출            |
| `ProfileRoute`  | ViewModel 상태를 Compose State로 수집하고 연결      |
| ViewModel       | 화면 정책, API 호출, repository 연동, UI state 생산 |
| Repository      | 데이터 source, 캐시, 저장소, 네트워크 경계              |

Composable은 ViewModel의 상태를 소비하지만, ViewModel은 `remember`로 만들거나 Composition 수명에 묶는 대상이 아닙니다.

---

## 9. 영상 흐름 기준 해설

정확한 타임코드보다 중요한 것은 발표자가 어떤 순서로 사고방식을 쌓는가입니다.

| 구간     | 발표 의도                             | Flutter 개발자에게 대응되는 감각                                             |
|:-------|:----------------------------------|:------------------------------------------------------------------|
| 0~3분   | 상태는 UI를 결정하는 값이다                  | `build()`는 현재 상태로 Widget tree를 계산한다                               |
| 3~6분   | Composable은 상태를 읽어 UI를 만든다        | `Widget` 클래스보다 `build()` 함수 자체에 더 가깝다                             |
| 6~10분  | Compose가 state read/write를 추적한다   | `ref.watch`, `ValueListenableBuilder` 같은 구독이 Runtime 안에 들어간 느낌    |
| 10~13분 | `mutableStateOf`로 변경을 관찰 가능하게 만든다 | 일반 `int` 변경은 rebuild를 만들지 않고, `ValueNotifier` 같은 observable이 필요하다 |
| 13~16분 | 필요한 곳만 recomposition할 수 있다        | `Consumer`, `Selector`를 잘게 나누는 목적을 Runtime이 더 세밀하게 수행한다           |
| 16~18분 | recomposition을 두려워하지 않는다          | `build()`가 자주 호출되어도 안전해야 한다는 Flutter 원칙과 같다                       |
| 18분 이후 | 상태 owner를 수명과 책임에 맞게 고른다          | 로컬 `State`, Provider/Riverpod/Bloc, repository를 구분하는 것과 같다        |

---

## 10. 실무 판단 규칙

Compose에서 상태 관련 코드를 볼 때는 다음 순서로 점검합니다.

```text
1. 이 값은 Compose가 관찰 가능한 State인가?

2. 이 값을 읽는 위치가 너무 높은가?

3. 이 상태는 composable과 같이 사라져도 되는가?

4. 화면 회전/process death 후 복원이 필요한 작은 UI 상태인가?

5. 화면 정책, API 호출, validation, loading/error가 섞였는가?

6. 앱 재시작 후에도 남아야 하는 데이터인가?
```

대응은 다음과 같습니다.

| 판단                            | 선택                              |
|:------------------------------|:--------------------------------|
| 한 Composable 안에서만 쓰는 임시 UI 상태 | `remember`                      |
| 작은 UI 복원 상태                   | `rememberSaveable`              |
| 여러 Composable이 공유하는 UI 상태     | 가장 낮은 공통 parent로 state hoisting |
| 화면 정책과 비동기 작업이 있는 상태          | ViewModel + `StateFlow`         |
| Compose State를 Flow로 다뤄야 함    | `snapshotFlow`                  |
| 영구 데이터                        | Repository + DataStore/Room     |

---

## 11. 한 문장 요약

Flutter에서는 "어디를 rebuild할까?"를 자주 고민하지만, Compose에서는 "어떤 상태를 어디에서 읽고, 그 상태의 owner가 누구인가?"를 먼저 고민합니다.

Compose Runtime은 state read를 자동으로 관찰하고, state write가 발생했을 때 그 정보를 바탕으로 필요한 recomposition을 예약합니다. 이
관점을
이해하면 `remember`, `mutableStateOf`, state hoisting, ViewModel, `StateFlow`가 서로 분리된 API가 아니라 하나의 상태 관찰
모델 위에
놓인 선택지로 보입니다.
