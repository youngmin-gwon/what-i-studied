# interface만 있고 구현체 연결이 없음

```kotlin
interface Api

@Inject
class Repository(private val api: Api)
```

Metro는 `Api`를 어떤 구현체로 만들지 모릅니다.

해결:

```kotlin
@Provides
fun provideApi(): Api = ApiImpl()
```

또는 `@Binds`로 구현체를 interface에 연결합니다.
