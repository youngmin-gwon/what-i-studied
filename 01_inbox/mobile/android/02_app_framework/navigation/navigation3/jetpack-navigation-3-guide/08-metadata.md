# Metadata

상위 노트: [jetpack-navigation-3-guide](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide.md)

metadata는 `NavEntry`, `Scene`, `NavDisplay`, `SceneStrategy` 사이에서 화면 표시 정책을 전달하는 typed map입니다.

```kotlin
entry<FilterRoute>(
    metadata = DialogSceneStrategy.dialog(
        DialogProperties(windowTitle = "Filter")
    ) + metadata {
        put(NavDisplay.TransitionKey) {
            fadeIn() togetherWith fadeOut()
        }
    }
) {
    FilterScreen()
}
```

직접 metadata key를 만들 때는 값을 읽는 컴포넌트 안에 nested object로 둡니다.

```kotlin
class RequiresChromeSceneDecorator<T : Any> : SceneDecoratorStrategy<T> {
    object ChromeKey : NavMetadataKey<Boolean>

    override fun SceneDecoratorStrategyScope<T>.decorateScene(
        scene: Scene<T>,
    ): Scene<T> {
        return if (scene.metadata[ChromeKey] == false) {
            scene
        } else {
            ChromeScene(scene)
        }
    }
}
```

metadata 사용처:

- 화면별 transition override
- dialog, list pane, detail pane 같은 scene strategy hint
- scene decorator가 top app bar, bottom navigation, chrome 표시 여부를 판단하는 hint

자세한 Kotlin 문법과 metadata DSL은 [navigation-3-metadata-kotlin-syntax](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation-3-metadata-kotlin-syntax.md)를 함께 봅니다.

---
