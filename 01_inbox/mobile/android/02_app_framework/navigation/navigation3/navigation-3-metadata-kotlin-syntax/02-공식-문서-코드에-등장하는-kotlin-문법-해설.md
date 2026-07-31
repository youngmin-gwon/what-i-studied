# 공식 문서 코드에 등장하는 Kotlin 문법 해설

### 2-1. `Map<String, Any>` — 제네릭(Generics)과 Any 타입
```kotlin
metadata = mapOf("key" to "value")
```
* `Map<String, Any>`는 **키가 String이고, 값이 Any(아무 타입이나 가능)인 딕셔너리**입니다.
* Kotlin에서 `Any`는 Java의 `Object`와 같은 최상위 타입입니다. 모든 클래스의 부모이므로 String, Int, 함수, 객체 등 뭐든 넣을 수 있습니다.
* `mapOf("key" to "value")`에서 `to`는 Kotlin의 중위 함수(infix function)로, `Pair("key", "value")`를 만드는 축약 문법입니다.

### 2-2. `object` 선언 — 싱글톤 객체
```kotlin
object NavDisplay {
    object TransitionKey : NavMetadataKey<...>
}
```
* Kotlin의 `object`는 **클래스 선언과 동시에 단 하나의 인스턴스만 존재하는 싱글톤 객체**를 만듭니다.
* `new` 같은 키워드로 인스턴스를 만들 필요 없이, 그 자체가 곧 유일한 인스턴스입니다.
* 여기서 `TransitionKey`는 `NavDisplay`라는 객체 안에 중첩(nested)된 또 다른 싱글톤입니다.
* 사용할 때는 `NavDisplay.TransitionKey`처럼 마치 Java의 `static` 상수처럼 접근합니다.

### 2-3. `data object` vs `object`
```kotlin
// Navigation3 Route 정의 시
@Serializable
data object Home : NavKey     // data object

// Metadata Key 정의 시
object TransitionKey : NavMetadataKey<...>  // 일반 object
```
| 구분 | `object` | `data object` |
| :--- | :--- | :--- |
| 인스턴스 개수 | 단 1개 (싱글톤) | 단 1개 (싱글톤) |
| `toString()` | `패키지명@해시코드` (기본값) | `"Home"` (클래스 이름을 자동 반환) |
| `equals` / `hashCode` | 참조 비교 (기본값) | 자동 생성됨 |
| 용도 | 내부 키, 전략 객체 등 | 직렬화가 필요하거나 로그에 이름이 찍혀야 할 때 |

### 2-4. 인터페이스 상속 — `: NavMetadataKey<String>`
```kotlin
object MyStringMetadataKey : NavMetadataKey<String>
```
* Kotlin에서 `:` (콜론)은 **상속 또는 인터페이스 구현**을 의미합니다. Java의 `extends`/`implements`에 해당합니다.
* `NavMetadataKey<String>`은 **"이 키로 꺼낸 값은 반드시 String 타입이다"**라고 컴파일러에게 약속하는 제네릭 인터페이스입니다.
* 이 덕분에 나중에 `metadata[MyStringMetadataKey]`로 값을 꺼내면 자동으로 `String?` 타입이 되어, 별도의 타입 캐스팅(`as String`)이 필요 없습니다.

### 2-5. 후행 람다(Trailing Lambda) — DSL의 핵심
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

### 2-6. 중위 함수(Infix Function) — `togetherWith`
```kotlin
fadeIn() togetherWith fadeOut()
```
* Kotlin에서 `infix` 키워드가 붙은 함수는 **점(`.`)과 괄호 없이 마치 연산자처럼** 호출할 수 있습니다.
* 위 코드는 사실 다음과 완전히 동일합니다:
```kotlin
fadeIn().togetherWith(fadeOut())
```
* `togetherWith`는 Compose Animation 라이브러리가 제공하는 중위 함수로, 두 개의 전환 효과를 결합하여 하나의 `ContentTransform`을 만들어 줍니다.

### 2-7. `when` 표현식과 `is` 패턴 매칭
```kotlin
when (key) {
    is Home -> NavEntry(key, metadata = mapOf("key" to "value")) {}
}
```
* `when`은 Java/C의 `switch`문과 유사하지만 훨씬 강력합니다.
* `is Home`은 **"key 변수의 실제 타입이 Home 클래스인가?"**를 확인하는 **타입 체크** 패턴입니다. Java의 `instanceof`에 해당합니다.
* `->` 뒤에 나오는 코드가 해당 조건이 참일 때 실행됩니다.

### 2-8. 연산자 오버로딩 — `contains`와 `get`
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

### 2-9. 중첩 `object`를 키로 쓰는 이유
```kotlin
class MySceneStrategy<T : Any> : SceneStrategy<T> {
    object MyStringMetadataKey : NavMetadataKey<String>
}
```
* **"이 키를 읽는 주체(MySceneStrategy)와 키 자체를 같은 클래스 안에 묶어놓자"**는 코드 조직화 관례(Convention)입니다.
* 이렇게 하면 `MySceneStrategy.MyStringMetadataKey`로 접근하므로, 어떤 컴포넌트가 이 메타데이터를 사용하는지 이름만으로도 직관적으로 파악할 수 있습니다.
* `NavDisplay` 역시 함수이지만 같은 이름의 `object NavDisplay`를 만들어 그 안에 `TransitionKey`를 넣어둔 것이 같은 관례를 따른 것입니다.

---
