# ❌ 안티패턴 3: State 업데이트 지연을 방지하고자 Effect를 무분별하게 재생성
```kotlin
@Composable
fun BadTimer(onTick: () -> Unit) {
    // onTick이 바뀔 때마다 LaunchedEffect가 취소되고 처음부터 다시 시작하여 타이머가 정상 동작하지 못합니다!
    LaunchedEffect(onTick) {
        while(true) {
            delay(1000L)
            onTick()
        }
    }
}
```
