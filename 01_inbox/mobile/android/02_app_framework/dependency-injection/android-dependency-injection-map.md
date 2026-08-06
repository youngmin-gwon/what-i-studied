---
title: android-dependency-injection-map
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 15:22:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Android DI Map 은 객체 수명과 프레임워크 경계를 정리하는 지도다

Android DI 문서는 프레임워크별 사용법 목록이 아니라 객체 graph, binding, lifetime, framework boundary 를 정리하는 지도다.

### 읽는 순서

1. DI의 기본 계약과 컴파일 타임 안전성을 먼저 이해한다.
2. 프레임워크 생명주기(Android Context, [viewmodel](../viewmodel.md), Worker)와 DI가 만나는 경계를 파악한다.
3. 멀티 모듈, Dynamic feature, 테스트 환경에서의 교체 전략을 이해한다.

### Contract Groups

- Graph basics: constructor injection, provider method, binds, qualifier.
- Android boundaries: Context, ViewModel, WorkManager, framework-created class.
- Framework choices: Hilt/Dagger, **Koin**, **Metro**.
- Project boundaries: tests, multi-module, DSL, dynamic feature.

### DI Contracts

모든 세부 원칙은 3개의 문서로 통합되었다:
- [DI 바인딩과 생성 계약](di-contracts/di-binding-creation-contracts.md)
- [DI 소유권과 스코프 계약](di-contracts/di-ownership-scope-contracts.md)
- [DI 도구 및 엔진 비교](di-contracts/di-tool-comparison.md)

### 상위 문서
- [DI Contracts 전체 보기](di-contracts/di-contracts.md)
