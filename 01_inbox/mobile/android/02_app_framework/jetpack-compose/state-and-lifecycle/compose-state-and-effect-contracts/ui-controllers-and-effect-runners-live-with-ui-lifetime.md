---
title: ui-controllers-and-effect-runners-live-with-ui-lifetime
tags: ["android", "android/app-framework"]
aliases: [State Holder Boundary, UI Controller Lifetime]
date modified: 2026-08-05 18:58:24 +09:00
date created: 2026-07-31 16:53:16 +09:00
---

## UI controller 와 effect runner 는 [viewmodel](../../../viewmodel.md) 이 아니라 UI 수명에 둔다

### 1. 개념 정의 (What)

**UI 컨트롤러 수명주기 격리 원칙(UI State Holder & Controller Boundary)**이란 화면의 레이아웃 조작 객체(`LazyListState`, `ScrollState`, `DrawerState`, `AnimationController`, `FocusRequester` 등)와 UI 기반 이펙트 구동자를 AAC `ViewModel` 에 보관하지 않고, **Composition 트리의 수명주기(UI Lifetime)에 철저히 바인딩하여 배치해야 한다는 아키텍처 경계 규약**이다.

---

### 2. UI 컨트롤러와 ViewModel 분리의 필요성 (Why)

많은 안드로이드 개발자들이 ViewModel 에 모든 상태를 몰아넣는 과정에서 UI 컨트롤러 객체(`LazyListState` 등)를 ViewModel 에 필드로 정의하는 실수를 범한다.

이 경우 다음과 같은 중대한 위험이 일어난다:

- **메모리 누수(Memory Leak)**: UI 컨트롤러 객체는 내부적으로 Android UI Context, Canvas, 또는 View 트리 노드 지표를 직접/간접 참조한다. Activity 회전 시 ViewModel 이 이들을 계속 붙들고 있으면 메모리 누수가 발생한다.
- **다중 UI 렌더링 파괴**: 동일한 ViewModel 을 수평형 대화면(Folderable / Tablet)에서 2 개의 Composable UI 노드가 동시에 구독할 때, 단일 컨트롤러 객체를 공유하므로 레이아웃 상태가 꼬이거나 무한 루프가 발생한다.

UI 세부 레이아웃 컨트롤러는 UI 계층(Composition Tree)에 두고, ViewModel 은 도메인 비즈니스 데이터 및 순수 화면 상태(Screen State)만 다루어야 한다.

---

### 3. 영역 분리 레이어 메커니즘 (How)

```mermaid
graph TD
    subgraph UI["Composition / UI Layer"]
        A["State Holders: LazyListState, DrawerState, AnimationState<br/>수명주기: UI Lifetime (rememberLazyListState)<br/>역할: 픽셀 스크롤 좌표, 애니메이션 틱, 포커스 제어"]
    end

    subgraph VM["ViewModel / Domain Layer"]
        B"State Holders: [stateflow&lt;ScreenUiState&gt;<br/>수명주기: Screen / Activity Navigation Lifetime<br/>역할: 서버 데이터 연동, 비즈니스 검증, 도메인 변환"]
    end

    A -->|"Pure UI Events / Screen State"| B
```

---

### 4. 올바른 UI 컨트롤러 및 ViewModel 상태 분리 예제

```kotlin
// ❌ 안티패턴: ViewModel 내부에서 UI 레이아웃 컨트롤러 보유
class BadSearchViewModel : ViewModel() {
    val listState = LazyListState() // 메모리 누수 및 UI 수명주기 위반!
}

// ✅ 올바른 패턴: 역할의 명확한 분리
data class SearchUiState(
    val items: List<String> = emptyList(),
    val isLoading: Boolean = false
)

@HiltViewModel
class GoodSearchViewModel @Inject constructor(
    private val repository: SearchRepository
) : ViewModel() {
    // ViewModel 은 순수 비즈니스 Screen State 만 소유
    val uiState: StateFlow<SearchUiState> = repository.getSearchResults()
        .map { SearchUiState(items = it) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), SearchUiState())
}

@Composable
fun SearchScreen(viewModel: GoodSearchViewModel = hiltViewModel()) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    // ✅ UI 레이아웃 컨트롤러는 Composition 수명(UI Lifetime)에 둔다
    val listState = rememberLazyListState()

    LazyColumn(state = listState) {
        items(uiState.items) { item ->
            Text(item)
        }
    }
}
```

---

상위 문서: [Compose 상태와 Effect 계약](./compose-state-and-effect-contracts.md)

관련 노트: [Compose 상태 API는 필요한 수명에 맞춰 선택한다](./compose-state-api-selection-by-lifetime.md), [ViewModel의 StateFlow는 collectAsStateWithLifecycle로 화면 상태로 변환한다](./viewmodel-stateflow-becomes-screen-state-with-lifecycle-collection.md)

출처: [State holders and UI State](https://developer.android.com/topic/architecture/ui-layer/stateholders)

검증일: 2026-08-05. 안드로이드 권장 아키텍처 가이드의 State Holders 단락을 대조하여 UI Controller 와 ViewModel 간의 레이어 경계, 메모리 누수 방지 및 UI Lifetime 바인딩 규약 서술을 정밀 보강했다.
