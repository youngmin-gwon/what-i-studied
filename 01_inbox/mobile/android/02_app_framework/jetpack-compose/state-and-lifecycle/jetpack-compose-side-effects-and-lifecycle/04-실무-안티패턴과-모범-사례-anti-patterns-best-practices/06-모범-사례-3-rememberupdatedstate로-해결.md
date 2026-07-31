# 모범 사례 3: `rememberUpdatedState`로 해결
```kotlin
@Composable
fun GoodTimer(onTick: () -> Unit) {
    val currentOnTick by rememberUpdatedState(onTick)
    
    // LaunchedEffect는 Unit으로 최초 1회만 실행하고 변경되지 않지만,
    // currentOnTick은 항상 최신의 onTick을 안전하게 참조합니다.
    LaunchedEffect(Unit) {
        while(true) {
            delay(1000L)
            currentOnTick()
        }
    }
}

---
