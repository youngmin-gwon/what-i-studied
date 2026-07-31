# `LaunchedEffect` (코루틴 기반 비동기 작업)

* **목적**: Composable의 수명 주기에 맞춰 코루틴을 실행합니다.
* **동작**: Composition이 시작될 때 코루틴 블록을 실행하고, 지정된 `key`가 변경되면 기존 코루틴을 취소하고 새로운 코루틴을 실행합니다. 컴포저블이 화면에서 사라지면 코루틴도 자동으로 취소됩니다.
* **주요 사용처**: 화면 진입 시 일회성 데이터 로드, 특정 상태 변경에 따른 스낵바 표시, 화면 네비게이션 이벤트 처리.

```kotlin
@Composable
fun UserProfileScreen(userId: String, snackbarHostState: SnackbarHostState) {
    // userId가 변경될 때마다 기존 로딩 작업을 취소하고 새로운 사용 정보를 로드합니다.
    LaunchedEffect(userId) {
        try {
            val user = repository.getUserProfile(userId)
            // 성공 처리
        } catch (e: Exception) {
            snackbarHostState.showSnackbar("사용자 정보를 가져오는데 실패했습니다.")
        }
    }
}
```

> [!WARNING]
> `LaunchedEffect(Unit)` 또는 `LaunchedEffect(true)`와 같이 고정 상수를 키로 사용하면 Composition 시작 시 단 한 번만 실행됩니다. 하지만 이는 파라미터 변경에 유연하게 대처하지 못하므로, Effect 내부에서 사용하는 모든 동적 변수는 가급적 키로 명시하는 것이 권장됩니다.

---
