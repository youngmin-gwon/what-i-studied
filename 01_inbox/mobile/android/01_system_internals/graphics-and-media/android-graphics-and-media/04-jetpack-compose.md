# Jetpack Compose

상위 노트: [[android-graphics-and-media]]

### 선언형 UI

```kotlin
@Composable
fun Greeting(name: String) {
    Text(
        text = "Hello $name",
        modifier = Modifier.padding(16.dp)
    )
}
```

**Compose Runtime**:

1. **Composition**: UI 트리 구축
2. **Layout**: 위치/크기 계산
3. **Drawing**: Skia 로 그리기

### 리컴포지션 최적화

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    
    Button(onClick = { count++ }) {
        Text("Count: $count")  // count 변경 시만 리컴포지션
    }
}
```

**스마트 리컴포지션**:

- 변경된 상태를 사용하는 Composable 만 재실행
- `remember`, `derivedStateOf` 로 최적화

---
