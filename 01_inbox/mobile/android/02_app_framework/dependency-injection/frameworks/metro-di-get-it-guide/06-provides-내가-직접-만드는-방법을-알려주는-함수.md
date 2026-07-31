# `@Provides`: 내가 직접 만드는 방법을 알려주는 함수

상위 노트: [[metro-di-get-it-guide]]

모든 객체를 `@Inject` 생성자로 만들 수 있는 것은 아닙니다.

예를 들어 아래 객체들은 보통 직접 만드는 함수가 필요합니다.

```text
Retrofit
OkHttpClient
RoomDatabase
DataStore
Android Context
외부 SDK 객체
interface의 구현체
```

이럴 때 `@Provides`를 씁니다.

```kotlin
@DependencyGraph
interface AppGraph {
    val sessionRepository: SessionRepository

    @Provides
    fun provideBaseUrl(): String = "https://api.example.com"

    @Provides
    fun provideSessionApi(baseUrl: String): SessionApi {
        return Retrofit.Builder()
            .baseUrl(baseUrl)
            .build()
            .create(SessionApi::class.java)
    }
}
```

`@Provides` 함수도 의존성을 받을 수 있습니다.

```kotlin
@Provides
fun provideRepository(
    api: SessionApi,
    storage: SessionStorage,
): SessionRepository {
    return SessionRepository(api, storage)
}
```

Metro가 `api`와 `storage`를 먼저 찾고, 그 결과로 `SessionRepository`를 만듭니다.

> [!TIP]
> 공식 문서에서도 `@Provides` 함수는 명시적인 반환 타입을 두는 예시를 사용합니다. 초보 단계에서는 항상 반환 타입을 명시하는 습관이 좋습니다.

---
