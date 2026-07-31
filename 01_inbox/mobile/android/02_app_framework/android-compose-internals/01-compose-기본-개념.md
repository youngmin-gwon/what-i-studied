# Compose 기본 개념

상위 노트: [[android-compose-internals]]

Compose 는 선언적 UI 프레임워크다. 상태가 바뀌면 UI 가 자동으로 업데이트된다.

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Hello, $name!")
}

// 사용
setContent {
    Greeting("Android")
}
```
