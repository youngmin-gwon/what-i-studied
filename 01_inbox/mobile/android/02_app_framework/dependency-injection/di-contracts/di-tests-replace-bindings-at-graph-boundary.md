---
title: di-tests-replace-bindings-at-graph-boundary
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 16:30:16 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## DI 테스트는 내부 구현을 건드리지 않고 graph boundary 에서 binding 을 교체한다

DI 가 테스트에 주는 이점은 production code 내부의 생성 코드를 바꾸지 않고 fake, test dispatcher, in-memory database, fake API 를 graph boundary 에서 바꿀 수 있다는 점이다.

테스트가 consumer 내부 필드를 직접 덮어쓰거나 singleton registry 를 공유하면 순서 의존성과 누수가 생긴다. test graph, module replacement, factory injection 처럼 명시적인 교체 지점을 둔다.

### 판단 기준

- 테스트 환경에서는 DI 그래프의 모듈이나 바인딩을 Fake 또는 Mock 객체로 교체하여 경계 밖의 인프라(DB, 네트워킹)를 격리할 수 있어야 한다.

### 경계

- 개별 유닛 테스트에서는 가급적 DI 프레임워크를 띄우지 않고 생성자에 직접 Fake 를 주입하며, Hilt 등 DI 프레임워크를 활용한 바인딩 교체는 통합 테스트나 UI 테스트 범위에서만 사용한다.
