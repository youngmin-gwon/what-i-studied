---
title: scope-matches-object-reuse-to-owner-lifetime
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Scope 는 singleton 장식이 아니라 owner lifetime 에 맞춘 재사용 계약이다
배경 지식: [의존성 역전 원칙](../../../../../../02_references/oop/solid/DIP%28Dependency%20Inversion%20Principle%29.md), [독립 수명 모델](../../../00_foundations/learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)

**Scope**(스코프 — 의존성 객체의 생명주기를 특정 DI 컨테이너 수명과 일치시켜 재사용을 제어하는 어노테이션) 는 "한 번만 만든다"는 느낌보다 "어떤 graph/component instance 안에서 재사용되는가"를 정의한다. Application scope, Activity scope, ViewModel scope 는 서로 다른 owner lifetime 을 가진다.

짧은 lifetime 객체를 긴 graph 에 넣으면 leak 이 생기고, 긴 lifetime 객체를 짧은 graph 마다 새로 만들면 cache, connection, observer 정책이 흔들린다. scope 를 붙이기 전에는 객체가 누구의 상태를 들고 누구와 함께 사라져야 하는지 먼저 정한다.

### 최소 예시

```kotlin
@ActivityScoped
class CheckoutSession @Inject constructor()

@Module
@InstallIn(ActivityComponent::class)
object CheckoutModule {
    @Provides
    @ActivityScoped
    fun checkoutSession(): CheckoutSession = CheckoutSession()
}
```

같은 `ActivityComponent` instance 안에서는 같은 객체를 재사용하지만 새 Activity component에는 새 객체가 생긴다. unscoped binding은 요청할 때마다 새 instance를 만들 수 있다. `@Singleton`도 앱 설치 전체의 전역 객체가 아니라 `SingletonComponent` instance 안의 재사용 계약이다.

### 실패와 관찰 신호

- `@ActivityScoped` binding을 `SingletonComponent`에 설치하면 Hilt가 incompatible scope로 build를 실패시킨다.
- 동일 화면에서 injection 지점 둘의 `System.identityHashCode()`가 같아야 하는지, 화면 재생성 뒤에도 같아야 하는지를 owner 계약으로 먼저 적는다.
- 긴 scope 객체가 Activity/View를 field로 보관하면 scope annotation이 있어도 leak을 막아주지 않는다.

관련 노트: [Context lifetime in DI](./android-context-in-di-must-match-graph-lifetime.md), [ViewModel](../../architecture/state-management/viewmodel/viewmodel.md)

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Hilt components and scopes](https://dagger.dev/hilt/components.html), [Dagger scopes](https://dagger.dev/dev-guide/basic-usage#singletons-and-scoped-bindings)
