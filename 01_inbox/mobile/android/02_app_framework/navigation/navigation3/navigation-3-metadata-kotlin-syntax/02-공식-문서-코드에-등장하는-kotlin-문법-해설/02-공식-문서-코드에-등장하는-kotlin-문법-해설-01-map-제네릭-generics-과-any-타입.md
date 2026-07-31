# `Map<String, Any>` — 제네릭(Generics)과 Any 타입
```kotlin
metadata = mapOf("key" to "value")
```
* `Map<String, Any>`는 **키가 String이고, 값이 Any(아무 타입이나 가능)인 딕셔너리**입니다.
* Kotlin에서 `Any`는 Java의 `Object`와 같은 최상위 타입입니다. 모든 클래스의 부모이므로 String, Int, 함수, 객체 등 뭐든 넣을 수 있습니다.
* `mapOf("key" to "value")`에서 `to`는 Kotlin의 중위 함수(infix function)로, `Pair("key", "value")`를 만드는 축약 문법입니다.
