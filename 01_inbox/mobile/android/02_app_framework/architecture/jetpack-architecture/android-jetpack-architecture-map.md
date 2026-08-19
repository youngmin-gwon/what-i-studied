---
title: android-jetpack-architecture-map
tags: [android, android/architecture, android/jetpack]
aliases: ["Jetpack Architecture Map"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Jetpack Architecture Map 은 세부 API 설명보다 기존 정본으로 연결하는 decision map 이다

**`Jetpack Architecture Map` 은 Jetpack 의 개별 라이브러리 개요를 나열하는 카탈로그가 아니며, 애플리케이션 아키텍처 설계 시 수명(Lifetime), 관심사 분리(SoC), 단방향 데이터 흐름(UDF) 계약에 따라 최적의 기술을 선택하도록 안내하는 의사결정 지도(Decision Map)**다.

---

### 1. 정본 계약 노드 하위 지형도

- [Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다](./architecture/jetpack-architecture-is-recommended-responsibility-map-not-mandatory-stack.md)
- [아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다](./architecture/architecture-decisions-start-from-owner-lifetime-and-survival-requirements.md)
- [UI, domain, data layer는 rendering, policy, source of truth를 분리한다](./architecture/ui-domain-data-layers-separate-rendering-policy-and-source-of-truth.md)
- [Jetpack Architecture 문서는 세부 구현을 반복하지 않는 map이어야 한다](./architecture/jetpack-architecture-map-links-to-canonical-android-guides.md)

---

### 2. 세부 도메인별 정본 맵

1. **UI & State Holder**:
   - [Jetpack Compose UI & State](../../jetpack-compose/state-and-lifecycle/compose-state-and-effect/compose-state-and-effect.md)
   - [ViewModel & State Flow](../state-management/viewmodel/viewmodel.md)
2. **Data & Async Stream**:
   - [Kotlin Coroutines & Flow](../../data/async-flow/coroutines/coroutine.md)
   - [Persistence (Room / DataStore)](../../data/storage/persistence/persistence.md)
3. **Dependency Injection**:
   - [Android Dependency Injection (Hilt / Dagger)](../../dependency-injection/android-dependency-injection-map.md)
4. **Navigation & Multiplatform**:
   - [Navigation 3 Contracts](../../navigation/navigation3/navigation3/navigation3.md)
   - [Multiplatform Contracts](../multiplatform/multiplatform.md)

---

### 3. 참고 및 공식 문서

- 상위 문서: [Android App Architecture](../android-app-architecture.md)
- 공식 가이드: [Android Jetpack Architecture](https://developer.android.com/jetpack/guide)

검증일: 2026-08-05. Jetpack 아키텍처 Decision Map 구조 대조 확인 완료.
