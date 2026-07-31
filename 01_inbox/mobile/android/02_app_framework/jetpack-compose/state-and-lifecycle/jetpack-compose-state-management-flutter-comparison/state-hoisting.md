# State hoisting

상위 노트: [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)

Compose에서는 상태를 가능하면 필요한 곳까지 끌어올립니다. 이를 **state hoisting**이라고 합니다.

상태를 가진 Composable:

```kotlin
@Composable
fun SearchBox() {
    var query by rememberSaveable { mutableStateOf("") }

    TextField(
        value = query,
        onValueChange = { query = it },
    )
}
```

상태를 밖으로 올린 Composable:

```kotlin
@Composable
fun SearchBox(
    query: String,
    onQueryChange: (String) -> Unit,
) {
    TextField(
        value = query,
        onValueChange = onQueryChange,
    )
}
```

두 번째 형태가 더 재사용하기 쉽고 테스트하기 쉽습니다.

Compose의 기본 흐름은 다음과 같습니다.

```text
state down
events up
```

즉 부모는 상태를 내려주고, 자식은 이벤트를 올립니다.

Flutter의 `value` + `onChanged` 패턴과 거의 같습니다.

---
