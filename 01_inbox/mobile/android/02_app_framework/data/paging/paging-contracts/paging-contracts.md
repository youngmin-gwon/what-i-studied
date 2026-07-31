---
title: "Paging Contracts"
tags: [android, android/data, android/paging]
aliases: ["Paging Contracts"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Paging Contracts

Paging 정본은 대량 목록을 “페이지 로딩 알고리즘”이 아니라 source construction, stream lifetime, UI state, local cache synchronization의 경계로 나눈다.

## 정본 노트

- [PagingSource는 한 번에 한 페이지를 읽고 다음 key를 돌려준다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/paging-source-loads-one-page-and-returns-keys.md)
- [Pager는 PagingSource factory로 PagingData Flow를 만든다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/pager-exposes-pagingdata-flow-from-pagingsource-factory.md)
- [cachedIn은 PagingData Flow를 ViewModel 수명에 묶는다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/cachedin-ties-pagingdata-flow-to-viewmodel-lifetime.md)
- [LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/loadstate-models-refresh-append-and-prepend-ui-states.md)
- [Paging item diffing은 identity와 content 비교를 분리한다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/paging-item-identity-and-content-drive-diffing.md)
- [RemoteMediator는 network page와 local cache를 연결한다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/remote-mediator-connects-network-pages-to-local-cache.md)

## 중복 방지 규칙

- Flow의 수집, 공유, `stateIn` 판단은 [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)로 둔다.
- Room/DataStore와 durable source of truth는 [영속 저장소 계약](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)로 둔다.
- ViewModel scope와 화면 상태 조합은 [Android ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md)로 둔다.
