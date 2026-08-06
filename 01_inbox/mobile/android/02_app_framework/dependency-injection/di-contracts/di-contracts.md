---
title: di-contracts
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## DI 계약은 전역 객체 접근이 아니라 조립 경계다

DI를 읽을 때는 프레임워크 문법보다 세 질문을 먼저 고정한다. **누가 객체를 만드는가**, **어느 component instance가 재사용과 폐기를 소유하는가**, **잘못된 연결은 빌드와 실행 중 언제 드러나는가**다.

### 1. 생성과 binding

- [DI는 전역 조회가 아니라 composition root에서 객체를 조립하는 경계다](./dependency-injection-is-composition-boundary-not-global-object-access.md)
- [소비자는 구체 객체를 만들지 않고 생성자로 요구한다](./consumers-should-declare-dependencies-in-constructors.md)
- [Constructor injection은 소유한 구체 타입의 기본 생성 경로다](./constructor-injection-is-default-binding-path.md)
- [`@Binds`는 생성 가능한 구현을 interface key에 연결한다](./binds-connects-interface-to-implementation-without-construction-code.md)
- [`@Provides`는 외부 타입·설정·런타임 입력의 생성 정책을 캡슐화한다](./provider-methods-create-external-runtime-or-configured-objects.md)
- [Qualifier는 동일한 타입을 의미가 다른 binding key로 분리한다](./qualifiers-distinguish-values-that-share-the-same-type.md)

### 2. 소유권과 scope

- [Scope는 component instance 안의 재사용 계약이다](./scope-matches-object-reuse-to-owner-lifetime.md)
- [Android Context는 graph lifetime과 UI capability에 맞춰 넣는다](./android-context-in-di-must-match-graph-lifetime.md)
- [ViewModel DI는 dependency를 제공하지만 ViewModelStore 소유권을 대신하지 않는다](./viewmodel-di-injects-dependencies-not-viewmodel-ownership.md)
- [Entry point는 Hilt가 소유하지 않는 framework 객체의 제한된 bridge다](./entry-points-bridge-framework-owned-objects-to-the-graph.md)
- [Worker 주입은 WorkManager의 WorkerFactory 경계를 지난다](./worker-injection-crosses-workmanager-factory-boundary.md)
- [DI 테스트는 unit test의 직접 생성과 graph test의 binding 교체를 구분한다](./di-tests-replace-bindings-at-graph-boundary.md)
- [멀티 모듈 graph는 Gradle 의존 방향과 feature API 경계를 따른다](./modular-di-follows-module-dependency-direction-and-feature-entry-contracts.md)
- [Dynamic feature는 base의 provision contract와 설치 뒤 feature graph를 연결한다](./dynamic-feature-di-needs-base-owned-contracts-and-install-boundaries.md)

### 3. 엔진과 검증 시점

- [Dagger는 정적 graph 엔진이며 Android lifecycle 정책은 직접 설계해야 한다](./dagger-is-static-graph-engine-not-android-lifecycle-policy.md)
- [Hilt는 Dagger graph를 표준 Android component hierarchy에 통합한다](./hilt-is-official-android-dagger-integration.md)
- [Koin classic DSL은 runtime resolution이고 compiler plugin을 쓰면 일부 오류를 build에서 검증할 수 있다](./koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience.md)
- [Metro는 Kotlin compiler plugin이 graph를 생성·검증하는 compile-time DI다](./metro-is-compile-time-kotlin-di-not-get-it-style-global-locator.md)
- [Compile-time DI와 runtime DI는 실패가 드러나는 시점과 검증 범위가 다르다](./compile-time-and-runtime-di-fail-at-different-points.md)
- [DSL 문법 자체는 owner와 lifetime을 결정하지 않는다](./dsl-syntax-does-not-change-ownership-lifetime-contracts.md)

### 진단 순서

1. 요청한 타입과 qualifier가 정확히 같은 binding key인지 확인한다.
2. 그 binding을 생성할 constructor, `@Binds`, `@Provides`가 graph에 포함됐는지 확인한다.
3. binding의 scope와 설치 component가 일치하는지 확인한다.
4. Android framework가 생성하는 타입이면 지원 annotation, entry point 또는 factory가 연결됐는지 확인한다.
5. compile-time graph는 compiler diagnostic을, runtime graph는 module verification과 실제 entry flow 테스트를 근거로 삼는다.

상위 문서: [Android 의존성 주입 지도](../android-dependency-injection-map.md)
