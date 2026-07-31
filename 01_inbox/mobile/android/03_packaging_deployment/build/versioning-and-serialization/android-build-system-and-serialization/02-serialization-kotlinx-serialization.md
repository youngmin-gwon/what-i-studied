# Serialization (`kotlinx.serialization`)

상위 노트: [[android-build-system-and-serialization]]

### 2-1. 두 가지 Serializable의 정체

| 구분        | Java 표준 `Serializable`            | Kotlin `kotlinx.serialization` ★     |
|:----------|:----------------------------------|:-------------------------------------|
| **패키지**   | `java.io.Serializable`            | `kotlinx.serialization.Serializable` |
| **태생/소속** | Java 표준 (Android 아님)              | Kotlin 전용 확장 (Android 아님)            |
| **형태**    | 인터페이스 (`implements Serializable`) | 어노테이션 (`@Serializable`)              |
| **특징**    | 옛날 자바 시절부터 쓰던 방식 (느림)             | 코틀린 컴파일러가 직접 직렬화 코드를 생성 (매우 빠름)      |

> [!IMPORTANT]
> 둘 다 안드로이드 OS 자체 패키지가 아닙니다. 안드로이드 자체 직렬화 기술로는 `android.os.Parcelable`이 별도로 존재합니다.

### 2-2. 직렬화(Serialization)의 역할

* **직렬화**: 메모리에 살아있는 코틀린 객체를 **바이트 배열이나 JSON 문자열** 형태로 포장하는 행위
* **역직렬화**: 전달받은 텍스트/바이트를 다시 코틀린 객체로 조립해 내는 행위

### 2-3. 왜 Navigation에서 핵심으로 쓰이나?

최신 Navigation(2.8+/3)은 문자열 주소 대신 **코틀린 객체 자체를 라우트 주소로 사용(Type-Safe Navigation)**합니다.

```kotlin
// 라우트 주소를 담을 데이터 규격 정의
@Serializable
data class RestaurantDetail(val id: Int, val name: String)

// 화면 이동 (오타가 나면 컴파일 에러)
navController.navigate(RestaurantDetail(id = 3, name = "pawtato"))
```

Navigation 내부 시스템이 이 객체를 다른 화면으로 **안전하게 포장·전달(직렬화)**하기 위해, `@Serializable` 표식이 필수가 된 것입니다.

---
