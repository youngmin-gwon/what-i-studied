---
title: consumers-should-declare-dependencies-in-constructors
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## 소비자는 의존성을 생성하지 말고 생성자로 요구한다

Repository, UseCase, state holder 같은 일반 Kotlin 객체는 협력 객체를 생성자에 선언하고 graph 또는 수동 composition root가 그 생성자를 호출하게 둔다. 이렇게 해야 객체가 유효해지기 전에 필요한 dependency가 모두 채워지고 테스트가 같은 API로 fake를 전달할 수 있다.

직접 생성이 섞이면 fake 교체, scope 통제, configuration 주입, dependency graph 검증이 깨진다. Android framework class 처럼 생성자를 framework 가 호출하는 타입은 예외이며, 이때는 **Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) entry point, factory, assisted injection 같은 별도 boundary 가 필요하다.

관련 노트: [ViewModel](../../architecture/state-management/viewmodel/viewmodel.md), [Hilt integration](./hilt-is-official-android-dagger-integration.md).

### 최소 예시

```kotlin
class SyncUser(
    private val users: UserRepository,
    private val io: CoroutineDispatcher,
) {
    suspend operator fun invoke(id: UserId) = withContext(io) { users.sync(id) }
}
```

`SyncUser`는 저장소 구현이나 `Dispatchers.IO`를 내부에서 고르지 않는다. 값 객체처럼 스스로 생성해도 되는 내부 구현 세부까지 모두 주입할 필요는 없으며, 외부 자원·시간·dispatcher·정책처럼 교체와 lifetime이 의미 있는 협력 객체가 대상이다.

### 실패와 관찰 신호

- `Retrofit.Builder()`, `Room.databaseBuilder()`, `Dispatchers.IO`가 소비자 내부에 박히면 테스트 대체와 구성 변경이 그 클래스의 수정으로 번진다.
- 필드 주입 전 메서드가 호출되어 `lateinit property ... has not been initialized`가 발생하면 일반 클래스에 불필요한 members injection을 쓴 신호다.
- unit test에서는 `SyncUser(FakeUserRepository(), testDispatcher)`처럼 graph 없이 직접 생성할 수 있어야 한다.

Activity, Fragment처럼 framework가 생성하는 타입은 지원되는 `@AndroidEntryPoint`, factory 또는 entry point 경계를 사용하고, 비즈니스 객체까지 그 예외를 퍼뜨리지 않는다.

상위 문서: [DI 계약](./di-contracts.md)
