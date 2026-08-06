---
title: dynamic-feature-di-needs-base-owned-contracts-and-install-boundaries
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## Dynamic feature DI 는 base-owned contract 와 install boundary 를 분리해야 한다

Dynamic feature module 은 필요할 때 설치되는 선택 feature unit 이다. DI graph 가 dynamic feature implementation 을 base 가 compile time 에 직접 알아야만 동작한다면 dynamic delivery 의 장점과 충돌한다.

Base module 에는 feature entry contract, navigation route, dependency interface 처럼 안정적으로 알아야 할 것만 둔다. Dynamic feature 내부 implementation 과 binding 은 설치 이후 entry boundary 에서 연결한다.

관련 노트: [Dynamic feature module](../../../03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md).

Hilt annotation processing은 base가 compile-time에 의존하지 않는 feature module의 binding을 base graph로 런타임 병합하지 않는다. 공식 패턴은 base graph가 provision contract를 제공하고, 설치된 feature가 그 contract에 의존하는 별도 Dagger component를 만드는 것이다.

### 최소 구조

```kotlin
// base module
@EntryPoint
@InstallIn(SingletonComponent::class)
interface FeatureDependencies {
    fun userRepository(): UserRepository
}

// dynamic feature module
@Component(dependencies = [FeatureDependencies::class])
interface FeatureComponent {
    fun inject(activity: FeatureActivity)
}
```

feature가 시작된 뒤 `EntryPointAccessors.fromApplication(...)`로 base provision interface를 얻어 `DaggerFeatureComponent.builder().featureDependencies(...)`에 전달한다. split 설치 성공을 확인하기 전에는 feature class를 참조하거나 component를 만들지 않는다.

### 실패와 관찰 신호

- base가 feature implementation/module을 import하면 reversed dependency라 compile할 수 없다.
- 필요한 provision이 contract에 빠지면 feature component compilation에서 missing binding trace가 난다.
- split 미설치 상태에서 feature class를 로드하면 class-not-found 또는 navigation 실패가 나므로 설치 state와 component 생성 log를 함께 본다.

관련 노트: [Dynamic feature module](../../../03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md)

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Hilt in multi-module apps — feature modules](https://developer.android.com/training/dependency-injection/hilt-multi-module)
