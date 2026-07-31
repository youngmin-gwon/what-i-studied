# Compose + ViewModel에서의 기본 흐름

상위 노트: [metro-di-get-it-guide](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide.md)

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
