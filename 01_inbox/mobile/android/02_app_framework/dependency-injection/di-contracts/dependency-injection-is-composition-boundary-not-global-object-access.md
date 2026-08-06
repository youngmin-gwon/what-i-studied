---
title: dependency-injection-is-composition-boundary-not-global-object-access
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## DI 는 전역 객체 접근이 아니라 조립 경계다

Dependency Injection의 핵심은 필요한 객체를 소비자가 직접 만들거나 전역 registry에서 꺼내지 않고, 바깥 **composition root**에서 연결해 넣는 것이다. 이 경계가 객체 생성 정책, 테스트 대체와 lifetime을 사용 코드에서 분리한다.

Android 에서는 이 조립 경계가 `Application`, feature entry, screen owner, Worker factory 처럼 OS/framework lifetime 과 만나는 지점에 놓인다. DI framework 선택보다 먼저 정해야 하는 것은 어떤 객체가 어떤 owner 아래에서 만들어지고 재사용되는가다.

관련 노트: [app architecture](../../architecture/android-app-architecture.md), [Context boundaries](../../architecture/context-and-modularity/android-context-boundaries.md).

### 최소 예시

```kotlin
class FeedRepository(private val api: FeedApi)
class FeedScreenModel(private val repository: FeedRepository)

fun createFeedScreenModel(baseUrl: String): FeedScreenModel {
    val api = RetrofitFeedApi(baseUrl)
    return FeedScreenModel(FeedRepository(api))
}
```

`createFeedScreenModel`이 수동 composition root다. Dagger/Hilt/Koin/Metro를 쓰더라도 생성 책임이 compiler-generated graph나 module 선언으로 이동할 뿐, 소비자가 `ServiceLocator.get<FeedApi>()`를 호출하는 구조가 DI로 바뀌는 것은 아니다.

### 실패와 관찰 신호

- 일반 클래스에서 container API나 전역 singleton을 import하면 dependency가 생성자 API에 드러나지 않는다.
- 테스트가 전역 registry 초기화 순서에 의존하거나 병렬 실행에서 서로의 binding을 덮으면 composition boundary가 새고 있다는 신호다.
- composition root 바깥에서는 생성자만 보고 필수 dependency를 열거할 수 있어야 한다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Dependency injection in Android](https://developer.android.com/training/dependency-injection)
