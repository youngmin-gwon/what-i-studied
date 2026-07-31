# DI graph에 넣는 Android Context는 graph lifetime과 맞아야 한다

`Context`는 단순 dependency가 아니라 resource, service, permission, theme, lifecycle과 연결된 platform capability다. Application graph에는 `applicationContext`처럼 app lifetime과 맞는 Context만 넣어야 한다.

Activity나 Fragment Context를 app-wide graph에 넣으면 화면이 사라진 뒤에도 UI owner가 붙잡힐 수 있다. 반대로 theme, window, UI-bound service가 필요한 작업에는 Application Context가 충분하지 않을 수 있으므로 더 짧은 owner boundary에서 받아야 한다.

관련 정본: [Context boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md).
