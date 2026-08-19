---
title: pager-exposes-pagingdata-flow-from-pagingsource-factory
tags: [android, android/data, android/paging]
aliases: ["Pager는 PagingSource factory로 PagingData Flow를 만든다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Pager 는 PagingSource factory 로 PagingData Flow 를 만든다

`Pager` 는 `PagingConfig` 와 `PagingSource` factory 를 받아 `Flow<PagingData<T>>` 를 노출한다. 이 흐름은 UI 가 직접 page key 를 관리하지 않고, 필요한 시점에 page loading 을 요청하게 만드는 [viewmodel](../../../viewmodel.md)-facing API 다.

Repository 는 `PagingSource` 를 직접 UI 에 노출하기보다 `Pager.flow` 를 제공하고, ViewModel 은 이 flow 를 화면 수명에 맞게 보관한다. 이렇게 하면 source construction, page size, prefetch policy 가 UI rendering 과 분리된다.

```kotlin
class BenefitRepository(private val api: BenefitApi) {
    fun pagedBenefits(): Flow<PagingData<Benefit>> =
        Pager(
            config = PagingConfig(pageSize = 20, prefetchDistance = 5),
            pagingSourceFactory = { BenefitPagingSource(api) }, // 매 refresh마다 새 인스턴스 생성
        ).flow
}
```

`pagingSourceFactory` 는 람다이며, `Pager` 는 refresh 나 invalidate 가 필요할 때마다 이 람다를 다시 호출해 새 `PagingSource` 인스턴스를 만든다. `pagingSourceFactory = { existingSourceInstance }` 처럼 이미 만든 인스턴스를 밖에서 캡처해 재사용하도록 작성하면, 이미 `invalidate()` 된 `PagingSource` 가 다시 반환되어 `Pager` 가 새 로드를 시작하지 못하고 refresh 요청이 조용히 무시되는 형태로 드러난다. 공식 문서는 이 실수를 피하기 위해 factory 람다가 매번 새 인스턴스를 생성하도록 명시한다.

### 판단 기준

- `PagingConfig` 는 page size, prefetch distance, placeholder 정책을 성능과 UX 요구에 맞춘다.
- query/filter 가 바뀌면 새 `Pager` 또는 새 `PagingSource` factory 를 만들어 이전 sequence 를 무효화한다.
- `Pager.flow` 는 cold flow 이므로 화면 수명 안에서 공유하려면 `cachedIn` 을 명시한다.
- UI 는 `PagingSource` 를 직접 호출하지 않고 `PagingData` 를 rendering input 으로 받는다.

관련 노트: [cachedIn은 PagingData Flow를 ViewModel 수명에 묶는다](./cachedin-ties-pagingdata-flow-to-viewmodel-lifetime.md), [Flow와 [stateflow](../../../stateflow-and-sharedflow.md) 상태 계약](../../async-flow/flow-state/flow-state.md)
