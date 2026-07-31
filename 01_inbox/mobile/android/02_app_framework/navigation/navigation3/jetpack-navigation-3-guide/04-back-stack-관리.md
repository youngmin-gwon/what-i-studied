# Back Stack 관리

상위 노트: [[jetpack-navigation-3-guide]]

가장 단순한 형태는 시작 route 하나로 `rememberNavBackStack()`을 만드는 방식입니다.

```kotlin
val backStack = rememberNavBackStack(DashboardRoute)

NavDisplay(
    backStack = backStack,
    onBack = { backStack.removeLastOrNull() },
    entryProvider = appEntryProvider(backStack),
)
```

자주 쓰는 조작은 helper로 감싸는 편이 안전합니다.

```kotlin
fun NavBackStack<NavKey>.replaceAll(route: NavKey) {
    clear()
    add(route)
}

fun NavBackStack<NavKey>.replaceTopLevel(route: MainFeatureTopLevelRoute) {
    clear()
    add(route)
}

fun NavBackStack<NavKey>.openTrainingDetail(id: String) {
    removeIf { it is TrainingDetailRoute }
    add(TrainingDetailRoute(id))
}
```

로그인 후 main 영역은 top-level destination별 back stack을 따로 유지하는 편이 좋습니다. 탭을 바꿀 때 stack을 매번 지우면 각 탭의 detail state가 사라집니다.

```text
Dashboard stack:
DashboardRoute

Training stack:
TrainingRoute -> TrainingDetailRoute(id)

Settings stack:
SettingsRoute -> AccountSettingsRoute
```

---
