# Metro의 3대 기본 요소

상위 노트: [[metro-di-get-it-guide]]

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
