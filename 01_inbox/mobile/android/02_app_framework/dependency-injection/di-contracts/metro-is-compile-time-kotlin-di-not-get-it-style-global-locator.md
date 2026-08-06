---
title: metro-is-compile-time-kotlin-di-not-get-it-style-global-locator
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Metro 는 get_it 식 전역 locator 가 아니라 compile-time Kotlin DI 로 이해한다

Flutter `get_it` 경험자는 DI 를 전역 registry 에서 객체를 꺼내는 방식으로 떠올리기 쉽다. **Metro**(Kotlin Multiplatform 환경 등에서 컴파일 타임 그래프 검증을 수행하는 정적 DI 프레임워크) 는 Kotlin compiler plugin 기반의 compile-time DI 이므로, 핵심은 어디서든 꺼내 쓰는 것이 아니라 graph 가 생성자를 호출하고 binding 을 검증하게 두는 것이다.

`@DependencyGraph`, `@Inject`, `@Provides`, scope annotation 은 "등록 목록"이라기보다 graph construction contract 다. Android 앱에서는 이 graph 를 Application 또는 feature entry 같은 명확한 owner 에 보관해야 한다.

### 최소 예시

```kotlin
@Inject
class UserRepository(private val api: UserApi)

@DependencyGraph
interface AppGraph {
    val repository: UserRepository

    @Provides
    fun provideApi(): UserApi = RealUserApi()
}

val graph = createGraph<AppGraph>()
```

`AppGraph`의 property가 외부 entry point이고 compiler plugin이 reachable binding graph를 생성·검증한다. Android에서는 `createGraph` 호출 위치와 graph reference를 `Application` 또는 feature owner에 두고, 일반 consumer는 graph를 전역 조회하지 않는다.

### 실패와 관찰 신호

- `provideApi()`를 지우면 `UserRepository`까지의 dependency path와 함께 compiler diagnostic이 난다.
- graph instance를 화면 recomposition마다 만들면 scoped object도 반복 생성될 수 있으므로 graph creation log나 identity를 확인한다.
- provider body가 던지는 예외와 외부 I/O 실패는 compile-time validation 범위 밖이다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Metro dependency graphs](https://zacsweers.github.io/metro/latest/dependency-graphs/), [Metro API](https://zacsweers.github.io/metro/latest/api/)
