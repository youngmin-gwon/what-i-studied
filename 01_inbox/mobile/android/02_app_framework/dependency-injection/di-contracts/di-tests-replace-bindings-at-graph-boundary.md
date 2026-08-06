---
title: di-tests-replace-bindings-at-graph-boundary
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## DI 테스트는 내부 구현을 건드리지 않고 graph boundary 에서 binding 을 교체한다

DI 가 테스트에 주는 이점은 production code 내부의 생성 코드를 바꾸지 않고 fake, test dispatcher, in-memory database, fake API 를 graph boundary 에서 바꿀 수 있다는 점이다.

테스트가 consumer 내부 필드를 직접 덮어쓰거나 singleton registry 를 공유하면 순서 의존성과 누수가 생긴다. test graph, module replacement, factory injection 처럼 명시적인 교체 지점을 둔다.

### 두 종류의 테스트 seam

```kotlin
@Test
fun refresh_uses_repository() = runTest {
    val subject = RefreshFeed(FakeFeedRepository(), testDispatcher)
    subject()
}
```

일반 Kotlin unit test는 graph를 띄우지 않고 생성자로 fake를 전달한다. Android graph 통합을 검증할 때는 production module과 같은 component에 test module을 설치한다.

```kotlin
@Module
@TestInstallIn(
    components = [SingletonComponent::class],
    replaces = [NetworkModule::class],
)
object FakeNetworkModule {
    @Provides fun api(): FeedApi = FakeFeedApi()
}
```

`@TestInstallIn`은 source set 전체가 공유하는 교체에 적합하다. `@UninstallModules`나 `@BindValue`는 테스트별 custom component를 생성하므로 편리하지만 build 비용이 커질 수 있다.

### 실패와 관찰 신호

- production module을 replace/uninstall하지 않고 같은 key를 제공하면 duplicate binding build error가 난다.
- fake scope와 설치 component가 production contract와 다르면 실제 lifetime 결함을 가릴 수 있다.
- 테스트 순서에 따라 결과가 바뀌면 전역 container 또는 singleton fake state가 공유되는지 확인한다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Hilt testing guide](https://developer.android.com/training/dependency-injection/hilt-testing), [Hilt testing design](https://dagger.dev/hilt/testing.html)
