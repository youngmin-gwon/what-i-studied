---
title: architecture-contracts
tags: [android, android/architecture, android/jetpack]
aliases: ["Architecture Contracts", "Architecture 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Architecture 계약은 layer 이름보다 책임과 수명으로 판단한다

안드로이드 앱 아키텍처 아티팩트는 클래스 패키지 이름이나 단순 3-Layer(UI/Domain/Data) 레이블에 종속되지 않고, **각 구성 요소가 맡은 책임(Responsibility), 수명 주기 소유권(Owner Lifetime), 및 시스템 회수 생존성(Survival Requirements)**에 따라 계약을 판단한다.

---

### 하위 정본 계약 노드

- [Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다](./jetpack-architecture-is-recommended-responsibility-map-not-mandatory-stack.md)
- [아키텍처 결정은 owner, lifetime, survival 요구에서 시작한다](./architecture-decisions-start-from-owner-lifetime-and-survival-requirements.md)
- [UI, domain, data layer는 rendering, policy, source of truth를 분리한다](./ui-domain-data-layers-separate-rendering-policy-and-source-of-truth.md)
- [Jetpack Architecture 문서는 세부 구현을 반복하지 않는 map이어야 한다](./jetpack-architecture-map-links-to-canonical-android-guides.md)

상위 문서: [Jetpack Architecture Map](../android-jetpack-architecture-map.md)
