# Navigation entry 수명에 묶고 싶을 때

상위 노트: [[jetpack-compose-state-lifetime-api-selection]]

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
