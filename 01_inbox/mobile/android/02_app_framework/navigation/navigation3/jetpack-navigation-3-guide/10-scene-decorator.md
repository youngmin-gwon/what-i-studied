# Scene Decorator

상위 노트: [jetpack-navigation-3-guide](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide.md)

`SceneStrategy`가 "어떤 scene을 만들지" 결정한다면, `SceneDecoratorStrategy`는 "계산된 scene을 어떤 공통 UI로 감쌀지" 결정합니다.

사용 예:

- top-level destination에 top app bar 추가
- compact/expanded 조건에 따라 navigation chrome 추가
- 특정 route에서는 app chrome 숨김
- scene class와 key를 유지하면서 공통 wrapper 적용

```kotlin
NavDisplay(
    backStack = backStack,
    sceneDecoratorStrategies = listOf(
        remember { AppChromeSceneDecorator() },
    ),
    entryProvider = appEntryProvider(backStack),
)
```

주의할 점:

- `OverlayScene`은 별도 window에 렌더링되므로 `NavDisplay`가 decorate하지 않습니다.
- decorator가 scene key를 단순 복사하면 scene class 변화에 따른 animation이 막힐 수 있습니다.
- 첫 decorator에서 `scene::class to scene.key`처럼 원본 scene 정보를 반영한 key를 만드는 패턴이 안전합니다.

---
