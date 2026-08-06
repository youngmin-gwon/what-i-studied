---
title: android-paging-map
tags: [android, android/data, android/paging]
aliases: ["Android Paging Map"]
date modified: 2026-08-06 15:25:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Paging 은 대량 목록을 페이지 단위로 로드하고 UI 에 반영하는 데이터 계약이다

Paging 문서는 대량 목록을 한 번에 모두 읽지 않고 page 단위로 가져와 UI 에 반영하는 data loading 계약을 정리한다. 핵심은 "목록을 어떻게 그릴까"보다 source, cache, load state, item identity 의 책임을 어느 layer 에 둘지다.

### 정본 묶음

[Paging contracts](./paging-contracts/paging-contracts.md)가 `PagingSource`, `Pager`, `cachedIn`, `LoadState`, item identity, `RemoteMediator`의 읽는 순서와 원자 노트 목록을 소유한다. 이 상위 지도는 Data Layer에서 Paging이 맡는 경계만 설명하며 같은 목록을 반복하지 않는다.

### Layer Boundary

- Repository 는 `PagingSource` 와 `RemoteMediator` 를 통해 data source 와 cache 정책을 소유한다.
- ViewModel 은 `Pager.flow` 를 화면 상태에 연결하고 `cachedIn` 으로 화면 수명 안의 공유 범위를 정한다.
- UI 는 `PagingData` 를 표시하고 `LoadState`, retry, empty state, item identity 를 표현한다.

공식 문서: [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)
