# 런타임 값 넣기: Context, baseUrl, userId

상위 노트: [[metro-di-get-it-guide]]

`get_it`에서는 외부 값을 등록해 두고 꺼내는 경우가 많습니다.

```dart
getIt.registerSingleton<AppConfig>(AppConfig(baseUrl));
```

Metro에서는 graph를 만들 때 값을 넣을 수 있습니다. 공식 문서에서는 `@DependencyGraph.Factory`와 `@Provides` 파라미터를 사용합니다.

Android에서는 `Context`를 이렇게 넣는 경우가 많습니다.

```kotlin
@DependencyGraph(AppScope::class)
interface AppGraph {
    val sessionRepository: SessionRepository

    @DependencyGraph.Factory
    fun interface Factory {
        fun create(
            @Provides appContext: Context,
            @Provides baseUrl: String,
        ): AppGraph
    }
}
```

앱 시작 시:

```kotlin
class MyBenefitApplication : Application() {
    lateinit var appGraph: AppGraph
        private set

    override fun onCreate() {
        super.onCreate()

        appGraph = createGraphFactory<AppGraph.Factory>()
            .create(
                appContext = applicationContext,
                baseUrl = "https://api.example.com",
            )
    }
}
```

이제 graph 내부 어디서든 `Context`나 `String`이 필요하면 Metro가 넣어줄 수 있습니다.

```kotlin
@Inject
class DataStoreSessionStorage(
    private val appContext: Context,
)
```

> [!IMPORTANT]
> 오래 사는 AppGraph에는 Activity Context가 아니라 `applicationContext`를 넣는 편이 안전합니다. Context의 수명
> 차이는 [[android-context]]를
> 참조하세요.

---
