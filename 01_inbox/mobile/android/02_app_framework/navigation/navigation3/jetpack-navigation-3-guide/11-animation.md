# Animation

상위 노트: [jetpack-navigation-3-guide](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide.md)

`NavDisplay`는 scene class와 `Scene.key`에서 파생된 key가 바뀔 때 transition을 실행합니다.

전역 animation:

```kotlin
NavDisplay(
    backStack = backStack,
    transitionSpec = {
        slideInHorizontally { it } togetherWith slideOutHorizontally { -it }
    },
    popTransitionSpec = {
        slideInHorizontally { -it } togetherWith slideOutHorizontally { it }
    },
    predictivePopTransitionSpec = {
        slideInHorizontally { -it } togetherWith slideOutHorizontally { it }
    },
    entryProvider = appEntryProvider(backStack),
)
```

화면별 animation은 metadata로 override합니다.

```kotlin
entry<TrainingDetailRoute>(
    metadata = metadata {
        put(NavDisplay.TransitionKey) {
            fadeIn() togetherWith fadeOut()
        }
    }
) { route ->
    TrainingDetailScreen(trainingId = route.id)
}
```

custom scene 사이에서 같은 entry가 다른 scene으로 이동하는 경우에는 `SharedTransitionLayout`으로 `NavDisplay`를 감싸고 `sharedTransitionScope`를 넘기는 방식을 검토합니다.

---
