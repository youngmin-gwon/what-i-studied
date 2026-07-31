# Automatic State Observation의 실제 의미

상위 노트: [[jetpack-compose-automatic-state-observation-for-flutter-developers]]

다음 코드에서 `Header`와 `Footer`는 `userNameState.value`를 읽지 않습니다.

```kotlin
@Composable
fun ProfileScreen(
    userNameState: State<String>,
    cartCount: Int,
) {
    Column {
        Header(cartCount)
        UserName(userNameState)
        Footer()
    }
}

@Composable
fun UserName(userNameState: State<String>) {
    Text(userNameState.value)
}
```

`userNameState.value`를 `UserName` 내부에서만 읽는다면, Compose는 그 읽기 정보를 기반으로 다시 실행해야 할 범위를 좁힐 수 있습니다.

```text
Header
-> userNameState.value를 읽지 않음

UserName
-> userNameState.value를 읽음

Footer
-> userNameState.value를 읽지 않음
```

그래서 Compose에서 성능을 생각할 때는 "Composable이 자주 호출되면 안 된다"가 아니라 "상태 읽기를 어디에서 하는가"를 먼저 봐야 합니다.

다만 public reusable Composable에는 보통 `State<T>` 자체보다 plain value와 event callback을 넘기는 편이 좋습니다. 부모에서
`val userName by state`처럼 값을 이미 읽었다면 부모가 invalidation scope가 되고, 그 이후에는 안정적인 파라미터와 skipping 규칙이 실제
재실행 범위를 줄입니다.

---
