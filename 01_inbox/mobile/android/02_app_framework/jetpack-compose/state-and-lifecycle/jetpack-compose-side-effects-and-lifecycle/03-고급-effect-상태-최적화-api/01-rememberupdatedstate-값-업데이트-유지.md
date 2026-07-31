# `rememberUpdatedState` (값 업데이트 유지)
* **목적**: Effect가 재생성(Re-launch)되는 비용을 피하면서, 비동기 작업 중에도 항상 최신의 변수 값을 참조하도록 보장합니다.
* **동작**: `rememberUpdatedState`로 값을 감싸면, Effect의 `key`를 변경하지 않아도 코루틴 내부에서 항상 최신 상태를 읽어올 수 있습니다.
* **주요 사용처**: 시간 경과 후 실행되는 콜백(예: Timer, Timeout) 등에서, 최신 이벤트 핸들러를 실행하되 이펙트를 처음부터 재시작하고 싶지 않을 때.

```kotlin
@Composable
fun TimeoutHandler(onTimeout: () -> Unit) {
    // onTimeout 람다가 변경되더라도 LaunchedEffect가 재시작되지 않도록 감싸줍니다.
    val currentOnTimeout by rememberUpdatedState(onTimeout)

    LaunchedEffect(Unit) {
        delay(5000L) // 5초 대기
        currentOnTimeout() // 이펙트 재시작 없이 항상 가장 최신의 onTimeout 실행
    }
}
```

---
