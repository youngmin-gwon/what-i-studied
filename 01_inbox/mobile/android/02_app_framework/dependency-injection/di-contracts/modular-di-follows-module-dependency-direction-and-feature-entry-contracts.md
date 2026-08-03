---
title: modular-di-follows-module-dependency-direction-and-feature-entry-contracts
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:07 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## 멀티 모듈 DI 는 module dependency 방향과 feature entry 계약을 따른다

DI graph 가 모듈 의존성 방향을 거꾸로 만들면 build graph 와 runtime graph 가 충돌한다. base/app module 은 feature 가 요구하는 contract 를 알 수 있어야 하고, feature 는 자신이 소유한 implementation 과 entry 를 명확히 노출해야 한다.

Navigation, dynamic feature, feature API module, implementation module 이 섞일수록 graph 를 하나로 크게 만드는 것보다 boundary 별 dependency contract 를 분리하는 편이 낫다.

관련 노트: [Navigation contracts](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md), [Dynamic feature module](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md).

### 판단 기준

- 모듈화된 프로젝트에서 DI 그래프는 Gradle 모듈 의존성 방향과 일치해야 하며, 피쳐 모듈은 자체적인 내부 DI 를 구성하고 외부에 필요한 의존성만 인터페이스 계약으로 요구해야 한다.

### 경계

- 피쳐 모듈이 애플리케이션 전체의 DI 그래프 확장을 강제하지 않도록, Component Dependencies 나 인터페이스 기반 Entry Point 를 활용해 모듈 간 DI 결합도를 최소화해야 한다.
