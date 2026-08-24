---
title: architecture-guide-links
tags: [android, android/architecture, android/jetpack]
aliases: ["Jetpack Architecture 문서는 세부 구현을 반복하지 않는 map이어야 한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Jetpack Architecture 문서는 세부 구현을 반복하지 않는 map이어야 한다

**`Jetpack Architecture` 개요 문서는 개별 기술 라이브러리의 코드 파라미터나 API 상세 설명을 중복 작성하는 장소가 되어서는 안 된다.** 각 도메인별 정본 노트(Canonical Guides)로 신속하고 정확하게 연결하는 **상위 내비게이션 맵(Navigation Decision Map)** 역할을 수행해야 한다.

---

### 1. 개념 및 핵심 명제 (What)

- **단일 정보 출처 ([single source of truth](../../jetpack-compose/runtime/compose-ssot.md) in Knowledge Base)**:
  [viewmodel](../state-management/viewmodel.md), Compose Runtime, Room, [Coroutines](../../data/async-flow/coroutines/kotlin-coroutines.md) 등의 상세 기술 서술은 각 하위 도메인 정본 파일에 단 한 번 작성하며, Architecture Map 은 링크와 의사결정 인과관계만 정리한다.

---

### 2. 관련 문서 및 참조

- 상위 문서: [Architecture Contracts](android-jetpack-architecture-map.md)
- 세부 연결 정본 노트:
  - [Jetpack Architecture Map](android-jetpack-architecture-map.md)
  - [Android State Management](../state-management/android-state-management.md)
  - [Android Context Boundaries](../context/context.md)

검증일: 2026-08-05. 지식 베이스 단일 정보 출처 원칙 검증 완료.
