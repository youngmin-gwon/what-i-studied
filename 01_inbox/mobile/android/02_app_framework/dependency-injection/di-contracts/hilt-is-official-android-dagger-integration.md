---
title: hilt-is-official-android-dagger-integration
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Hilt 는 Android 용 공식 Dagger 통합 경로다

Hilt는 Dagger를 Android component 생성 시점과 표준 component hierarchy에 통합한 Google 권장 DI 라이브러리다. `@HiltAndroidApp`이 application root를 만들고, `@AndroidEntryPoint`가 지원되는 Activity·Fragment·View·Service·BroadcastReceiver에 injection hook을 생성한다. ViewModel은 `@HiltViewModel`과 `ViewModelProvider` 통합을 사용한다.

Hilt가 owner별 component 생성과 제거를 연결해도 scope 선택이나 reference 방향까지 대신 설계하지는 않는다. 예를 들어 `SingletonComponent` binding이 Activity를 field로 보관하면 component가 정상 종료돼도 Activity leak이 생긴다.

### Component와 재사용 범위

| Component | 대략적인 owner lifetime | 맞는 scope |
| --- | --- | --- |
| `SingletonComponent` | `Application` 생성부터 process 종료까지 | `@Singleton` |
| `ActivityRetainedComponent` | Activity의 첫 생성부터 마지막 destruction까지, configuration change 유지 | `@ActivityRetainedScoped` |
| `ViewModelComponent` | ViewModel 생성부터 제거까지 | `@ViewModelScoped` |
| `ActivityComponent` | 한 Activity instance | `@ActivityScoped` |
| `FragmentComponent` | 한 Fragment instance | `@FragmentScoped` |
| `ServiceComponent` | 한 Service instance | `@ServiceScoped` |

scope는 optional이다. unscoped binding은 요청마다 새 instance를 만들 수 있고, scoped binding은 해당 component instance에서 한 instance를 공유한다. module의 `@InstallIn` component와 binding scope가 맞아야 한다.

### 최소 예시

```kotlin
@HiltAndroidApp
class MainApplication : Application()

@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds
    @Singleton
    abstract fun bindUserRepository(impl: UserRepositoryImpl): UserRepository
}

@HiltViewModel
class UserProfileViewModel @Inject constructor(
    private val userRepository: UserRepository,
    savedStateHandle: SavedStateHandle,
) : ViewModel()

@AndroidEntryPoint
class UserProfileActivity : ComponentActivity() {
    private val viewModel: UserProfileViewModel by viewModels()
}
```

### 실패와 관찰 신호

- 누락·중복 binding과 scope/component 불일치는 generated graph build에서 dependency trace로 나타난다.
- `@AndroidEntryPoint` Activity가 Hilt-enabled `Application` 아래 있지 않거나 상위 Android class에 annotation이 빠지면 injection 초기화가 실패한다.
- ContentProvider는 직접 지원 대상이 아니므로 제한된 `@EntryPoint` bridge를 사용한다. BroadcastReceiver는 지원되지만 `SingletonComponent`의 binding만 직접 받는다.

관련 노트: [Dagger lifecycle policy](./dagger-is-static-graph-engine-not-android-lifecycle-policy.md), [ViewModel ownership](./viewmodel-di-injects-dependencies-not-viewmodel-ownership.md), [Entry point](./entry-points-bridge-framework-owned-objects-to-the-graph.md)

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Dependency injection with Hilt](https://developer.android.com/training/dependency-injection/hilt-android), [Hilt components](https://dagger.dev/hilt/components.html)
