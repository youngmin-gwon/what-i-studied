# Application Context

상위 노트: [[android-context]]

`Application Context`는 앱 프로세스 전체에 묶인 Context입니다.

```kotlin
val appContext = context.applicationContext
```

수명이 길기 때문에, 오래 살아야 하는 객체가 Context를 필요로 할 때는 보통 `Application Context`가 안전합니다.

적합한 예:

```kotlin
class SessionStorage(
    private val appContext: Context,
) {
    private val dataStore = appContext.dataStore
}
```

```kotlin
val database = Room.databaseBuilder(
    appContext,
    AppDatabase::class.java,
    "app.db",
).build()
```

`Application Context`가 적합한 곳:

```text
DataStore 생성
Room database 생성
파일/cache directory 접근
Repository 내부 Android API 접근
WorkManager enqueue
NotificationManager 같은 system service 접근
```

> [!TIP]
> DI에서 `Context`를 주입해야 한다면 먼저 "이 객체가 화면보다 오래 사는가?"를 확인하세요. 오래 사는 객체라면 Activity Context가 아니라
> Application Context가 맞는 경우가 많습니다.

---
