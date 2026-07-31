# interface와 구현체 연결하기

상위 노트: [metro-di-get-it-guide](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide.md)

앱 코드에서는 구현체보다 interface에 의존하는 편이 좋습니다.

```kotlin
interface SessionStorage {
    suspend fun save(sessionKey: String)
}

@Inject
class DataStoreSessionStorage(
    private val context: Context,
) : SessionStorage {
    override suspend fun save(sessionKey: String) {
        // DataStore 저장
    }
}
```

문제는 Metro가 `SessionStorage`가 필요할 때 `DataStoreSessionStorage`를 써야 한다는 것을 알아야 한다는 점입니다.

간단한 방법은 `@Provides`입니다.

```kotlin
@DependencyGraph
interface AppGraph {
    val sessionStorage: SessionStorage

    @Provides
    fun provideSessionStorage(
        impl: DataStoreSessionStorage,
    ): SessionStorage = impl
}
```

Metro에는 `@Binds`도 있습니다.

```kotlin
@DependencyGraph
interface AppGraph {
    val sessionStorage: SessionStorage

    @Binds
    val DataStoreSessionStorage.bindSessionStorage: SessionStorage
}
```

초보 단계에서는 이렇게 기억하면 됩니다.

```text
직접 만드는 코드가 필요하다
-> @Provides

이미 @Inject로 만들 수 있는 구현체를 interface로 노출하고 싶다
-> @Binds
```

---
