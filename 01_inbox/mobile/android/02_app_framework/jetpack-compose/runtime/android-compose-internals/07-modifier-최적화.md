# Modifier 최적화

상위 노트: [[android-compose-internals]]

```kotlin
// ❌ 나쁜 예: 재구성마다 새 Modifier 생성
@Composable
fun BadModifier(isSelected: Boolean) {
    Box(
        modifier = Modifier
            .size(100.dp)
            .background(if (isSelected) Color.Blue else Color.Gray)
    )
}

// ✅ 좋은 예: Modifier 재사용
@Composable
fun GoodModifier(isSelected: Boolean) {
    val backgroundColor = if (isSelected) Color.Blue else Color.Gray
    
    Box(
        modifier = Modifier
            .size(100.dp)
            .background(backgroundColor)
    )
}

// ✅ 더 좋은 예: remember 사용
@Composable
fun BetterModifier(isSelected: Boolean) {
    val modifier = remember(isSelected) {
        Modifier
            .size(100.dp)
            .background(if (isSelected) Color.Blue else Color.Gray)
    }
    
    Box(modifier = modifier)
}
```
