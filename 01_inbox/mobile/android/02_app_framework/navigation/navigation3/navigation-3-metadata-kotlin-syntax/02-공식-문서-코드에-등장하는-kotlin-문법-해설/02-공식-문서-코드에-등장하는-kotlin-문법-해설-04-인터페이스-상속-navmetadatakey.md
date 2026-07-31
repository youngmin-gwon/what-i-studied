# 인터페이스 상속 — `: NavMetadataKey<String>`
```kotlin
object MyStringMetadataKey : NavMetadataKey<String>
```
* Kotlin에서 `:` (콜론)은 **상속 또는 인터페이스 구현**을 의미합니다. Java의 `extends`/`implements`에 해당합니다.
* `NavMetadataKey<String>`은 **"이 키로 꺼낸 값은 반드시 String 타입이다"**라고 컴파일러에게 약속하는 제네릭 인터페이스입니다.
* 이 덕분에 나중에 `metadata[MyStringMetadataKey]`로 값을 꺼내면 자동으로 `String?` 타입이 되어, 별도의 타입 캐스팅(`as String`)이 필요 없습니다.
