---
title: viewmodel-di-injects-dependencies-not-viewmodel-ownership
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## ViewModel DI 는 dependency 주입이지 ViewModel 소유권을 DI graph 로 옮기는 일이 아니다

ViewModel 은 화면 상태 owner 이며 lifecycle 은 ViewModelStoreOwner 가 관리한다. DI framework 는 ViewModel 이 필요로 하는 Repository, UseCase, dispatcher, saved state collaborator 를 제공할 수 있지만, ViewModel 생명주기 자체를 임의의 app graph singleton 으로 바꾸면 안 된다.

**Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) 의 `@HiltViewModel` 이나 수동 `ViewModelProvider.Factory` 는 DI graph 와 ViewModel owner 사이의 연결 boundary 다. Compose 에서 ViewModel 을 얻을 때도 screen owner 와 navigation back stack owner 를 먼저 확인해야 한다.

관련 노트: [ViewModel](../../architecture/state-management/viewmodel/viewmodel.md), [Compose runtime/state](../../jetpack-compose/runtime/compose-runtime-and-state-model.md).

### 최소 예시

```kotlin
@HiltViewModel
class FeedViewModel @Inject constructor(
    private val refreshFeed: RefreshFeed,
    savedStateHandle: SavedStateHandle,
) : ViewModel()

@AndroidEntryPoint
class FeedFragment : Fragment() {
    private val viewModel: FeedViewModel by viewModels()
}
```

Hilt는 factory에 dependency를 공급하지만 instance cache와 `onCleared()` 호출은 `ViewModelStoreOwner`가 맡는다. Compose Navigation에서는 `viewModel()`/`hiltViewModel()`에 어느 `NavBackStackEntry`가 owner로 전달되는지가 instance 공유 범위를 결정한다.

### 실패와 관찰 신호

- `@Inject lateinit var viewModel: FeedViewModel`처럼 직접 주입하면 ViewModel API를 우회하므로 Hilt는 직접 요청을 금지하는 compile error를 낸다.
- 같은 route인데 ViewModel이 예상보다 자주 새로 생기면 owner key/back-stack entry가 달라졌는지 constructor log와 `onCleared()`를 관찰한다.
- app singleton에 ViewModel을 저장하면 back stack에서 제거돼도 해제되지 않으므로 금지한다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Hilt and Jetpack — ViewModel](https://developer.android.com/training/dependency-injection/hilt-jetpack#viewmodels)
