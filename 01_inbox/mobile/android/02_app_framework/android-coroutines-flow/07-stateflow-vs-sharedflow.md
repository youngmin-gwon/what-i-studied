# StateFlow vs SharedFlow

상위 노트: [[android-coroutines-flow]]

| 특성 | StateFlow | SharedFlow |
|------|-----------|------------|
| 초기값 | **필수** | 불필요 |
| 최신 값 보관 | `.value` 로 즉시 접근 | `replay` 설정 시 |
| 동일 값 방출 | **무시** (distinctUntilChanged) | 허용 |
| 구독자 없을 때 | 값 유지 | 설정에 따라 |
| **용도** | **UI 상태** (Loading, Success, Error) | **이벤트** (토스트, 네비게이션) |

```kotlin
class UserViewModel : ViewModel() {
    // ✅ UI 상태: StateFlow
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
    
    // ✅ 일회성 이벤트: SharedFlow 또는 Channel
    private val _events = MutableSharedFlow<UiEvent>()
    val events: SharedFlow<UiEvent> = _events.asSharedFlow()
    
    // Channel 방식 (이벤트가 반드시 소비되어야 할 때)
    private val _navEvents = Channel<NavEvent>()
    val navEvents = _navEvents.receiveAsFlow()
    
    fun navigateToDetail(id: String) {
        viewModelScope.launch {
            _navEvents.send(NavEvent.GoToDetail(id))
        }
    }
}
```
