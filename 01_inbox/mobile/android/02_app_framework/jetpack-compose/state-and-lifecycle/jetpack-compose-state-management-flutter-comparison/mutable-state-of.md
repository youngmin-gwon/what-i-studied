# `mutableStateOf`

상위 노트: [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)

`mutableStateOf`는 Compose가 관찰할 수 있는 상태 객체를 만듭니다.

```kotlin
val countState = remember { mutableStateOf(0) }

Text(text = "${countState.value}")

Button(onClick = { countState.value += 1 }) {
    Text("Increase")
}
```

`countState.value`를 읽은 Composable은 그 값이 바뀌면 recomposition 대상이 됩니다.

일반 Kotlin 변수는 Compose가 관찰하지 못합니다.

```kotlin
@Composable
fun WrongCounter() {
    var count = 0

    Button(onClick = { count += 1 }) {
        Text(text = "$count")
    }
}
```

이 코드는 클릭해도 UI가 기대대로 갱신되지 않습니다. 값 변경을 Compose runtime이 알 수 없고, recomposition이 일어나면 `count`가 다시 `0`으로
만들어질 수 있습니다.

---
