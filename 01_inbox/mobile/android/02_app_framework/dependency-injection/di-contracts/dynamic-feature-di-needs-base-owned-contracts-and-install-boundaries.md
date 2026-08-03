---
title: "Dynamic feature DI는 base-owned contract와 install boundary를 분리해야 한다"
tags: ["android", "android/app-framework"]
---

# Dynamic feature DI는 base-owned contract와 install boundary를 분리해야 한다

Dynamic feature module은 필요할 때 설치되는 선택 feature unit이다. DI graph가 dynamic feature implementation을 base가 compile time에 직접 알아야만 동작한다면 dynamic delivery의 장점과 충돌한다.

Base module에는 feature entry contract, navigation route, dependency interface처럼 안정적으로 알아야 할 것만 둔다. Dynamic feature 내부 implementation과 binding은 설치 이후 entry boundary에서 연결한다.

관련 노트: [Dynamic feature module](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md).

## 판단 기준

- 동적 기능 모듈(Dynamic Feature)의 DI는 베이스 앱이 정의한 Component Contract(인터페이스)에 의존해야 하며, 베이스 모듈은 런타임에 동적으로 컴포넌트를 병합할 수 있어야 한다.

## 경계

- 동적 모듈은 베이스 모듈에 접근할 수 있지만 반대는 불가능하므로, Dagger Component 의존성을 구성할 때 Provision Interface를 활용하거나 Hilt의 `@EntryPoint`를 통해 런타임에 분리된 그래프를 연결해야 한다.
