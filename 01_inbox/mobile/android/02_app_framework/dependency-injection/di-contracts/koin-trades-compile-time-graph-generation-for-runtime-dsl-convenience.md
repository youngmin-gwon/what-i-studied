---
title: koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Koin classic DSL은 런타임 resolve하고 compiler plugin은 검증 시점을 앞당긴다

Koin classic DSL은 Kotlin 코드로 definition을 선언하고 container가 런타임에 dependency를 resolve한다. Dagger/Hilt처럼 generated component가 모든 요청 경로를 기본적으로 compile하는 모델과 실패 시점이 다르다. 그러나 현재 Koin에는 module `verify()`와 별도의 compiler plugin이 있으므로 “코드 생성 없이 runtime 검증만 하는 도구”로 고정해 설명하면 오래된 비교가 된다.

따라서 Koin 을 선택할 때는 간단한 setup 만 보지 말고 startup cost, runtime resolution failure, module loading, test override, IDE/build integration 까지 같이 판단한다.

### 최소 예시

```kotlin
val appModule = module {
    single<UserApi> { RealUserApi(get()) }
    factory { UserRepository(get()) }
}

@Test
fun verifyGraph() {
    appModule.verify()
}
```

`single`은 Koin container lifetime에서 definition의 instance를 재사용하고 `factory`는 요청마다 만든다. Android 화면 lifetime이 필요하면 scope를 명시하고 scope를 여닫는 owner를 정해야 한다. `single`이 Activity를 잡는다고 leak이 방지되는 것은 아니다.

### 실패와 관찰 신호

- `RealUserApi`가 요구하는 dependency definition이 빠지면 `verify()`에서 잡히거나 해당 path의 최초 `get()`에서 definition-not-found 예외가 난다.
- 과거의 `checkModules()`는 Koin 4.0부터 deprecated이므로 새 문서와 테스트는 `verify()`를 쓴다.
- compiler plugin을 도입했다면 plugin이 분석하지 못하는 동적 module loading·parameterized injection 경계는 별도 테스트 대상으로 남긴다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Koin module verification](https://insert-koin.io/docs/reference/koin-test/verify/), [Koin compiler plugin](https://insert-koin.io/docs/setup/koin-compiler-plugin/)
