# Swift와의 비교

| 기능         | Kotlin                       | Swift                                  |
|:-----------|:-----------------------------|:---------------------------------------|
| 함수의 지위     | 1급 객체                        | 1급 객체                                  |
| 소괄호 탈출 문법  | **Trailing Lambda**          | **Trailing Closure** (후행 클로저)          |
| DSL 치트키 엔진 | 수신 객체 지정 람다 (`T.() -> Unit`) | **Result Builders** (`@resultBuilder`) |

```kotlin
// Kotlin (Jetpack Compose DSL)
Row {
    Text("안녕 안드로이드")
}
```

```swift
// Swift (SwiftUI DSL)
HStack {
    Text("안녕 iOS")
}
```

> [!TIP]
> SwiftUI의 `VStack { }` 안에서 `return`도 없고 컴마도 없이 여러 `Text`를 나열할 수 있는 이유는, **`@ViewBuilder`라는 Result
Builder**가 컴파일 시 이를 자동으로 하나의 컴포넌트 묶음으로 변환해 주기 때문입니다.
