# Android Dependency Injection Map

Android DI 문서는 프레임워크별 사용법 목록이 아니라 객체 graph, binding, lifetime, framework boundary를 정리하는 지도다.

## 읽는 순서

1. [DI는 조립 경계다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/dependency-injection-is-composition-boundary-not-global-object-access.md)
2. [소비자는 생성자로 의존성을 요구한다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/consumers-should-declare-dependencies-in-constructors.md)
3. [scope는 owner lifetime에 맞춘다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/scope-matches-object-reuse-to-owner-lifetime.md)
4. [Context는 graph lifetime과 맞춘다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/android-context-in-di-must-match-graph-lifetime.md)
5. [Hilt는 공식 Android Dagger 통합 경로다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/hilt-is-official-android-dagger-integration.md)

## Contract Groups

- Graph basics: constructor injection, provider method, binds, qualifier.
- Android boundaries: Context, ViewModel, WorkManager, framework-created class.
- Framework choices: Hilt/Dagger, Koin, Metro.
- Project boundaries: tests, multi-module, DSL, dynamic feature.

## Contracts

- [DI는 전역 객체 접근이 아니라 조립 경계다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/dependency-injection-is-composition-boundary-not-global-object-access.md)
- [소비자는 의존성을 생성하지 말고 생성자로 요구한다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/consumers-should-declare-dependencies-in-constructors.md)
- [Constructor injection은 기본 binding 경로다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/constructor-injection-is-default-binding-path.md)
- [Provider method는 외부 타입, 런타임 값, 설정된 객체를 만들 때 쓴다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/provider-methods-create-external-runtime-or-configured-objects.md)
- [Binds는 interface와 implementation을 연결하고 생성 코드는 추가하지 않는다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/binds-connects-interface-to-implementation-without-construction-code.md)
- [Qualifier는 같은 타입의 서로 다른 의미를 구분한다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/qualifiers-distinguish-values-that-share-the-same-type.md)
- [Scope는 singleton 장식이 아니라 owner lifetime에 맞춘 재사용 계약이다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/scope-matches-object-reuse-to-owner-lifetime.md)
- [DI graph에 넣는 Android Context는 graph lifetime과 맞아야 한다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/android-context-in-di-must-match-graph-lifetime.md)
- [Hilt는 Android용 공식 Dagger 통합 경로다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/hilt-is-official-android-dagger-integration.md)
- [Dagger는 정적 graph 엔진이지 Android lifecycle 정책 자체가 아니다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/dagger-is-static-graph-engine-not-android-lifecycle-policy.md)
- [Koin은 런타임 DSL 편의와 정적 graph 검증의 트레이드오프를 가진다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience.md)
- [Compile-time DI와 runtime DI는 실패 시점이 다르다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/compile-time-and-runtime-di-fail-at-different-points.md)
- [Metro는 get_it식 전역 locator가 아니라 compile-time Kotlin DI로 이해한다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/metro-is-compile-time-kotlin-di-not-get-it-style-global-locator.md)
- [ViewModel DI는 dependency 주입이지 ViewModel 소유권을 DI graph로 옮기는 일이 아니다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/viewmodel-di-injects-dependencies-not-viewmodel-ownership.md)
- [Entry point는 framework-owned 객체와 DI graph를 잇는 예외 경계다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/entry-points-bridge-framework-owned-objects-to-the-graph.md)
- [Worker 주입은 WorkManager factory boundary를 지난다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/worker-injection-crosses-workmanager-factory-boundary.md)
- [DI 테스트는 내부 구현을 건드리지 않고 graph boundary에서 binding을 교체한다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/di-tests-replace-bindings-at-graph-boundary.md)
- [멀티 모듈 DI는 module dependency 방향과 feature entry 계약을 따른다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/modular-di-follows-module-dependency-direction-and-feature-entry-contracts.md)
- [DSL 문법은 ownership과 lifetime 계약을 바꾸지 않는다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/dsl-syntax-does-not-change-ownership-lifetime-contracts.md)
- [Dynamic feature DI는 base-owned contract와 install boundary를 분리해야 한다](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/dynamic-feature-di-needs-base-owned-contracts-and-install-boundaries.md)
