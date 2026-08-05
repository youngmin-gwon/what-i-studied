---
title: android-dependency-injection-map
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Android DI Map 은 객체 수명과 프레임워크 경계를 정리하는 지도다

Android DI 문서는 프레임워크별 사용법 목록이 아니라 객체 graph, binding, lifetime, framework boundary 를 정리하는 지도다.

### 읽는 순서

1. [DI는 조립 경계다](./di-contracts/dependency-injection-is-composition-boundary-not-global-object-access.md)
2. [소비자는 생성자로 의존성을 요구한다](./di-contracts/consumers-should-declare-dependencies-in-constructors.md)
3. [scope는 owner lifetime에 맞춘다](./di-contracts/scope-matches-object-reuse-to-owner-lifetime.md)
4. [Context는 graph lifetime과 맞춘다](./di-contracts/android-context-in-di-must-match-graph-lifetime.md)
5. [**Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리)는 공식 Android Dagger 통합 경로다](./di-contracts/hilt-is-official-android-dagger-integration.md)

### Contract Groups

- Graph basics: constructor injection, provider method, binds, qualifier.
- Android boundaries: Context, ViewModel, WorkManager, framework-created class.
- Framework choices: Hilt/Dagger, **Koin**(코드 생성 없이 런타임에 서비스 로케이터 방식으로 의존성을 주입하는 Kotlin 전용 DSL 기반 DI 프레임워크), **Metro**(Kotlin Multiplatform 환경 등에서 컴파일 타임 그래프 검증을 수행하는 정적 DI 프레임워크).
- Project boundaries: tests, multi-module, DSL, dynamic feature.

### Contracts

- [DI는 전역 객체 접근이 아니라 조립 경계다](./di-contracts/dependency-injection-is-composition-boundary-not-global-object-access.md)
- [소비자는 의존성을 생성하지 말고 생성자로 요구한다](./di-contracts/consumers-should-declare-dependencies-in-constructors.md)
- [**Constructor injection**(생성자 주입 — 필요한 의존성을 생성자 매개변수로 명시하여 필수 의존성을 주입받는 기본 주입 방식)은 기본 binding 경로다](./di-contracts/constructor-injection-is-default-binding-path.md)
- [**Provider method**(`@Provides` — 외부 라이브러리 타입이나 런타임 설정 객체의 생성 로직을 명시하는 모듈 메서드)는 외부 타입, 런타임 값, 설정된 객체를 만들 때 쓴다](./di-contracts/provider-methods-create-external-runtime-or-configured-objects.md)
- [Binds는 interface와 implementation을 연결하고 생성 코드는 추가하지 않는다](./di-contracts/binds-connects-interface-to-implementation-without-construction-code.md)
- [**Qualifier**(한정자 — 동일한 타입의 의존성이 여러 개 존재할 때 특정 바인딩 대상을 구별하기 위한 식별 어노테이션)는 같은 타입의 서로 다른 의미를 구분한다](./di-contracts/qualifiers-distinguish-values-that-share-the-same-type.md)
- [**Scope**(스코프 — 의존성 객체의 생명주기를 특정 DI 컨테이너 수명과 일치시켜 재사용을 제어하는 어노테이션)는 singleton 장식이 아니라 owner lifetime에 맞춘 재사용 계약이다](./di-contracts/scope-matches-object-reuse-to-owner-lifetime.md)
- [DI graph에 넣는 Android Context는 graph lifetime과 맞아야 한다](./di-contracts/android-context-in-di-must-match-graph-lifetime.md)
- [Hilt는 Android용 공식 Dagger 통합 경로다](./di-contracts/hilt-is-official-android-dagger-integration.md)
- [Dagger는 정적 graph 엔진이지 Android lifecycle 정책 자체가 아니다](./di-contracts/dagger-is-static-graph-engine-not-android-lifecycle-policy.md)
- [Koin은 런타임 DSL 편의와 정적 graph 검증의 트레이드오프를 가진다](./di-contracts/koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience.md)
- [Compile-time DI와 runtime DI는 실패 시점이 다르다](./di-contracts/compile-time-and-runtime-di-fail-at-different-points.md)
- [Metro는 get_it식 전역 locator가 아니라 compile-time Kotlin DI로 이해한다](./di-contracts/metro-is-compile-time-kotlin-di-not-get-it-style-global-locator.md)
- [ViewModel DI는 dependency 주입이지 ViewModel 소유권을 DI graph로 옮기는 일이 아니다](./di-contracts/viewmodel-di-injects-dependencies-not-viewmodel-ownership.md)
- [**Entry Point**(`@EntryPoint` — 안드로이드 OS가 생성하는 프레임워크 객체에서 Hilt DI 그래프에 접근하기 위한 비상 인터페이스 경계)는 framework-owned 객체와 DI graph를 잇는 예외 경계다](./di-contracts/entry-points-bridge-framework-owned-objects-to-the-graph.md)
- [Worker 주입은 WorkManager factory boundary를 지난다](./di-contracts/worker-injection-crosses-workmanager-factory-boundary.md)
- [DI 테스트는 내부 구현을 건드리지 않고 graph boundary에서 binding을 교체한다](./di-contracts/di-tests-replace-bindings-at-graph-boundary.md)
- [멀티 모듈 DI는 module dependency 방향과 feature entry 계약을 따른다](./di-contracts/modular-di-follows-module-dependency-direction-and-feature-entry-contracts.md)
- [DSL 문법은 ownership과 lifetime 계약을 바꾸지 않는다](./di-contracts/dsl-syntax-does-not-change-ownership-lifetime-contracts.md)
- [Dynamic feature DI는 base-owned contract와 install boundary를 분리해야 한다](./di-contracts/dynamic-feature-di-needs-base-owned-contracts-and-install-boundaries.md)


### DI Contracts
- [DI Contracts](di-contracts/di-contracts.md)
