---
title: android-data-layer-map
tags: [android, android/data]
aliases: ["Android Data Layer Map"]
date modified: 2026-08-06 15:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Data Layer 는 영속 저장소와 파일 접근 Paging 을 분리한다

Android data layer 는 영속 저장소, 파일 접근, paged loading, 네트워크 클라이언트를 분리해서 읽는다.

데이터를 **어떤 스트림으로 실어 나르는가**(Coroutine/Flow)는 이 클러스터가 아니라 형제 클러스터인 [async-flow](../async-flow/android-coroutines-flow.md) 가 소유한다. Coroutine 과 Flow 는 data 뿐 아니라 jetpack-compose·architecture 도 함께 쓰는 언어·라이브러리 계층이기 때문이다.

### 정본 지도

- [영속 저장소 계약](storage/persistence.md) - Room, DataStore, SQLite, migration.
- [파일 접근 계약](storage/file-access.md) - app-specific files, MediaStore, SAF, Photo Picker, Scoped Storage.
- [Paging Map](paging/paging.md) - PagingSource, Pager, PagingData, cachedIn, LoadState.
- [네트워크 클라이언트 계층 계약](networking/networking.md) - Retrofit/OkHttp 계층 분리, interceptor, suspend 취소, timeout/retry 상태.

### 선행 계약

- [Android Coroutine과 Flow 지도](../async-flow/android-coroutines-flow.md) - 작업 수명, dispatcher, cold/hot stream 선택.
- [Flow와 StateFlow 상태 계약](../async-flow/flow-state/flow-state.md) - repository stream 을 screen state 로 조합하는 지점.

### 읽는 기준

데이터가 시간에 따라 변하면 형제 클러스터의 Flow 계약을 본다. 앱 재시작 뒤에도 남아야 하면 persistence 계약을 본다. 사용자 파일이나 shared media 를 다루면 file access 계약을 본다. 목록이 너무 커서 부분적으로 읽고 그려야 하면 Paging 계약을 본다. 서버 API 호출 자체의 계층 구성과 실패 분류가 궁금하면 네트워크 클라이언트 계층 계약을 본다.
