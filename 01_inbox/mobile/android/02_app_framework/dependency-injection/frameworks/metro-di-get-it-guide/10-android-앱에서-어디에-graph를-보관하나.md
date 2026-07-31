# Android 앱에서 어디에 graph를 보관하나?

상위 노트: [[metro-di-get-it-guide]]

가장 단순한 시작점은 `Application`입니다.

```kotlin
class MyBenefitApplication : Application() {
    lateinit var appGraph: AppGraph
        private set

    override fun onCreate() {
        super.onCreate()
        appGraph = createGraphFactory<AppGraph.Factory>()
            .create(applicationContext)
    }
}
```

Activity나 Compose에서 접근:

```kotlin
val appGraph = (applicationContext as MyBenefitApplication).appGraph
```

하지만 앱이 커지면 직접 캐스팅을 여기저기 퍼뜨리지 않고, CompositionLocal이나 ViewModel factory, navigation entry 단위 factory로
감싸는 편이 좋습니다.

초보 단계의 기준:

```text
앱 전체에서 하나면 충분한 의존성
-> Application의 AppGraph

로그인 후에만 필요한 의존성
-> SessionGraph / LoggedInGraph

화면마다 새로 필요한 의존성
-> ViewModel factory 또는 feature graph
```

---
