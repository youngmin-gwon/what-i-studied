# 등록과 해제가 쌍이면 DisposableEffect

상위 노트: [[jetpack-compose-state-lifetime-api-selection]]

listener, observer, callback 등록처럼 반드시 정리해야 하는 작업은 `DisposableEffect`를 씁니다.

```kotlin
@Composable
fun LifecycleLogger(
    lifecycleOwner: LifecycleOwner,
) {
    DisposableEffect(lifecycleOwner) {
        val observer = LifecycleEventObserver { _, event ->
            // log event
        }

        lifecycleOwner.lifecycle.addObserver(observer)

        onDispose {
            lifecycleOwner.lifecycle.removeObserver(observer)
        }
    }
}
```

적합한 작업:

- listener 등록/해제
- sensor callback 등록/해제
- 외부 SDK attach/detach
- lifecycle observer 등록/해제

정리 작업이 필요 없다면 `LaunchedEffect`나 `SideEffect`가 더 맞을 수 있습니다.

---
