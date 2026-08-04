---
title: loadstate-models-refresh-append-and-prepend-ui-states
tags: [android, android/data, android/paging]
aliases: ["LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## LoadState 는 refresh, append, prepend 상태를 UI 에 명시적으로 드러낸다

Paging 의 loading/error UI 는 별도 boolean 몇 개로 흩어뜨리기보다 `LoadState` 로 표현한다. `refresh` 는 초기 또는 전체 갱신, `append` 는 뒤쪽 추가 loading, `prepend` 는 앞쪽 추가 loading 상태를 나타낸다.

각 상태는 loading, error, not loading 을 구분하고 retry UI 와 empty/loading/error surface 를 결정하게 한다. `RemoteMediator` 를 쓰면 source 와 mediator load state 가 나뉘므로, cache 가 비어 있는지와 network sync 중인지를 구분해 표현해야 한다.

```kotlin
adapter.addLoadStateListener { loadState ->
    progressBar.isVisible = loadState.refresh is LoadState.Loading
    retryButton.isVisible = loadState.refresh is LoadState.Error
    emptyView.isVisible =
        loadState.refresh is LoadState.NotLoading && adapter.itemCount == 0
    footerAdapter.loadState = loadState.append
}
```

`loadState.refresh` 가 `LoadState.Error` 이면 `(loadState.refresh as LoadState.Error).error` 로 실제 예외(예: `IOException`, `HttpException`)를 꺼내 메시지를 보여줄 수 있다. `refresh` 상태만 보고 empty view 를 그리면, append 로딩 중 일시적으로 비어 보이는 화면에서도 empty view 가 잘못 뜰 수 있으므로 `adapter.itemCount == 0` 같은 조건을 함께 확인해야 한다.

### 판단 기준

- full-screen loading 은 보통 `refresh` 와 item count 를 함께 보고 결정한다.
- append/prepend loading 은 list footer/header 처럼 기존 content 를 유지한 상태로 표현한다.
- retry 는 실패한 load type 에 맞게 연결하고 전체 새로고침과 page retry 를 섞지 않는다.
- empty state 는 loading 이 끝났고 item 이 없는 상태인지 확인한 뒤 보여준다.

관련 노트: [Android UI State](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-state.md), [RemoteMediator는 network page와 local cache를 연결한다](01_inbox/mobile/android/02_app_framework/data/paging/paging-contracts/remote-mediator-connects-network-pages-to-local-cache.md)

공식 문서: [Manage and present loading states](https://developer.android.com/topic/libraries/architecture/paging/load-state)
