---
title: "Dynamic feature DI는 base-owned contract와 install boundary를 분리해야 한다"
tags: ["android", "android/app-framework"]
---

# Dynamic feature DI는 base-owned contract와 install boundary를 분리해야 한다

Dynamic feature module은 필요할 때 설치되는 선택 feature unit이다. DI graph가 dynamic feature implementation을 base가 compile time에 직접 알아야만 동작한다면 dynamic delivery의 장점과 충돌한다.

Base module에는 feature entry contract, navigation route, dependency interface처럼 안정적으로 알아야 할 것만 둔다. Dynamic feature 내부 implementation과 binding은 설치 이후 entry boundary에서 연결한다.

관련 노트: [Dynamic feature module](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md).

## 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

## 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime을 먼저 확인한다.
