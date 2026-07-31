# `when` 표현식과 `is` 패턴 매칭
```kotlin
when (key) {
    is Home -> NavEntry(key, metadata = mapOf("key" to "value")) {}
}
```
* `when`은 Java/C의 `switch`문과 유사하지만 훨씬 강력합니다.
* `is Home`은 **"key 변수의 실제 타입이 Home 클래스인가?"**를 확인하는 **타입 체크** 패턴입니다. Java의 `instanceof`에 해당합니다.
* `->` 뒤에 나오는 코드가 해당 조건이 참일 때 실행됩니다.
