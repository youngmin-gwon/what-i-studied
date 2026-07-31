# LocalContext는 Composition에서 읽는 Android Context이지 Flutter BuildContext가 아니다

`LocalContext.current`는 Compose tree를 통해 전달되는 현재 Android `Context`다. resource formatting, toast, activity start 같은 UI event 근처의 Android API 호출에 사용할 수 있다.

이 값은 Flutter의 `BuildContext`와 같지 않다. Flutter `BuildContext`는 widget이 element tree에서 어디에 있는지를 나타내는 handle이고, Android `Context`는 platform environment capability다. 둘 다 유효 수명 밖에서 쓰면 문제가 되지만, 소유 모델과 실패 방식은 다르다.

`LocalContext`를 ViewModel이나 repository에 넘겨 장기 보관하면 Compose의 explicit state/data flow가 흐려진다. 필요한 값이나 action을 좁게 만들어 전달하고, long-lived dependency에는 application context나 abstraction을 사용한다.

관련 노트: [Context 기본 경계](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-is-android-environment-capability-not-dependency-container.md), [Compose runtime 정본](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [ViewModel/Repository Context 경계](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/viewmodel-and-repository-should-not-retain-ui-context.md).

공식 문서: [CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal)
