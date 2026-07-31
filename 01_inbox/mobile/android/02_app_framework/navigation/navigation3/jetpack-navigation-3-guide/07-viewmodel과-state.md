# ViewModel과 State

상위 노트: [[jetpack-navigation-3-guide]]

Navigation 3에서 ViewModel scope는 `NavEntry` 단위로 잡는 것이 기본적으로 가장 예측 가능합니다. 화면이 back stack에서 제거되면 해당 entry의 ViewModel도 정리됩니다.

이 섹션은 Navigation과 ViewModel scope의 연결만 다룹니다. 수명별 state/effect owner 선택은 [[jetpack-compose-state-lifetime-api-selection]]를, ViewModel이 `UiState`, user action, 일회성 이벤트, Reducer를 어떻게 다룰지는 [[viewmodel-ui-state-reducer]]를 참조하세요.

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
                state = viewModel.state,
            )
        }
    },
)
```

인자 전달 원칙:

- screen 복원에 필요한 값은 `NavKey`에 둡니다.
- ViewModel은 `NavKey`에서 받은 id로 repository 데이터를 조회합니다.
- 여러 화면이 공유해야 하는 상태는 parent composable 또는 명시적인 shared ViewModel scope를 둡니다.

---
