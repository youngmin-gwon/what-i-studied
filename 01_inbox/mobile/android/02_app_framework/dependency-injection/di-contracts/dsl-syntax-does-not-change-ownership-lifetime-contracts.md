---
title: dsl-syntax-does-not-change-ownership-lifetime-contracts
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## DSL 문법은 ownership 과 lifetime 계약을 바꾸지 않는다
배경 지식: [메모리 레이아웃 및 캐시](../../../../../../02_references/computer-science/memory-layout-and-cache.md)

Compose, Gradle Kotlin DSL, **Koin**(코드 생성 없이 런타임에 서비스 로케이터 방식으로 의존성을 주입하는 Kotlin 전용 DSL 기반 DI 프레임워크) DSL, Navigation DSL 은 선언을 읽기 쉽게 만들지만 owner 와 lifetime 을 자동으로 올바르게 만들어 주지는 않는다. DSL 안에 쓰였다는 이유만으로 state, graph, route, build configuration 의 책임이 사라지지 않는다.

DI/Navigation 관련 DSL 을 볼 때는 문법보다 "무엇을 선언하는가", "누가 실행하는가", "언제 생성되고 언제 사라지는가", "어느 모듈이 이 이름을 알 수 있는가"를 먼저 본다.

관련 노트: [Navigation contracts](../../navigation/navigation-contracts/navigation-contracts.md).

### 판단 기준

- Koin 같은 DSL 기반 DI 를 사용하더라도 객체의 소유권과 생명주기 관리라는 DI 본질적 계약은 달라지지 않는다. 모듈 선언 구문이 다를 뿐 메모리 관리 책임은 여전히 구조적 스코프에 있다.

### 경계

- 런타임 DSL 방식은 컴파일 타임에 누락을 잡지 못하므로, 앱 구동 시점이나 테스트 환경에서 모듈 간 의존성 연결(CheckModules 등)이 완전한지 조기에 검증해야 한다.


### Detailed Contracts
- [di-tests-replace-bindings-at-graph-boundary.md](di-tests-replace-bindings-at-graph-boundary.md)
- [scope-matches-object-reuse-to-owner-lifetime.md](scope-matches-object-reuse-to-owner-lifetime.md)
- [viewmodel-di-injects-dependencies-not-viewmodel-ownership.md](viewmodel-di-injects-dependencies-not-viewmodel-ownership.md)
- [dagger-is-static-graph-engine-not-android-lifecycle-policy.md](dagger-is-static-graph-engine-not-android-lifecycle-policy.md)
- [koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience.md](koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience.md)
- [metro-is-compile-time-kotlin-di-not-get-it-style-global-locator.md](metro-is-compile-time-kotlin-di-not-get-it-style-global-locator.md)
- [di-contracts.md](di-contracts.md)
- [binds-connects-interface-to-implementation-without-construction-code.md](binds-connects-interface-to-implementation-without-construction-code.md)
- [dependency-injection-is-composition-boundary-not-global-object-access.md](dependency-injection-is-composition-boundary-not-global-object-access.md)
- [compile-time-and-runtime-di-fail-at-different-points.md](compile-time-and-runtime-di-fail-at-different-points.md)
- [hilt-is-official-android-dagger-integration.md](hilt-is-official-android-dagger-integration.md)
- [entry-points-bridge-framework-owned-objects-to-the-graph.md](entry-points-bridge-framework-owned-objects-to-the-graph.md)
- [android-context-in-di-must-match-graph-lifetime.md](android-context-in-di-must-match-graph-lifetime.md)
- [constructor-injection-is-default-binding-path.md](constructor-injection-is-default-binding-path.md)
- [worker-injection-crosses-workmanager-factory-boundary.md](worker-injection-crosses-workmanager-factory-boundary.md)
- [qualifiers-distinguish-values-that-share-the-same-type.md](qualifiers-distinguish-values-that-share-the-same-type.md)
- [provider-methods-create-external-runtime-or-configured-objects.md](provider-methods-create-external-runtime-or-configured-objects.md)
- [modular-di-follows-module-dependency-direction-and-feature-entry-contracts.md](modular-di-follows-module-dependency-direction-and-feature-entry-contracts.md)
- [consumers-should-declare-dependencies-in-constructors.md](consumers-should-declare-dependencies-in-constructors.md)
- [dynamic-feature-di-needs-base-owned-contracts-and-install-boundaries.md](dynamic-feature-di-needs-base-owned-contracts-and-install-boundaries.md)
