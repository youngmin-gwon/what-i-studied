# Activity Context는 window와 theme를 가지지만 수명이 짧다

Activity context는 현재 화면 인스턴스의 theme, window, configuration, lifecycle 경계를 포함한다. dialog, layout inflation, themed resource, activity launch처럼 UI 환경이 필요한 작업에는 Activity context가 맞다.

하지만 Activity context의 수명은 화면 인스턴스와 함께 끝난다. singleton, repository, static cache, 오래 살아남는 coroutine이나 callback이 Activity context를 잡고 있으면 destroyed Activity가 계속 reachable해질 수 있다.

UI 작업은 UI layer에서 처리하고, 오래 사는 객체에는 Context 대신 필요한 값이나 좁은 인터페이스를 주입한다. Activity context를 application context로 바꿔 leak만 막는 것은 설계 해결이 아닐 수 있다.

관련 노트: [Activity lifecycle 콜백](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/activity-lifecycle-callbacks-describe-visibility-and-interaction-boundaries.md), [ViewModel/Repository Context 경계](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/viewmodel-and-repository-should-not-retain-ui-context.md), [Context leak 경계](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/context-contracts/context-leaks-happen-when-reference-outlives-component-lifetime.md).

공식 문서: [Context reference](https://developer.android.com/reference/android/content/Context)
