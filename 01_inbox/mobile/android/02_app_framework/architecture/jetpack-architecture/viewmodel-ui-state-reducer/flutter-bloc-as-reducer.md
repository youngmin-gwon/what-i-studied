# Flutter Bloc을 Reducer 관점에서 다시 보면

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

앞에서는 Bloc을 Android ViewModel과 역할 관점에서 비교했습니다. 하지만 패턴 관점에서 Bloc은 MVVM보다 MVI/Redux 계열에 가깝습니다. Reducer까지
도입한 Android 구조를 Flutter Bloc 경험으로 다시 풀면 다음 대응이 더 정확합니다.

| Flutter Bloc  | Android ViewModel 구조       |
|:--------------|:---------------------------|
| `Event`       | `UiAction` 또는 ViewModel 함수 |
| `Bloc`        | `ViewModel + Reducer`      |
| `emit(State)` | `_uiState.update { ... }`  |
| `State`       | `UiState`                  |

차이는 책임 분리입니다.

Flutter Bloc은 보통 event 처리, async 작업, state emit을 한 클래스에서 처리합니다.

```text
Event
 -> Bloc
 -> emit(Loading)
 -> Repository call
 -> emit(Success)
```

Android의 `ViewModel + Reducer` 구조에서는 async 작업은 ViewModel이 맡고, 상태 전이 계산은 Reducer가 맡습니다.

```text
UiAction
 -> ViewModel
 -> Repository call
 -> Reducer
 -> UiState
```

그래서 Reducer를 "Bloc 자체"로 보면 안 됩니다. Android에서 Bloc에 가장 가까운 덩어리는 `ViewModel + Reducer`이고, Reducer는 그중
**state transition**만 떼어낸 작은 순수 함수입니다.

---
