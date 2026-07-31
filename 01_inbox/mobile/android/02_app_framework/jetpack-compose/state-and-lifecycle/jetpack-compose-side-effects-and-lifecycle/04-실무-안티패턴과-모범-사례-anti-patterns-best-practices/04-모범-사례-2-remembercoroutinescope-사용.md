# 모범 사례 2: `rememberCoroutineScope` 사용
```kotlin
@Composable
fun GoodButton() {
    val scope = rememberCoroutineScope()
    
    Button(
        onClick = {
            // 이벤트 핸들러 내부에서는 스코프를 활용해 코루틴을 실행합니다.
            scope.launch {
                doSomething()
            }
        }
    ) { Text("Click") }
}
```

---
