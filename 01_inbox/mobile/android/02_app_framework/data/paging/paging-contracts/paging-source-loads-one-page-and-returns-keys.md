---
title: paging-source-loads-one-page-and-returns-keys
tags: [android, android/data, android/paging]
aliases: ["PagingSource는 한 번에 한 페이지를 읽고 다음 key를 돌려준다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## PagingSource 는 한 번에 한 페이지를 읽고 다음 key 를 돌려준다

`PagingSource` 는 paged data 의 단일 source 와 page loading 방식을 정의한다. `load()` 는 현재 key 와 load size 를 받아 data, `prevKey`, `nextKey` 또는 error 를 반환한다.

이 객체는 전체 목록 상태를 소유하지 않는다. 한 번의 load request 를 어떻게 수행하고, refresh 이후 어느 key 에서 다시 시작할지 계산하는 repository 계층의 boundary 다.

```kotlin
class BenefitPagingSource(
    private val api: BenefitApi,
) : PagingSource<Int, Benefit>() {
    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, Benefit> {
        val page = params.key ?: 1
        return try {
            val response = api.fetchBenefits(page = page, size = params.loadSize)
            LoadResult.Page(
                data = response.items,
                prevKey = if (page == 1) null else page - 1,
                nextKey = if (response.items.isEmpty()) null else page + 1,
            )
        } catch (e: IOException) {
            LoadResult.Error(e)
        }
    }

    override fun getRefreshKey(state: PagingState<Int, Benefit>): Int? =
        state.anchorPosition?.let { anchor ->
            state.closestPageToPosition(anchor)?.prevKey?.plus(1)
        }
}
```

`load()` 가 `LoadResult.Error(e)` 를 반환하면 UI 쪽 `LoadState.Error` 로 전달되어 retry 버튼을 그릴 수 있다. 반대로 예외를 그대로 던지면 Paging 라이브러리가 이를 잡아 같은 `LoadState.Error` 로 변환하지만, 어떤 예외를 error 로 다룰지 명시적으로 잡지 않으면 `CancellationException` 처럼 취소를 나타내는 예외까지 오류로 잘못 표시될 위험이 있다.

### 판단 기준

- page key 는 API cursor, page number, database position 중 source 계약에 맞는 값을 사용한다.
- `load()` 는 실패를 숨기지 않고 `LoadResult.Error` 로 전달해 retry 경로를 열어 둔다.
- invalidate 는 source data 가 바뀌어 기존 page sequence 가 더 이상 유효하지 않을 때 사용한다.
- UI state 나 selection state 를 `PagingSource` 안에 넣지 않는다.

관련 노트: [Pager는 PagingSource factory로 PagingData Flow를 만든다](./pager-exposes-pagingdata-flow-from-pagingsource-factory.md)

공식 문서: [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)
