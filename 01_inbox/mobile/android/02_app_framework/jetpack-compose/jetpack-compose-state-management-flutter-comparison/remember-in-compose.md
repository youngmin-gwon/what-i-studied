# `remember`

상위 노트: [[jetpack-compose-state-management-flutter-comparison]]

`remember`는 Composable이 recomposition되더라도 값을 유지하게 해줍니다.

```kotlin
@Composable
fun SearchBox() {
    var query by remember { mutableStateOf("") }

    TextField(
        value = query,
        onValueChange = { query = it },
    )
}
```

`remember`의 수명은 **Composition에 남아 있는 동안**입니다.

```text
recomposition: 유지됨
화면 회전으로 Activity 재생성: 기본적으로 사라짐
프로세스 종료 후 복원: 사라짐
해당 Composable이 화면에서 제거됨: 사라짐
```

### key가 있는 `remember`

`remember`는 key를 받을 수 있습니다.

```kotlin
val formatter = remember(locale) {
    DateTimeFormatter.ofPattern("yyyy.MM.dd", locale)
}
```

`locale`이 같으면 기존 값을 재사용하고, `locale`이 바뀌면 block을 다시 실행해 새 값을 만듭니다.

이 패턴은 "이 값은 특정 입력이 바뀔 때만 다시 계산되어야 한다"는 뜻을 코드에 남깁니다.

---
