# 재구성 (Recomposition)

상위 노트: [[android-compose-internals]]

상태가 변경되면 Composable 함수가 다시 실행된다.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    
    Column {
        Text("Count: $count") // count 변경 시 이 부분만 재구성
        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}
```

#### 재구성 범위 최소화

```kotlin
// ❌ 나쁜 예: 전체 재구성
@Composable
fun BadExample() {
    var count by remember { mutableStateOf(0) }
    
    Column {
        ExpensiveComposable() // count 변경 시 불필요하게 재구성
        Text("Count: $count")
        Button(onClick = { count++ }) { Text("+") }
    }
}

// ✅ 좋은 예: 필요한 부분만 재구성
@Composable
fun GoodExample() {
    var count by remember { mutableStateOf(0) }
    
    Column {
        ExpensiveComposable() // 재구성 안 됨
        CountDisplay(count) // 이 부분만 재구성
        Button(onClick = { count++ }) { Text("+") }
    }
}

@Composable
fun CountDisplay(count: Int) {
    Text("Count: $count")
}
```
