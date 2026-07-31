# 안드로이드 앱 컴포넌트는 OS가 호출하는 실행 경계다

Android 앱 컴포넌트는 앱 내부 객체 모델이 아니라 OS가 앱을 시작하거나 앱과 상호작용할 때 찾는 entry point다.

고전적인 네 가지 컴포넌트는 Activity, Service, BroadcastReceiver, ContentProvider다. Android 앱은 하나의 `main()`에서만 시작하지 않고, Manifest와 Intent, Binder, URI 같은 외부 계약을 통해 여러 지점에서 프로세스가 만들어지고 코드가 호출될 수 있다.

그래서 앱 아키텍처에서 컴포넌트는 비즈니스 로직의 집이 아니라 경계 어댑터로 보는 편이 안전하다. Activity는 화면과 lifecycle을 연결하고, Service는 UI 없는 작업 경계를 제공하며, Receiver는 짧은 이벤트를 받아 후속 작업을 위임하고, Provider는 URI 기반 데이터 접근 계약을 공개한다.

App Functions 같은 최신 agent/assistant surface는 별도 플랫폼 capability다. 고전적인 네 컴포넌트 목록에 억지로 섞기보다 [assistant/agent 정본](01_inbox/mobile/android/04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)으로 연결한다.

관련 노트: [컴포넌트 통신 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary.md), [수명 기준 아키텍처 결정](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/architecture-contracts/architecture-decisions-start-from-owner-lifetime-and-survival-requirements.md).

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
