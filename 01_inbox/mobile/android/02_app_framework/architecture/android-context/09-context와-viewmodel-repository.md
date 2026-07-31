# Context와 ViewModel/Repository

상위 노트: [[android-context]]

현대 Android 구조에서는 ViewModel이 Activity Context를 직접 들고 있지 않게 설계하는 편이 좋습니다.

```kotlin
class BadViewModel(
    private val activityContext: Context,
) : ViewModel()
```

이 구조는 ViewModel 수명이 Activity보다 길 수 있는 상황과 충돌합니다.

권장 구조:

```kotlin
class SessionRepository(
    private val appContext: Context,
) {
    fun sessionFile(): File {
        return File(appContext.filesDir, "session.json")
    }
}

class SessionViewModel(
    private val repository: SessionRepository,
) : ViewModel()
```

더 좋은 구조는 Repository도 가능하면 `Context` 자체를 퍼뜨리지 않고, 필요한 Android API를 더 좁은 인터페이스로 감싸는 것입니다.

```kotlin
interface SessionStorage {
    suspend fun save(sessionKey: String)
    suspend fun clear()
}

class DataStoreSessionStorage(
    private val appContext: Context,
) : SessionStorage {
    override suspend fun save(sessionKey: String) {
        // DataStore 저장
    }

    override suspend fun clear() {
        // DataStore 삭제
    }
}
```

이렇게 하면 ViewModel과 UseCase는 Android `Context`를 몰라도 됩니다.

---
