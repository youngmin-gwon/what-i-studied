# State changes need to be tracked by Compose

상위 노트: [[jetpack-compose-automatic-state-observation-for-flutter-developers]]

일반 Kotlin 변수는 Compose가 관찰하지 못합니다.

```kotlin
@Composable
fun BadCounter() {
    var count = 0

    Button(onClick = { count += 1 }) {
        Text("$count")
    }
}
```

`count += 1`은 Kotlin 변수만 바꿉니다. Compose Runtime 입장에서는 어떤 observable state가 바뀌었는지 알 수 없고, 다음
recomposition에서
`count`는 다시 `0`으로 초기화될 수도 있습니다.

Compose가 추적할 수 있는 상태로 만들어야 합니다.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }

    Button(onClick = { count += 1 }) {
        Text("$count")
    }
}
```

여기서 중요한 점은 두 가지입니다.

- `mutableStateOf(0)`은 Compose가 관찰할 수 있는 `MutableState<Int>`를 만듭니다.
- `remember`는 이 state holder가 recomposition마다 새로 만들어지지 않게 Composition 안에 보관합니다.

Flutter로 비유하면 `MutableState<T>`는 `ValueNotifier<T>`에 가깝고, `remember`는 `State` 객체 없이 Element tree 안에
값을 보존하는
느낌에 가깝습니다.

---
