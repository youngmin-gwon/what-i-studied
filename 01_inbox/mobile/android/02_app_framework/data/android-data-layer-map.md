---
title: android-data-layer-map
tags: [android, android/data]
aliases: ["Android Data Layer Map"]
date modified: 2026-08-03 18:09:16 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Data Layer 는 데이터 흐름과 영속 저장소 Paging 을 분리한다

Android data layer 는 원천 데이터 흐름, 영속 저장소, 파일 접근, paged loading 을 분리해서 읽는다.

### 정본 지도

- [Flow와 StateFlow 상태 계약](./async-flow/flow-state-contracts/flow-state-contracts.md) - repository stream 과 screen state 조합.
- [영속 저장소 계약](./storage/persistence-contracts/persistence-contracts.md) - Room, DataStore, SQLite, migration.
- [파일 접근 계약](./storage/file-access-contracts/file-access-contracts.md) - app-specific files, MediaStore, SAF, Photo Picker, Scoped Storage.
- [Paging Map](./paging/android-paging-map.md) - PagingSource, Pager, PagingData, cachedIn, LoadState.

### 읽는 기준

데이터가 시간에 따라 변하면 Flow 계약을 본다. 앱 재시작 뒤에도 남아야 하면 persistence 계약을 본다. 사용자 파일이나 shared media 를 다루면 file access 계약을 본다. 목록이 너무 커서 부분적으로 읽고 그려야 하면 Paging 계약을 본다.
