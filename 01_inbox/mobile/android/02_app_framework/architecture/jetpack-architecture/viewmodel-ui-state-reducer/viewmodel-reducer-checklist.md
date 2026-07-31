# 체크리스트

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

- UI가 `StateFlow<UiState>`를 읽고 있는가?
- mutable state holder는 ViewModel 내부에 숨겼는가?
- Composable body에서 API 호출이나 저장 작업을 직접 하지 않는가?
- 화면 상태와 일회성 이벤트를 구분했는가?
- 놓치면 안 되는 흐름을 event stream에만 넣지 않았는가?
- ViewModel이 `Context`, `NavController`, `SnackbarHostState` 같은 UI 객체를 장기 보관하지 않는가?
- 단순 화면에 Reducer, Action, Result, Processor를 과하게 만들지 않았는가?
- Reducer를 만들었다면 `oldState + action -> newState`만 담당하는가?
- Reducer 테스트가 Android/coroutine/Flow 없이 순수 JVM 테스트로 가능한가?
