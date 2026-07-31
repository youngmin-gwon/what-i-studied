# 후행 람다(Trailing Lambda) — DSL의 핵심
```kotlin
metadata = metadata {
    put(NavDisplay.TransitionKey) { fadeIn() togetherWith fadeOut() }
}
```
이 코드가 가장 낯설어 보이실 텐데, 단계별로 풀어보면 다음과 같습니다:

```kotlin
// 원래 문법 (정식 호출)
metadata = metadata({ /* 이 블록이 함수의 마지막 매개변수인 람다 */ })

// Kotlin 규칙: 함수의 마지막 파라미터가 람다이면, 괄호 밖으로 뺄 수 있다
metadata = metadata() { /* 람다 */ }

// Kotlin 규칙: 괄호 안에 다른 인자가 없으면, 빈 괄호도 생략 가능
metadata = metadata { /* 람다 */ }
```

즉, `metadata { ... }`는 **`metadata`라는 함수를 호출하면서 `{ ... }` 블록(람다)을 인자로 넘기는 것**입니다. 이 람다 블록 안에서 `put()` 등의 함수를 쓸 수 있는데, 이것이 Kotlin **DSL(Domain Specific Language)** 패턴의 핵심입니다.
