# 디버깅

상위 노트: [[android-compose-internals]]

```kotlin
// Layout Inspector 사용
// Android Studio → Tools → Layout Inspector

// Recomposition 횟수 확인
@Composable
fun DebugComposable() {
    val count = remember { mutableStateOf(0) }
    
    SideEffect {
        count.value++
        Log.d("Compose", "Recomposed ${count.value} times")
    }
    
    Text("Hello")
}

// Composition Tracing
// adb shell setprop debug.compose.trace on
```
