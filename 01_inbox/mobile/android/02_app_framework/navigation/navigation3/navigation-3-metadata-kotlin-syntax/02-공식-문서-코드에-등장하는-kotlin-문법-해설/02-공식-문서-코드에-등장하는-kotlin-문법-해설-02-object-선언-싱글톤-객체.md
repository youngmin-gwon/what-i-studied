# `object` 선언 — 싱글톤 객체
```kotlin
object NavDisplay {
    object TransitionKey : NavMetadataKey<...>
}
```
* Kotlin의 `object`는 **클래스 선언과 동시에 단 하나의 인스턴스만 존재하는 싱글톤 객체**를 만듭니다.
* `new` 같은 키워드로 인스턴스를 만들 필요 없이, 그 자체가 곧 유일한 인스턴스입니다.
* 여기서 `TransitionKey`는 `NavDisplay`라는 객체 안에 중첩(nested)된 또 다른 싱글톤입니다.
* 사용할 때는 `NavDisplay.TransitionKey`처럼 마치 Java의 `static` 상수처럼 접근합니다.
