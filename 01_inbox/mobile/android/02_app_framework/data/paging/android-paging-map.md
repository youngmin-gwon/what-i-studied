---
title: android-paging-map
tags: [android, android/data, android/paging]
aliases: ["Android Paging Map"]
date modified: 2026-08-03 18:08:04 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Paging 은 대량 목록을 페이지 단위로 로드하고 UI 에 반영하는 데이터 계약이다

Paging 문서는 대량 목록을 한 번에 모두 읽지 않고 page 단위로 가져와 UI 에 반영하는 data loading 계약을 정리한다. 핵심은 "목록을 어떻게 그릴까"보다 source, cache, load state, item identity 의 책임을 어느 layer 에 둘지다.

### 정본 노트

- [PagingSource는 한 번에 한 페이지를 읽고 다음 key를 돌려준다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/paging-source-loads-one-page-and-returns-keys.md)
- [Pager는 PagingSource factory로 PagingData Flow를 만든다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/pager-exposes-pagingdata-flow-from-pagingsource-factory.md)
- [cachedIn은 PagingData Flow를 ViewModel 수명에 묶는다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/cachedin-ties-pagingdata-flow-to-viewmodel-lifetime.md)
- [LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/loadstate-models-refresh-append-and-prepend-ui-states.md)
- [Paging item diffing은 identity와 content 비교를 분리한다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/paging-item-identity-and-content-drive-diffing.md)
- [RemoteMediator는 network page와 local cache를 연결한다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/remote-mediator-connects-network-pages-to-local-cache.md)

### Layer Boundary

- Repository 는 `PagingSource` 와 `RemoteMediator` 를 통해 data source 와 cache 정책을 소유한다.
- ViewModel 은 `Pager.flow` 를 화면 상태에 연결하고 `cachedIn` 으로 화면 수명 안의 공유 범위를 정한다.
- UI 는 `PagingData` 를 표시하고 `LoadState`, retry, empty state, item identity 를 표현한다.

공식 문서: [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)
