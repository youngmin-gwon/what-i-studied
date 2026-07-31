# State Down, Events Up

상위 노트: [jetpack-compose-automatic-state-observation-for-flutter-developers](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers.md)

Automatic state observation은 "상태를 아무 데나 둬도 된다"는 뜻이 아닙니다. Compose 코드는 여전히 단방향 데이터 흐름으로 설계해야 합니다.

```kotlin
@Composable
fun SearchBar(
    query: String,
    onQueryChange: (String) -> Unit,
) {
    TextField(
        value = query,
        onValueChange = onQueryChange,
    )
}
```

흐름은 다음처럼 잡습니다.

```text
State Down
-> 부모 또는 state holder가 현재 값을 내려준다

Events Up
-> 자식은 사용자의 의도를 callback으로 올린다
```

Flutter의 `TextField(controller: ...)`보다 Compose의 `value` + `onValueChange`는 상태 소유자를 더 명시적으로 드러냅니다.
Riverpod으로
비유하면 `Provider -> Widget -> Callback -> Notifier` 흐름과 가깝습니다.

---
