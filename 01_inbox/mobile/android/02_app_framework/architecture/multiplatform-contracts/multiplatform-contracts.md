---
title: multiplatform-contracts
tags: [android, android/architecture, android/multiplatform]
aliases: ["Multiplatform Contracts"]
date modified: 2026-08-06 14:50:00 +09:00
date created: 2026-08-05 10:00:00 +09:00
---

## Multiplatform Contracts 는 Android 전용 아키텍처와 달리 공유 경계 자체를 계약으로 다룬다

[Android 앱 아키텍처](../android-app-architecture.md)와 [Jetpack Architecture Map](../jetpack-architecture/android-jetpack-architecture-map.md)은 Activity/ViewModel/Repository 가 전부 Android 프로세스 하나 안에서 동작한다고 전제하고 owner·lifetime·survival 을 다룬다. Kotlin Multiplatform(KMP)은 이 전제 자체를 하나 더 쪼갠다 — "이 코드를 여러 플랫폼이 함께 쓸 것인가, 이 플랫폼만 쓸 것인가"라는 경계 결정이 아키텍처 결정보다 먼저 온다. 이 클러스터는 그 경계가 어디서 그어지고(무엇을 공유하는지) 어떤 메커니즘으로 강제되는지(`expect`/`actual`)를 다룬다.

### 정본 노트

- **Kotlin Multiplatform은 공유 로직과 플랫폼 UI 또는 Compose Multiplatform 공유 UI를 선택할 수 있다**
- [expect/actual은 공통 코드가 플랫폼별 구현을 요구하는 컴파일 타임 계약이다](./expect-actual-is-compile-time-contract-for-platform-specific-implementation.md)

### 읽는 기준

KMP 가 정확히 무엇을 공유하고 무엇을 공유하지 않는지, Compose Multiplatform 을 켜야 하는지 궁금하면 첫 번째 노트로 간다. `commonMain` 에서 플랫폼별 구현이 실제로 필요할 때 그 경계를 코드로 어떻게 표현하는지 궁금하면 두 번째 노트로 간다.

### 중복 방지 규칙

- 순수 Android 전용 앱의 owner/lifetime 기반 아키텍처 결정 자체는 [Architecture Contracts](../jetpack-architecture/architecture-contracts/architecture-contracts.md) 에 둔다. 이 클러스터는 그 결정 이전에 오는 "여러 플랫폼이 이 코드를 공유하는가"라는 경계 질문만 다룬다.
- `Context` 의 종류·lifetime·leak 위험 자체는 [Context Contracts](../context-and-modularity/context-contracts/context-contracts.md) 에 둔다. 이 클러스터는 `Context` 가 왜 `commonMain` 에 직접 등장할 수 없는지, 그 경계를 `expect`/`actual` 로 어떻게 넘기는지만 다룬다.
- DI 그래프 구성, scope, Hilt/Metro 바인딩은 [DI Contracts](../../dependency-injection/di-contracts/di-contracts.md) 에 둔다. `expect`/`actual` 은 런타임 그래프가 아니라 컴파일 타임에 타겟별로 고정되는 계약이라는 차이만 여기서 다룬다.

상위 지도: [Android App Architecture](../android-app-architecture.md)
