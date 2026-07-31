# LoadState는 refresh, append, prepend 상태를 UI에 명시적으로 드러낸다

Paging의 loading/error UI는 별도 boolean 몇 개로 흩어뜨리기보다 `LoadState`로 표현한다. `refresh`는 초기 또는 전체 갱신, `append`는 뒤쪽 추가 loading, `prepend`는 앞쪽 추가 loading 상태를 나타낸다.

각 상태는 loading, error, not loading을 구분하고 retry UI와 empty/loading/error surface를 결정하게 한다. `RemoteMediator`를 쓰면 source와 mediator load state가 나뉘므로, cache가 비어 있는지와 network sync 중인지를 구분해 표현해야 한다.

공식 문서: [Manage and present loading states](https://developer.android.com/topic/libraries/architecture/paging/load-state)
