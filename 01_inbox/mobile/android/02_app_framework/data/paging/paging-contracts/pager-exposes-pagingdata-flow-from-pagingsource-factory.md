---
title: "Pager는 PagingSource factory로 PagingData Flow를 만든다"
tags: [android, android/data, android/paging]
aliases: ["Pager는 PagingSource factory로 PagingData Flow를 만든다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Pager는 PagingSource factory로 PagingData Flow를 만든다

`Pager`는 `PagingConfig`와 `PagingSource` factory를 받아 `Flow<PagingData<T>>`를 노출한다. 이 흐름은 UI가 직접 page key를 관리하지 않고, 필요한 시점에 page loading을 요청하게 만드는 ViewModel-facing API다.

Repository는 `PagingSource`를 직접 UI에 노출하기보다 `Pager.flow`를 제공하고, ViewModel은 이 flow를 화면 수명에 맞게 보관한다. 이렇게 하면 source construction, page size, prefetch policy가 UI rendering과 분리된다.

## 판단 기준

- `PagingConfig`는 page size, prefetch distance, placeholder 정책을 성능과 UX 요구에 맞춘다.
- query/filter가 바뀌면 새 `Pager` 또는 새 `PagingSource` factory를 만들어 이전 sequence를 무효화한다.
- `Pager.flow`는 cold flow이므로 화면 수명 안에서 공유하려면 `cachedIn`을 명시한다.
- UI는 `PagingSource`를 직접 호출하지 않고 `PagingData`를 rendering input으로 받는다.

관련 노트: [cachedIn은 PagingData Flow를 ViewModel 수명에 묶는다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/cachedin-ties-pagingdata-flow-to-viewmodel-lifetime.md), [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)
