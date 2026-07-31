# Scene과 기본 제공 Strategy

상위 노트: [jetpack-navigation-3-guide](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide.md)

`Scene`은 하나 이상의 `NavEntry`를 표시하는 단위입니다. `NavDisplay`는 `sceneStrategies`를 순서대로 평가하고, 어떤 strategy도 scene을 만들지 못하면 single-pane scene으로 fallback합니다.

| Strategy | Artifact | 역할 | 사용 방식 |
|:---|:---|:---|:---|
| `SinglePaneSceneStrategy` | `androidx.navigation3:navigation3-ui` | 마지막 `NavEntry` 하나만 표시하는 기본 single-pane scene | 보통 직접 넣지 않아도 `NavDisplay`가 fallback으로 사용 |
| `DialogSceneStrategy` | `androidx.navigation3:navigation3-ui` | metadata가 붙은 destination을 dialog overlay scene으로 표시 | `sceneStrategies = listOf(DialogSceneStrategy())`, entry metadata에 `DialogSceneStrategy.dialog(...)` 지정 |
| `ListDetailSceneStrategy` | `androidx.compose.material3.adaptive:adaptive-navigation3` | list/detail/extra pane을 화면 폭과 device state에 맞춰 1~3 pane으로 표시 | `rememberListDetailSceneStrategy()`, metadata에 `listPane()`, `detailPane()`, `extraPane()` 지정 |
| `SupportingPaneSceneStrategy` | `androidx.compose.material3.adaptive:adaptive-navigation3` | main pane 옆에 supporting/extra pane을 adaptive하게 표시 | `rememberSupportingPaneSceneStrategy()`, metadata에 `mainPane()`, `supportingPane()`, `extraPane()` 지정 |

예시:

```kotlin
val dialogStrategy = remember { DialogSceneStrategy<NavKey>() }
val listDetailStrategy = rememberListDetailSceneStrategy<NavKey>()

NavDisplay(
    backStack = backStack,
    onBack = { backStack.removeLastOrNull() },
    sceneStrategies = listOf(
        dialogStrategy,
        listDetailStrategy,
    ),
    entryProvider = appEntryProvider(backStack),
)
```

판단 기준:

- 단순 push/pop 화면이면 custom scene이 필요 없습니다.
- dialog route가 있으면 `DialogSceneStrategy`를 추가합니다.
- list-detail, supporting pane은 직접 layout을 만들기 전에 Material adaptive strategy를 먼저 검토합니다.
- 공식 recipe의 `TwoPaneSceneStrategy`, `BottomSheetSceneStrategy`는 custom strategy 예시입니다. 현재 프로젝트 artifact의 기본 제공 class로 취급하지 않습니다.
- overlay 성격 strategy는 일반 multi-pane strategy보다 앞쪽에 두는 편이 안전합니다.

---
