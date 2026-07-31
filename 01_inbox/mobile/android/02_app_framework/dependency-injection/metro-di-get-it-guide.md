# Metro DI 초보자 가이드 (`get_it` 경험자용)

이 문서는 Flutter에서 `get_it`을 써 본 개발자가 Android/Kotlin의 **Metro DI**를 처음 배울 때 필요한 개념과 사용 방법을 설명합니다.

Metro는 Kotlin Multiplatform을 지원하는 **컴파일 타임 의존성 주입(Dependency Injection) 프레임워크**입니다. Zac Sweers가 만든
오픈소스 라이브러리이며, Kotlin compiler plugin으로 동작합니다.

관련 공식 문서:

- [Metro GitHub README](https://github.com/ZacSweers/metro)
- [Metro Installation](https://zacsweers.github.io/metro/latest/installation/)
- [Metro Dependency Graphs](https://zacsweers.github.io/metro/latest/dependency-graphs/)
- [Metro Injection Types](https://zacsweers.github.io/metro/latest/injection-types/)
- [Metro Bindings](https://zacsweers.github.io/metro/latest/bindings/)
- [Metro Scopes](https://zacsweers.github.io/metro/latest/scopes/)

---

## 1. 먼저 DI가 뭔가?

DI는 **객체가 필요한 의존성을 직접 만들지 않고, 바깥에서 받게 하는 방식**입니다.

나쁜 예:

```kotlin
class BenefitRepository {
    private val api = BenefitApi()
    private val storage = BenefitStorage()
}
```

이 코드는 `BenefitRepository`가 `BenefitApi`와 `BenefitStorage`를 직접 만들어 버립니다. 그래서 테스트할 때 fake API로 바꾸기
어렵고, 앱 전체에서 같은 인스턴스를 공유하기도 어렵습니다.

좋은 예:

```kotlin
class BenefitRepository(
    private val api: BenefitApi,
    private val storage: BenefitStorage,
)
```

이제 `BenefitRepository`는 "나는 `BenefitApi`와 `BenefitStorage`가 필요하다"라고 선언만 합니다. 누가 만들어서 넣어줄지는 바깥에서
결정합니다.

Metro는 이 바깥의 조립 작업을 컴파일 타임에 자동으로 만들어주는 도구입니다.

---

## 2. get_it과 Metro의 가장 큰 차이

Flutter `get_it`은 보통 **전역 서비스 로케이터**처럼 씁니다.

```dart
final getIt = GetIt.instance;

getIt.registerSingleton<Api>(ApiImpl());
getIt.registerFactory<BenefitRepository>(
  () => BenefitRepository(getIt<Api>()),
);

final repository = getIt<BenefitRepository>();
```

Metro는 보통 이렇게 생각합니다.

```text
객체를 전역 보관함에 등록한다
-> getIt 방식

객체들이 필요한 것을 생성자로 선언한다
-> Metro가 컴파일 시 그래프를 만들고 연결한다
```

| 개념      | get_it                | Metro                                      |
|:--------|:----------------------|:-------------------------------------------|
| 등록 위치   | `getIt.register...()` | `@DependencyGraph`, `@Provides`, `@Inject` |
| 가져오는 방식 | `getIt<T>()`로 직접 꺼냄   | 생성자 파라미터로 받음                               |
| 검증 시점   | 주로 런타임                | 컴파일 타임                                     |
| 누락된 의존성 | 실행 중 에러 가능            | 빌드 실패                                      |
| 전역성     | 전역 singleton으로 쓰기 쉬움  | graph 인스턴스 수명에 묶임                          |
| 사고방식    | service locator       | dependency graph                           |

> [!IMPORTANT]
> Metro에서는 `getIt<Api>()`처럼 아무 곳에서나 꺼내 쓰는 습관을 줄이는 것이 핵심입니다. 필요한 객체는 생성자에서 받고, Metro가 그 생성자를 호출하게
> 만듭니다.

---

## 3. Metro의 3대 기본 요소

Metro를 처음 볼 때는 아래 3개만 잡으면 됩니다.

| 요소                 | 역할                         | get_it 감각으로 보면                             |
|:-------------------|:---------------------------|:-------------------------------------------|
| `@Inject`          | 이 클래스는 Metro가 생성할 수 있다고 표시 | `registerFactory(() => Foo(...))`에 가까움     |
| `@Provides`        | 직접 만들기 어려운 객체를 만드는 함수      | `registerSingleton<Api>(ApiImpl())`의 등록 함수 |
| `@DependencyGraph` | 앱의 의존성 지도. 무엇을 꺼낼 수 있는지 정의 | `GetIt.instance`를 타입 안전하게 만든 그래프           |

가장 작은 예시는 다음입니다.

```kotlin
import dev.zacsweers.metro.DependencyGraph
import dev.zacsweers.metro.Inject
import dev.zacsweers.metro.Provides
import dev.zacsweers.metro.createGraph

interface Api {
    fun fetch(): String
}

class ApiImpl : Api {
    override fun fetch(): String = "benefit"
}

@Inject
class BenefitRepository(
    private val api: Api,
) {
    fun load(): String = api.fetch()
}

@DependencyGraph
interface AppGraph {
    val repository: BenefitRepository

    @Provides
    fun provideApi(): Api = ApiImpl()
}

val graph = createGraph<AppGraph>()
val repository = graph.repository
```

무슨 일이 일어나는가?

1. `graph.repository`를 요청합니다.
2. Metro는 `BenefitRepository`를 만들려면 `Api`가 필요하다는 것을 봅니다.
3. `Api`는 `provideApi()`로 만들 수 있다는 것을 찾습니다.
4. `ApiImpl`을 만들고 `BenefitRepository(api)`에 넣습니다.
5. 이 전체 연결이 컴파일 시점에 검증됩니다.

---

## 4. Gradle 설정

공식 문서 기준으로 Metro는 Gradle plugin을 적용하는 방식이 기본입니다.

```kotlin
plugins {
    kotlin("android")
    id("dev.zacsweers.metro")
}
```

Version Catalog를 쓰면 보통 이런 형태가 됩니다.

```toml
[versions]
metro = "1.3.0"

[plugins]
metro = { id = "dev.zacsweers.metro", version.ref = "metro" }
```

```kotlin
plugins {
    alias(libs.plugins.metro)
}
```

> [!NOTE]
> 위 버전은 문서를 작성할 때 Metro GitHub README에서 확인한 최신 예시입니다. 실제 프로젝트에서는 Kotlin, AGP, Gradle 버전과 맞는 Metro 버전을 다시 확인하세요.

여기서 중요한 점은 `libs.versions.toml`의 `[libraries]`가 아니라 `[plugins]`에 Metro를 추가해야 한다는 것입니다.

```toml
[libraries]
metro = { group = "dev.zacsweers", name = "metro", version.ref = "metro" }
```

이 선언은 Metro runtime artifact를 라이브러리 의존성처럼 추가하는 선언입니다. 하지만 Metro는 Kotlin compiler plugin이 있어야 `@DependencyGraph`, `@Inject`, `@Provides`를 보고 코드를 생성할 수 있습니다. 공식 설치 방식은 Gradle plugin 적용이고, 이 plugin이 runtime dependency 추가와 compiler plugin wiring을 함께 처리합니다.

따라서 일반적인 Android Gradle 프로젝트에서는 아래처럼 plugin alias를 만들고:

```toml
[plugins]
metro = { id = "dev.zacsweers.metro", version.ref = "metro" }
```

모듈의 `build.gradle.kts`에 적용합니다.

```kotlin
plugins {
    alias(libs.plugins.metro)
}
```

`implementation(libs.metro)`만 추가한 상태라면 annotation type은 보일 수 있지만, Metro가 그래프 구현 코드를 생성하지 못합니다.

---

## 5. `@Inject`: 생성자 주입

Metro에서 가장 기본은 **생성자 주입(Constructor Injection)**입니다.

```kotlin
@Inject
class SessionRepository(
    private val storage: SessionStorage,
    private val api: SessionApi,
)
```

뜻:

```text
Metro야, SessionRepository를 만들 때
SessionStorage와 SessionApi를 찾아서 생성자에 넣어줘.
```

생성자 주입이 좋은 이유:

* 어떤 의존성이 필요한지 클래스 선언만 봐도 알 수 있음
* 테스트에서 fake 객체를 넣기 쉬움
* `lateinit` 주입보다 안전함
* 객체가 만들어진 뒤 의존성이 비어 있는 상태가 없음

get_it에서는 보통 이렇게 했을 것입니다.

```dart
getIt.registerFactory<SessionRepository>(
  () => SessionRepository(
    getIt<SessionStorage>(),
    getIt<SessionApi>(),
  ),
);
```

Metro에서는 클래스 쪽에 `@Inject`만 붙이고, 나머지는 그래프가 해결하게 합니다.

---

## 6. `@Provides`: 내가 직접 만드는 방법을 알려주는 함수

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

## 7. interface와 구현체 연결하기

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

## 8. 런타임 값 넣기: Context, baseUrl, userId

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

## 9. Scope: singleton과 factory 감각

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

## 10. Android 앱에서 어디에 graph를 보관하나?

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

## 11. Compose + ViewModel에서의 기본 흐름

초보 단계에서는 ViewModel을 직접 Metro에서 꺼내기보다, 먼저 Repository와 UseCase를 Metro로 관리한다고 생각하는 편이 이해하기 쉽습니다.

```kotlin
@Inject
class BenefitRepository(
    private val api: BenefitApi,
)

class BenefitViewModel(
    private val repository: BenefitRepository,
) : ViewModel()
```

ViewModel factory:

```kotlin
class BenefitViewModelFactory(
    private val repository: BenefitRepository,
) : ViewModelProvider.Factory {
    @Suppress("UNCHECKED_CAST")
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        return BenefitViewModel(repository) as T
    }
}
```

Graph에 factory를 노출:

```kotlin
@DependencyGraph(AppScope::class)
interface AppGraph {
    val benefitRepository: BenefitRepository

    @Provides
    fun provideBenefitViewModelFactory(
        repository: BenefitRepository,
    ): BenefitViewModelFactory {
        return BenefitViewModelFactory(repository)
    }
}
```

Compose route:

```kotlin
@Composable
fun BenefitRoute(
    appGraph: AppGraph,
) {
    val viewModel: BenefitViewModel = viewModel(
        factory = appGraph.provideBenefitViewModelFactory(),
    )

    BenefitScreen(/* ... */)
}
```

실제 프로젝트에서는 MetroX ViewModel integration 같은 확장도 검토할 수 있습니다. 하지만 처음에는 이 수동 factory 방식을 이해하면 DI의 흐름을 더
잘 잡을 수 있습니다.

---

## 12. 멀티 모듈에서의 사고방식

이 프로젝트처럼 `core`, `feature:session`, `feature:dashboard` 같은 모듈이 있으면 DI의 목적은 더 중요해집니다.

기본 방향:

```text
api module
-> interface / model / contract

impl module
-> 실제 구현체 + @Inject

app module
-> 최종 AppGraph 조립
```

예시:

```kotlin
// feature/session/api
interface SessionRepository {
    suspend fun logout()
}
```

```kotlin
// feature/session/impl
@Inject
class RealSessionRepository(
    private val api: SessionApi,
    private val storage: SessionStorage,
) : SessionRepository
```

```kotlin
// app
@DependencyGraph(AppScope::class)
interface AppGraph {
    val sessionRepository: SessionRepository

    @Provides
    fun provideSessionRepository(
        impl: RealSessionRepository,
    ): SessionRepository = impl
}
```

Metro의 aggregation 기능(`@ContributesTo`, `@ContributesBinding`)을 쓰면 각 feature module이 자신의 binding을
기여하고 app graph가 자동으로 모으는 구조도 가능합니다. 다만 초보 단계에서는 먼저 명시적인 `@Provides`/`@Binds`로 흐름을 이해하는 편이 안전합니다.

---

## 13. get_it에서 Metro로 옮길 때의 매핑표

| get_it 코드/개념                                     | Metro에서의 대응                                                      |
|:-------------------------------------------------|:-----------------------------------------------------------------|
| `getIt.registerFactory<Foo>(() => Foo(getIt()))` | `@Inject class Foo(dep: Dep)`                                    |
| `getIt.registerSingleton<Api>(ApiImpl())`        | `@SingleIn(AppScope::class)` + `@Provides fun provideApi(): Api` |
| `getIt<Api>()`                                   | 생성자 파라미터 `class Foo(private val api: Api)`                       |
| `registerLazySingleton`                          | scoped binding. 처음 요청될 때 생성되어 graph 안에서 재사용                      |
| `reset()`                                        | graph 인스턴스를 버리고 새로 만들기                                           |
| `getIt.pushNewScope()`                           | 별도 graph/graph extension 생성                                      |
| `registerFactoryParam`                           | assisted injection 또는 graph factory parameter                    |
| test에서 `registerSingleton<FakeApi>`              | test graph 또는 factory parameter로 fake 주입                         |

---

## 14. 자주 하는 실수

### 14-1. 그래프를 만들었는데 아무 것도 노출하지 않음

```kotlin
@DependencyGraph
interface AppGraph
```

이렇게 하면 밖에서 꺼낼 수 있는 것이 없습니다.

```kotlin
@DependencyGraph
interface AppGraph {
    val repository: BenefitRepository
}
```

`val repository` 같은 accessor가 있어야 graph 밖에서 시작점으로 사용할 수 있습니다.

### 14-2. interface만 있고 구현체 연결이 없음

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

### 14-3. Activity Context를 AppGraph에 넣음

AppGraph가 앱 전체 수명이라면 Activity Context를 넣으면 안 됩니다.

```kotlin
// 나쁜 예
factory.create(this) // Activity this
```

```kotlin
// 좋은 예
factory.create(applicationContext)
```

### 14-4. DI를 쓰면서도 내부에서 직접 생성

```kotlin
@Inject
class Repository {
    private val api = ApiImpl()
}
```

이러면 Metro가 `Api`를 교체하거나 테스트용 fake를 넣을 수 없습니다.

```kotlin
@Inject
class Repository(
    private val api: Api,
)
```

### 14-5. 모든 것을 singleton으로 만듦

`get_it`을 오래 쓰면 모든 것을 `registerSingleton`으로 등록하고 싶어질 수 있습니다.

하지만 Metro에서는 먼저 이렇게 생각하는 편이 좋습니다.

```text
상태가 없고 가벼운 객체인가?
-> unscoped로 시작

생성 비용이 크거나 공유 상태를 가져야 하나?
-> scope 적용

Activity/ViewModel 수명에 묶여야 하나?
-> AppScope에 넣지 말고 더 좁은 graph 고려
```

---

## 15. 최소 학습 순서

1. `@Inject` 생성자 주입
2. `@DependencyGraph`와 `createGraph`
3. `@Provides`로 외부 객체 만들기
4. interface를 구현체에 연결하기
5. `@DependencyGraph.Factory`로 `Context` 같은 런타임 값 넣기
6. `@SingleIn`으로 scope 이해하기
7. ViewModel factory와 연결하기
8. 멀티 모듈에서는 `@Binds`, `@ContributesBinding`, `@ContributesTo` 검토하기

---

## 16. 한 문장 요약

```text
get_it은 "전역 보관함에 등록하고 꺼내 쓰는 방식"이고,
Metro는 "필요한 것을 생성자에 적어두면 컴파일러가 그래프를 만들어 연결하는 방식"입니다.
```

처음에는 이 원칙만 지키면 됩니다.

```text
직접 만들지 말고 생성자로 받기
전역에서 꺼내지 말고 graph가 넣어주게 하기
오래 사는 graph에는 applicationContext만 넣기
interface에는 @Provides 또는 @Binds로 구현체 연결하기
```

> [!NOTE]
> DI의 큰 그림과 Metro가 Navigation/Dynamic Feature와 연결되는
> 이유는 [[dependency-injection-dsl-dynamic-feature]]
> 를 참조하세요.
> Context의 수명
> 차이는 [[android-context]]를
> 참조하세요.
