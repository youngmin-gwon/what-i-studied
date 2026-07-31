# DI는 전역 객체 접근이 아니라 조립 경계다

Dependency Injection의 핵심은 필요한 객체를 소비자가 직접 만들거나 전역 registry에서 꺼내지 않고, 바깥 조립 경계에서 연결해 넣는 것이다. 이렇게 해야 객체 생성 정책, 테스트 대체, lifetime이 사용 코드와 분리된다.

Android에서는 이 조립 경계가 `Application`, feature entry, screen owner, Worker factory처럼 OS/framework lifetime과 만나는 지점에 놓인다. DI framework 선택보다 먼저 정해야 하는 것은 어떤 객체가 어떤 owner 아래에서 만들어지고 재사용되는가다.

관련 노트: [app architecture](01_inbox/mobile/android/02_app_framework/architecture/android-app-architecture.md), [Context boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md).
