# CompositionLocal이란?

상위 노트: [[jetpack-compose-compositionlocal-and-designsystem-locals]]

Compose에서 기본 데이터 흐름은 명시적인 parameter 전달입니다.

```kotlin
@Composable
fun Parent() {
    Child(color = Color.Red)
}

@Composable
fun Child(color: Color) {
    Text("Hello", color = color)
}
```

이 방식은 의존성이 명확합니다. 하지만 앱 전체에서 매우 자주 쓰이고, 중간 계층이 굳이 알 필요 없는 값은 매번 parameter로 넘기면 코드가 지저분해집니다.

대표 예시는 다음과 같습니다.

```text
theme color
typography
layout direction
Android Context
현재 adaptive layout 정보
현재 overlay inset 정보
```

`CompositionLocal`은 이런 값을 Compose tree 아래로 암묵적으로 전달하는 도구입니다.

```kotlin
CompositionLocalProvider(LocalValue provides value) {
    SomeScreen()
}
```

아래쪽 Composable은 가장 가까운 provider가 제공한 값을 읽습니다.

```kotlin
val value = LocalValue.current
```

Flutter 경험으로 보면 `InheritedWidget`, `Provider`, `Theme.of(context)`와 비슷한 역할입니다. 다만 Compose에서는
`BuildContext`를 넘기지 않고, `LocalSomething.current` 형태로 현재 Composition의 값을 읽습니다.

---
