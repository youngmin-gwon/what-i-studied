# 하나의 Composable과 같이 사라져야 하는 상태

상위 노트: [jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)

해당 composable 내부에서만 쓰고, composable이 제거되면 같이 사라져도 되는 상태는 `remember`가 가장 단순합니다.

```kotlin
@Composable
fun PasswordField() {
    var passwordVisible by remember {
        mutableStateOf(false)
    }

    IconButton(
        onClick = { passwordVisible = !passwordVisible }
    ) {
        // icon
    }
}
```

적합한 상태:

- tooltip expanded 여부
- password visibility
- 임시 pressed/selected UI 상태
- 화면 밖으로 나가면 의미 없는 animation toggle

주의할 점:

- `remember`는 process death 복원을 보장하지 않습니다.
- composable이 조건부 렌더링에서 빠지면 상태도 사라집니다.
- 여러 sibling이 함께 읽어야 하면 더 높은 parent로 올립니다.

---
