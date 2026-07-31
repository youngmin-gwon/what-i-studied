# PagingSource는 한 번에 한 페이지를 읽고 다음 key를 돌려준다

`PagingSource`는 paged data의 단일 source와 page loading 방식을 정의한다. `load()`는 현재 key와 load size를 받아 data, `prevKey`, `nextKey` 또는 error를 반환한다.

이 객체는 전체 목록 상태를 소유하지 않는다. 한 번의 load request를 어떻게 수행하고, refresh 이후 어느 key에서 다시 시작할지 계산하는 repository 계층의 boundary다.

공식 문서: [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)
