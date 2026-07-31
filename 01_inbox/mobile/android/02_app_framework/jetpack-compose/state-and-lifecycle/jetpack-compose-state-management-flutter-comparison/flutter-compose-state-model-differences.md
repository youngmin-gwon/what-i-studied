# Flutter와 Compose의 큰 차이

상위 노트: [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)

| 관점           | Flutter                                  | Jetpack Compose                             |
|:-------------|:-----------------------------------------|:--------------------------------------------|
| UI 선언        | `Widget build(BuildContext context)`     | `@Composable fun Screen()`                  |
| 로컬 상태        | `StatefulWidget` + `State`               | `remember { mutableStateOf(...) }`          |
| 상태 변경        | `setState { ... }`                       | `state.value = ...` 또는 `var value by state` |
| 다시 그리기       | `build()` 재실행                            | recomposition                               |
| 화면 단위 상태     | Provider, Riverpod, Bloc, Cubit 등        | ViewModel + StateFlow/Flow                  |
| 암묵적 의존성 전달   | InheritedWidget, Provider context lookup | CompositionLocal                            |
| 복원 가능한 UI 상태 | RestorationMixin, PageStorage 등          | `rememberSaveable`, `SavedStateHandle`      |

Compose는 Flutter처럼 선언형 UI입니다. 하지만 Flutter의 `StatefulWidget`처럼 클래스를 나누지 않고, 함수 안에서 `remember`로
Composition에 값을 저장합니다.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }

    Button(onClick = { count += 1 }) {
        Text(text = "$count")
    }
}
```

위 코드는 Flutter로 치면 `StatefulWidget` 안의 `int count`와 `setState`에 가까운 로컬 UI 상태입니다.

---
