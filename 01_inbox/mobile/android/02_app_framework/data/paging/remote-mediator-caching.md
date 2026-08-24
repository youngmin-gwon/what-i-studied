---
title: remote-mediator-caching
tags: [android, android/data, android/paging]
aliases: ["RemoteMediator는 network page와 local cache를 연결한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## RemoteMediator 는 network page 와 local cache 를 연결한다

`RemoteMediator` 는 network 와 local database 가 함께 있는 layered source 에서 boundary 역할을 한다. UI 는 local cache 에서 읽고, mediator 는 refresh/append/prepend 시점에 network page 를 가져와 database 를 갱신한다.

이 구조에서는 source of truth 가 network response 가 아니라 local database 가 된다. offline, retry, sync indicator, invalidation 정책은 paging 자체보다 persistence 와 synchronization contract 로 같이 판단해야 한다.

```kotlin
@OptIn(ExperimentalPagingApi::class)
class BenefitRemoteMediator(
    private val api: BenefitApi,
    private val db: AppDatabase,
) : RemoteMediator<Int, BenefitEntity>() {
    override suspend fun load(
        loadType: LoadType,
        state: PagingState<Int, BenefitEntity>,
    ): MediatorResult {
        val page = when (loadType) {
            LoadType.REFRESH -> 1
            LoadType.PREPEND -> return MediatorResult.Success(endOfPaginationReached = true)
            LoadType.APPEND -> (state.lastItemOrNull()?.page ?: 1) + 1
        }
        return try {
            val response = api.fetchBenefits(page)
            db.withTransaction {
                if (loadType == LoadType.REFRESH) db.benefitDao().clearAll()
                db.benefitDao().insertAll(response.items.map { it.toEntity(page) })
            }
            MediatorResult.Success(endOfPaginationReached = response.items.isEmpty())
        } catch (e: IOException) {
            MediatorResult.Error(e)
        }
    }
}
```

`db.withTransaction { }` 없이 `clearAll()` 과 `insertAll()` 을 각각 실행하면, 두 호출 사이에 `PagingSource` 가 database 변경을 감지해 잠깐 빈 목록을 읽어 화면이 깜빡이거나, 두 번째 호출이 실패했을 때 `Room` 이 `SQLiteConstraintException` 을 던지며 이미 지운 데이터를 복구하지 못하는 상태로 남을 수 있다. `MediatorResult.Error(e)` 는 `LoadState.Error` 로 전달되어 append/prepend 실패에도 이미 로드된 local cache 는 그대로 유지된다.

### 판단 기준

- network result 는 바로 UI 에 밀어 넣지 말고 transaction 으로 local cache 에 반영한다.
- remote key 는 item table 과 별도로 저장해 refresh/append/prepend 위치를 복원한다.
- cache invalidation 과 stale data 정책은 product 요구에 맞춰 명시한다.
- network error 는 기존 cache 표시와 retry UI 를 동시에 고려한다.

관련 노트: [영속 저장소 계약](../storage/persistence.md), [Room은 누적되고 조회되는 로컬 데이터를 저장한다](../storage/room-local-database.md)
