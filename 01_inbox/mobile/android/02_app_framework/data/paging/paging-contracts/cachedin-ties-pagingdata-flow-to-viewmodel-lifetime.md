# cachedIn은 PagingData Flow를 ViewModel 수명에 묶는다

`cachedIn(viewModelScope)`는 같은 화면 수명 안에서 paging stream을 공유하고 configuration change 등으로 collector가 바뀌어도 불필요한 reload를 줄이기 위한 boundary다.

`cachedIn`은 영구 cache가 아니다. ViewModel scope가 끝나면 해당 paging stream도 끝난다. 앱 재시작 뒤에도 남아야 하는 데이터는 Room, DataStore, file storage 같은 persistence contract에서 다룬다.

관련 노트: [ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [Persistence contracts](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md).
