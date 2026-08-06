---
title: qualifiers-distinguish-values-that-share-the-same-type
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Qualifier 는 같은 타입의 서로 다른 의미를 구분한다

DI graph 는 타입만으로 binding 을 찾는 경우가 많다. 같은 `String`, `CoroutineDispatcher`, `OkHttpClient`, `Context` 가 여러 의미로 존재하면 타입만으로는 어떤 값을 넣어야 하는지 알 수 없다.

**Qualifier**(한정자 — 동일한 타입의 의존성이 여러 개 존재할 때 특정 바인딩 대상을 구별하기 위한 식별 어노테이션) 는 같은 타입의 값을 의미별로 분리하는 이름표다. `@ApplicationContext` 와 `@ActivityContext`, `@IoDispatcher` 와 `@MainDispatcher` 처럼 lifetime 이나 역할이 다른 값을 구분할 때 사용한다.

### 최소 예시

```kotlin
@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class IoDispatcher

@Provides
@IoDispatcher
fun provideIoDispatcher(): CoroutineDispatcher = Dispatchers.IO

class RefreshFeed @Inject constructor(
    @IoDispatcher private val dispatcher: CoroutineDispatcher,
)
```

binding key는 단순 `CoroutineDispatcher`가 아니라 `@IoDispatcher CoroutineDispatcher`다. 요청과 제공 중 한쪽에서 qualifier를 빼면 다른 key가 되어 missing binding이 발생한다. 동일 key를 둘 제공하면 duplicate binding이 된다.

문자열 기반 `@Named("io")`도 가능하지만 rename 안전성과 의미 검색이 중요한 공용 경계에서는 사용자 정의 qualifier가 더 명시적이다. 하나의 dependency 요청에 qualifier 여러 개를 조합하지 않는다.

관련 노트: [Context boundaries](../../architecture/context-and-modularity/android-context-boundaries.md)

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Dagger qualifiers](https://dagger.dev/dev-guide/basic-usage#qualifiers)
