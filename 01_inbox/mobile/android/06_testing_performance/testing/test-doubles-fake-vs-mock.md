---
title: test-doubles-fake-vs-mock
tags: ["android", "android/testing-performance"]
aliases: ["Test double는 행동의 소유권으로 Fake와 Mock을 구분해 선택한다"]
date modified: 2026-08-04 20:00:00 +09:00
date created: 2026-08-04 20:00:00 +09:00
---

## Test double 는 행동의 소유권으로 Fake 와 Mock 을 구분해 선택한다

상위 문서: [테스트 품질 계약](./testing-quality.md)

### 핵심 주장

Fake 는 실제 로직을 간단하게라도 스스로 구현한 대역이고(예: in-memory `Map` 기반 Repository), Mock/Stub 는 호출을 기록하거나 미리 정한 값만 반환하는 대역이다. 이 vault 의 [viewmodel](../../02_app_framework/architecture/state-management/viewmodel.md) 테스트가 "fake repository 만으로 충분하다"고 반복해서 말하는 이유는, Fake 가 실제 행동(성공/실패/빈 값 조건 분기)을 스스로 소유해서 `Repository` interface 가 조금만 바뀌어도 Fake 코드 자체가 컴파일 에러로 드러나는 반면, Mock 은 `every { ... } returns ...` 스텁이 interface 변경과 무관하게 계속 통과할 수 있어 리팩터링 안전성이 낮기 때문이다.

Kotlin/Android 생태계에서 이 역할을 실제로 수행하는 라이브러리는 MockK(Kotlin 우선, `mockk`/`coEvery`)와 Mockito(Java 우선, `mockito-kotlin` 으로 Kotlin 사용)다. 두 라이브러리는 서로 대체 가능하지만 이 vault 의 다른 코루틴 테스트 노트들이 `coEvery`/`coVerify` 를 전제로 예시를 들 때는 MockK 를 기준으로 한다.

### 메커니즘

MockK 는 mock 을 "strict"(기본값)와 "relaxed"(`relaxed = true` 또는 `mockk(relaxed = true)`)로 나눈다. strict mock 은 스텁하지 않은 메서드를 호출하면 즉시 실패하고, relaxed mock 은 스텁하지 않은 메서드에 대해 참조 타입은 체이닝 가능한 mock 을, 값 타입은 기본값(0, false, 빈 컬렉션 등)을 자동으로 반환한다.

```kotlin
// strict mock: 스텁 안 한 호출은 실패한다
val repo = mockk<UserRepository>()
every { repo.getUser(any()) } returns User("id1", "Alice")
// repo.deleteUser("id1") 호출 시 MockKException: no answer found

// relaxed mock: 스텁 안 한 호출도 기본값을 반환한다
val repo = mockk<UserRepository>(relaxed = true)
repo.deleteUser("id1") // Unit 반환, 예외 없음 — 이 호출이 실제로 뭘 하는지는 검증되지 않는다
```

relaxed mock 은 "이 호출의 세부 동작은 이 테스트의 관심사가 아니다"를 명시적으로 표현하는 도구이지, strict mock 대신 기본값으로 쓰라는 뜻이 아니다. 테스트 대상 동작을 검증해야 하는 메서드까지 relaxed 로 두면 실제로는 깨진 로직도 테스트가 통과하는 거짓 양성(false positive)이 생긴다.

### 판단 기준

- 여러 조건 분기(성공/빈 값/네트워크 실패)를 가진 데이터 소스는 Fake 로 만들어 ViewModel/UseCase 단위 테스트가 실제 분기 로직을 통과하게 한다.
- 호출 여부·횟수·인자 자체가 검증 대상(예: "저장 성공 시 애널리틱스 이벤트가 정확히 1번 전송됐는가")이면 Mock 의 `verify`/`coVerify` 를 쓴다 — 이건 Fake 로 표현하기 어려운 "상호작용 검증"이다.
- 인터페이스가 크고 테스트마다 일부 메서드만 관심 대상이면 `relaxed = true` 로 나머지를 자동 처리하되, 실제로 검증하는 메서드는 반드시 `every`/`verify` 로 명시한다.

### 경계

이 노트는 test double 선택 기준만 다룬다. 어떤 테스트 레이어(unit/integration/UI/E2E)에서 test double 을 쓸지는 [테스트 레이어는 피드백 비용으로 선택한다](test-pyramid-strategy.md)가 다룬다. dispatcher/코루틴 자체를 통제하는 방법은 [Coroutine 과 Flow 테스트는 dispatcher 와 virtual time 을 통제해야 한다](coroutine-flow-testing.md)가 다룬다.

### 관찰 가능한 신호

strict mock 에서 스텁하지 않은 호출이 발생하면 `io.mockk.MockKException: no answer found for: <method>` 예외가 테스트 실행 시점에 바로 던져진다. 이 예외가 CI 로그에 나타나면 "이 테스트가 실제로는 더 많은 상호작용을 하고 있는데 스텁을 놓쳤다"는 신호로 읽는다. relaxed mock 을 과용해 이런 신호가 전혀 나오지 않는 테스트 스위트는, 리팩터링 시 로직이 깨져도 초록불이 유지될 위험이 크다는 것도 함께 관찰 대상이다.

관련 노트: [테스트 레이어는 피드백 비용으로 선택한다](test-pyramid-strategy.md), [회귀와 flaky 테스트는 릴리즈 게이트의 신뢰도를 낮춘다](flaky-tests-regression-gates.md)

공식 문서: [MockK](https://mockk.io/)

검증일: 2026-08-04. relaxed/strict mock 동작 차이를 mockk.io 공식 문서로 확인.
