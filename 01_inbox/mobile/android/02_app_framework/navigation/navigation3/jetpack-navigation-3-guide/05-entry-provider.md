# Entry Provider

상위 노트: [jetpack-navigation-3-guide](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide.md)

`entryProvider`는 route key를 실제 화면으로 바꾸는 registry입니다. feature module 경계를 유지하려면 각 feature가 자기 route entry를 제공하고 app layer에서 합치는 구조가 적합합니다.

```kotlin
fun appEntryProvider(
    backStack: NavBackStack<NavKey>,
) = entryProvider {
    entry<DashboardRoute> {
        DashboardScreen()
    }

    entry<TrainingRoute>(
        metadata = ListDetailSceneStrategy.listPane()
    ) {
        TrainingListScreen(
            onTrainingClick = { id -> backStack.openTrainingDetail(id) },
        )
    }

    entry<TrainingDetailRoute>(
        metadata = ListDetailSceneStrategy.detailPane()
    ) { route ->
        TrainingDetailScreen(trainingId = route.id)
    }
}
```

실무 기준:

- route key 타입과 screen 함수 인자를 일대일로 맞춥니다.
- navigation callback은 screen 내부에서 직접 stack을 만지기보다 route-level composable이 주입합니다.
- metadata는 화면 content가 아니라 container가 화면을 어떻게 다룰지 알려주는 정보로 사용합니다.

---
