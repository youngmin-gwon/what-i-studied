# Scope는 singleton 장식이 아니라 owner lifetime에 맞춘 재사용 계약이다

Scope는 "한 번만 만든다"는 느낌보다 "어떤 graph/component instance 안에서 재사용되는가"를 정의한다. Application scope, Activity scope, ViewModel scope는 서로 다른 owner lifetime을 가진다.

짧은 lifetime 객체를 긴 graph에 넣으면 leak이 생기고, 긴 lifetime 객체를 짧은 graph마다 새로 만들면 cache, connection, observer 정책이 흔들린다. scope를 붙이기 전에는 객체가 누구의 상태를 들고 누구와 함께 사라져야 하는지 먼저 정한다.

관련 노트: [Context lifetime in DI](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/android-context-in-di-must-match-graph-lifetime.md), [ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md).
