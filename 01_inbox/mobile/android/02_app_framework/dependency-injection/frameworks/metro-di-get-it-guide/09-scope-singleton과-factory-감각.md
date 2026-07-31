# Scope: singleton과 factory 감각

상위 노트: [metro-di-get-it-guide](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide.md)

`get_it`에서 자주 쓰는 두 가지가 있습니다.

```dart
registerSingleton<Api>(ApiImpl())
registerFactory<ViewModel>(() => ViewModel(...))
```

Metro에서는 **scope가 있으면 graph 안에서 재사용**되고, scope가 없으면 필요할 때마다 새로 만들 수 있다고 이해하면 됩니다.

```kotlin
@Scope
annotation class AppScope

@DependencyGraph(AppScope::class)
interface AppGraph {
    val api: SessionApi
    val repository: SessionRepository
}
```

`AppScope`는 평범한 Kotlin annotation이 아니라, Metro가 scope로 인식할 수 있도록 `@Scope`가 붙은 annotation입니다.

```kotlin
@SingleIn(AppScope::class)
@Inject
class SessionApi
```

또는 provider에 붙일 수 있습니다.

```kotlin
@SingleIn(AppScope::class)
@Provides
fun provideSessionApi(): SessionApi {
    return SessionApi()
}
```

의미:

```text
이 AppGraph 인스턴스 안에서는 SessionApi를 한 번만 만들고 재사용한다.
```

주의할 점:

* 앱 전체 singleton이면 `AppScope`
* 로그인 후 세션 단위라면 `SessionScope`
* 화면 단위라면 screen/feature graph를 따로 두는 방식 검토

> [!IMPORTANT]
> scope는 "전역 singleton"이라는 뜻이 아닙니다. **어떤 graph 인스턴스 안에서 재사용할 것인가**를 정하는 규칙입니다.

---
