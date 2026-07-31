# Android Paging Map

Paging 문서는 대량 목록을 한 번에 모두 읽지 않고, page 단위로 가져와 UI에 반영하는 data loading 계약을 정리한다.

## 정본 노트

- [PagingSource는 한 번에 한 페이지를 읽고 다음 key를 돌려준다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/paging-source-loads-one-page-and-returns-keys.md)
- [Pager는 PagingSource factory로 PagingData Flow를 만든다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/pager-exposes-pagingdata-flow-from-pagingsource-factory.md)
- [cachedIn은 PagingData Flow를 ViewModel 수명에 묶는다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/cachedin-ties-pagingdata-flow-to-viewmodel-lifetime.md)
- [LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/loadstate-models-refresh-append-and-prepend-ui-states.md)
- [Paging item diffing은 identity와 content 비교를 분리한다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/paging-item-identity-and-content-drive-diffing.md)
- [RemoteMediator는 network page와 local cache를 연결한다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/remote-mediator-connects-network-pages-to-local-cache.md)

## Layer Boundary

- Repository: [PagingSource](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/paging-source-loads-one-page-and-returns-keys.md)와 source construction.
- ViewModel: [Pager/PagingData Flow](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/pager-exposes-pagingdata-flow-from-pagingsource-factory.md)와 [cachedIn](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/cachedin-ties-pagingdata-flow-to-viewmodel-lifetime.md).
- UI: [LoadState](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/loadstate-models-refresh-append-and-prepend-ui-states.md)와 item identity/diffing.

공식 문서: [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)
