# ❌ 안티패턴 2: 비-코루틴 콜백에서 LaunchedEffect 실행 시도
```kotlin
@Composable
fun BadButton() {
    Button(
        onClick = {
            // Composable 함수 내부가 아닌 onClick 람다 내부이므로 LaunchedEffect를 직접 호출할 수 없어 컴파일 오류 발생!
            LaunchedEffect(Unit) { 
                doSomething()
            }
        }
    ) { Text("Click") }
}
```
