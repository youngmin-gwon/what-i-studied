# 연산자 오버로딩 — `contains`와 `get`
```kotlin
// import를 통해 확장 함수를 불러옴
// import androidx.navigation3.runtime.contains
// import androidx.navigation3.runtime.get

val hasMyString: Boolean = metadata.contains(MySceneStrategy.MyStringMetadataKey)
val myString: String? = metadata[MySceneStrategy.MyStringMetadataKey]
```
* Kotlin에서는 특정 이름의 함수를 정의하면 **연산자 기호로 호출**할 수 있습니다:
  * `contains` → `in` 연산자: `MyStringMetadataKey in metadata`
  * `get` → `[]` 연산자: `metadata[MyStringMetadataKey]`
* 즉, `metadata[MyStringMetadataKey]`는 내부적으로 `metadata.get(MyStringMetadataKey)`를 호출하는 것이며, 반환 타입은 `NavMetadataKey<String>`의 제네릭 덕분에 자동으로 `String?`이 됩니다.
