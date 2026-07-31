# ViewModel DI는 dependency 주입이지 ViewModel 소유권을 DI graph로 옮기는 일이 아니다

ViewModel은 화면 상태 owner이며 lifecycle은 ViewModelStoreOwner가 관리한다. DI framework는 ViewModel이 필요로 하는 Repository, UseCase, dispatcher, saved state collaborator를 제공할 수 있지만, ViewModel 생명주기 자체를 임의의 app graph singleton으로 바꾸면 안 된다.

Hilt의 `@HiltViewModel`이나 수동 `ViewModelProvider.Factory`는 DI graph와 ViewModel owner 사이의 연결 boundary다. Compose에서 ViewModel을 얻을 때도 screen owner와 navigation back stack owner를 먼저 확인해야 한다.

관련 노트: [ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [Compose runtime/state](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md).
