# Pager는 PagingSource factory로 PagingData Flow를 만든다

`Pager`는 `PagingConfig`와 `PagingSource` factory를 받아 `Flow<PagingData<T>>`를 노출한다. 이 흐름은 UI가 직접 page key를 관리하지 않고, 필요한 시점에 page loading을 요청하게 만드는 ViewModel-facing API다.

Repository는 `PagingSource`를 직접 UI에 노출하기보다 `Pager.flow`를 제공하고, ViewModel은 이 flow를 화면 수명에 맞게 보관한다. 이렇게 하면 source construction, page size, prefetch policy가 UI rendering과 분리된다.

관련 노트: [Flow state contracts](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md).
