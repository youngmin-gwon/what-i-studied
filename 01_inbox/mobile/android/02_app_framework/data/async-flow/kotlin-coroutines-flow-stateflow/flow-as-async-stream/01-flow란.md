# Flow란?

`Flow`는 **한 프로세스 안에서 시간에 따라 여러 값이 흘러오는 비동기 데이터 스트림**입니다.

일반 `suspend` 함수는 값을 한 번 반환합니다.

```kotlin
suspend fun fetchUser(): User
```

반면 `Flow`는 값을 0번, 1번, 여러 번 계속 내보낼 수 있습니다.

```kotlin
fun observeBenefits(): Flow<List<Benefit>>
```

쉽게 말하면:

| 형태                                           | 의미                |
|:---------------------------------------------|:------------------|
| `suspend fun getUser(): User`                | 유저를 한 번 가져온다      |
| `fun observeUser(): Flow<User>`              | 유저 정보 변화를 계속 관찰한다 |
| `suspend fun fetchProducts(): List<Product>` | 상품 목록을 한 번 요청한다   |
| `fun observeProducts(): Flow<List<Product>>` | 상품 목록 변화를 계속 받는다  |

> [!IMPORTANT]
> Kotlin Flow는 **앱 내부의 비동기 상태/데이터 흐름**을 표현하는 도구입니다. 다른 앱으로 데이터를 공개하거나 전달하는 Android OS 컴포넌트가 아닙니다. 앱
> 밖으로 데이터를 열어야 하면 `ContentProvider`, `FileProvider`, `Intent`, App Link, App Functions, Binder/AIDL
> 같은
> 플랫폼 경계를 사용해야 합니다.
