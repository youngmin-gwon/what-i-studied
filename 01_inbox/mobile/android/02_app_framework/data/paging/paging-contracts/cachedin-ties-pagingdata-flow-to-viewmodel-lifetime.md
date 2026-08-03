---
title: cachedin-ties-pagingdata-flow-to-viewmodel-lifetime
tags: [android, android/data, android/paging]
aliases: ["cachedIn은 PagingData Flow를 ViewModel 수명에 묶는다"]
date modified: 2026-08-03 18:07:50 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## cachedIn 은 PagingData Flow 를 ViewModel 수명에 묶는다

`cachedIn(viewModelScope)` 는 같은 화면 수명 안에서 paging stream 을 공유하고 configuration change 등으로 collector 가 바뀌어도 불필요한 reload 를 줄이기 위한 boundary 다.

`cachedIn` 은 영구 cache 가 아니다. ViewModel scope 가 끝나면 해당 paging stream 도 끝난다. 앱 재시작 뒤에도 남아야 하는 데이터는 Room, DataStore, file storage 같은 persistence contract 에서 다룬다.

### 판단 기준

- 같은 화면의 여러 collector 가 같은 paging generation 을 봐야 하면 `cachedIn` 을 사용한다.
- process death 뒤 복원되어야 하는 데이터는 `cachedIn` 이 아니라 local database 나 saved state 로 설계한다.
- `cachedIn` 을 repository singleton scope 에 무심코 두면 query 별 메모리와 lifetime 이 과하게 커질 수 있다.
- UI event 나 selection state 는 `PagingData` cache 와 별도로 둔다.

관련 노트: [Android ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [영속 저장소 계약](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)
