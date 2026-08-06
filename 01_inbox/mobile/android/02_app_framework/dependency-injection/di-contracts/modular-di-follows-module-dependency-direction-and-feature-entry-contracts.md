---
title: modular-di-follows-module-dependency-direction-and-feature-entry-contracts
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## 멀티 모듈 DI 는 module dependency 방향과 feature entry 계약을 따른다

DI graph 가 모듈 의존성 방향을 거꾸로 만들면 build graph 와 runtime graph 가 충돌한다. base/app module 은 feature 가 요구하는 contract 를 알 수 있어야 하고, feature 는 자신이 소유한 implementation 과 entry 를 명확히 노출해야 한다.

Navigation, dynamic feature, feature API module, implementation module 이 섞일수록 graph 를 하나로 크게 만드는 것보다 boundary 별 dependency contract 를 분리하는 편이 낫다.

관련 노트: [Navigation contracts](../../navigation/navigation-contracts/navigation-contracts.md), [Dynamic feature module](../../../03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md).

### 최소 계약 예시

```kotlin
// :feature:payments:api — app과 impl 양쪽이 볼 수 있는 안정된 계약
interface PaymentsEntry {
    fun open(orderId: String)
}

// :feature:payments:impl — 내부 graph와 구현을 소유
class RealPaymentsEntry @Inject constructor(
    private val checkout: Checkout,
) : PaymentsEntry
```

`:app -> :feature:payments:impl -> :feature:payments:api` 같은 Gradle 방향에서 app root가 구현 binding을 조립할 수 있다. 반대로 feature가 app concrete type을 import해야만 만들어지면 dependency direction이 깨진다. feature가 필요한 app-owned dependency는 작은 provision interface나 component dependency로 표현한다.

### 실패와 관찰 신호

- Gradle circular dependency가 나면 graph 선언으로 module 방향을 우회하려 하지 말고 contract의 소유 module을 다시 정한다.
- feature API가 Retrofit, Room, Hilt component 같은 구현 세부를 노출하면 교체 경계가 아니다.
- generated component의 dependency trace에 금지된 상위 module concrete type이 나타나는지 확인한다.

관련 노트: [Navigation contracts](../../navigation/navigation-contracts/navigation-contracts.md), [Dynamic feature DI](./dynamic-feature-di-needs-base-owned-contracts-and-install-boundaries.md)

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Dagger in multi-module apps](https://developer.android.com/training/dependency-injection/dagger-multi-module)
